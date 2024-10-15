# Ian Bullard
# UWYO COSC 1010
# 10/11/24
# HW 01
# Lab Section: 14
# Sources, people worked with, help given to: Bounced ideas around with Patrick McGrath
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student and their scores in different subjects.
#
# Student Data:
students = [
    {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
    {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
    {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]
#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names of students 
# whose average score is greater than 80.
#Solution

## Notes to self
#
#print(students[0]['scores']['Math'])
#To access and print Alice's Math score ^


#Part 1
print(" ")
print('Part 1')

Alice_Avg = round((students[0]['scores']['Math'] + students[0]['scores']['Science'] + students[0]['scores']['English'])/len(students[0]["scores"]), 2)
Bob_Avg = round((students[1]['scores']['Math'] + students[1]['scores']['Science'] + students[1]['scores']['English'])/len(students[1]["scores"]), 2)
Charlie_Avg = round((students[2]['scores']['Math'] + students[2]['scores']['Science'] + students[2]['scores']['English'])/len(students[2]["scores"]), 2)
David_Avg = round((students[3]['scores']['Math'] + students[3]['scores']['Science'] + students[3]['scores']['English'])/len(students[3]["scores"]), 2)
print(f"Alice's average is {Alice_Avg}")
print(f"Bob's average is {Bob_Avg}")
print(f"Charlie's average is {Charlie_Avg}")
print(f"David's average is {David_Avg}")

print(" ")
#Part 2
print("Part 2")

Avg_Score = {
    "Alice": Alice_Avg,
    "Bob": Bob_Avg,
    "Charlie": Charlie_Avg,
    "David": David_Avg
}
print(Avg_Score)
print(" ")
#Part 3
print('Part 3')

for name, value in Avg_Score.items():
    if value > 80:
        print(f"{name}'s average score was above 80%")

#The Lines below print out everyone's average scores and tells you whether their score was above, below, or equal to 80%
print(" ")
print(" ")
print("Additonal work")

for name, value in Avg_Score.items():
    if value > 80:
        print(f"{name}'s average score was above 80%")
    elif value == 80:
        print(f"{name}'s average score was 80%")
    else:
        print(f"{name}'s average score was below 80%")


print(" ")

## Note to self:
# Another way of doing it
#stu_avg = {}
#for stu in students:
#    scores = stu["scores"]
#    score_avg = sum(scores.values())/len(scores)
#    print(f"{stu['name']}'s average score is {score_avg}")
#    stu_avg[stu["name"]] = round(score_avg, 2)
#print(stu_avg)