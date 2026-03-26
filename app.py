data = ["  Apple", "Banana  ", "  Mango  ", "Orange"]

cleaned_data = [item.strip().lower() for item in data]

print("Cleaned Data:", cleaned_data)