class BookNotFoundError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class BookAlreadyExistsError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class BookUnavailableError(Exception):
    pass

class BookNotIssuedError(Exception):
    pass

class IssuedBookError(Exception):
    pass