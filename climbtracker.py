boulder = 0
route = 3
route2 = ["a","b","c","d"]
route3 = 0
while True:
	yodel = input("Do you want to add your max boulder or route grade:")
	if yodel == "boulder":
		boulder+=1
	if yodel == "route" and route >= 9:
		if route3 == 3:
			route3 = 0
			route +=1
		else:
			route+=1

	print("Your Max Boulder Grade: V",boulder)
	if route > 9:
		print("Your Max Route Grade: 5.",route,route2[route3])
	else:
		print("Your Max Route Grade: 5.",route)



