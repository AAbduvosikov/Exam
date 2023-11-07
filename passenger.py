from place import Place
from place import EndPlace
class Passanger:
    def __init__(self,id,place:Place) -> None:
        self._id = id
        self._place = place
        self._taxi_id = None
    
    @property 
    def taxi_id(self):
        return self._taxi_id
    def __str__(self) -> str:
        return (f"id = {self._id} , {self._place}")
    
    def getPlace(self):
        return (f"id = {self._id} , {self._place}")


