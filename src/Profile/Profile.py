class Profile:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")


# Example usage:
user_profile = Profile("John Doe", 30, "New York")
user_profile.display_info()
