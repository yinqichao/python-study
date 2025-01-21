import datetime

import pandas as pd
from docxtpl import DocxTemplate

xuqiu_excel = pd.read_excel('/Users/yinqichao/Downloads/新建村需求变更最终版.xlsx')

muban_doc = DocxTemplate("/Users/yinqichao/Downloads/周报/模板.docx")

start_date = datetime.datetime.strptime('2023-01-09', '%Y-%m-%d')

for i in range(0, 201, 3):

    end_date = start_date + datetime.timedelta(days=4)

    date = start_date.strftime('%Y.%m.%d') + '-' + end_date.strftime('%Y.%m.%d')

    thisWeekContent = (
        f'1、{xuqiu_excel.values[i, 0]}-{xuqiu_excel.values[i, 1]}-{xuqiu_excel.values[i, 2]}-{xuqiu_excel.values[i, 3]}\n'
        f'2、{xuqiu_excel.values[i + 1, 0]}-{xuqiu_excel.values[i + 1, 1]}-{xuqiu_excel.values[i + 1, 2]}-{xuqiu_excel.values[i + 1, 3]}\n'
        f'3、{xuqiu_excel.values[i + 2, 0]}-{xuqiu_excel.values[i + 2, 1]}-{xuqiu_excel.values[i + 2, 2]}-{xuqiu_excel.values[i + 2, 3]}\n'
        f'\n'
    )

    nextWeekContent = (
        f'1、{xuqiu_excel.values[i + 3, 0]}-{xuqiu_excel.values[i + 3, 1]}-{xuqiu_excel.values[i + 3, 2]}-{xuqiu_excel.values[i + 3, 3]}\n'
        f'2、{xuqiu_excel.values[i + 4, 0]}-{xuqiu_excel.values[i + 4, 1]}-{xuqiu_excel.values[i + 4, 2]}-{xuqiu_excel.values[i + 4, 3]}\n'
        f'3、{xuqiu_excel.values[i + 5, 0]}-{xuqiu_excel.values[i + 5, 1]}-{xuqiu_excel.values[i + 5, 2]}-{xuqiu_excel.values[i + 5, 3]}\n'
    )

    context = {
        "date": date,
        "thisWeekContent": thisWeekContent,
        "nextWeekContent": nextWeekContent,
    }
    muban_doc.render(context)
    muban_doc.save("/Users/yinqichao/Downloads/周报/【" + start_date.strftime('%Y') + "项目周报" + start_date.strftime(
        '%m.%d') + "-" + end_date.strftime('%m.%d') + "】新建村未来乡村数字化项目周报.docx")

    start_date = start_date + datetime.timedelta(days=7)

    # 抛开节假日
    if (start_date.strftime('%Y.%m.%d') == '2023.01.23'
            or start_date.strftime('%Y.%m.%d') == '2023.05.01'
            or start_date.strftime('%Y.%m.%d') == '2023.10.02'
            or start_date.strftime('%Y.%m.%d') == '2024.02.12'
            or start_date.strftime('%Y.%m.%d') == '2024.04.29'):
        start_date = start_date + datetime.timedelta(days=7)
