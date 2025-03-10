import data
import sandwich_maker
import cashier
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for item validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

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
