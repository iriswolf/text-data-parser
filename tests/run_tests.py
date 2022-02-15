import time

from text_data_parser import DataParser, Pattern

#print("-----Running test-----")

"""
dp = DataParser()
pattern = Pattern("Привет меня зовут <name> и мне <age:int> лет, у меня есть <apple_val:int> яблок")
""
Как из этого получить что и куда вставлять?
надо сделать карту
""


res1 = dp.parse(
    pattern,
    "Привет меня зовут Andrew и мне 19 лет, у меня есть 46 яблок"
)  # good result: {'name': 'Andrew', 'age': 19, 'apple_val': 46}

res2 = dp.parse(
    pattern,
    "Привет меня зовут Andrew и мне 19.5 лет, у меня есть 46 яблок"
)  # pattern does not match (requested <age:int>, but received float) - result: None


print(res1)
print(res2)
"""

text = "Привет, меня зовут Ahmed и мне 19 лет, у меня есть 40 яблок"


dp = DataParser(validate_types=False)
pattern = Pattern("Привет, меня зовут <name> и мне <age:int> лет, у меня есть <apple:int> яблок") # todo > click <


s = time.time()
parsed = dp.parse(pattern, text)
e = time.time()

print(parsed)
print(f"{e-s}s")

