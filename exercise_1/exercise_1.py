def exercise_1(inputs): # DO NOT CHANGE THIS LINE


from abc import ABC, abstractmethod

students=["Ben","Bob","Zoro","Win","Best"]
teachers=["Andy","Jack","Shanks","John"]
lectures=["Physics","Biology","Chemistry","Mathematics"]
lect_dict={
        "Physics":["Andy",["Ben","Bob","Zoro"]],
        "Biology":[["Jack","John"],["Ben","Zoro"]],
        "Chemistry":["Shanks",["Bob","Ben","Win","Zoro"]],
        "Mathematics":["John",["Win","Zoro","Best","Ben"]],
        }

class Person(ABC):
    name=""
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_attribute(self):
        pass

class Student(Person):

    def __init__(self,name,student_id,lectures_enrolled):

        self.name = name
        self.student_id = student_id
        self.lectures_enrolled = lectures_enrolled

    def __add__(self,lecture):
        print("new_student + lecture does not work")

    def get_attribute(self):
        pass


class Teacher(Person):
    def __init__(self,name,teacher_id,lecture_taught):

        self.name = name
        self.teacher_id = teacher_id
        self.lecture_taught = lecture_taught

    def get_attribute(self):
        pass

class Lecture:
    def __init__(self,Lecture_id,students):
        self.Lecture_id = Lecture_id
        self.lecturer = ""
        self.students = students
        
    def assign_teacher(self,teacher):
        self.teacher = teacher
        self.lecturer = teacher.name
        teacher.lecture_taught.append(self.Lecture_id)

    def get_teacher(self):
        return self.lecturer

    def assign_student(self,student):
        self.student = student

        if len(student.lectures_enrolled)>=3:
            print(student.name,"cannot take more than 3 classes")

        else:
            students.append(student.name)
            student.lectures_enrolled.append(self.Lecture_id)

    def __add__(self,student):
        self.assign_student(student)
        return self

    def get_students(self):
        return students

stuid=[]
teaid=[]
lecid=[]

a=10100
b=90900

for i in students:
    a=a+1
    stuid.append(Student(i,a,[]))

for t in teachers:
    b=b+1
    teaid.append(Teacher(t,b,[]))

for l in lectures:
    lecid.append(Lecture(l,[]))

print("Natural Error messages (if any):".upper())

for k in lect_dict:
    for x in lecid:
        if x.Lecture_id==k:
            c=lect_dict.get(k)[0]
            d=lect_dict.get(k)[1]
            if type(c)==str:
                for y in teaid:
                    if y.name==c:
                        x.assign_teacher(y)  
                        
            else:
                print(*c,sep=" and ",end=" ")
                print("cannot be the teacher in the same lecture","("+k+")")

            for e in d:
                for z in stuid:
                    if z.name==e:
                        x=x+z

#print("\nlist of people:".upper())
#for i in stuid:
#    print(i.name)
#for t in teaid:
#    print(t.name)


#print("\nlist of students (name and student id):".upper())
#for i in stuid:
#    print(i.name,i.student_id)

#print("\nlist of teachers (name and student id):".upper())
#for t in teaid:
#    print(t.name,t.teacher_id)

#print("\nlist of lectures with details".upper())

#for k in lect_dict:
#    for x in lecid:
#        if x.Lecture_id==k:
#            c=lect_dict.get(k)[0]
#            d=lect_dict.get(k)[1]
 #           for y in teaid:
  #              if y.name==c:
   #                 x.assign_teacher(y)  
    #                print("\n"+k.upper())
     #               print("Lecturer of",k,"class :",x.get_teacher())
                    

      #      print("Students of",k,"class : ")
       #     for e in d:
        #        for z in stuid:
         #           if z.name==e:
          #              print(e)
                        
  
#print("\nList of students and teachers with their unique ID: ".upper())

#for i in stuid:
#    print(i.name,"has a unique ID",i.student_id)

#for t in teaid:
#    print(t.name,"has a unique ID",t.teacher_id)

output = [Person, Teacher, Student, Lecture]

    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.
    
    p, q, r = inputs
    
    p => ['t101', 't102', 't103']
    q => ['s101', 's102', 's103']
    r => {
        'l101':['t101': ['s101', 's102']], 
        'l102': ['s101', 's102', 's103']]
    }
    p = Person()
    s = Student()
    t = Teacher()
    l = Lecture()
    
    output = {
        1: [Person, p], 
        2: [Teacher, Student, t, s], 
        3: [Lecture, l], 
        4: [Lecture, l], 
        5: [Lecture, Student, l, s], 
        6: [Teacher, Student, t, s]
    }
    """
    output = inputs


    return output       # DO NOT CHANGE THIS LINE
