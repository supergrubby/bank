import csv

def replace_string_with_int(line):
    line

def cluster_age(age):
    if age <= 30:
        return 1
    elif 30 < age <= 40:
        return 2
    elif 40 < age <= 50:
        return 3
    elif age > 50:
        return 4


def cluster_balance(balance):
    if balance < 0:
        return 1
    elif 0 <= balance < 1000:
        return 2
    elif balance >= 1000:
        return 3


# age;"job";"marital";"education";"default";"balance";"housing";"loan";"contact";"day";"month";"duration";"campaign";"pdays";"previous";"poutcome";"y"

with open("bank.csv") as f, open('processed_bank.csv', 'wb') as result:
    csv_writer = csv.writer(result)

    titles = f.readline().strip().replace("\"", "").split(";")
    csv_writer.writerow([x for x in titles])

    next(f)
    for line in f:
        item = line.strip().replace("\"", "") \
            .replace("primary", "1") \
            .replace("secondary", "2") \
            .replace("tertiary", "3") \
            .replace("unknown", "0") \
            .replace("single", "1") \
            .replace("married", "2") \
            .replace("divorced", "3") \
            .replace("admin.", "1") \
            .replace("blue-collar", "2") \
            .replace("entrepreneur", "3") \
            .replace("housemaid", "4") \
            .replace("management", "5") \
            .replace("retired", "6") \
            .replace("self-employed", "7") \
            .replace("services", "8") \
            .replace("student", "9") \
            .replace("technician", "10") \
            .replace("unemployed", "11") \
            .replace("no", "0") \
            .replace("yes", "1") \
            .split(";")
        # age
        item[0] = cluster_age(float(item[0]))
        # balance
        item[5] = cluster_balance(float(item[5]))

        csv_writer.writerow([x for x in item])
