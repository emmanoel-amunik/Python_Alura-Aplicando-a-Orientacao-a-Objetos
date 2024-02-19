from models.restaurant import Restaurant


restaurant_square = Restaurant("square", "Gourmet")
restaurant_square.collect_rating("Gui", 10)
restaurant_square.collect_rating("Lais", 8)
restaurant_square.collect_rating("Emy", 5)


def main():
    Restaurant.list_restaurants()


if __name__ == "__main__":
    main()
