import csv


# copying emails into a new file
def findEmails(fromfile, email):
    with open(fromfile, 'r') as csvReader:
        csv_reader = csv.DictReader(csvReader)
    # next(csv_reader)  # Loops first row
        with open(email, 'w') as writescv:
            emailField = ['email']
            csv_writer = csv.DictWriter(
                writescv, fieldnames=emailField, delimiter='\t')
            for line in csv_reader:
                del line['first_name']
                del line['last_name']
                csv_writer.writerow(line)
            print("Copying Email ... Done")


findEmails('names.csv', 'email.csv')


# creating a copy of the file with -
def copycsv(old, new):
    with open(old, 'r') as rfile:
        reader = csv.reader(rfile)
        with open(new, 'w') as wfile:
            writer = csv.writer(wfile, delimiter='\t')
            for line in reader:
                writer.writerow(line)
            print("Done..")


# copycsv('names.csv', 'updated.csv')

# Using csv-dict
with open('names.csv', 'r') as readfile:
    reader = csv.DictReader(readfile)
    with open("new-csv-file.csv", 'w') as writefile:
        fieldNames = ['first_name', 'last_name', 'email']
        writer = csv.DictWriter(
            writefile, fieldnames=fieldNames, delimiter='\t')
        # header text
        writer.writeheader()
        for line in reader:
            pass
            # writer.writerow(line)  # Writing to the file each line
