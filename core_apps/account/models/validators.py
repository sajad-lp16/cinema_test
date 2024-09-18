import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    pattern = r"^((0?9)|(\+?989))\d{9}$"
    if not re.match(pattern, value):
        raise ValidationError('Phone number is invalid.')
