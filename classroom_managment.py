classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def find_student(name):
    for student in classroom:
        if student['name']==name:
            return student


def add_student(name, email=None):
    if(email):
        new_email=email
    else:
        new_email=name+"@gmail.com"
    grades=[]
    new_student={
        'name': name,
        'email': new_email,
        'grades': grades,
        
    }
    classroom.append(new_student)
    

def delete_student(name):
     for student in classroom:
        if student['name'] == name:
           classroom.remove(student)


def set_email(name, email):
    for student in classroom:
        if student['name'] == name:
            student['email']=email
   


def add_grade(name, profession, grade):
      for student in classroom:
        if student['name'] == name:
            student['grades'].append((profession, grade))
    


def avg_grade(name, profession):
    grades = []
    for student in classroom:
        if student['name'] == name:
            for grade in student['grades']:
                if grade[0] == profession:
                    grades.append(grade[1])
    if grades:
        return sum(grades) / len(grades)


def get_professions(name):
    professions = set()
    for student in classroom:
        if student['name'] == name:
            for grade in student['grades']:
                professions.add(grade[0])
    return list(professions)
