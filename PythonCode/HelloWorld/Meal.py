menus = {'Breakfast' : ['Sandwich', 'Tea', 'Coffee'],
         'Lunch' : ['Paneer Bhurji', 'Chapati'],
         'Dinner' : ['Soup', 'Salad', 'Taco']
         }

print('\n')
for name, menu in menus.items():
    for item in menu:
       print(name, ' : ', item)

