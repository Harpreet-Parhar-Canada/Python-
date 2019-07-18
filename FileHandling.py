# Downloaded Census by Community - 2018
# Use Python to read/import data:

#readlines: reads until end of file using readline (reads single line from file). Returns list for each line

def read_file():
    file = open('Census_by_Community_2018.csv', 'r')
    contents = file.readlines()[1:]
    dict = {}
    sectordict = {}
    count = 0

    for item in contents:
        count = count + 1
        split_item = item.split(',')

        if(split_item[0] in dict.keys()):
            dict[split_item[0]] = dict[split_item[0]] + int(split_item[9])      #update the value of the non-unique key
        else:
            dict[split_item[0]] = int(split_item[9])                            #assign unique key/value pair

        if(split_item[4] in sectordict.keys()):
            sectordict[split_item[4]] = sectordict[split_item[4]] + int(split_item[9])
        else:
            sectordict[split_item[4]] = int(split_item[9])

    string1 = ''
    for item in dict:
        string1 = string1 + f"{format(item, '30')} {format(dict[item],'10,d')} \n"

    string2 = ''
    for item in sectordict:
        string2 = string2 + f"{format(item, '30')} {format(sectordict[item], '10,d')} \n"

    text_file = open('Census_Report.txt', 'w+')
    text_file.write('Summary of 2018 Calgary Census Data : \n')
    text_file.write(f"Total Count: {format(count, '10')} \n \n")
    text_file.write('Summary by Classification: \n')
    text_file.write(string1)
    text_file.write('\nSummary by Sector: \n')
    text_file.write(string2)
    text_file.close()

read_file()

