from django.core.exceptions import ValidationError

VALIDATE_PLUS = 'The phone number must start with "+" !'
VALIDATE_NUMBER = 'The phone number must contain only numbers!'
VALIDATE_OWNER_NAME = "The owner's name must contain only letters!"
VALIDATE_OWNER_NAME_SPACE = 'The owner name must be separated by a space!'
VALIDATE_NAME = 'The name must contain only letters!'


def phone_number_validator(value):
    new_value = value[1::]
    if not value.startswith('+'):
        raise ValidationError(VALIDATE_PLUS, code='validate_plus')
    if not new_value.isdigit():
        raise ValidationError(VALIDATE_NUMBER, code="validate_number")


def owner_name_validator(value):
    index = ''
    is_space = False
    for ind in range(len(value)):
        if value[ind].isspace():
            index = ind
            is_space = True
    if not is_space:
        raise ValidationError(VALIDATE_OWNER_NAME_SPACE, code="validate_owner_name_space")
    new_value = value[:index] + value[index+1:]
    if not new_value.isalpha():
        raise ValidationError(VALIDATE_OWNER_NAME, code="validate_owner_name")


def name_validator(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_NAME, code="validate_name")
