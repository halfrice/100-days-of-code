city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pets name?\n")
print('Your band name could be ' + city + ' ' + pet)

# For extra credit, look up python string interpolation
print('Your band name could be %s %s' % (city, pet))

# Also check out fstrings, my personal choice
print(f'Your band name could be {city} {pet}')
