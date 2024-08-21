import datetime

# Data structure to hold vaccination schedules
vaccination_schedule = {
    "Polio": [2, 4, 6, 18],  # months for each dose
    "DTP": [2, 4, 6, 15],
    "MMR": [12, 15],
    "HepB": [0, 1, 6]
}

class Child:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.vaccination_history = []

class Parent:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.children = []

class VaccinationSystem:
    def __init__(self):
        self.parents = []

    def add_parent(self, parent):
        self.parents.append(parent)
    
    def add_child(self, parent_name, child_name, birth_date):
        for parent in self.parents:
            if parent.name == parent_name:
                child = Child(child_name, birth_date)
                parent.children.append(child)
                print(f"Child {child_name} added to {parent_name}'s profile.")
                return
        print(f"No parent found with the name {parent_name}.")
    
    def schedule_appointment(self, parent_name, child_name, vaccine):
        for parent in self.parents:
            if parent.name == parent_name:
                for child in parent.children:
                    if child.name == child_name:
                        next_dose = self.get_next_dose(vaccine, child.birth_date)
                        if next_dose:
                            print(f"Appointment for {vaccine} scheduled on {next_dose}.")
                        else:
                            print(f"All doses for {vaccine} completed.")
                        return
        print(f"Parent or child not found.")
    
    def get_next_dose(self, vaccine, birth_date):
        if vaccine in vaccination_schedule:
            current_age = self.get_child_age_in_months(birth_date)
            for dose_age in vaccination_schedule[vaccine]:
                if current_age < dose_age:
                    next_dose_date = birth_date + datetime.timedelta(days=dose_age * 30)
                    return next_dose_date
        return None
    
    def get_child_age_in_months(self, birth_date):
        today = datetime.date.today()
        age_in_days = (today - birth_date).days
        return age_in_days // 30

    def view_updates(self, parent_name, child_name):
        for parent in self.parents:
            if parent.name == parent_name:
                for child in parent.children:
                    if child.name == child_name:
                        print(f"Vaccination history for {child_name}: {child.vaccination_history}")
                        return
        print(f"Parent or child not found.")

# Example Usage
system = VaccinationSystem()

parent1 = Parent("John Doe", "123-456-7890")
system.add_parent(parent1)

# Adding children
birth_date = datetime.date(2021, 1, 15)
system.add_child("John Doe", "Alice Doe", birth_date)

# Scheduling a vaccination
system.schedule_appointment("John Doe", "Alice Doe", "Polio")

# Viewing updates
system.view_updates("John Doe", "Alice Doe")
