class InvalidRequestError(Exception):
    #exception raised for invalid requests
    pass

class ConflictError(Exception):
    #exception raised for conflicts,
    #such as duplicate entries
    pass