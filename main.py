from taxicompany import TaxiCompany
from taxi import Taxi
from place import Place
from passenger import Passanger
from place import EndPlace

taxi = TaxiCompany()
taksit1 = Taxi(1)
taksit2 = Taxi(2)
print (taksit1)
print(taxi.addTaxi(taksit1))
print(taxi.addTaxi(taksit2))
print(taxi.getAvailable())



joy1 = Place ("yunsabod19","14 dom")
endjoy1 = EndPlace("Chorsu","20 dom")
mijoz2= Passanger (1,joy1)
mijoz3 = Passanger (2,joy1)
mijoz4 = Passanger (3,joy1)
mijoz5 = Passanger (4,joy1)
print(mijoz2)
mijoz2.getPlace()
print(taxi.callTaxi(mijoz3))
print (taxi.callTaxi(mijoz2))
print (taxi.callTaxi(mijoz4))
print (taxi.callTaxi(mijoz5))
print(taxi.getAvailable())
print(taxi.getLostTrips())



