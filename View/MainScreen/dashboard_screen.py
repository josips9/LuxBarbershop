from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from Model import database
from Model.barber_model import Barber
from Model.database import DataBase
from View.base_screen import BaseScreenView
from Controller.barber_controller import BarberController


class BarberListItem(MDBottomNavigationItem):
    pass


class DashboardScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super(DashboardScreenView, self).__init__(**kwargs)
        self.barber_controller = BarberController(database)

    barber_list = BarberListItem()


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def display_barbers(self, barbers):
        barber_list = self.ids.barber_list
        barber_list.clear_widgets()

        for barber in barbers:
            barber_item = BarberListItem(barber_name=barber.name)
            barber_list.add_widget(barber_item)

    def create_barber_button(self):
        barber_id = self.barber_controller.database.generate_id()

        # Retrieve the inputs from the UI fields
        barber_name_input = self.ids.barber_name_input
        barber_specialty_input = self.ids.barber_specialty_input

        name = barber_name_input.text
        specialty = barber_specialty_input.text

        # Check if the inputs are not empty
        if name and specialty:
            # Create the barber
            # barber_controller.create_barber(name, specialty)
            barber_id = self.barber_controller.database.generate_id()
            barber = Barber(barber_id, name, specialty)
            self.barber_controller.create_barber(name, specialty)
