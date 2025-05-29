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
    
class Cart(collection):
    def __init__(self, owner):
        super().__init__(owner)

    def remove_item(self, item):
        super().remove_item(item)

    def discard_item(self, item):
        super().remove_item(item)
        self._owner(None)
        
class Bundle(collection):
    
    def __init__(self, owner):
        super().__init__(owner)

    def add_item(self,item):
        super().add_item(item):
        self._owner.get_cart().remove_item(item)

    def remove_item(self, item):
        super().remove_item(item)
        self._owner.get_cart().add_item(item)
