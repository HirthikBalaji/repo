
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

