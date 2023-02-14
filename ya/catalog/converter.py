class PositiveIntegerConverter:
    regex = r'[1-9]\d*'

    @staticmethod
    def to_python(value):
        return int(value)

    @staticmethod
    def to_url(value):
        return '%d' % value
