import csv

def replace_string_with_int(line):
    line

def cluster_age(age):
    if age <= 25:
        return 1
    elif 25 < age <= 35:
        return 2
    elif 35 < age <= 50:
        return 3
    elif age > 50:
        return 4


# def cluster_balance(balance):
#     if balance < 0:
#         return 1
#     elif 0 <= balance < 1000:
#         return 2
#     elif balance >= 1000:
#         return 3


# age;"job";"marital";"education";"default";"balance";"housing";"loan";"contact";"day";"month";"duration";"campaign";"pdays";"previous";"poutcome";"y"

with open("bank-additional-full.csv") as f, open('processed-bank-additional-full.csv', 'wb') as result:
    csv_writer = csv.writer(result)

    titles = f.readline().strip().replace("\"", "").split(";")
    csv_writer.writerow([x for x in titles])

    next(f)
    for line in f:
        item = line.strip().replace("\"", "") \
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
            .replace("basic.4y","1")\
            .replace("basic.6y","2")\
            .replace("basic.9y","3")\
            .replace("high.school","4")\
            .replace("illiterate","5")\
            .replace("professional.course","6")\
            .replace("university.degree","7")\
            .replace("no", "0") \
            .replace("yes", "1") \
            .split(";")
        # age
        item[0] = cluster_age(float(item[0]))

        csv_writer.writerow([x for x in item])
