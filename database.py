
def fetch_data(endpoint):
    # Simulated API call
    return {"status": 200, "data": []}


def calculate_total(price, tax):
    return price + price * tax


class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# refactored based on Hirthik Balaji's review
