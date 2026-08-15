# Report Card Calculator
print("Report Card Calculator")

# This section for collecting values for variables
math_score = float(input("Maths score: "))
biology_score = float(input("Biology score: "))
chemistry_score = float(input("Chemistry score :" ))
physic_score = float(input("Physics score: "))
english_score = float(input("English score: "))

# Calculation and analysis section
average = float((math_score + biology_score + chemistry_score + physic_score + english_score) / 5 )

# Ranking Grades
if average == 100:
    print("Perfect score! A+")
elif average >= 90 and average != 100:
    print("Your average is " + str(average))
    print("Well done! Your grade is 'A'!")
elif average >= 80 and average < 90:
    print("Your average is " + str(average))
    print("Congrats! Your grade is ""B""!")
elif average >= 70 and average < 80:
    print("Your average is " + str(average))
    print("Your grade is 'C'!")
elif average < 70 and average > 65 :
    print("Your average is " + str(average))
    print("Your grade is 'D'!") 
elif average <= 65 :
    print("Your average is " + str(average))
    print("You Fail!(F)")
