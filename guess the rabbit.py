import random

#welcome
print ('welcome to place the rabbit ')

#shape
shape = [['.' , '.' , '.'] , ['.' , '.' , '.'] , ['.' , '.' , '.']]

print ( '' , shape[0] , '\n' , shape[1] , '\n' , shape[2])

#ask
print ('where should the rabbit go?')
ask = input ('pls choose a row and a column and put between it comma').split(',')

#ai
row = shape = random.randint(0,2)
column = shape = random.randint(0,2)

#resalt
if row == ask[0] and column == ask[1] :
    print ('you win')

else :
    print ('sr but you lost')
