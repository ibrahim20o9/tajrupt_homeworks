# integer 5

n = 47
tens = n // 10  # десятки
units = n % 10  # единицы
result = units * 10 + tens
print(f"Новое число:", result)

# integer 6
n = 123
hundreds = n // 100  # сотни
tens = (n // 10) % 10  # десятки
units = n % 10  # единицы
result = units * 100 + tens * 10 + hundreds
print(f"Новое число:", result)
