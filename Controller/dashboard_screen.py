import importlib

import View.MainScreen.dashboard_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MainScreen.dashboard_screen)


class DashboardScreenController:
    """
    The `DashboardScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """
    def __init__(self, model):
        self.model = model # Model.dashboard_scree.SignUpScreenModel
        self.view = View.MainScreen.dashboard_screen.DashboardScreenView(controller=self, model=self.model)

    def get_view(self) -> View.MainScreen.dashboard_screen:
        # self.update_barber_list()
        # self.update_service_list()
        return self.view

    # def update_barber_list(self):
    #     barbers = self.model.get_all_barbers()
    #     self.view.display_barbers(barbers)

    # def update_service_list(self):
    #     services = self.model.get_all_services()
    #     self.view.display_services(services)

