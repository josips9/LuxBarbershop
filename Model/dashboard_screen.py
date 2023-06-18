from Model.base_model import BaseScreenModel


class DashboardScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.dashboard_screen.DashboardScreenView` class.
    """
    def __init__(self, database):
        self.database = database