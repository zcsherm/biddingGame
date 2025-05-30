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

class 
