import re
import os
import random
global a,b,c,d


def createBankAcc(a,b,c,d):
  customer = open('customer.txt', 'a')
  customer.write(a)
  customer.write(b)
  customer.write(c)
  customer.write(d)
  passw=""
  for i in range(1,10):
    passw+= str(random.randrange(1,9))

    customer.write(passw)
  print('The customer\'s password is: '+passw )
  print()
  print('1. Create new bank account')
  print('2. Check account details')
  print('3. logout')
  x = input('Enter and option')
  if x=='1':
      print('Enter the following details please: ')
      a = input('Account Name: ')
      b = input('Opening Balance: ')
      c = input('Account Type: ')
      d = input('Account Email: ')
      createBankAcc(a,b,c,d)
  elif x=='2':
      checkAppDet()
  else:
      logout()

  
def login(userName, pword):
  myStr= open('staff.txt', 'r').read()
  y= str(myStr)
  x = re.search(userName, y )
  userName=x.group()
  z= re.search(pword,y)
  pword= z.group()
  if pword=='none' or userName=='none':
    print('wrong password or username')
    start()
  else:
    session= open('session.txt','a')
    session.write(userName)
    print('You have been logged in')
    print('1. Create new bank account')
    print('2. Check account details')
    print('3. logout')
    x = input('Enter an option')
    if x=='1':
      print('Enter the following details please: ')
      a = str(input('Account Name: '))
      b = str(input('Opening Balance: '))
      c = str(input('Account Type: '))
      d = str(input('Account Email: '))
      createBankAcc(a,b,c,d)
    #elif x=='2':
      #checkAppDet()
    #else:
      #logout()

def start():
  print('What would you like to do?')
  print('1. Login')
  print('2. Close App\nenter 1 or 2')
  x = input()

  if x=='1':
    print('Enter your user name')
    u = input()
    print('Enter your password')
    v = input()
    login(u,v)
    if x=='1':
      print('Enter you password')
    x = input()

  else:
    exit()
    
start()




