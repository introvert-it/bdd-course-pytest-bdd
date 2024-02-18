import requests


class FridgeApi:
    def __init__(self, domain):
        self.url = f"{domain}/api/fridge"

    def get_fridges_list(self):
        """
        Get list of all fridges
        GET http://<url>/api/fridge/

        :return: list, existing fridges
        """
        response = requests.get(self.url)
        list_of_existing_fridges = response.json()
        return list_of_existing_fridges

    def create_fridge(self):
        """
        Create new fridge
        POST http://<url>/api/fridge/

        :return: http response object (containing status_code, json() etc.)
        """
        response = requests.post(self.url)
        return response

    def get_food_in_fridge(self, fridge_id):
        """
        Get all food stored in fridge

        GET http://<url>/api/fridge/<fridge_id>/food
        :param fridge_id: str, fridge id (called "_id")
        :return: http response object (containing status_code, json() etc.)
        """
        food_url = f"{self.url}/{fridge_id}/food"
        response = requests.get(food_url)
        return response

    def add_food_to_fridge(self, fridge_id, food_name, quantity, expires_in):
        """
        Add new food item to fridge.

        PUT http://<url>/api/fridge/<fridge_id>/food

        :param fridge_id: str, fridge id (called "_id")
        :param food_name: str, name of food
        :param quantity: int, how much food items you want to store in the fridge
        :param expires_in: int, how many hours are left until food expires (for
            simplicity it's being counted in seconds: 1 hour = 1 second)
        :return: http response object (containing status_code, json() etc.)
        """
        food_url = f"{self.url}/{fridge_id}/food"
        response = requests.put(
            food_url,
            json={
                "food_name": food_name,
                "quantity": str(quantity),
                "expires_in": str(expires_in)
            }
        )
        return response
