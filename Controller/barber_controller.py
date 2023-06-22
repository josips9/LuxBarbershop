from Model.barber_model import Barber
from Model.database import DataBase


class BarberController:
    def __init__(self, database: DataBase):
        self.database = database

    def create_barber(self, name, specialty) -> None:
        barber_id = self.database.generate_id()
        barber = Barber(barber_id, name, specialty)
        self.database.add_barber(barber_id, barber)

    def get_all_barbers(self) -> object:
        return self.database.get_all_barbers()
