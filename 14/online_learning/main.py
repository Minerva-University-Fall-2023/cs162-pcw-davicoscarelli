from models.base import Base, engine, Session
import scripts.insert_data as insert_data
import scripts.query_data as query_data

# Create tables
Base.metadata.create_all(engine)

# Insert data
user_id = insert_data.insert_user("Jane Smith")
course_id = insert_data.insert_course("Python Programming")
insert_data.insert_enrollment(user_id, course_id)

# Query data
courses = query_data.get_courses_by_user_name("Jane Smith")

# Print results
print("Courses enrolled by Jane Smith:")
for course in courses:
    print(course.name)
