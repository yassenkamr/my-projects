the_own_books = []
the_wishlist_books = []

the_own_q = input ('enter the name of a book you own :').lower()

the_own_books.append(the_own_q)

sec_own = input ('enter the name of another book you have(or press enter to skip) :').lower()

if sec_own :
    the_own_books.append(sec_own)

print (f'your library {the_own_books}')

the_wish_q = input ('enter the name of a book you wish to have (or press enter to skip) :').lower()

if the_wish_q :
    the_wishlist_books.append(the_wish_q)

sec_wish = input ('enter the name of onther book you wish to have (or press enter to skip) :').lower()

if sec_wish :
    the_wishlist_books.append(sec_wish)

print (f'your wishlist {the_wishlist_books}')

the_acq_q = input ('enter the name of a book in your wishlist you have acquired (or press enter to start) :').lower()

if the_acq_q :
    the_own_books.append(the_acq_q)
    the_wishlist_books.remove(the_acq_q)

print (f'update your own books :{the_own_books}')
print (f'update your wishlist books:{the_wishlist_books}')

the_donation_q = input ('enter the name of a book from your library you want to donate (or press enter to skip) :').lower()

if the_donation_q :
    the_own_books.remove(the_donation_q)

print (f'the final library after donatoins {the_own_books}')
