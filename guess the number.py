import random
the_password_number = int(input ('please write 1 digits :'))

the_random_number = random.randint(1,9)

if the_password_number == the_random_number :
  print ('we are same')
elif the_password_number != the_random_number :
  print ('we are not same ' + 'my number is ' + str (the_random_number))
else :
  print ('please write 4 digits')