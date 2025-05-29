class Player:
    def __init__(self, number):
        self._player_number = number
        self._chits = None # implement class
        self._cart = None # implement class
        self._contract_one = None
        self._contract_two = None
        self._contract_three = None
        self._contracts = [self._contract_one, self._contract_two, self._contract_three]
        self._bundle_one = None
        self._bundle_two = None
        self._bundle_three = None
        self._bundles = [self._bundle_one,self._bundle_two,self._bundle_three]
        self._points = 0

    def add_points(self, points):
        self._points += points

    def get_points(self):
        return self._points

    def assign_contract(self, contract):
        contract.set_player(self)
        if self._contract_one is None:
            self._contract_one = contract
        elif self._contract_two is None:
            self._contract_two = contract
        elif self._contract_three is None:
            self._contract_three = contract
        return

    def pick_item(self, item):
        self._cart.add_item(item)

    def assign_item(self, item, contract_number):
        self._bundles[contract_number-1].add_item(item)
