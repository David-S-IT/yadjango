import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustContain:
    def __init__(self, *args):
        self.args = args

    def __call__(self, value):
        for arg in self.args:
            if re.search(rf'\b{arg}\b', value):
                return value
        raise ValidationError(
            'В тексте должны содержаться слова {}'.format(self.args)
        )
