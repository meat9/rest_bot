import pandas as pd



filename = 'Рестораны.xlsx'





link = 'Ссылка на гугл карты'
option1 = 'Веранда'
option2 = 'Завтраки'
option3 = 'Дог-френдли'

data_file = pd.read_excel(filename, sheet_name='Москва')

category_list = set()
# создаем категории
for i in data_file.index:
    category_list.add(data_file['Категория 1'][i])
    category_list.add(data_file['Категория 2'][i])
    category_list.add(data_file['Категория 3'][i])





# Создаем рестораны
# for i in data_file.index:
#     rest_name = data_file['Название ресторана'][i]
#     short_desc = data_file['Описание ресторана'][i]
#     address = data_file['Адрес ресторана'][i]
#     full_desc = data_file['Описание полное'][i]
