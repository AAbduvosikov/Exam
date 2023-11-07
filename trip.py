from place import Place
from place import EndPlace
class Trip:
    def __init__(self,place:Place,endPlace:EndPlace) -> None:
        self._place = place
        self._endPlace = endPlace
    
    def __str__(self) -> str:
        return (f"Boshlanish joyi == {self._place} Manzil == {self._endPlace}")
