from project.decorators.decorators import values_comparison, validate_value_length, validate_value_characters


@values_comparison
@validate_value_length
@validate_value_characters
def validate_name(*args, **kwargs):
    return args[0]


@validate_value_length
@validate_value_characters
def validate_value_registration(*args, **kwargs):
    return args[0]


@values_comparison
def validate_value_changed(*args, **kwargs):
    return args[0]


@values_comparison
@validate_value_length
@validate_value_characters
def validate_identification_number(*args, **kwargs):
    return args[0]
