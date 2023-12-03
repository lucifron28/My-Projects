class StudentManagementSystem:
    def __init__(self, course_name):
        self.course_name = course_name
        self.enrolled_students_file = f"{course_name}_enrolled_students.txt"

    def add_student(self):
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        grade = input("Enter student's grade: ")

        student_data = f"Name: {name}, Age: {age}, Grade: {grade}\n"

        with open("student_records.txt", "a") as file:
            file.write(student_data)
        print("Student information saved successfully!")

    def display_students(self):
        try:
            with open("student_records.txt", "r") as file:
                data = file.read()
                if data:
                    print("Student Information:\n")
                    print(data)
                else:
                    print("No student records found.")
        except FileNotFoundError:
            print("No student records found.")

    def enroll_student(self):
        name_to_enroll = input("Enter student's name to enroll: ")
        try:
            with open(self.enrolled_students_file, "a") as file:
                file.write(f"{name_to_enroll}\n")
            print(f"{name_to_enroll} has been enrolled in {self.course_name}.")
        except Exception as e:
            print(f"Error enrolling {name_to_enroll}: {str(e)}")

    def drop_student(self):
        name_to_drop = input("Enter student's name to drop: ")
        try:
            with open(self.enrolled_students_file, "r") as file:
                lines = file.readlines()
            with open(self.enrolled_students_file, "w") as file:
                dropped = False
                for line in lines:
                    if name_to_drop.lower() not in line.lower():
                        file.write(line)
                    else:
                        dropped = True
                if dropped:
                    print(f"{name_to_drop} has been dropped from {self.course_name}.")
                else:
                    print("Student not enrolled in this course.")
        except FileNotFoundError:
            print("No enrolled students found for this course.")
    
    def display_enrolled_students(self):
        try:
            with open(self.enrolled_students_file, "r") as file:
                data = file.read()
                if data:
                    print(f"Enrolled Students in {self.course_name}:\n")
                    print(data)
                else:
                    print(f"No enrolled students found for {self.course_name}.")
        except FileNotFoundError:
            print(f"No enrolled students found for {self.course_name}.")

    def main_menu(self):
        while True:
            print("\nCourse Information System")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Enroll Student")
            print("4. Drop Student")
            print("5. Display Enrolled Students")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.enroll_student()
            elif choice == '4':
                self.drop_student()
            elif choice == '5':
                self.display_enrolled_students()
            elif choice == '6':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


courses = ["Physics", "Mathematics", "Biology"]

while True:
    print("\nAvailable Courses:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course}")

    course_choice = input("Enter course number to manage (or 'exit' to quit): ")

    if course_choice.lower() == 'exit':
        print("Exiting program.")
        break
    elif course_choice.isdigit():
        course_index = int(course_choice) - 1
        if 0 <= course_index < len(courses):
            selected_course = StudentManagementSystem(courses[course_index])
            selected_course.main_menu()
        else:
            print("Invalid course number. Please try again.")
    else:
        print("Invalid input. Please enter a course number or 'exit'.")