def make_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            ingredients = []
            meal_name = line.strip()
            quantity = int(file.readline())
            for _ in range(quantity):
                meal_ingredient = file.readline()
                l_meal_ingredient = meal_ingredient.strip().split(' | ')
                dict_ingr = {'ingredient name': l_meal_ingredient[0], 'quantity': int(l_meal_ingredient[1]), 'measure':
                            l_meal_ingredient[2]}
                ingredients.append(dict_ingr)
            cook_book[meal_name] = ingredients
            file.readline()
    return cook_book


print(make_cook_book('recipes.txt'))
dishes = ['Омлет', 'Утка по-пекински']


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = make_cook_book('recipes.txt')
    result = {}
    for _ in range(len(dishes)):
        ingredients = cook_book[dishes[_]]
        for item in ingredients:
            name_it = item.pop('ingredient name')
            if name_it in result:  # if we have the same ingredient
                item['quantity'] *= 2
                item['quantity'] += result.pop(name_it)['quantity']
                result[name_it] = item
            else:
                item['quantity'] *= 2
                result[name_it] = item
    return result


print()
print(get_shop_list_by_dishes(dishes, 2))
