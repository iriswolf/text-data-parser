from collections import namedtuple


class Pattern:

    def __init__(self, text: str, validate: bool = True):
        """
        :param text: pattern text
        :param validate: validate pattern types?
        """
        self.pattern = text
        self.validate = validate

        self._parse_pattern(text)

    def _parse_pattern(self, pattern):
        a = self._parse_tokens(pattern)
        print(a)

    def _parse_tokens(self, pattern: str):
        tokens = []

        previous_token: str | None = None
        for i, s in enumerate(pattern):
            if s == '<':
                if previous_token == '<':  # Если токен повторился
                    raise Exception("Найден открывающий токен '<', но перед ним не было найдено токена закрытия '>'")

                previous_token = s
                tokens.append((i, s))
            elif s == '>':
                """ В цикле проверяем, не было ли до этого закрывающего токена - открывающего """
                if previous_token == '>' or previous_token is None:
                    # Если прошлый токен был повторяющим этот или до этого токена не было токена открытия
                    raise Exception("Найден закрывающий токен '>', но перед ним не был найден открывающий токен '<'")

                previous_token = s
                tokens.append((i, s))


        """
        _tok = []

        previous_index: int | None = None
        for index, token in enumerate(tokens):
            if index+1 == len(tokens):
                break
            if previous_index == index:
                break

            previous_index = index
            _tok.append((token, tokens[index+1]))

        #print(_tok)"""
        return tokens


if __name__ == '__main__':
    pattern = Pattern("Привет меня зовут <name> и мне <age:int> лет, у меня есть <apple_val:int> яблок")
