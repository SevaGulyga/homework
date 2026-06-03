class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError('Количество должно быть положительным')
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f'Ingredient({self.name!r}, {self.quantity}, {self.unit!r})'

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False


class Recipe:
    def __init__(self, title):
        self.title = title
        self.ingredients = []

    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        return self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError('Ratio not valid')
        nrecipe = Recipe(self.title)
        for y in self.ingredients:
            newy = Ingredient(y.name, y.quantity * ratio, y.unit)
            nrecipe.add_ingredient(newy)
        return nrecipe

    def len(self):
        return len(self.ingredients)

    def __str__(self):
        str_ingredients = [str(item) for item in self.ingredients]
        return self.title + ':\n' + '\n'.join(str_ingredients)


# class ShoppingList:








