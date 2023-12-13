import pandas as pd


class Student:
    def __init__(self, name, age, contact, subjects, parent_contact):
        self.max_students_per_class = 40
        self.name = name
        self.age = age
        self.contact = contact
        self.subjects = ['english', 'malay']
        self.classes = {'english': {'13': [], '14': [], '15': [], '16': [], '17': []},
                        'malay': {'13': [], '14': [], '15': [], '16': [], '17': []}}
        self.parent_contact = parent_contact

    def update_info(self, age=None, contact=None, parent_contact=None):
        if age:
            self.age = age
        if contact:
            self.contact = contact
        if parent_contact:
            self.parent_contact = parent_contact

    def register_subject(self, subject):
        valid_subjects = ["malay", "english"]
        if subject.lower() in valid_subjects and subject.lower() not in self.subjects:
            self.subjects.append(subject.lower())
            print(f"{self.name} has been registered for {subject.capitalize()}.")
        elif subject.lower() not in valid_subjects:
            print("Invalid subject. Only Malay and English are allowed.")
        else:
            print(f"{self.name} is already registered for {subject.capitalize()}.")

    def calculate_fee(self):
        subject_count = len(self.subjects)
        fee_per_subject = 50
        total_fee = subject_count * fee_per_subject
        return total_fee

    def generate_receipt(self):
        receipt = f"Student Name: {self.name}\nAge: {self.age}\nContact: {self.contact}\nSubjects: {', '.join(self.subjects)}\nTotal Fee: RM {self.calculate_fee()}\n\n"
        return receipt

def validate_age(age):
    return 13 <= age <= 17

def register_student(students, name):
    found_student = None
    for student in students:
        if student.name.lower() == name.lower():
            found_student = student
            break
    if found_student:    
            # if student exists, give options to update or register
            choice = input(f"{name} already exists. Do you want to update info or register a subject? (update/register): ")
            # Students exist, student chose to update their information 
            if choice.lower() == "update":
                age = None
                contact = None
                parent_contact = None
    
                choice = input("Update student's age? (y/n)")
                if choice.lower() == "y":
                    age = int(input("Enter new age: "))
                    if not validate_age(age):
                        print("Sorry, only students aged 13 to 17 are allowed to register.")
                        return

                choice = input("Update student's contact number? (y/n)")
                if choice.lower() == "y":
                    contact = input("Enter new student contact number: ")

                    choice = input("Update parent's/guardian's contact number? (y/n)")
                    if choice.lower() == "y":
                        parent_contact = input("Enter new parent's contact number: ")
    
                    found_student.update_info(age, contact, parent_contact)
                    print("Student information updated.")
            # Students exist, student chose to register                  
            elif choice.lower() == "register":
                subject = input("Enter the subject to register (Malay/English): ")
                
                if validate_age(found_student.age) and subject.lower() in ["malay", "english"]:
                    if len(found_student.classes[subject][str(found_student.age)]) < found_student.max_students_per_class:
                        found_student.register_subject(subject)
                        found_student.classes[subject][str(found_student.age)].append(name)
                        print(f"Registration successful for {name} in {subject} class (Age {found_student.age}).")
                         # Calculate fee and generate receipt
                        total_fee = found_student.calculate_fee()
                        receipt = found_student.generate_receipt()
                        print(receipt)
                        # Save data to Excel
                        save_to_excel(students)
                        quit_program = input("Do you want to quit? (yes/no): ")
                        if quit_program.lower() == "yes":
                            return
                    else:
                        print("The class is full, registration is closed.")
                else:
                    print("Invalid age or subject.")
    else:
        age = int(input("Enter student age: "))
        # if student's age does not meet the requirement, the system will be closed
        if not validate_age(age):
            print("Sorry, only students aged 13 to 17 are allowed to register.")
        else:
            contact = input("Enter student contact number: ")
            parent_contact = input("Enter parent's contact number: ")
            subjects = []
            new_student = Student(name, age, contact, subjects,parent_contact)
            students.append(new_student)
            print(f"{name} has been registered.")
            save_to_excel(students)

def calculate_total_fee(students):
    total_fee = 0
    for student in students:
        fee = student.calculate_fee()
        total_fee += fee
    return total_fee

def calculate_balance(self, student_index, amount_paid):
    total_fees = self.calculate_total_fees(student_index)
    balance = amount_paid - total_fees
    return balance

def save_to_excel(students):
    try:
        # Load existing data from the Excel file, if it exists
        existing_data = pd.read_excel("student_data.xlsx")
        
        # Create a DataFrame for the new data
        new_data = {
            "Name": [student.name for student in students],
            "Age": [student.age for student in students],
            "Contact": [student.contact for student in students],
            "Subjects": [', '.join(student.subjects) for student in students],
            "Total Fee": [student.calculate_fee() for student in students]
        }
        
        # Append the new data to the existing DataFrame
        updated_data = pd.concat([existing_data, pd.DataFrame(new_data)], ignore_index=True)
        
        # Save the updated DataFrame to the Excel file
        updated_data.to_excel("student_data.xlsx", index=False)
        
        print("Data appended to students_data.xlsx successfully.")
    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        df = pd.DataFrame(new_data)
        df.to_excel("student_data.xlsx", index=False)
        print("New file created: students_data.xlsx.")

def read_from_excel(file_name):
    try:
        data = pd.read_excel(file_name)
        print("Data read successfully from Excel:")
        print(data)
        return data
    except FileNotFoundError:
        print("File not found.")

# Usage example:
file_name = "students_data.xlsx"  # Replace with your Excel file name
read_from_excel(file_name)
def generate_receipts(students):
    for student in students:
        receipt_data = student.generate_receipt()
        file_name = f"{student.name}_receipt.txt"
        with open(file_name, "w") as file:
            file.write(receipt_data)
            file.write(f"""
            --------------------------------------------------------------------
                                    Timetable
            --------------------------------------------------------------------
                        Monday    Tuesday   Wednesday  Thursday    Friday 
            --------------------------------------------------------------------  
            Secondary   Form 1    Form 2    Form 3     Form 4     Form 5
            Level
            1:00 pm-    English   English   English    English    English
            3:00 pm
            7:00 pm-    Malay     Malay     Malay      Malay      Malay
            9:00 pm
            --------------------------------------------------------------------
            """)
    print(f"Receipt generated for {student.name} in {file_name}.")

def main():
    students = []

    while True:
        name = input("Enter student's name (or 'quit' to exit the program): ")
        if name.lower() == 'quit':
            break
        else:
            register_student(students, name)
    
    generate_receipts(students)

if __name__ == "__main__":
    main()
