class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.pet_type = pet_type

        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner.")
        self.owner = owner

        Pet.all.append(self)


# create some owners
o1 = Owner("Elijah")
o2 = Owner("Mary")

# create some pets
p1 = Pet("Buddy", "dog", o1)
p2 = Pet("Kitty", "cat", o1)
p3 = Pet("Tweety", "bird", o2)

# add a pet later
p4 = Pet("Rex", "dog")
o2.add_pet(p4)

# print owners and their pets
print(f"{o1.name}'s pets: {[pet.name for pet in o1.pets()]}")
print(f"{o2.name}'s pets: {[pet.name for pet in o2.pets()]}")

# test get_sorted_pets
print(f"{o1.name}'s sorted pets: {[pet.name for pet in o1.get_sorted_pets()]}")
