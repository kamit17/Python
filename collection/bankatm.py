 #Program to Simulate ATM activity

 print('Welcome to Wells Fargo')
 restart = ('Y')
 chances = 3
 balance = 67.14
 while chances >= 0:
 	pin = int(input("Please enter your 4 Digit Pin: "))
 	if pin = (1234):
 		print("You entered your pin correctly\n")
 		while restart not in ('n','NO','no','N'):
 			print('Please Press 1 for your Balance\n')
 			print('Please Press 2 to Make a wihtdrawal\n')
 			print('Please press 3 to Pay in\n')
 			print('Please press 4 to Return Card\n')
 			option = int(input("What would you like to choose?"))
 			if option == 1:
 				print('Your balance is Rs',balance,'\n')
 				restart = input('would you like to go back? ')
 				if restart in ('n','NO','no','N'):
 					print('Thank You')
 					break
 				elif option == 2:
 					option2 == ('y')
 					wihtdrawal = float(input('how much would you like to wihtdraw? 100/200/500/2000'))
 					if wihtdrawal in [100,200,500,2000]:
 						balance = balance - wihtdrawal
 						print('\nYour balance is now',balance)
 						restart = input('would you like to go back? ')
 						if restart in ('n','NO','no','N'):
 							print('Thank you')
 							break
 							


