# in this program, i called a class from classes.py into this program and added an object to it
from classes import user

student = user('Ade', 'ade@gmail.com', 63)
student2 = user('bianca', 'bianca@gmail.com', 23)

print(student.name, student2.name)