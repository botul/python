import openpyxl
import os
wb = openpyxl.load_workbook('example1.xlsx')
ws = wb['Arkusz1']
d=''
new_d=''
i = 0
for row in ws.iter_rows(min_col=2, max_col=2, min_row=2, max_row=11):
    for cell in row:
        d = str(cell.value)
        new_d = d[:-3]
        cell.value=new_d

wb.save('gotowe.xlsx')




