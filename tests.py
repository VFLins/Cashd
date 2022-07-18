import csv


with open('C:\\Users\\vflin\\OneDrive\\Documentos\\GitHub\\Cashd\\data\\random_names.csv', newline='') as f:
    reader = csv.reader(f)
    ACCOUNTS = [str(row) for row in reader]

print(ACCOUNTS)