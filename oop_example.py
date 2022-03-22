class Airplane:
    def __init__(self, passengers, seats, pilots=[]):
        self.passengers = passengers
        self.seats = seats
        self._pilots = pilots

    def takeoff(self):
        pass

airplane = Airplane(passengers=20, seats=30, pilots=['Tom', 'Billy'])
airplane.passengers = 31
airplane.takeoff()