
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def fetch_data(endpoint):
    # Simulated API call
    return {"status": 200, "data": []}


class Database:
    def connect(self):
        pass
    def query(self, q):
        return []


# refactored based on Anandha Priya's review

class Database:
    def connect(self):
        pass
    def query(self, q):
        return []


def fetch_data(endpoint):
    # Simulated API call
    return {"status": 200, "data": []}


# refactored based on John Smith's review

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

