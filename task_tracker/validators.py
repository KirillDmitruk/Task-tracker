import re

from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("^[а-яА-Яa-zA-Z0-9\.\-\,\№]")
        val = dict(value).get(self.field)
        if not bool(reg.match(val)):
            raise ValidationError(
                f"{self.field} может содержать только буквы, цифры, точки, дефисы, запятые и пробелы."
            )
