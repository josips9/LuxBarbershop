# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController

from Model.signup_screen import SignUpScreenModel
from Controller.signup_screen import SignUpScreenController

from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController

from Model.dashboard_screen import DashboardScreenModel
from Controller.dashboard_screen import DashboardScreenController

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "signup screen": {
        "model": SignUpScreenModel,
        "controller": SignUpScreenController,
    },
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController
    },
    "dashboard screen": {
        "model": DashboardScreenModel,
        "controller": DashboardScreenController
    }
}
