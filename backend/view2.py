from backend import app

@app.route('/hello/')
def index2():
    # students = Student.query.all()
    return "Hello there from view 2!"