from flask import Blueprint
from .models import Student
from . import db
view1 = Blueprint('view1', __name__)

@view1.route('/', methods = ["GET", "POST"])
def index():
    new_student = Student(firstname = "Himanshu", lastname = "Gupta")
    db.session.add(new_student)
    db.session.commit()
    students = Student.query.all()
    print(students)

    return "Hello students!"