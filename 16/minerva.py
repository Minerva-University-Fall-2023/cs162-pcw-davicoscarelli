class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.courses = {}

class Student(User):
    pass

class Professor(User):
    pass

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.enrolled_users = {}

    def enroll_user(self, user, role):
        self.enrolled_users[user.user_id] = role
        user.courses[self.course_id] = role

class AccessControl:
    def can_perform_action(self, user, course_id, action):
        if course_id in user.courses:
            role = user.courses[course_id]
            return action in role.permissions
        return False
    
teacher_role = Role("Teacher", ["breakout", "grade"])
student_role = Role("Student", ["participate"])
tech_support_role = Role("Tech Support", ["breakout", "repair", "upgrade"])

alice = Professor("001", "Alice")
bob = Student("002", "Bob")

cs162 = Course("cs162", "CS162")

cs162.enroll_user(alice, teacher_role)
cs162.enroll_user(bob, student_role)

access_control = AccessControl()

print(f"Alice can send to breakout in CS162: {access_control.can_perform_action(alice, 'cs162', 'breakout')}")
print(f"Bob can send to breakout in CS162: {access_control.can_perform_action(bob, 'cs162', 'breakout')}")

cs110 = Course("cs110", "CS110")
cs110.enroll_user(alice, student_role)

print(f"Alice can participate in CS110: {access_control.can_perform_action(alice, 'cs110', 'participate')}")
