from faker import Faker
import random
from .models import *
fake = Faker()

def create_subjects(n=10):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                marks = random.randint(0,100)
                SubjectMarks.objects.create(student = student, subject = subject, marks = marks)

    except Exception as e:
        print(e)

def seed_db(n=10) ->None:

    try: 
    
        for _ in range(0,n):

            # [1,2,3,4]
            departments_objs = Department.objects.all()
            random_index = random.randint(0,len(departments_objs)-1)
            student_id = f'STU-0{random.randint(100, 999)} '
            department  = departments_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )

    except Exception as e:
        print(e)