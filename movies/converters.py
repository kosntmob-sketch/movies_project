class FourDigitYearConverter:
    # Регулярное выражение: строго 4 цифры от 0 до 9
    regex = '[0-9]{4}'

    def to_python(self, value):
        # Превращает строку из URL в число для функции во views.py
        return int(value)

    def to_url(self, value):
        # Превращает число обратно в строку для генерации ссылок в HTML
        return '%04d' % value