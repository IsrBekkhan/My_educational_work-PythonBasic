class House:
    cash = 100
    food = 50
    cat_food = 30
    dirt = 0
    tenants = []
    money_earned = 0
    food_eaten = 0
    bought_fur_coats = 0

    def house_pollution(self):
        self.dirt += 5
