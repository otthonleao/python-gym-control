class Activity:
    def __init__(self, name, instructor, date, duration, capacity, type_plan, active, id = None):
        self.name = name
        self.instructor = instructor
        self.date = date
        self.duration = duration
        self.capacity = capacity
        self.type_plan = type_plan
        self.active = active
        self.id = id