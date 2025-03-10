import data, sandwich_maker, cashier
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union [str, None] = None):
    return {"item_id": item_id, "q": q}

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
        sandwich_maker_instance.is_on = True
        while sandwich_maker_instance.is_on:
            choice = input("What would you like? (small/medium/large/off/report): ").lower()

            if choice == "off":
                sandwich_maker_instance.is_on = False
                print("Goodbye! Thanks for shopping!")
            elif choice == "report":
                for item, amount in resources.items():
                    print(f"{item.capitalize()}: {amount}")
            elif choice in recipes:
                sandwich = recipes[choice]
                if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                    transaction = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(transaction, sandwich[
                        "cost"]):
                        sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
            else:
                print("Invalid choice. Please select again.")


if __name__=="__main__":
    main()
