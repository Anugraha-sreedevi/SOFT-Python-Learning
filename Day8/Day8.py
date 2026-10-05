person = {
    'first_name': 'Anugraha',
    'last_name': 'S',
    'age': 250,
    'country': 'Kochi',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'C++', 'Python'],
    'address': {
        'street': 'Space street'
    }
}

print(person.get('first_name'))  # Anugraha
print(person.get('last_name'))   # S    
print(person.get('country'))     # Kochi
print(person.get('skills'))      # ['JavaScript', 'React', 'Node', 'C++', 'Python']
print(person.get('city'))        # None