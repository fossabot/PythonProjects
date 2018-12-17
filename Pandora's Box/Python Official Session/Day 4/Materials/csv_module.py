import csv

print('-' * 50)

# Create the CSV File
csv_fname = 'data.csv'
csv_file = open(csv_fname, 'w', newline='')

# Configure the CSV File
csv_writer = csv.writer(csv_file,
                        delimiter=',')

# Write the contents to the CSV File
csv_writer.writerow(('Script Name', 'Version'))
csv_writer.writerows((('Python Script', '3.7'),
                      ('Perl Script', '5.6'),
                      ('PHP', '5.5')))

csv_writer.writerows((('Script 1', '3.7'),
                      ('Script 2', '5.6'),
                      ('Script 3', '5.5')))

csv_writer.writerows((('Script 4', '3.7'),
                      ('Script 5', '5.6'),
                      ('Script 6', '5.5')))

csv_writer.writerows((('Script 7', '3.7'),
                      ('Script 8', '5.6'),
                      ('Script 9', '5.5')))

print('CSV File Written')
csv_file.close()

print('-' * 50)

# Read the contents of CSV File
with open(csv_fname) as read_csv:
    '''
    for row in csv.DictReader(read_csv):
        print('Record ->', row)
    '''
    recs = [{head: value for head, value in row.items()}
             for row in csv.DictReader(read_csv)]

    for rec in recs:
        print('Record ->', rec)

print('-' * 50)

for line in recs[-3:]:
    print('Line ->', line)

print('-' * 50)

print('Particular Value ->', recs[8]['Script Name'])

print('-' * 50)
