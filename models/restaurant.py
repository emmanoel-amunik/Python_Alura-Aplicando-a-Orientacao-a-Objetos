class Restaurant:

    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._activate = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    @classmethod
    def list_restaurants(cls):

        print(f"{'Name'.ljust(27)} {'Category'.ljust(27)} {'Status'}\n")

        for restaurant in cls.restaurants:
            print(f"{restaurant.get_name().ljust(25)} | "
                  f"{restaurant.get_category().ljust(25)} | "
                  f"{restaurant.activate}")

    @property
    def activate(self):
        return "true" if self._activate else "false"

    def change_status(self):
        self._activate = not self._activate


restaurant_square = Restaurant("square", "Gourmet")
restaurant_pizza = Restaurant("pizza Express", "Italian")

Restaurant.change_status(restaurant_square)
Restaurant.list_restaurants()
