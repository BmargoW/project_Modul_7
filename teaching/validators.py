from rest_framework.exceptions import ValidationError

keyword = "youtube"

def link_validator(value):

    if keyword not in value.lower():
        raise ValidationError("нельзя иные ссылки кроме youtube")


