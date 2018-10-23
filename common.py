"""
Main classes to manage sample data
"""

class Product(object):
    id = 0
    velocity = 0
    motion_factor = 0
    due_date = 0
    tasks = []

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = int(kwargs.get('id', 0))
            self.velocity = kwargs.get('velocity', None)
            self.motion_factor = kwargs.get('motion_factor', None)
            self.due_date = kwargs.get('due_date', None)
            self.tasks = kwargs.get('tasks', [])
        if args:
            self.id = int(args[0][0])
            self.velocity = args[3][0]
            self.motion_factor = args[4][0]
            self.due_date = args[5][0]
            self.tasks = [int(arg) for arg in args[2]]


class Station(object):
    id = 0
    velocity = 0
    motion_factor = 0
    tasks = []

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = int(kwargs.get('id', 0))
            self.velocity = kwargs.get('velocity', 0)
            self.motion_factor = kwargs.get('motion_factor', 0)
            self.tasks = kwargs.get('tasks', [])
        elif args:
            self.id = int(args[0][0])
            self.velocity = args[4][0]
            self.motion_factor = args[5][0]
            self.tasks = [int(t) for t in args[2]]


class Task(object):
    id = 0
    process_step_id = 0
    description = ''
    processing_time = 0

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get('id', 0)
            self.process_step_id = kwargs.get('process_step_id', 0)
            self.description = kwargs.get('description', '')
            self.processing_time = kwargs.get('processing_time', 0)
        elif args:
            self.id = args[0]
            self.process_step_id = args[1]
            self.description = args[2]
            self.processing_time = args[3]


class SampleData(object):
    products = []
    stations = []
    tasks = []

    def __init__(self, *args, **kwargs):
        products = []
        stations = []
        tasks = []
        if args:
            products = args[0]
            stations = args[1]
            tasks = args[2]
        elif kwargs:
            products = kwargs.get('products', [])
            stations = kwargs.get('stations', [])
            tasks = kwargs.get('tasks', [])

        for item in products:
            product = Product(*item)
            self.products.append(product)
        
        for item in stations:
            station = Station(*item)
            self.stations.append(station)

        for item in tasks:
            task = Task(*item)
            self.tasks.append(task)
        

    def get_product_ids(self):
        return [p.id for p in self.products]
    
    def get_station_ids(self):
        return [s.id for s in self.stations]