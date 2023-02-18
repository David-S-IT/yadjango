class PositiveIntegerConverter:
    regex = r'[1-9]\d*'

    def to_python(self, value):
        return f'{value}'

    def to_url(self, value):
        return f'{value}'
