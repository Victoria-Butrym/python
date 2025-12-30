age = int(input('What is your age?: '))

# if (age >= 18 and age < 50):
#     print('You can be a bartender')
# else:
#     print('Nope')

legal_age_ternar = True if age > 18 else False
legal_age = age > 18

print(legal_age)
print(legal_age_ternar)