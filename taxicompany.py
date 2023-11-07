from taxi import Taxi
from passenger import Passanger
class TaxiCompany:
    def __init__(self) -> None:
        self._taxi_list:list[Taxi] = []
        self._lost_trips = []

    def checkTaxi(self,id):
        for taxi in self._taxi_list:
            if taxi.id == id:
                return True
        return False

    def addTaxi(self,taxi:Taxi):
        if self.checkTaxi(taxi.id) == False:
            self._taxi_list.append(taxi)
            return (f"taxi royxatdan o'tdi")
        return (f"taxi mavjud")

    def getAvailable(self):
        return self._taxi_list
    
    
    def callTaxi(self,passanger:Passanger):
        count = 0
        if len(self._taxi_list) > 0 :
            passanger = self._taxi_list.pop(0)
        else:
            count += 1
            self._lost_trips.append(count)
        return passanger
    
    def getLostTrips(self):
            return len (self._lost_trips)
    
    






    

    


    
    
    
    
    
