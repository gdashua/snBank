
 #creates staff.txt file
 staff = open("staff.txt", "w");
 #create staff information to enable login
 staff.write("staffs = { 'staff1': {'userName': 'Jpee', 'password':'jstart.ng', 'email':'j@gmail.com'},'staff2': {'userName': 'kobey', 'password':'kstart.ng', 'email':'k@gmail.com'}}");
 staff.close();

 #creates customer.txt file
customer = open("customer.txt", "w");
customer.close();

	#staff login
 def login():
 	print 'enter user name and password'
 	x = input("user name: ")
 	x = input("password: ")
 	#code written into staff.txt to loop through the staff details for authentication
 	staff.write("/n foreach i staff{}:/n if staff[i][userName]==x && staff[i][password]==y /n open('session.txt','x') /n print('1. Create account')/n print('2. Check account detail')/n print('3. logout') ")
 	exec(staff.oper(staff.txt).read())#runs the staff.txt file to run the python script

 	x = input('enter your option here: ')
 	#conditional statement to determine next line of action after staff has made a choose of action
 	if x=='1':
 		w= input("enter preferred account name: ")
 		x= input("enter openning balance: ")
 		y= input("enter account type: ")
 		z= input("enter account email: ")

#compile new customer informatio to be sent the customer.txt
 customer.write(customers = {'custormer1'= {'account name': w, 'openning balance': x, 'account type': y, 'account email':z}})
#loop to generate 10 digit Account Number for new customer
for i in range(1,6):
  pass1+= str(random.randrange(1,9))

  print('the account password is: '+ pass1)

#function to start the program
 def start():
	 print('Choose one of the options below');
	 print('1. Login');
	 print('2. Close App');
	 x = input('enter 1 or 2:');

	 if x==1:
	 	login();
	 elif x==2:
	 	closeApp();
	 else start();
