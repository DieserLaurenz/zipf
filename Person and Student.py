# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:17:16 2023

@author: laure
"""


class Person:
    def __init__(self, name):
        self.name = name
        
    def printInfo(self):
        print("Name: " + self.name)
        
class Student(Person):
    def __init__(self, name, university, study_program):
        super().__init__(name)
        self.university = university
        self.study_program = study_program
        self.creditpoints = 0
    
    def printInfo(self):
        super().printInfo()
        print("University:", self.university)
        print("Study Program:", self.study_program)
        
    def setCreditPoints(self, creditpoints):
        self.creditpoints = creditpoints
        
    def getCreditPoints(self):
        return self.creditpoints
    
if __name__ == "__main__":
# create a student
    student = Student("Alice Johnson", "University of ABC", "Data Science")
    student.printInfo()
    student.setCreditPoints(50)
    print("Credit Points:", student.getCreditPoints())

# create a person
    person = Person("John Doe")
    person.printInfo()

