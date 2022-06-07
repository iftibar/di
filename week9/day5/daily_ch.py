import datetime


class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes_airline = []



class Flight(Airline):
    def __init__(self, destination, origin, plane, id):
        self.date = datetime.date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = id
        super(Flight, self).__init__()
        
    def take_off(self):
        pass

    def land(self):
        pass


class Airplane(Flight):
    def __init__(self, id, current_loc, company):
        self.id = id
        self.current_loc = current_loc
        self.company = company
        self.next_flight = []
        super(Airplane, self).__init__()

    def fly(self, destination):
        self.current_loc = destination

    def location_on_date(self, date):
        self

    def available_on_date(self, date, location):
        pass


class Airport(Airplane):
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []
        super(Airport, self).__init__()

    def schedule_flight(self, destination, date):
        if self.planes_airline in self.available_on_date(date):

    def info(self, start_date, end_date):
        pass