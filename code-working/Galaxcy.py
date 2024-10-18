class Galaxy:
    def __init__(self, name, mega_light_years, mass, galaxy_type):
        self.name = name
        self.mega_light_years = mega_light_years
        self.mass = mass  # Adding a mass attribute
        self.galaxy_type = galaxy_type

class GType:
    def __init__(self, type_char):
        type_mapping = {
            'S': 'Spiral',
            'E': 'Elliptical',
            'I': 'Irregular',
            'L': 'Lenticular'
        }
        self.my_gtype = type_mapping.get(type_char.upper(), 'Unknown')

def iterate_through_list():
    galaxies = [
        Galaxy("Tadpole", 400, 1e12, GType('S')),  
        Galaxy("Pinwheel", 25, 3e10, GType('S')),
        Galaxy("Cartwheel", 500, 8e11, GType('L')),
        Galaxy("Small Magellanic Cloud", 0.2, 1e9, GType('I')),
        Galaxy("Andromeda", 3, 1e12, GType('S')),
        Galaxy("Maffei 1", 11, 2e11, GType('E')),
        Galaxy("Sombrero", 1.2, 4e10, GType('S')),
        Galaxy("Whirlpool", 23, 5e10, GType('E')),
        Galaxy("Triangulum", 2.7, 1e10, GType('I')),
        Galaxy("Messier 87", 53.5, 6e11, GType('L')),
        Galaxy("Centaurus A", 12.5, 7e10, GType('E'))
    ]
    
    for i, galaxy in enumerate(galaxies):
        print(f"{i + 1}. {galaxy.name} ({galaxy.mega_light_years} MLY, {galaxy.mass} kg), Type: {galaxy.galaxy_type.my_gtype}")

    total_mass = sum(galaxy.mass for galaxy in galaxies)  
    print(f"Total mass of galaxies: {total_mass:.2e} kg")

if __name__ == "__main__":
    print("Welcome to Galaxy News!")
    iterate_through_list() 


# class Galaxy:
#     def __init__(self, name, mega_light_years, mass, galaxy_type):
#         self.name = name
#         self.mega_light_years = mega_light_years
#         try:
#             self.mass = float(mass)  # Convert mass to float
#         except ValueError:
#             raise ValueError(f"Mass for {name} must be a number, got {mass}")
#         self.galaxy_type = galaxy_type

# class GType:
#     def __init__(self, type_char):
#         type_mapping = {
#             'S': 'Spiral',
#             'E': 'Elliptical',
#             'I': 'Irregular',
#             'L': 'Lenticular'
#         }
#         self.my_gtype = type_mapping.get(type_char.upper(), 'Unknown')

# def iterate_through_list():
#     galaxies = [
#         Galaxy("Tadpole", 400, "1e12", GType('S')),  # Changed mass to float
#         Galaxy("Pinwheel", 25, 3e10, GType('S')),
#         Galaxy("Cartwheel", 500, 8e11, GType('L')),
#         Galaxy("Small Magellanic Cloud", 0.2, 1e9, GType('I')),
#         Galaxy("Andromeda", 3, 1e12, GType('S')),
#         Galaxy("Maffei 1", 11, 2e11, GType('E')),
#         Galaxy("Sombrero", 1.2, 4e10, GType('S')),
#         Galaxy("Whirlpool", 23, 5e10, GType('E')),
#         Galaxy("Triangulum", 2.7, 1e10, GType('I')),
#         Galaxy("Messier 87", 53.5, 6e11, GType('L')),
#         Galaxy("Centaurus A", 12.5, 7e10, GType('E'))
#     ]
    
#     for i, galaxy in enumerate(galaxies):
#         print(f"{i + 1}. {galaxy.name} ({galaxy.mega_light_years} MLY, {galaxy.mass:.2e} kg), Type: {galaxy.galaxy_type.my_gtype}")

#     total_mass = sum(galaxy.mass for galaxy in galaxies)  
#     print(f"Total mass of galaxies: {total_mass:.2e} kg")

# if __name__ == "__main__":
#     print("Welcome to Galaxy News!")
#     iterate_through_list()