import csv

with open("olympics.txt","r") as file_ref:
    reader = csv.reader(file_ref)
    print(next(reader))
    print("============================================")

    for line in reader:
        if line[5] != 'NA':
            print(f"NAME: {line[0]} \nEVENT: {line[4]} \nMEDAL: {line[5]}")
            print("================")
