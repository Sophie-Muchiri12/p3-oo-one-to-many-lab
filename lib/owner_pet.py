class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # This will store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type
        
       
        if owner and not isinstance(owner, Owner):
            raise Exception("Invalid owner type")
        
        self.owner = owner

        
        Pet.all.append(self)

        
        if owner is not None:
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = [] 

    def pets(self):
        """Returns a list of all pets associated with this owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's list, checking if the pet is valid."""
        if not isinstance(pet, Pet):
            raise Exception("Invalid Pet type")
        self._pets.append(pet)
        pet.owner = self  # Associate the pet with this owner

    def get_sorted_pets(self):
        """Returns a list of the owner's pets, sorted by their name."""
        return sorted(self.pets(), key=lambda pet: pet.name)

# Test function
def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    
    
    assert owner.pets() == [pet1, pet2]

def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)

    # The pets will now be added to the owner's list and sorted
    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]
    
test_owner_has_pets()
test_get_sorted_pets()
print("All tests passed!")
