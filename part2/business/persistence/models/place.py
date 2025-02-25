from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, user_id, description="", number_rooms=0,
                 number_bathrooms=0, max_guest=0, price_by_night=0,
                 latitude=0.0, longitude=0.0):
        super().__init__()
        self.name = name
        self.user_id = user_id
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
