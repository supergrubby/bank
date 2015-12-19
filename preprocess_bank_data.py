import csv

with open("bank.csv") as f, open('processed_bank.csv', 'wb') as result:
    csv_writer = csv.writer(result)

    for line in f:

        item = line.strip().replace("\"","")\
            .replace("primary","1")\
            .replace("secondary","2")\
            .replace("tertiary","3")\
            .replace("unknown","0")\
            .replace("single","1")\
            .replace("married","2")\
            .replace("divorced","3")\
            .replace("admin.","1")\
            .replace("blue-collar","2")\
            .replace("entrepreneur","3")\
            .replace("housemaid","4")\
            .replace("management","5")\
            .replace("retired","6")\
            .replace("self-employed","7")\
            .replace("services","8")\
            .replace("student","9")\
            .replace("technician","10")\
            .replace("unemployed","11")\
            .replace("no","0")\
            .replace("yes","1")\
            .split(";")
        csv_writer.writerow([x for x in item])
