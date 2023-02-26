from random import randint
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string

print('HI piple')
columns_count = int(input('Ввидите ширину маирицы: ')) 
rows_count = int(input('Ввидите высоту матрицы: '))
#print(columns_count, rows_count)
#print(randint(1, 100))

# создаем книгу 
wb = Workbook()
# делаем единственный лист активным 
ws = wb.active
ws.title = input("Введите название страницы: ")

for colum in range(columns_count):
#    ws[f"A{colum+1}"] = colum
    for row in range(rows_count):
#        ws.
#        print("\nтекущий столбик: ", colum)
#        print("текущий строка: ", row)
# wb.save("AZAZA.xls")