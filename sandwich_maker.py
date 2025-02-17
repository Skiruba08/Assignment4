import cashier

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
           for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

