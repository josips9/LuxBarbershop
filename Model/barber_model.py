from Model.base_model import BaseScreenModel


class Barber(BaseScreenModel):
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.service = specialty
