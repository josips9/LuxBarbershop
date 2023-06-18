from firebase_admin import auth

from Model.base_model import BaseScreenModel

class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.login_screen.LoginScreenView` class.
    """
    def __init__(self, database):
        self._data = None
        self.db = database

    def login_user(self, email, password):
            try:
                # Authenticate the user with Firebase Authentication
                user = auth.get_user_by_email(email)

                # Print success message
                print("User logged in successfully")

            except Exception as e:
                # Handle login error
                print("Login failed:", str(e))
            else:
                print("No login data found")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.MainScreen.login_screen.LoginScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("login screen")