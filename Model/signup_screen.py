from firebase_admin import auth
from Model.base_model import BaseScreenModel


class SignUpScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.signup_screen.SignUpScreenView` class.
    """
    def __init__(self, database):
        self._data = None
        self.db = database

    def register_user(self, username, email, password):
        try:
            # Create the user in Firebase Authentication
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username
            )
            user_id = user.uid

            # Store the user in the database
            user_ref = self.db.real_time_firebase.put(
                self.db.DATABASE_URL,
                f'{self.db.USER_DATA}/{user_id}',
                {
                    'username': username,
                    'email': email
                }
            )

            # Clear the input fields
            self.notify_observers("signup screen", success=True)

            print("User created successfully")

        except Exception as e:
            self.notify_observers("signup screen", success=False, error=str(e))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.MainScreen.signup_scree.SignUpScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("signup screen")


