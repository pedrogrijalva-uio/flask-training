class NameException(Exception):
    pass


class NameTooShort(NameException):
    pass


class NameContainsSpecialCharacters(NameException):
    pass


class IdentificationNumberException(Exception):
    pass


class IdentificationNumberIncomplete(IdentificationNumberException):
    pass


class IdentificationNumberContainsSpecialCharacters(IdentificationNumberException):
    pass
