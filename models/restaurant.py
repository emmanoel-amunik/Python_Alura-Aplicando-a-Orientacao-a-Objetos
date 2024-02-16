class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.activate = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self.name} | {self.category}"

    @staticmethod
    def list_restaurants():

        for restaurant in Restaurant.restaurants:
            print(f"{restaurant.name} | {restaurant.category} | "
                  f"{restaurant.activate}")


restaurant_square = Restaurant("Square", "Gourmet")
restaurant_pizza = Restaurant("Pizza Express", "Italian")
