import os
from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, db
from app.forms import santaMessageForm
import openai
from app.email.email import send_santa_email


# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

user_routes = Blueprint('users', __name__)

@user_routes.route('/create', methods=['POST'])
def create_user():
    """
    Creates a user and sends a Santa message
    """
    form = santaMessageForm()
    if form.validate_on_submit():
        # Save the user data to the database
        user = User(
            first_name=form.data['firstName'],
            email=form.data['email'],
            phone_number=form.data['phoneNumber'],
            message=form.data['message']
        )
        db.session.add(user)
        db.session.commit()

        # Use OpenAI to generate a message from Santa
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct model name
            messages=[
                {"role": "system", "content": "You are Santa Claus, and you are writing a heartfelt message."},
                {"role": "user", "content": f"Write a warm and joyful message to {form.data['firstName']}."}
            ]
        )

        # Extract the generated message
        santa_message = response['choices'][0]['message']['content']

        # Send the message via email
        send_santa_email(user.email, santa_message)

        return jsonify({"message": santa_message, "user": user.first_name}), 201

    return jsonify({"error": "Form validation failed"}), 400
