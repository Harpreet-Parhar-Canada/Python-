from openpyxl import load_workbook
wb = load_workbook(filename = 'Invoice-Example.xlsx')

def reading_Data():
    list_Excel = []
    innerList =[]
    for sheet in wb:
        ws = wb.get_sheet_by_name(sheet.title)
        for row in ws.values:
             innerList.append(row)
        list_Excel.append(innerList)
    return list_Excel

def particular_Column():
    listEmpty=[]
    listInner=[]
    listEmpty = reading_Data()
    for 
    for item in listEmpty:
        if item in listEmpty:
         print("Its is:",listEmpty[0])
        else:
         print("its is not true",item[0])


def display_list_linebyline():
    list_Excel=reading_Data()
    for item  in list_Excel:
        print(list(item))

# display_list_linebyline()
particular_Column()