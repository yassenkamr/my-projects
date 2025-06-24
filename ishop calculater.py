print('**** Welcome to iShop Calculator ****')

item_prices = []  
item_names = []

total_items = input('\nHow many items do you have: ')

while not total_items.isdigit():
    total_items = input('Please enter a valid number: ')

total_items = int(total_items)


print("\nLet's count them!")

for i in range(1, total_items + 1):
    name = input(f'\nEnter name for item #{i}: ')

    while not name.replace (' ', '').isalpha():
        name = input('Please enter a valid name: ')
    
    price = input('Enter price for this item (EGP): ')

    while not price.isdigit():
        price = input('Please enter a valid price: ')

    price = int(price)
    
    item_names.append(name)
    item_prices.append(price)

done_shopping = input('\nAre you done with your shopping? (yes/no): ').lower()

while done_shopping not in ['yes', 'no']:
    done_shopping = input('Please enter either "yes" or "no": ').lower()

if done_shopping == 'yes':
    calculate_total = input('Do you want to calculate your total price? (yes/no): ').lower()

    while calculate_total not in ['yes', 'no']:
        calculate_total = input('Please enter either "yes" or "no": ').lower()

    if calculate_total == 'yes':
        print('\n==== Your Receipt ====')
        for i in range(len(item_names)):
            print(f'{i + 1}. {item_names[i]}: {item_prices[i]} EGP')
        print('======================')
        print(f'Total: {sum(item_prices)} EGP')

else:
    add_more = input('Do you want to add more items? (yes/no): ').lower()
    
    while add_more not in ['yes', 'no']:
        add_more = input('Please enter either "yes" or "no": ').lower()

    if add_more == 'yes':
        extra_items = input('\nHow many more items do you want to add: ')
        
        while not extra_items.isdigit():
            extra_items = input('Please enter a valid number: ')

        extra_items = int(extra_items)

        for j in range(1, extra_items + 1):
            name = input(f'\nEnter name for extra item #{j}: ')

            while not name.replace (' ', '').isalpha():
                name = input('Please enter a valid name: ')
            
            price = input('Enter price for this item (EGP): ')

            while not price.isdigit():
                price = input('Please enter a valid price: ')

            price = int(price)
            
            item_names.append(name)
            item_prices.append(price)

    done_after_add = input('\nNow are you done with your shopping? (yes/no): ').lower()

    while done_after_add not in ['yes', 'no']:
        done_after_add = input('Please enter either "yes" or "no": ').lower()

    if done_after_add == 'yes':
        calculate_total = input('Do you want to calculate your total price? (yes/no): ').lower()
        
        while calculate_total not in ['yes', 'no']:
            calculate_total = input('Please enter either "yes" or "no": ').lower()

        if calculate_total == 'yes':
            print('\n==== Your Receipt ====')
            for i in range(len(item_names)):
                print(f'{i + 1}. {item_names[i]}: {item_prices[i]} EGP')
            print('======================')
            print(f'Total: {sum(item_prices)} EGP')
