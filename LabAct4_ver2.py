#Lab Act 4:
	#ver 2:

marks = int(input("say grade:"))
if marks <= 0:
	print("invalid score! Please enter a value greater than 0.")
if marks >= 101:
	print("invalid score! Please enter a value less than 100.")
elif marks >= 90:
	print("Grade: A")
elif marks >= 80:
	print("Grade: B")
elif marks >= 70:
	print("Grade: C")
elif marks >= 69:
	print("Grade: D")
else:
	print("Grade: F")

#Jose Diego