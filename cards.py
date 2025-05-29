import ITEM_CARDS from items
import CONTRACT_CARDS from contracts
import random
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
    def __init__(self, name, budget, target, points):
        super().__init__(name)
        self._budget = budget
        self._modified_budget = budget
        self._target = target
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
        self._number_of_cards = 0
        self._card_pointer = 0
        self.generate_deck(self._type)

    def draw_card(self):
        if self._card_pointer >= len(self._cards):
            self.shuffle()
        card = self._cards[self._card_indices[self._card_pointer]]
        self._card_pointer += 1
        return card

    def shuffle(self):
        # Use knuth shuffle method, shuffle in place by moving random picks to end of list, decrementing range by 1
        num_of_cards_unshuffled = self._number_of_cards-1
        while num_of_cards_unshuffled != 0:
            index = random.randint(0,num_of_cards_unshuffled)
            tmp = self._card_indices[num_of_cards_unshuffled]
            self._card_indices[num_of_cards_unshuffled] =self._card_indices[index]
            self._card_indices[index] = tmp
            num_of_cards_unshuffled -= 1
        

    def generate_deck(self,type):
        if type == 'items':
            cards = ITEM_CARDS
            card = Item
        elif type == 'contracts':
            cards = CONTRACT_CARDS
            card = Contract
        else:
            # Change to an error
            return False
        counter = 0
        for name, attributes in cards.items():
            new_card = card(name,*attributes)
            self._cards.append(new_card)
            counter += 1
        self._number_of_cards = counter
        self._card_indices = [i for i in range(counter)]
        self.shuffle()
        
    def get_type(self):
        return self._type

    def get_card_pointer(self):
        return self._card_pointer

    def get_card_indices(self):
        return self._card_indices

    def get_cards(self):
        return self._cards

    
