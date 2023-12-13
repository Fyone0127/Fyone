def register_subject(self, subject):
        valid_subjects = ["malay", "english"]
        if subject.lower() in valid_subjects and subject.lower() not in self.subjects:
            self.subjects.append(subject.lower())
            print(f"{self.name} has been registered for {subject.capitalize()}.")
        elif subject.lower() not in valid_subjects:
            print("Invalid subject. Only Malay and English are allowed.")
        else:
            print(f"{self.name} is already registered for {subject.capitalize()}.")