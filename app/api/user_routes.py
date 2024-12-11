from dotenv import load_dotenv
import os
from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User, db
from app.forms import SantaMessageForm
from app.email.email import send_santa_email

from openai import OpenAI


load_dotenv()

# Initialize OpenAI API

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
user_routes = Blueprint('users', __name__)

@user_routes.route('/create', methods=['POST'])
def create_user():
    """
    Creates a user and sends a Santa message
    """
    form = SantaMessageForm()
    form['csrf_token'].data = request.cookies.get('csrf_token')
    if form.validate_on_submit():
        try:
            # Save user to the database
            user = User(
                first_name=form.data['first_name'],
                email=form.data['email'],
                message=form.data['message']
            )
            db.session.add(user)
            db.session.commit()

            # Generate a Santa message with OpenAI
            response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": f'Personalized message from santa for {user.first_name}, include stuff written in {user.message}'
                    }
                ]
                },
            ],
            response_format={
                "type": "text"
            },
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            santa_message = response.choices[0].message.content
            print('SANTA!!!!! ',santa_message)

            # Send email with the Santa message
            send_santa_email(user.email, santa_message)
            print('yeeeeet ', santa_message)
            return jsonify({"message": "Santa's message sent successfully!", "user": user.first_name}), 201
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"error": "Form validation failed"}), 400
