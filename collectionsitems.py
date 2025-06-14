COUNT = 5

class Collection:
    def __init__(self, owner):
        self._items = []
        self._owner = owner
        self._value = 0
        self._cost = 0

    def add_item(self,item):
        self._value += item.get_value()
        self._cost += item.get_cost()
        item.set_owner(self._owner)
        self._items.append(item)

    def remove_item(self, item):
        index = self._items.indexOf(item)
        self._items.pop(index)
        self._value -= item.get_value()
        self._cost -= item.get_cost()

    def get_value(self):
        return self._value

    def get_cost(self):
        return self._cost

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner
        
    def get_items(self):
        return self._items

    def get_item(self, index):
        return self._items[index]
    
class Cart(Collection):
    def __init__(self, owner):
        super().__init__(owner)

    def remove_item(self, item):
        super().remove_item(item)

    def discard_item(self, item):
        super().remove_item(item)
        item.set_owner(None)
        # Move to market
        
class Bundle(Collection):
    
    def __init__(self, owner):
        super().__init__(owner)

    def add_item(self,item):
        super().add_item(item)
        self._owner.get_cart().remove_item(item)

    def remove_item(self, item):
        super().remove_item(item)
        self._owner.get_cart().add_item(item)

    def discard_item(self, item):
        super().remove_item(item)
        item.set_owner(None)

class Market(Collection):

    def __init__(self, count):
        super().__init__('game')
        self._capacity = count
        self._slots = {i:None for i in range(count)}
        self._used_slots = len(self._items)
        self.update_item_slots(self._items)

    def update_item_slots(self, items):
        self._slots = {i:None for i in range(15)}
        counter = 0
        for item in self._items:
            self._slots[counter] = item
            counter += 1
        
        
    def remove_item(self, item):
        super().remove_item(item)
        self._used_slots -= 1
        for key in self._items:
            if self._items[key] == item:
                self._items[key] = None
                return
                
    def add_item(self, item):
        super().add_item(item)
        self._used_slots += 1
        for key in self._items:
            if self._items[key] is None:
                self._items[key] = item
                return

    def refill_slots(self, deck):
        while self._used_slots < COUNT:
            self.add_item(deck.draw_card())
            self._used_slots += 1

class Contracts(Market):

    def __init__(self, count):
        super().__init__('game')
        
    def discard_all(self):
        for key in self._slots:
            if self._slots[key] is not None:
                self.remove_item(self._slots[key])
        
class Chits:

    def __init__(self, player):
        self._player = player
        self._chits = {}
        self.create_chits()

    def create_chits(self):
        # Create all chits for the player
        pass

    def get_chit(self, chit_id):
        return self._chits[chit_id]

    def reset_chits(self):
        # On starting a new round, return all chits to a player
        for chit in self._chits:
            self._chits[chit].reset()
