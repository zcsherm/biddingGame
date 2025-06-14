from items import ITEM_CARDS
from contracts import CONTRACT_CARDS
import random
from errors import *

class Card:
    """
    Represents a generic card
    """
    def __init__(self,name):
        if not isinstance(name,str):
            raise InvalidNameError(name, self)
        self._name = name
    
    def get_name(self):
        return self._name

    def set_owner(self, owner):
        if owner not in VALID_OWNERS:
            raise InvalidOwnerError(owner, self)
        self._owner = owner
        
class Item(Card):
    """
    Represents an item card, with name, a cost, and a resale value
    """
    def __init__(self, name, cost, resale_value):
        """
        Setup the card with basic attributes, set the cards owner as None, indicating it should be in the deck
        """
        super().__init__(name)
        if not isinstance(cost, int):
            raise InvalidValueError(cost, "cost", self)
        if not isinstance(resale_value, int):
            raise InvalidValueError(resale_value, "resale_value", self)
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
    """
    Represents a contract card, has a name, a budget, a desired value, and a point value
    """
    def __init__(self, name, budget, target, points):
        """
        setup basic attributes for the contract, owner as none implies card is not in use.
        """
        super().__init__(name)
        if not isinstance(budget, int):
            raise InvalidValueError(budget, "cost",self)
        if not isinstance(target,int):
            raise InvalidValueError(target, "target", self)
        if not isinstance(points,int):
            raise InvalidValueError(points, "points", self)        
        self._budget = budget
        self._modified_budget = budget
        self._target = target
        self._points = points
        self._owner = None

    
    def get_budget(self):
        return self._budget

    def get_target(self):
        return self._target

    def get_modified_budget(self):
        return self._modified_budget

    def modify_budget(self, modifier):
        """
        Modifies the budget based on the users bid for the contract
        """
        if not isinstance(modifier, int):
            raise InvalidValueError(modifier, "modified_budget", self)
        self._modified_budget = self._budget + modifier

    def get_points(self):
        return self._points

    def get_owner(self):
        return self._owner

class Deck:
    """
    Represents a deck of cards, keeps cards in order, but has shuffled indices to facilitate drawing.
    """
    def __init__(self, type):
        # indicate wether it is an item deck or contract deck
        self._type = type
        self._cards = []
        # Separate list used for the current shuffled order of cards
        self._card_indices = []
        self._number_of_cards = 0
        # which index of the card_indices is the top card
        self._card_pointer = 0
        self.generate_deck(self._type)

    def draw_card(self):
        """
        Pulls the top available card from the deck, returns the card object
        """
        # Shuffle the deck first if the deck is empty
        if self._card_pointer >= len(self._cards):
            self.shuffle()
        # Get the top card of the deck
        card = self._cards[self._card_indices[self._card_pointer]]
        while card._owner is not None:
            # If the card is currently in play, then we get the next card and continue until we get a valid card
            card = self.draw_card()
        self._card_pointer += 1
        return card

    def shuffle(self):
        # Use knuth shuffle method, shuffle in place by moving random picks to end of list, decrementing range by 1
        num_of_cards_unshuffled = self._number_of_cards-1
        while num_of_cards_unshuffled != 0:
            # Pick a random index and move that card to the end of the list
            index = random.randint(0,num_of_cards_unshuffled)
            tmp = self._card_indices[num_of_cards_unshuffled]
            self._card_indices[num_of_cards_unshuffled] =self._card_indices[index]
            self._card_indices[index] = tmp
            num_of_cards_unshuffled -= 1
        self._card_pointer=0

    def generate_deck(self,type):
        """
        Generate a new deck of cards
        """
        # generate the correct set of cards based on the deck type
        if type == 'items':
            cards = ITEM_CARDS
            card = Item
        elif type == 'contracts':
            cards = CONTRACT_CARDS
            card = Contract
        else:
            # Change to an error
            return False
        # Generate new cards based on the dictionary of card names and values
        counter = 0
        for name, attributes in cards.items():
            new_card = card(name,*attributes)
            try:
                validate_card(new_card)
            except:
                raise InvalidCard(new_card)
            self._cards.append(new_card)
            counter += 1
        self._number_of_cards = counter
        # Shuffle the card order
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
        
    def get_card_names(self):
        """
        Get each cards name
        """
        for i in range(self._number_of_cards):
            print(self._cards[self._card_indices[i]].get_name())

def validate_card(card):
    if not isinstance(card.get_name(), str):
        raise InvalidNameError(card.get_name(), card)
    if card.get_owner() not in VALID_OWNERS:
        raise InvalidOwnerError(card.get_owner())
    if card.__class__.__name__ == "Item":
        pass
    elif card.__class__.__name__ == "Contract":
        pass
    else:
        return False

