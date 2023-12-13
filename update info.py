def update_info(self, age=None, contact=None, parent_contact=None):
        if age:
            self.age = age
        if contact:
            self.contact = contact
        if parent_contact:
            self.parent_contact = parent_contact