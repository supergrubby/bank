import csv

with open("bank.csv") as f, open('processed-bank.csv', 'wb') as result:
    csv_writer = csv.writer(result)

    titles = f.readline().strip().replace("\"", "").split(";")
    csv_writer.writerow([x for x in titles])

    next(f)
    for line in f:
        item = line.strip().replace("\"", "").split(";")
        csv_writer.writerow([x for x in item])
