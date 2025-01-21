import re

import pandas as pd

excel_file_name_list = ['新日月', '小柏', '商汇通', '润家', '居家乐', '九如城', '安康通']

export_list = []

for excel_file_name in excel_file_name_list:
    excel_file = pd.read_excel(f'/Users/yinqichao/Desktop/镇海居家上门/旧系统数据/服务老人1025/{excel_file_name}.xlsx',
                               sheet_name=excel_file_name)
    for i in excel_file.index:
        no = excel_file.values[i, 0]
        name = str(excel_file.values[i, 1])
        gender = str(excel_file.values[i, 2])
        tel_phone = str(excel_file.values[i, 5])
        temp = re.findall(r"1\d{10}", str(tel_phone))
        phone = temp[0] if len(temp) > 0 else ''

        tel_phone = str(tel_phone).replace(phone, '')
        temp = re.findall(r"\d{8}", str(tel_phone))
        other_tel = temp[0] if len(temp) > 0 else ''

        remark = str(excel_file.values[i, 9])
        # print(excel_file_name, no, name, gender, phone, other_tel)

        if not name is None and len(name) > 0:
            export_list.append([
                name,
                gender if not gender is None and len(gender) > 0 else '',
                phone if not phone is None and len(phone) > 0 else '',
                other_tel if not other_tel is None and len(other_tel) > 0 else '',
                remark if not remark is None and len(remark) > 0 and remark != 'nan' else ''
            ])

# print(export_list)

# list转dataframe
df = pd.DataFrame(export_list, columns=['客户名称', '性别', '联系号码', '其他号码', '备注'])

# 保存到本地excel
df.to_excel("导入老人名单.xlsx", index=False)
