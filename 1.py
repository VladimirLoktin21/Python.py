class IterableWithGenerator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # Возвращает генератор при каждой итерации
        return (item for item in self.data)

# Пример использования
my_iterable = IterableWithGenerator([1, 2, 3, 4, 5])

# Итерация по объекту
for value in my_iterable:
    print(value)
