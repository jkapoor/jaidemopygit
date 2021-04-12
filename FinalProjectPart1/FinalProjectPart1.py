# Jai Kapoor 1901832 FinalProjectPart1

import csv
import os
from datetime import date
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
        items[row[0]] = {'manufacturer': row[1], 'type': row[2], 'price': item_price[row[0]],
                         'serviceDate': item_service_dates[row[0]], 'damaged': row[3]}

# appends item types to types
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
        v, items[v]['manufacturer'], items[v]['type'], items[v]['price'], items[v]['serviceDate'], items[v]['damaged'])
        writer.writerow(line)
    f.close()

# sort tempFullInventory.csv by manufacturer name
with open('tempFullInventory.csv', 'r') as sort_file:
    csvWorking = csv.reader(sort_file, delimiter=',')
    tempsort = sorted(csvWorking, key=operator.itemgetter(1))

# write final FullInventory.csv sorted by name
    with open('FullInventory.csv', 'w', newline='') as f:
        for sortedline in tempsort:
            csv.writer(f).writerow(sortedline)
    sort_file.close()

# removes temp file
os.remove("tempFullInventory.csv")

# writes tempDamagedInventory.csv
with open('tempDamagedInventory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for v in items:
        if items[v]['damaged'] == 'damaged':
            line = (v, items[v]['manufacturer'], items[v]['type'], items[v]['price'], items[v]['serviceDate'],
                    items[v]['damaged'])
            writer.writerow(line)
    f.close()

# sorts tempDamageInventory.csv by damage status
with open('tempDamagedInventory.csv', 'r') as sort_file:
    csvWorking = csv.reader(sort_file, delimiter=',')
    tempsort = sorted(csvWorking, key=operator.itemgetter(3), reverse=True)

# writes final DamagedInventory.csv sorted by cost
    with open('DamagedInventory.csv', 'w', newline='') as f:
        for sortedline in tempsort:
            csv.writer(f).writerow(sortedline)
    sort_file.close()
os.remove("tempDamagedInventory.csv")

# writes tempPastServiceDateInventory
from datetime import datetime
with open('tempPastServiceDateInventory.csv', 'w', newline='') as f:
    writer = csv.writer(f, escapechar=' ', quoting=csv.QUOTE_NONE)
    for v in items:
        # converts string argument to datetime
        my_date = datetime.strptime(items[v]['serviceDate'], "%m/%d/%Y")
        if my_date < datetime.today():
            line = (v, items[v]['manufacturer'], items[v]['type'], items[v]['price'], items[v]['serviceDate'],
                    items[v]['damaged'])
            writer.writerow(line)
    f.close()

# sorts tempPastServiceDateInventory.csv by date
with open('tempPastServiceDateInventory.csv', 'r') as sort_file:
    csvWorking = csv.reader(sort_file, delimiter=',')
    tempsort = sorted(csvWorking, key=operator.itemgetter(4))

# writes final PastServiceDateInventory
    with open('PastServiceDateInventory.csv', 'w', newline='') as f:
        for sortedline in tempsort:
            csv.writer(f).writerow(sortedline)
    sort_file.close()
os.remove("tempPastServiceDateInventory.csv")

filename = 'Inventory.csv'

# writes InventoryTypes.csv for each inventory type
for t in types:
    tcap = t.capitalize()
    tempName = tcap + filename
    finalName = tcap + filename

    with open(tempName, 'w', newline='') as f:
        writer = csv.writer(f, escapechar=' ', quoting=csv.QUOTE_NONE)
        for v in items:
            if items[v]['type'] == t:
                line = (v, items[v]['manufacturer'], items[v]['price'], items[v]['serviceDate'], items[v]['damaged'])
                writer.writerow(line)
        f.close()

    with open(tempName, 'r') as sort_file:
        csvWorking = csv.reader(sort_file, delimiter=',')
        tempsort = sorted(csvWorking, key=operator.itemgetter(0))
        with open(finalName, 'w', newline='') as f:
            for sortedline in tempsort:
                csv.writer(f).writerow(sortedline)
        sort_file.close()
        
