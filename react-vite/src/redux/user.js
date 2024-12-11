import { csrfFetch } from "./csrf";

const CREATE_USER = 'session/createUser';



const newUser = (user) => ({
    type: CREATE_USER,
    user
});



export const CreateUser = (user) => async (dispatch) => {
    let res;

    let newestUser = {
        first_name: user.first_name,
        email: user.email,
        message: user.message
    };

    try {
        res = await csrfFetch('/api/users/create', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(newUser)
        });
    } catch (err) {
        if (err.json) {
            return err.json();
        } else {
            return {error: "Am unexpected error occured"}
        }
    }

    const data = await res.json()

    dispatch(newUser(data))
}

const initialState = {user: {}}

// Reducer function
function userReducer(state = initialState, action) {
    switch (action.type) {
        case CREATE_USER: {
            // Update the state with the new user data
            return {
                ...state,
                user: action.user
            };
        }
        default:
            return state;
    }
}

export default userReducer;
