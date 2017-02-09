x = [1,2,3,4,5,6,7,8,9,10]
totalgrade = 0
totalcredit = 0
loop = True
for x in x:
	while loop:
		print()
		try:
			grade = float(input("Grade for Course "+str(x)+"(put in -1 when you are done):"))
			if grade == -1:
				loop = False
				break
			credit = float(input("Credits for Course "+str(x)+":"))
		except:
			print("Numbers Only!")
		else:
			if grade < 0:
				print("Impossible!")
			elif grade > 110:
				print("Impossible!")
			elif credit > 10:
				print("Impossible!")
			elif credit < 1:
				print("Impossible!")
			else:
				grade1 = grade * credit
				totalgrade = totalgrade + grade1
				totalcredit = totalcredit + credit
				break
if totalgrade > 0 and totalcredit > 0:
	final = totalgrade/totalcredit
	print("Your GPA so far is a ", format(final, ",.2f"), "%.", sep='')
elif totalgrade <= 0 and totalcredit <= 0:
	print("No GPA :(")
