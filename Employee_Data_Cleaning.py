# Raw Data
#Handling null values
#Coverting data types
#Filtering
#Removing Duplicates

data=[
    {"name": "Ravi", "age": "25", "salary": "50000"},
    {"name": "Anita", "age": None, "salary": "60000"},
    {"name": "John", "age": "30", "salary": None},
    {"name": "Ravi", "age": "25", "salary": "50000"},  
    {"name": "Meena", "age": "28", "salary": "45000"}
]

print("Raw Data:",data)

#Handling Nulls
cleaned_data = []
for row in data:
    if None not in row.values():
        cleaned_data.append(row)

print("Data after handling nulls:", cleaned_data)

#Removing Duplicates
unique_data = []
seen = set()
for row in cleaned_data:
    identifier=(row['name'], row['age'], row['salary'])
    if identifier not in seen:
        seen.add(identifier)
        unique_data.append(row)

print("Data after removing duplicates:", unique_data)

#Converting Data Types
for row in unique_data:
    row['age'] = int(row['age'])
    row['salary'] = int(row['salary'])

print("Data after converting data types:", unique_data)

#Filtering Data(keep employees with salary > 45000)
filtered_data = [row for row in unique_data if row['salary'] > 45000]
"""for row in unique_data:
    if row["salary"] > 45000:
        filtered_data.append(row)"""
print("Filtered data:",filtered_data)
