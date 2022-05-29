import datetime


class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []



class Flight:
    def __init__(self, destination, origin, plane, id):
        self.date = datetime.date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = id

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
        self.

    def available_on_date(self, date, location):
        pass


class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        pass

    def info(self, start_date, end_date):
        pass