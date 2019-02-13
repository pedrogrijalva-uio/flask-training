import re

from project.exceptions.custom_exceptions import ValueTooShort, ValueContainsSpecialCharacters


def values_comparison(func):
    def wrapper(*args, **kwargs):
        name = args[1] if args[0] == args[1] else args[0]
        print(type(func))
        return func(name, **kwargs)

    return wrapper


def validate_value_length(func):
    def wrapper(*args, **kwargs):
        value_min_length = 10 if kwargs['type'] == 'identification' else 1
        value_type = 'Identification Number' if kwargs['type'] == 'identification' else kwargs['type'].capitalize()
        if len(args[0]) < value_min_length:
            raise ValueTooShort(f'{value_type} length is too short. Must be at least {value_min_length} characters')
        else:
            return func(args[0], **kwargs)

    return wrapper


def validate_value_characters(func):
    def wrapper(*args, **kwargs):
        global pattern
        if kwargs['type'] == 'identification':
            value_type = 'Identification Number'
            accepted_type = 'numbers'
            unaccepted_types = 'alphabet or'
            pattern = 'a-zA-Z'
        else:
            value_type = kwargs['type'].capitalize()
            accepted_type = 'alphabet characters' if kwargs['type'] == 'name' else 'alphabet characters and numbers'
            unaccepted_types = 'numeric or' if kwargs['type'] == 'name' else ''
            pattern = '0-9' if kwargs['type'] == 'name' else ''
        base_pattern = r'^\w[^' + pattern + '!@#$%^&*()_+=:;\'\"\\|~`/?><,.-]+$'
        match = re.search(base_pattern, args[0])
        if not match:
            raise ValueContainsSpecialCharacters(
                f'{value_type} must not have {unaccepted_types} special characters. It only accepts {accepted_type}.')
        else:
            return func(args[0], **kwargs)

    return wrapper
