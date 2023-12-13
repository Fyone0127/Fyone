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