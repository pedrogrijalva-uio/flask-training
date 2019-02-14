class ValueException(Exception):
    pass


class ValueTooShort(ValueException):
    pass


class ValueContainsSpecialCharacters(ValueException):
    pass


class IdentificationNumberException(Exception):
    pass


class IdentificationNumberIncomplete(IdentificationNumberException):
    pass



