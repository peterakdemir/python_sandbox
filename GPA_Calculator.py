#The GPA calculator
print("GPA Calculator\n\n")
#for this code we are going to make it easy for someone to calculate their GPA and average for their marking period. we assumed that the 

#for all the variables that start with g we are asking for average grade in that class for that marking period
g1 = float(input("Grade for Course 1:"))
 
#for all the variables that start with c we are asking for the number of in that class for that marking period
c1 = float(input("Amount of Credits the Course Takes:"))
 
g2 = float(input("\nGrade for Course 2:"))
c2 = float(input("Amount of Credits the Course Takes:"))
 
g3 = float(input("\nGrade for Course 3:"))
c3 = float(input("Amount of Credits the Course Takes:"))
 
g4 = float(input("\nGrade for Course 4:"))
c4 = float(input("Amount of Credits the Course Takes:"))
 
g5 = float(input("\nGrade for Course 5:"))
c5 = float(input("Amount of Credits the Course Takes:"))
 
g6 = float(input("\nGrade for Course 6:"))
c6 = float(input("Amount of Credits the Course Takes:"))
 
g7 = float(input("\nGrade for Course 7:"))
c7 = float(input("Amount of Credits the Course Takes:"))
 
g8 = input("\nGrade for Course 8 (if you don't have a course 8, put a dash):")
c8 = input("Amount of Credits the Course Takes (if you don't have a course 8, put a dash):")
 
print()
#I am now calculating the users average grade for the marking period.

#This is if the user is a freshman and takes a double period course
if g8 == "-":
	
	a1 = g1*c1
	a2 = g2*c2
	a3 = g3*c3
	a4 = g4*c4
	a5 = g5*c5
	a6 = g6*c6
	a7 = g7*c7
	 
	average = (a1+a2+a3+a4+a5+a6+a7)/(c1+c2+c3+c4+c5+c6+c7)
	
	#i made another variable dividing the average grade by 25 to put it into the 4.0 GPA grading system
	gpa = average/25
	 
	#this is my final out put where alll my work comes together.
	print("Your AVERAGE grade this semester/marking period so far is a ", format(average, ".2f"), ". \n\nYour GPA for this semester/marking peroid so far is a ", format(gpa, ".2f"), ".", sep="")
	
#this is if the user takes 8 1 period courses
elif g8 != "-" and c8 != "-":
	g8 = int(g8)
	c8 = int(c8)
	
	a1 = g1*c1
	a2 = g2*c2
	a3 = g3*c3
	a4 = g4*c4
	a5 = g5*c5
	a6 = g6*c6
	a7 = g7*c7
	a8 = g8*c8
	 
	average = (a1+a2+a3+a4+a5+a6+a7+a8)/(c1+c2+c3+c4+c5+c6+c7+c8)
	
	#i made another variable dividing the average grade by 25 to put it into the 4.0 GPA grading system
	gpa = average/25
	 
	#this is my final out put where alll my work comes together.
	print("Your AVERAGE grade this semester/marking period so far is a ", format(average, ".2f"), ". \n\nYour GPA for this semester/marking peroid so far is a ", format(gpa, ".2f"), ".", sep="")
