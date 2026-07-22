python = "Coding For All"
python.replace("Coding","Python")
print(python)

python = "Python for Everyone"
python.replace("Everyone","All")
print(python)

python = "Coding For All"
result = python.split(" ")
print(result)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list = companies.split(",")
print(companies_list.index("Facebook"))

python = "Coding For All"
print(python[len(python)-1])

python = "Python for Everyone"
python_list = python.split(" ")
Acronim = python_list[0][0] + python_list[1][0] + python_list[2][0]
print(Acronim)

python = "Coding For All"
python_list = python.split(" ")
Acronim = python_list[0][0] + python_list[1][0] + python_list[2][0]
print(Acronim)

python = "Coding For All"
print(python.index("C"))

python = "Coding For All"
print(python.index("F"))

python = "You cannot end a sentence with because because because is a conjunction"
print(python.index("because"))
python = "You cannot end a sentence with because because because is a conjunction"
print(python.rindex("because"))

python = "You cannot end a sentence with because because because is a conjunction"
start = python.index("because")
end = start + len("because because because")
print(python[start:end])
python = "You cannot end a sentence with because because because is a conjunction"
print(python.index("because because because"))

python = "   Coding For All      "
python = python.strip()
print(python)

python = "30DaysOfPython"
print(python.isidentifier())
python = "thirty_days_of_python"
print(python.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

result = " # ".join(libraries)

print(result)

python = "I am enjoying this challenge.\nI just wonder what is next."
print(python)

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")