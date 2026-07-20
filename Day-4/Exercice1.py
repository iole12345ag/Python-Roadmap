separate = "Thirty","Days","Of","Python"
together = " ".join(separate)
print(together)

separate_2 = 'Coding', 'For' , 'All'
together_2 = " ".join(separate_2)
print(together_2)

print(len(together_2))
together_2 = together_2.upper()
print(together_2)

together_2 = together_2.lower()
print(together_2)

together_2 = together_2.capitalize()
print(together_2)

together_2 = together_2.title()
print(together_2)

together_2 = together_2.swapcase()
print(together_2)

together_2 = together_2.swapcase()
print(together_2)

print(together_2[6:]) #Only prints " For All"

print(together_2.find("Coding"))

if together_2.find("Coding") >= 0:
    print("True")
else:
    print("False")


