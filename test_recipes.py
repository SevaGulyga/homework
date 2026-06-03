import pytest

from classes import Ingredient

def test_ingredients():
    x = Ingredient('Орехи', 200, 'г')
    assert x.name == 'Орехи'
    assert x.quantity == 200.0
    assert x.unit == 'г'

def test_ingredients2():
    x = Ingredient('Орехи', 200, 'г')
    assert str(x) == 'Орехи: 200.0 г'

def test_ingredients3():
    x = Ingredient('Орехи', 200, 'г')
    y = Ingredient('Орехи', 500, "г")
    assert x == y
    x1 = Ingredient('Гречка', 100, "г")
    y1 = Ingredient('Манка', 100, "г")
    assert x1 != y1
    x2 = Ingredient('Говядина', 400, "г")
    y2 = Ingredient('Говядина', 400, "кг")
    assert x2 != y2


from classes import Recipe, Ingredient
import pytest

def test_Recipe():
    t = Recipe('Борщ')
    assert t.title == 'Борщ'
    assert t.ingredients == []

def test_Recipe2():
    t = Recipe('Борщ')
    t.add_ingredient(Ingredient('Свекла', 200, "г"))
    assert len(t.ingredients) == 1

def test_Recipe3():
    t = Recipe('Борщ')
    t.add_ingredient(Ingredient('Картошка', 200, "г"))
    t.add_ingredient(Ingredient('Картошка', 300, 'г'))
    assert len(t.ingredients) == 1
    assert t.ingredients[0].quantity == 500.0

def test_Recipe4():
    t = Recipe('Борщ')
    t.add_ingredient(Ingredient('Картошка', 200, "г"))
    ratio = t.scale(3)
    assert ratio.ingredients[0].quantity == 600.0
    assert t.ingredients[0].quantity == 200.0
    assert ratio is not t

def test_Recipe5():
    t = Recipe('Борщ')
    t.add_ingredient(Ingredient('Картошка', 200, "г"))
    with pytest.raises(ValueError):
        t.scale(-50)

def test_Recipe6():
    t = Recipe('Борщ')
    t.add_ingredient(Ingredient('Картошка', 200, "г"))
    t.add_ingredient(Ingredient('Свекла', 200, "г"))
    assert len(t) == 2

from classes import ShoppingList, Recipe, Ingredient
import pytest

def test_ShoppingList():
    v = Recipe('Уха')
    v.add_ingredient(Ingredient("Щука", 300, "г"))
    v1 = ShoppingList()
    v1.add_recipe(v, 2)
    assert len(v1._items) == 1

def test_ShoppingList2():
    v = Recipe('Уха')
    v1 = ShoppingList()
    with pytest.raises(ValueError):
        v1.add_recipe(v, 0)

def test_ShoppingList3():
    v = Recipe('Уха')
    v.add_ingredient(Ingredient("Щука", 300, "г"))
    v1 = ShoppingList()
    v1.add_recipe(v, 2)
    v1.remove_recipe('Уха')
    assert len(v1._items) == 0

def test_ShoppingList4():
    v1 = ShoppingList()
    v1.remove_recipe("Нету")
    assert len(v1._items) == 0

def test_ShoppingList5():
    v = Recipe('Уха')
    p = Recipe("Бутерброды")
    v.add_ingredient(Ingredient("Щука", 300, "г"))
    p.add_ingredient(Ingredient("Щука", 400, "г"))
    v1 = ShoppingList()
    v1.add_recipe(v, 2)
    v1.add_recipe(p, 1)
    rez = v1.get_list()
    assert len(rez) == 1
    assert rez[0].quantity == 1000.0

def test_ShoppingList6():
    v = Recipe('Уха')
    v.add_ingredient(Ingredient("Щука", 300, "г"))
    v.add_ingredient(Ingredient("Гренки", 100, "г"))
    v1 = ShoppingList()
    v1.add_recipe(v, 1)
    rez = v1.get_list()
    gros = [i.name for i in rez]
    assert gros == sorted(gros)

def test_ShoppingList7():
    v = Recipe('Уха')
    v.add_ingredient(Ingredient("Щука", 300, "г"))
    v1 = ShoppingList()
    v1.add_recipe(v, 2)
    v2 = ShoppingList()
    v2.add_recipe(v, 1)
    sum = v1 + v2
    assert len(sum._items) == 2
    assert len(v1._items) == 1
    assert len(v2._items) == 1












