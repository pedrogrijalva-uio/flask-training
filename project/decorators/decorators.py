from project.exceptions.custom_exceptions import NameTooShort, NameContainsSpecialCharacters


def values_comparison(func):
    def wrapper(*args, **kwargs):
        name = args[1] if args[0] == args[1] else args[0]
        return func(name, **kwargs)

    return wrapper


def validate_value_length(func):
    def wrapper(*args, **kwargs):
        if len(args[0]) < 10 if kwargs['type'] == 'identification' else 5:
            raise NameTooShort
        else:
            return func(args[0], **kwargs)

    return wrapper


def validate_value_characters(func):
    def wrapper(*args, **kwargs):
        if args[0] is None:
            raise NameContainsSpecialCharacters
        else:
            return func(args[0], **kwargs)

    return wrapper
