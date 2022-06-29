from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
#


def get_recipe_omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe_omlet = {}
    for i, v in DATA['omlet'].items():
        recipe_omlet[i] = v * servings
    context = {
        'recipe': recipe_omlet,
    }
    return render(request, 'calculator/index.html', context)


def get_recipe_pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe_pasta = {}
    for i, v in DATA['pasta'].items():
        recipe_pasta[i] = v * servings
    context = {
        'recipe': recipe_pasta,
    }
    return render(request, 'calculator/index.html', context)


def get_recipe_buter(request):
    servings = int(request.GET.get('servings', 1))
    recipe_buter = {}
    for i, v in DATA['buter'].items():
        recipe_buter[i] = v * servings
    context = {
        'recipe': recipe_buter,
    }
    return render(request, 'calculator/index.html', context)