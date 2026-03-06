data = [
    {"name": "Ravi", "age": "25", "salary": "50000"},
    {"name": "Anita", "age": None, "salary": "60000"},
    {"name": "John", "age": "30", "salary": None}
]


cleaned_data = []

for row in data:
    if None not in row.values():
        cleaned_data.append(row)

print(cleaned_data)