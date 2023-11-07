class Place:
    def __init__(self,tuman,maxalla) -> None:
        self._tuman = tuman
        self._maxalla = maxalla
    @property
    def tuman(self):
        return self._tuman
    
    @property
    def maxalla(self):
        return self._maxalla

    def __str__(self) -> str:
        return (f"tuman = {self._tuman} , maxalla = {self._maxalla}")
    
class EndPlace(Place):
     def __init__(self, tuman, maxalla) -> None:
         super().__init__(tuman, maxalla)