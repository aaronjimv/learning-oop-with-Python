class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"The pet {self.name} is playing")


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def play(self):
        super().play()
        print(f"The {self.breed} breed dog is playing with his bone.")


class DomesticDog(Dog):
    def __init__(self, name, breed, owner):
        super().__init__(name, breed)
        self.owner = owner

    def play(self):
        super().play()
        print(f"The domestic dog wags its tail")

    def introduce(self):
        print(
            f"Hi, I'm {self.name}, a {self.breed} and my owner is {self.owner} "
        )

domestic_dog = DomesticDog("Max", "German Shepherd", "John Doe")
domestic_dog.play()
domestic_dog.introduce()
