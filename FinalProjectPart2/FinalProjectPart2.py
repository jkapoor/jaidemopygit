# Jai Kapoor 1901832 FinalProjectPart2 

import csv
import os
from datetime import datetime
import operator

# reads input file PriceList.csv, creates and populates dictionary with prices
with open('PriceList.csv', 'r') as input_file2:
    reader = csv.reader(input_file2)
    item_price = {}
    for row in reader:
        item_price[row[0]] = row[1]

# reads input file ServiceDatesList.csv, creates and populates dictionary with dates
with open('ServiceDatesList.csv', 'r') as input_file3:
    reader = csv.reader(input_file3)
    item_service_dates = {}
    for row in reader:
        item_service_dates[row[0]] = row[1]

# reads input file ManufacturerList.csv, creates and populates dictionary with all required fields
with open('ManufacturerList.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    items = {}
    for row in reader:
        items[row[0]] = {
            'manufacturer': row[1],
            'type': row[2],
            'price': item_price[row[0]],
            'serviceDate': item_service_dates[row[0]],
            'damaged': row[3]
        }


types = []
for v in items:
    new_type = items[v]['type']
    if new_type not in types:
        types.append(items[v]['type'])

# writes tempFullInventory.csv
with open('tempFullInventory.csv', 'w', newline='') as f:
    writer = csv.writer(f, escapechar=' ', quoting=csv.QUOTE_NONE)
    for v in items:
        line = (
            v, items[v]['manufacturer'], items[v]['type'], items[v]['price'], items[v]['serviceDate'],
            items[v]['damaged'])
        writer.writerow(line)
    f.close()

# sort tempFullInventory.csv by manufacturer name
with open('tempFullInventory.csv', 'r') as sort_file:
    csvWorking = csv.reader(sort_file, delimiter=',')
    tempsort = sorted(csvWorking, key=operator.itemgetter(2))

    # write final FullInventory.csv sorted by name
    with open('FullInventory.csv', 'w', newline='') as f:
        for sortedline in tempsort:
            csv.writer(f).writerow(sortedline)
    sort_file.close()

# adds manufacturer and type values to item_man_types list
item_man_types = []
for k in items:
    item_man_types.append(items[k]['manufacturer'])
    item_man_types.append(items[k]['type'])

user_query = ''

while user_query != 'q':

    user_query = input("Enter manufacturer and item type: ")
    x = user_query.split()
    results_by_man = {}

    # creates writer object
    with open('tempPriceSort.csv', 'w', newline='') as f:
        writer = csv.writer(f, escapechar=' ', quoting=csv.QUOTE_NONE)
    # for every element of user input
        for a in x:
            if any(a in s for s in item_man_types):
                for k in items:
                    my_date = datetime.strptime(items[k]['serviceDate'], "%m/%d/%Y")
                    if my_date > datetime.today() and items[k]['damaged'] != 'damaged':
                        if items[k]['manufacturer'] == a:
                            results_by_man[k] = {
                                'manufacturer': items[k]['manufacturer'],
                                'type': items[k]['type'],
                                'price': items[k]['price'],
                            }
                if len(results_by_man.keys()) == 0:
                    print('No such item in inventory')

                for m in x:
                    for j in results_by_man:
                        if results_by_man[j]['type'] == m:
                            line = (j, results_by_man[j]['manufacturer'], results_by_man[j]['type'],
                                    results_by_man[j]['price'])
                            writer.writerow(line)

    f.close()
    # reads temp csv with items related to input, sorts by price in descending order
    with open('tempPriceSort.csv', 'r') as sort_file:
        csvWorking = csv.reader(sort_file, delimiter=',')
        tempsort = sorted(csvWorking, key=operator.itemgetter(3), reverse=True)
        with open('finalPriceSort.csv', 'w', newline='') as f:
            for sortedline in tempsort:
                csv.writer(f).writerow(sortedline)
        sort_file.close()

    # prints first row (most expensive item) from finalPriceSort.csv
    with open('finalPriceSort.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print('Your item is:', *row)
            break


        os.remove('tempPriceSort.csv')
        os.remove('finalPriceSort.csv')

