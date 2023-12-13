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