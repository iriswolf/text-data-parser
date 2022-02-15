from collections import namedtuple


class Pattern:

    def __init__(self, text: str):
        """
        :param text: pattern text
        :param validate: validate pattern types?
        """
        self.__pattern = text

        self.__parsed_tokens = self.__create_pattern(text)

    def get_tokens(self) -> "__create_pattern":
        """Возвращает уже готовые токены для обработки классом DataParser в виде (name, type, index)
        name = имя токена
        type = тип токена для валидации
        index = индекс токена в list

        надо разделить строку из которой будем парсить
        """
        return self.__parsed_tokens

    def __create_pattern(self, pattern: str) -> list[tuple[str, str, int]] | list:
        tokens_ = []

        for i, t in enumerate(pattern.split()):
            if t.startswith('<') and t.endswith('>'):  # Если строка начинается с < и заканчивается >
                if t.count('<') != 1 or t.count('>') != 1:  # Если в токене больше чем 1 знак открытия/закрытия
                    raise Exception(
                        f"В токене {t!r} паттерна {pattern!r} должно быть по одному знаку открытия '<' и закрытия '>'")

                if t == '<>':
                    raise Exception(
                        f"В паттерне {pattern!r} должно быть имя переменной внутри токена {t!r}")

                """ Добавляем дефолтный тип str если тип не был указан """
                tkn_t = t[1:-1].split(':')
                if len(tkn_t) == 1:
                    tkn_t.append('str')

                tokens_.append((*tkn_t, i))  # tuple(name, type, index)
        return tokens_
