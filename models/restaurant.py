class Restaurant:

    name = ""
    category = ""
    activate = False


restaurant_square = Restaurant()
restaurant_square.name = "Square"
restaurant_square.category = "Gourmet"

restaurant_pizza = Restaurant()

restaurants = [restaurant_square, restaurant_pizza]

print(restaurant_square)
