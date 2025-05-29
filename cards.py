import ITEMS from items
class Card:
    
    def __init__(self,name):
        self._name = name
    
    def get_name(self):
        return self._name

class Item(Card):
    def __init__(self, name, cost, resale_value):
        super().__init__(name)
        self._cost = cost
        self._resale_value = resale_value
        self._owner = None

    def get_cost(self):
        return self._cost

    def get_value(self):
        return self._resale_value

    def get_owner(self):
        return self._owner
        
class Contract(Card):
    def __init__(self, name, budget, points):
        super().__init__(name)
        self._budget = budget
        self._modified_budget = budget
        self._points = points

    def get_budget(self):
        return self._budget

    def get_modified_budget(self):
        return self._modified_budget

    def modify_budget(self, modifier):
        self._modified_budget = self._budget + modifier

    def get_points(self):
        return self._points

class Deck:
    def __init__(self, type):
        self._type = type
        self._cards = []
        self._card_indices = []
        self._card_pointer = 0
        self.generate_decks(type)

    def draw_card(self):
        if self._card_pointer >= len(self._cards):
            self.shuffle()
        card = self._cards[self._card_indices[self._card_pointer]]
        self._card_pointer += 1
        return card

