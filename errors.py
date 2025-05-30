VALID_OWNERS = [
    "1",
    "2",
    "game",
    "Game",
    1,
    2,
    None
]

class invalidValueError(Exception):
    """
    Error raised when a game object is passed an invalid valid as an attribute
    """
    def __init__(self, value, param, object=None):
        message = f"An invalid value was passed for an attribute."
        if object is not None:
            message += f" {object.get_name()} of class {object.__class__.__name__} was passed {value} of type {typeOf(value)}. {param} only accepts integers."
        else:
            message += f" {value} was passed of type {typeOf(value)}. {param} only accepts integers"
        super().__init__(message)

class invalidNameError(Exception):
    """
    Error raised when a game oject is passed an invalid name on creation
    """
    def __init__(self, name, object):
        message = f"An invalid name was passed to an object on creation. {object.__class__.__name__} was passed "
        super().__init__(message)

class invalidOwnerError(Exception):
    """
    Error raised when a game object is passed an invalid owner id
    """
    def __init__(self, owner, object=None):
        message = f"An object was assigned an incorrect owner."
        if object is not None:
            message += f" {object.get_name()} was assigned an owner of  {owner}. Owners must be a player in the game (1 or 2), 'game', or None."
        else:
            message += f"Passed value was {owner}, but owner must be a player in the game (1 or 2), 'game', or None."
        super().__init__(message)
        
class invalidCard(Exception):
    """
    Error raised when a card without valid attributes is passed
    """
    def __init__(self, card, target: String):
        message = f"A card was passed to {target} that had invalid attributes. Card has attributes: \n"
        variables = vars(card)
        for key, value in variables:
            message += f"{key}: {value}\n"
        super().__init__(message)

class invalidCardTypeToDeck(Exception):
    """
    Handles when an invalid card type is passed to a deck
    """
    def __init__(self, card, deck_type):
        message = f"A card of type {card.get_type()} was passed to a deck of mismatching type. The deck only holds {deck_type} cards."
        super.__init__(message)
        
