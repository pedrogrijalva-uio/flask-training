from project.decorators.decorators import values_comparison, validate_value_length, validate_value_characters


@values_comparison
@validate_value_length
@validate_value_characters
def validate_name(*args, **kwargs):
    print('validate_name')
    print(len(args))
    return args[0]


@values_comparison
def validate_email(*args, **kwargs):
    return args[0]


@values_comparison
@validate_value_length
def validate_identification_number(*args, **kwargs):
    return args[0]
