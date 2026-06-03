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


class ShoppingList:
    def __init__(self, items):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError('Количество порций должно быть положительным')
        scaled_portion = recipe.scale(portions)
        for i in scaled_portion.ingredients:
            self._items.append((i, scaled_portion.title))

    def remove_recipe(self, title: str):
        remove = [x for x in self._items if x[1] == title]
        for i in remove:
            self._items.remove(i)

    def get_list(self):
        list_ingredients = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in list_ingredients:
                list_ingredients[key] += ingredient.quantity
            else:
                list_ingredients[key] = ingredient.quantity
        rez = []
        for (name, unit), quantity in list_ingredients.items():
            rez.append(Ingredient(name, quantity, unit))
        rez.sort(key=lambda x: x.name)
        return rez

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list









