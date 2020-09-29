import pandas as pd

# from app.models import Restaurant
from app.models import Category, Restaurant, City

filename = 'Рестораны.xlsx'

link = 'Ссылка на гугл карты'
option1 = 'Веранда'
option2 = 'Завтраки'
option3 = 'Дог-френдли'

data_file = pd.read_excel(filename, sheet_name='Москва')


# Создаем рестораны
def get_category(categories):
    cat_ids = []

    for i in categories:
        if type(i) != float:
            try:
                category = Category.objects.get(name=str(i))
                cat_ids.append(category.id)
            except:
                new_category = Category.objects.create(name=i)
                cat_ids.append(new_category)
            return cat_ids


def create_models():
    for i in data_file.index:
        rest_name = data_file['Название ресторана'][i]
        short_desc = data_file['Описание ресторана'][i]
        address = data_file['Адрес ресторана'][i]
        full_desc = data_file['Описание полное'][i]
        glink = data_file['Ссылка на гугл карты'][i]

        veranda = data_file['Веранда'][i]
        breakfast = data_file['Завтраки'][i]
        dog_friendly = data_file['Дог-френдли'][i]

        categories = [data_file['Категория 1'][i], data_file['Категория 2'][i], data_file['Категория 3'][i]]



        city = City.objects.get(name='Москва')
        print(city)

        rest = Restaurant(name=rest_name, short_description=short_desc, address=address,
                          full_description=full_desc, google_map_link=glink)
        rest.save()
        rest.cities.add(city.id)

        categories_id = get_category(categories)
        for i in categories_id:
            rest.categories.add(i)

