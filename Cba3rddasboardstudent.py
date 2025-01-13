class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = []
        self.homework = {}

    def mark_attendance(self, date, status):
        self.attendance.append({"date": date, "status": status})

    def assign_homework(self, assignment, due_date):
        self.homework[assignment] = {"due_date": due_date, "status": "Pending"}

    def submit_homework(self, assignment):
        if assignment in self.homework:
            self.homework[assignment]["status"] = "Submitted"


class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = {}
        self.announcements = []

    def add_student(self, student_id, name):
        self.students[student_id] = Student(student_id, name)
        print(f"Student {name} added.")

    def mark_attendance(self, student_id, date, status):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date, status)
            print(f"Attendance marked for {self.students[student_id].name} on {date} as {status}.")
        else:
            print("Student not found.")

    def assign_homework(self, assignment, due_date):
        for student in self.students.values():
            student.assign_homework(assignment, due_date)
        print(f"Homework '{assignment}' assigned to all students with due date {due_date}.")

    def make_announcement(self, message):
        self.announcements.append(message)
        print(f"Announcement made: {message}")

    def view_student_profile(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student.student_id}\nName: {student.name}")
            print("Attendance:")
            for record in student.attendance:
                print(f"  Date: {record['date']}, Status: {record['status']}")
            print("Homework:")
            for hw, details in student.homework.items():
                print(f"  {hw}: Due {details['due_date']}, Status: {details['status']}")
        else:
            print("Student not found.")


def main():
    classroom = Classroom("Grade 10 - Science")

    while True:
        print("\nClassroom Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Assign Homework")
        print("4. Make Announcement")
        print("5. View Student Profile")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            classroom.add_student(student_id, name)

        elif choice == "2":
            student_id = input("Enter Student ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (Present/Absent): ")
            classroom.mark_attendance(student_id, date, status)

        elif choice == "3":
            assignment = input("Enter Homework Assignment: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            classroom.assign_homework(assignment, due_date)

        elif choice == "4":
            message = input("Enter Announcement Message: ")
            classroom.make_announcement(message)

        elif choice == "5":
            student_id = input("Enter Student ID: ")
            classroom.view_student_profile(student_id)

        elif choice == "6":
            print("Exiting Classroom Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
