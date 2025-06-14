from collectionsitems import *
class Player:
    """
    Represents a player in the game. The player has a cart (hand), 3 contract slots, 3 bundles of items (one for each contract), and a collection of betting chits
    """
    def __init__(self, number):
        """
        Setup the basic attributes of the player
        """
        self._player_number = number
        self._chits = None # implement class
        self._cart = Cart(self._player_number) # implement class
        # Reference each contract individual, and bundle them in a list
        self._contract_one = None
        self._contract_two = None
        self._contract_three = None
        self._contracts = [self._contract_one, self._contract_two, self._contract_three]
        # Reference the set of objects in each bundle, and bundle them together into a list
        self._bundle_one = None
        self._bundle_two = None
        self._bundle_three = None
        self._bundles = [self._bundle_one,self._bundle_two,self._bundle_three]
        self._points = 0

    def add_points(self, points):
        """
        Increment or decrement the players points
        """
        self._points += points

    def get_points(self):
        return self._points

    def assign_contract(self, contract):
        """
        Given a chosen contract, the player is assigned the contract as its owner and the contract is listed as the object for the first available contract slot property
        """
        contract.set_player(self._player_number)
        if self._contract_one is None:
            self._contract_one = contract
        elif self._contract_two is None:
            self._contract_two = contract
        elif self._contract_three is None:
            self._contract_three = contract
        return

    def pick_item(self, item):
        """
        Add an item to the players cart
        """
        self._cart.add_item(item)

    def assign_item(self, item, contract_number):
        """
        Assign an item to one of the players contracts
        """
        self._bundles[contract_number-1].add_item(item)
