"""
Main class to manage sample data
"""

class SampleData(object):
    products = []
    stations = []

    def __init__(self, products=None, stations=None):
        if products is not None:
            self.products = products

        if stations is not None:
            self.stations = stations


    def get_product_ids(self):
        return [int(p[0][0]) for p in self.products]
    
    def get_station_ids(self):
        return [int(s[0][0]) for s in self.stations]