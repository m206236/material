password = "a123456"
i = 3
while i > 0:
	i = i - 1
	pwd = input("type the password:")
	if pwd == password :
		print ("login success")
		break
	else:
		print ("the password is not right")
		if i > 0:
			print (i ," chance left")
		
		

