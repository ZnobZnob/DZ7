with open ('files\cookbook.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        dish_count = int(file.readline())
        ingridients = []
        for _ in range(dish_count):
            idgridients_list = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = idgridients_list
            ingridients.append({'ingredient_name': ingredient_name,
                                'quantity': int(quantity),
                                'measure': measure})
        file.readline()
        dish = {'name': dish_name,
                'dish_count': dish_count,
                'ingridients': ingridients}
        cook_book[dish_name] = ingridients

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for i in dishes:
        for a in cook_book[i]:
            x = a['ingredient_name']
            m = a['quantity'] * person_count
            d = a['measure']
            if x not in res.keys():
                res[x] = {'measure': d, 'quantity': m}
            elif x in res.keys():
                res[x] = {'measure': d, 'quantity': m + m}
    return res

print(get_shop_list_by_dishes(['Омлет'], 2))
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

import os

current = os.getcwd()
folder_name = 'files'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_4 = '4.txt'

full_patch_1 = os.path.join(current, folder_name, file_name_1)
full_patch_2 = os.path.join(current, folder_name, file_name_2)
full_patch_3 = os.path.join(current, folder_name, file_name_3)
full_patch_4 = os.path.join(current, folder_name, file_name_4)


with open(full_patch_1, 'rt', encoding='utf-8') as file:
    name_file_1 = '1.txt'
    number_str_1 = file.readlines()
    file.seek(0)
    text_1 = file.read()
    full_1 = name_file_1, len(number_str_1), text_1

with open(full_patch_2, 'rt', encoding='utf-8') as file:
    name_file_2 = '2.txt'
    number_str_2 = file.readlines()
    file.seek(0)
    text_2 = file.read()
    full_2 = name_file_2, len(number_str_2), text_2

with open(full_patch_3, 'rt', encoding='utf-8') as file:
    name_file_3 = '3.txt'
    number_str_3 = file.readlines()
    file.seek(0)
    text_3 = file.read()
    full_3 = name_file_3, len(number_str_3), text_3

full_list = full_1, full_2, full_3
full_list_sorted = sorted(full_list, key=lambda file: file[1])

with open(full_patch_4, 'w', encoding='utf-8') as file:
    for files in full_list_sorted:
        file.write(str(files[0]) + '\n')
        file.write(str(files[1]) + '\n')
        file.write(str(files[2]) + '\n')

with open(full_patch_4, 'rt', encoding='utf-8') as file:
    text_4 = file.read()
    print(text_4)
