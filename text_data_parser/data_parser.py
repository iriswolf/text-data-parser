import typing
from typing import Dict

if typing.TYPE_CHECKING:
    from text_data_parser import Pattern


class DataParser:

    def __init__(self, validate_types: bool = True):
        self._validate = validate_types  # todo возможно перенести это в метод parse

    def parse(self, pattern: "Pattern", text: str) -> dict | None:
        pattern_tokens = pattern.get_tokens()

        if not pattern_tokens or not text:  # if pattern == [] or text == "" return None
            return

        text = text.split()
        text_len = len(text) - 1

        parsed_values = dict()
        for token in pattern_tokens:
            pattern_token_name = token[0]
            pattern_token_type = token[1]
            pattern_token_index = token[2]

            if not text_len >= pattern_token_index >= 0:  # if token index not in range text_len
                return

            if pattern_token_name in parsed_values.keys():  # Если имена токенов повторяются
                return  # todo убрать эту проверку в создание паттерна, ей не место в рантайме

            parsed_text = text[pattern_token_index]

            if self._validate:  # переделать эту макаронщину которая возникла из-за валидации

                if value := DataParser.validate(parsed_text, pattern_token_type):  # todo пора писать валидатор
                    """ Если значение прошло валидацию типа, получаем уже валидированное значение с нужным типом """
                    parsed_values[pattern_token_name] = value
                else:
                    return

            parsed_values[pattern_token_name] = parsed_text

        return parsed_values

    @staticmethod
    def validate(value, _type):
        # return True  # пока валидаторы не написаны, пока всегда тру кстати валидатор автоматом приводит типы
        return DataParser.temporary_validator(value, _type)

    @staticmethod
    def temporary_validator(value: str, _type: str):
        # print(f"i validate {value, _type}")

        match _type:
            case 'str':
                return value
            case 'int':
                if value.isdigit() and '.' not in value:
                    return int(value)
            case 'float':
                if value.isdigit() and '.' in value:
                    return float(value)
            case _:
                return
