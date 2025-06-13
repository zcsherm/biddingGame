class Chit:
    def __init__(self, value, player, id):
        self._id = id
        self._player = player
        self._value = value
        self._assigned_contract = None

    def assign_contract(self, contract):
        self._assigned_contract = contract

    def reset(self):
        self._assigned_contract = None

    def get_value(self):
        return self._value
