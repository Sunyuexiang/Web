#Import useful Flask Tools
import random
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_


#Use Photo and CSS document from folder "static"
app = Flask(__name__, static_folder='./static')

#Connect database(Configure Paths)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Syx13766776551.@localhost:3306/test'
app.config['SECRET_KEY'] = "SYX"

#Create database
db = SQLAlchemy(app)


#A function that verifies the existence of tables in the database
def table_exists(engine, table_name):
    with engine.connect() as con:
        sql = "show tables;"
        tables = con.execute(sql).fetchall()
        for table_col in tables:
            if table_name == table_col[0]:
                return True
        return False


#Table Student and initialize
class Students(db.Model):
    StudentID = db.Column(db.Integer, primary_key=True)
    ID = db.Column(db.String(18))
    Name = db.Column(db.String(24))
    Password = db.Column(db.String(16))
    Sex = db.Column(db.String(10))
    Major = db.Column(db.String(40))

    # course_list = db.relationship("Course", secondary=achievement,backref="student_list",lazy="dynamic")
    def __init__(self, StudentID, ID, Name, Password, Sex, Major):
        self.StudentID = StudentID
        self.ID = ID
        self.Name = Name
        self.Password = Password
        self.Sex = Sex
        self.Major = Major

    def __repr__(self):
        return self.Major

#Table Teacher and initialize
class Teachers(db.Model):
    TeacherID = db.Column(db.Integer, primary_key=True)
    TeacherName = db.Column(db.String(24))
    CourseName = db.Column(db.String(256))

    def __init__(self, TeacherID, TeacherName, CourseName):
        self.TeacherID = TeacherID
        self.TeacherName = TeacherName
        self.CourseName = CourseName


#Table Admin and initialize
class Admin(db.Model):
    AdminID = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    AdminPassword = db.Column(db.String(16))
    AdminStatus = db.Column(db.String(16))

    def __init__(self, AdminID, AdminPassword, AdminStatus):
        self.AdminID = AdminID
        self.AdminPassword = AdminPassword
        self.AdminStatus = AdminStatus

#Table Course and initialize
class Course(db.Model):
    CourseID = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    CourseName = db.Column(db.String(40))
    Teacher = db.Column(db.String(40))
    Major = db.Column(db.String(16))

    def __init__(self, CourseID, CourseName, Teacher, Major):
        self.CourseID = CourseID
        self.CourseName = CourseName
        self.Teacher = Teacher
        self.Major = Major


@app.route('/')
def start():
    #Create tables
    db.create_all()
    engine = create_engine('mysql+pymysql://root:Syx13766776551.@localhost:3306/test')
    #Check whether Tables exist
    if table_exists(engine, "admin"):
        Admin.query.filter('5' == Admin.AdminID).delete()
        Admin.query.filter('1' == Admin.AdminID).delete()
        db.session.commit()
    if table_exists(engine, "students"):
        Students.query.filter('2020110012' == Students.StudentID).delete()
        db.session.commit()
    if table_exists(engine, "teachers"):
        Teachers.query.filter('1' == Teachers.TeacherID).delete()
        Teachers.query.filter('2' == Teachers.TeacherID).delete()
        Teachers.query.filter('3' == Teachers.TeacherID).delete()
        Teachers.query.filter('4' == Teachers.TeacherID).delete()
        db.session.commit()
    if table_exists(engine, "course"):
        Course.query.filter('1' == Course.CourseID).delete()
        Course.query.filter('2' == Course.CourseID).delete()
        Course.query.filter('3' == Course.CourseID).delete()
        Course.query.filter('4' == Course.CourseID).delete()
        Course.query.filter('5' == Course.CourseID).delete()
        Course.query.filter('6' == Course.CourseID).delete()
        Course.query.filter('7' == Course.CourseID).delete()
        Course.query.filter('8' == Course.CourseID).delete()
        Course.query.filter('9' == Course.CourseID).delete()
        Course.query.filter('10' == Course.CourseID).delete()
        Course.query.filter('11' == Course.CourseID).delete()
        Course.query.filter('12' == Course.CourseID).delete()
        Course.query.filter('13' == Course.CourseID).delete()
        Course.query.filter('14' == Course.CourseID).delete()
        Course.query.filter('15' == Course.CourseID).delete()
        Course.query.filter('16' == Course.CourseID).delete()
        db.session.commit()
    # Built-in super administrator and general administrator
    a = Admin('5', 'Leeds0', 'Root')
    b = Admin('1', 'Leeds1', 'Administrator')
    # Built-in Teachers
    c = Teachers('1', 'Harry Harrop', 'Engineering Communication Skill')
    d = Teachers('2', 'Amy Beloe', 'Web Application Development,Physics I,Physics II')
    e = Teachers('3', 'Andrew Hollins', 'Operating Systems,Maths I,Maths II')
    f = Teachers('4', 'Zaid Al-Huda', 'English For Engineering')
    # Built-in Students
    g = Students(2020110012, '230603200110203310', 'Yuexiang Sun', 'Syx13766776551.', 'Male', 'CS')
    # Built-in Course
    C1 = Course('1', 'Engineering Communication Skill', 'Harry Harrop', 'CS')
    C2 = Course('2', 'Web Application Development', 'Amy Beloe', 'CS')
    C3 = Course('3', 'Operating Systems', 'Andrew Hollins', 'CS')
    C4 = Course('4', 'English For Engineering', 'Zaid Al-Huda', 'CS')
    C5 = Course('5', 'Engineering Communication Skill', 'Harry Harrop', 'EE')
    C6 = Course('6', 'Physics I', 'Amy Beloe', 'EE')
    C7 = Course('7', 'Maths II', 'Andrew Hollins', 'EE')
    C8 = Course('8', 'English For Engineering', 'Zaid Al-Huda', 'EE')
    C9 = Course('9', 'Engineering Communication Skill', 'Harry Harrop', 'ME')
    C10 = Course('10', 'Physics II', 'Amy Beloe', 'ME')
    C11 = Course('11', 'Maths II', 'Harry Harrop', 'ME')
    C12 = Course('12', 'English For Engineering', 'Zaid Al-Huda', 'ME')
    C13 = Course('13', 'Engineering Communication Skill', 'Harry Harrop', 'CE')
    C14 = Course('14', 'Physics II', 'Amy Beloe', 'CE')
    C15 = Course('15', 'Maths I', 'Andrew Hollins', 'CE')
    C16 = Course('16', 'English For Engineering', 'Zaid Al-Huda', 'CE')
    #Add to Tables
    db.session.add(a)
    db.session.add(b)
    db.session.add(c)
    db.session.add(d)
    db.session.add(e)
    db.session.add(f)
    db.session.add(g)
    db.session.add(C1)
    db.session.add(C2)
    db.session.add(C3)
    db.session.add(C4)
    db.session.add(C5)
    db.session.add(C6)
    db.session.add(C7)
    db.session.add(C8)
    db.session.add(C9)
    db.session.add(C10)
    db.session.add(C11)
    db.session.add(C12)
    db.session.add(C13)
    db.session.add(C14)
    db.session.add(C15)
    db.session.add(C16)
    db.session.commit()

    return render_template('Index.html')


@app.route('/Index')
def index():
    return render_template('Index.html')


@app.route('/StudentLogIn', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        StudentID = request.form.get('StudentID')
        StudentPassword = request.form.get('StudentPassword')
        if StudentID != '' and StudentPassword != '':
            if StudentID.isdigit() is True:
                StudentID = int(StudentID)
                result = db.session.query(Students).filter(and_(Students.StudentID == StudentID,
                                                                Students.Password == StudentPassword)).first()
                if result is None:
                    error = 'Invalid Username or Password. Please try again!'
                    return render_template('StudentLogIn.html', error=error)
                if StudentID == result.StudentID:
                    Mention = 'Successful'
                    return render_template('StudentCheck.html', Mention=Mention)
            else:
                error = "Invalid Student ID"
                return render_template('StudentLogIn.html', error=error)
        else:
            error = 'Enter Student ID or Password'
            return render_template('StudentLogIn.html', error=error)
    return render_template('StudentLogIn.html')


@app.route('/AdminLogIn', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        Administrator_ID = request.form.get('Administrator_ID')
        Administrator_Password = request.form.get('Administrator_Password')
        Administrator_ID = int(Administrator_ID)
        if Administrator_ID != '' and Administrator_Password != '':
            result = db.session.query(Admin).filter(and_(Admin.AdminID == Administrator_ID,
                                                         Admin.AdminPassword == Administrator_Password,
                                                         Admin.AdminStatus != 'Remove')).first()
            resultRole = db.session.query(Admin).filter(Admin.AdminStatus == 'Root')
            for i in resultRole:
                i.AdminID = int(i.AdminID)
                if Administrator_ID == i.AdminID and Administrator_Password == i.AdminPassword:
                    return render_template('AdminChoose.html')
                if Administrator_ID == resultRole and Administrator_Password != i.AdminPassword:
                    error = 'Invalid Password. Please try again!'
                    return render_template('AdminLogIn.html', error=error)
            if result is None:
                error = 'Invalid Username or Password. Please try again!'
                return render_template('AdminLogIn.html', error=error)
            result.AdminID = int(result.AdminID)
            if Administrator_ID == result.AdminID:
                return render_template('StudentLogIn.html')
        else:
            error = 'Enter Administrator ID or Password'
            return render_template('AdminLogIn.html', error=error)
    return render_template('AdminLogIn.html', error=error)


@app.route('/StudentSignIn', methods=['GET', 'POST'])
def student_signin():
    if request.method == 'POST':
        ID = request.form.get('ID')
        Name = request.form.get('StudentName')
        Password = request.form.get('StudentPassword')
        ConfirmPassword = request.form.get('ConfirmPassword')
        Sex = request.form.get('Sex')
        Major = request.form.get('Major')
        StudentID = random.randint(2020110000, 2020111000)
        if ID.isdigit() is True:
            if len(str(ID)) != 18:
                error = 'Invalid ID card number'
                return render_template('StudentSignIn.html', error=error)
            if Password == ConfirmPassword:
                result = db.session.query(Students).filter(Students.ID == StudentID).first()
                if result is None:
                    a = Students(StudentID, ID, Name, Password, Sex, Major)
                    db.session.add(a)
                    db.session.commit()
                    Mention = StudentID
                    return render_template('StudentSignIn.html', Mention=Mention)
                else:
                    error = 'This Student has exist'
                    return render_template('StudentSignIn.html', error=error)
            else:
                error = 'The password entered twice is inconsistent'
                return render_template('StudentSignIn.html', error=error)
        if ID.isdigit() is False:
            error = 'Invalid ID card number'
            return render_template('StudentSignIn.html', error=error)
    return render_template('StudentSignIn.html')


@app.route('/AddAdmin', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        AddID = request.form.get('AddID')
        AddPassword = request.form.get('AddPassword')
        AddRole = request.form.get('AddRole')
        ConfirmPassword = request.form.get('ConfirmPassword')
        if AddPassword == ConfirmPassword:
            result = db.session.query(Admin).filter(and_(Admin.AdminID == AddID,
                                                         Admin.AdminStatus != 'Remove')).first()
            AddID = int(AddID)
            if result is None:
                a = Admin(AddID, AddPassword, AddRole)
                db.session.add(a)
                db.session.commit()
                Mention = 'Add Successfully'
                return render_template('AddAdmin.html', Mention=Mention)
            else:
                error = 'This Administrator has exist'
                return render_template('AddAdmin.html', error=error)
        if AddPassword != ConfirmPassword:
            error = 'The password is inconsistent twice'
            return render_template('AddAdmin.html', error=error)
    return render_template('AddAdmin.html')


@app.route('/DeleteAdmin', methods=['GET', 'POST'])
def delete_admin():
    if request.method == 'POST':
        ChangeID = request.form.get('ChangeID')
        StatusChange = request.form.get('options')
        if ChangeID != '':
            result = db.session.query(Admin).filter(and_(Admin.AdminID == ChangeID,
                                                         Admin.AdminStatus != 'Root')).first()
            ChangeID = int(ChangeID)
            if result is None:
                error = 'Administrator ID do not exist'
                return render_template('DeleteAdmin.html', error=error)
            result.AdminID = int(result.AdminID)
            if ChangeID == result.AdminID:
                Admin.query.filter(ChangeID == Admin.AdminID).update({Admin.AdminStatus: StatusChange})
                db.session.commit()
                Mention = 'Change Successfully'
                return render_template('DeleteAdmin.html', Mention=Mention)
        else:
            error = 'Enter Administrator ID or Password'
            return render_template('AdminLogIn.html', error=error)
    return render_template('DeleteAdmin.html')


@app.route('/AdminChoose')
def admin_choose():
    return render_template('AdminChoose.html')


@app.route('/StudentCheck')
def check():
    return render_template('StudentCheck.html')


if __name__ == '__main__':
    app.run()
