import csv

# Header
employee_file = open('D:/repos/GUICanSatTT/examples/employee_file.csv', mode = 'at', newline = '')

employee_writer = csv.writer(employee_file, delimiter=',')
employee_writer.writerow(['10666', '-9660', '660'])