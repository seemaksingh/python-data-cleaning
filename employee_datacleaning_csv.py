"""write a code to clean the employee data by removing any rows that contain missing values. 
The data is stored in a CSV file called "employee.csv". 
The cleaned data should be stored in a new CSV file called "cleaned_employee_data.csv"."""

#import csv file and convert the csv rows into a list of dictionaries
import csv
data =[]
with open("employees.csv","r") as file:
    reader=csv.DictReader(file)  #it will read the csv file and convert each row into a dictionary
    for row in reader:
        data.append(row)

    print("Raw Data:",data)

#Handling Nulls
cleaned_data = []
for row in data:
    if ("" not in row.values()) and (None not in row.values()):
        cleaned_data.append(row)
print("Data after handling nulls:", cleaned_data)

#Removing Duplicates
unique_data = []
seen = set()
for row in cleaned_data:
    identifier=tuple(row.items())  #convert the dictionary into a tuple of key-value pairs
    if identifier not in seen:
        seen.add(identifier)
        unique_data.append(row)
print("Data after removing duplicates:", unique_data)

#Converting Data Types
for row in unique_data:  #iterate through each row in the unique_data list
    for key, value in row.items():  #iterate through each key-value pair in the row dictionary
        for convert in (int, float):  #created a tuple of conversions to try (int and float)
            try:                       #it will try to convert to int, if it fails it try to convert to float, if it fails it will pass and move to
                row[key] = convert(value)
                break                  #if the conversion is successful, Python stops trying other conversions. 
            except ValueError:         #If both conversions fail, it will pass and keep the original value as a string.
                pass
print("Data after converting data types:", unique_data)