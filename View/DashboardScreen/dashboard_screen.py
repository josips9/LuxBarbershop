from kivy.properties import ObjectProperty
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from Model import database
from Model.barber_model import Barber
from Model.database import DataBase
from View.base_screen import BaseScreenView
from Controller.barber_controller import BarberController


class BarberListItem(MDBottomNavigationItem):
    pass


class DashboardScreenView(BaseScreenView):
    barber_name_input = ObjectProperty()
    barber_specialty_input = ObjectProperty()

    barber_list = BarberListItem()
    barber_controller = BarberController(database)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def create_barber_button(self):
        barber_id = self.barber_controller.database.generate_id()

        # Retrieve the inputs from the UI fields
        name = self.barber_name_input.text
        specialty = self.barber_specialty_input.text

        # Check if the inputs are not empty
        if name and specialty:
            # Create the barber
            barber_id = self.barber_controller.database.generate_id()
            barber = Barber(barber_id, name, specialty)
            self.barber_controller.create_barber(name, specialty)

            # Clear the user inputs
            self.clear_inputs()

            barbers = self.database.get_all_barbers()
            self.display_barbers(barbers)

    def clear_inputs(self):
        self.barber_name_input.text = ""
        self.barber_specialty_input.text = ""

    def display_barbers(self, barbers):
        barber_list = self.ids.barber_list
        barber_list.clear_widgets()

        for barber in barbers:
            barber_item = BarberListItem(barber_name=barber.name)
            barber_list.add_widget(barber_item)




