print('**** Welcome to iShop Calculator ****')

prices = []  
items = []

x = int(input('\nHow many items do you have: '))

print("\nLet's count them!")

for i in range(1, x + 1):
    item = input(f'\nPlease enter the name of item number {i}: ')
    price = int(input('Please enter the price of the item: '))
    items.append(item)
    prices.append(price)

ask1 = input('\nAre you done with your shopping? (yes/no): ').lower()

if ask1 == 'yes':
    ask2 = input('Do you want to calculate your total price? (yes/no): ').lower()

    if ask2 == 'yes':
        print('\n==== Your Receipt ====')
        for i in range(len(items)):
            print(f'{i+1}. {items[i]}: {prices[i]} EGP')
        print('======================')
        print(f'Total: {sum(prices)} EGP')

else:
    ask3 = input('Do you want to add more items? (yes/no): ').lower()
    if ask3 == 'yes':
        x2 = int(input('\nHow many more items do you want to add: '))

        for j in range(1, x2 + 1):
            item2 = input(f'\nPlease enter the name of extra item number {j}: ')
            price2 = int(input('Please enter the price of the item: '))
            items.append(item2)
            prices.append(price2)

    ask4 = input('\nNow are you done with your shopping? (yes/no): ').lower()

    if ask4 == 'yes':
        ask5 = input('Do you want to calculate your total price? (yes/no): ').lower()

        if ask5 == 'yes':
            print('\n==== Your Receipt ====')
            for i in range(len(items)):
                print(f'{i+1}. {items[i]}: {prices[i]} EGP')
            print('======================')
            print(f'Total: {sum(prices)} EGP')
