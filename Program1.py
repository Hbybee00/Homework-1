# Hayden Bybee
# UWYO COSC 1010
# Submission Date
# HW 01
# Lab Section: 16
# Sources, people worked with, help given to: 
# N/A

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
# students = [
#     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
#     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
#     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
#     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
# ]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution

students = [ {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}} ]

bobavg = 0

charlieavg = 0

aliceavg = 0

davidavg = 0

Averages = {}

for student in students:
    if student["name"] == "Bob":
        Scorelist2 = student["scores"]
        bobavg = (Scorelist2["Math"] + Scorelist2["Science"] + Scorelist2["English"])/3
        print(f"Bob's average score is {bobavg}!")
        Averages[student["name"]] = bobavg
    elif student["name"] == "Alice":
        Scorelist1 = student["scores"]
        aliceavg = (Scorelist1["Math"] + Scorelist1["Science"] + Scorelist1["English"])/3
        print(f"Alice's average score is {aliceavg}!")
        Averages[student["name"]] = aliceavg
    elif student["name"] == "Charlie":
        Scorelist3 = student["scores"]
        charlieavg = (Scorelist3["Math"] + Scorelist3["Science"] + Scorelist3["English"])/3
        print(f"Charlie's average score is {charlieavg}!")
        Averages[student["name"]] = charlieavg
    elif student["name"] == "David":
        Scorelist4 = student["scores"]
        davidavg = (Scorelist4["Math"] + Scorelist4["Science"] + Scorelist4["English"])/3
        print(f"David's average score is {davidavg}!")
        Averages[student["name"]] = davidavg

print(Averages)