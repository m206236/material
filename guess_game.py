start = input("type a number to start :")
start = int(start)
end = input("type a number for the end :")
end = int (end)
import random 
r = random.randint (start, end)
count = 0
while True:
	count += 1
	number = input ("guess a number:")
	number = int(number)
	if number == r:
		print ("Bingo")
		print ("This is the ", count ,"guess")
		break
	elif number > r:
		print ("the number is smaller than the number you guess!")
	elif number < r:
		print ("the number is bigger than the number you guess!")

	print ("This is the ", count ,"guess")

	