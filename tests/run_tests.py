from text_data_parser import DataParser, Pattern

print("Run tests")


dp = DataParser()
pattern = Pattern("Привет меня зовут <name> и мне <age:int> лет, у меня есть <apple_val:int> яблок")
"""
Как из этого получить что и куда вставлять?
надо сделать карту
"""


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
