# - ეს საშუალებას გვაძლევს, ფუნქციის შედეგი შევინახოთ ცვლადში, გამოვიყენოთ სხვა გამოთვლებში, ან დავბეჭდოთ.
def product(numbers):
    result = 1
    for n in numbers:
        result = n
    return result

print(product([2, 3, 4]))

def pirveli_function(x):
    return x

def  meore_function(y):
    return y + 10

result = pirveli_function(meore_function(5))
print(result)