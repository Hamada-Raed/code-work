# class Metal:
#     def __init__(self, name, density, thermal_conductivity, expansion_coefficient, initial_strength):
#         self.name = name
#         self.density = density  # in kg/m^3
#         self.thermal_conductivity = thermal_conductivity  # in W/(m·K)
#         self.expansion_coefficient = expansion_coefficient  # in 1/K
#         self.initial_strength = initial_strength  # in MPa
#         self.new_volume = None
#         self.new_strength = None

#     def calculate_properties(self, initial_temp, final_temp):
#         temp_change = final_temp - initial_temp
#         expansion_ratio = 1 + self.expansion_coefficient * temp_change
        
#         # Simple linear expansion approximation
#         self.new_volume = expansion_ratio
#         # Simplified strength reduction model
#         strength_loss_factor = 0.005  # hypothetical reduction factor
#         self.new_strength = self.initial_strength * (1 - strength_loss_factor * abs(temp_change))

#     def generate_report(self):
#         return (f"---- Report for {self.name} ----\n"
#                 f"Original Density: {self.density} kg/m^3\n"
#                 f"Original Thermal Conductivity: {self.thermal_conductivity} W/(m·K)\n"
#                 f"Original Strength: {self.initial_strength} MPa\n"
#                 f"Volume Expansion Ratio: {self.new_volume:.2f}\n"
#                 f"Modified Strength: {self.new_strength:.2f} MPa\n")


# def main():
#     metals = [
#         Metal(name="Aluminum", density=2700, thermal_conductivity=237, expansion_coefficient=23.1e-6, initial_strength=300),
#         Metal(name="Copper", density=8960, thermal_conductivity=401, expansion_coefficient=16.5e-6, initial_strength=210),
#         Metal(name="Iron", density=7874, thermal_conductivity=80, expansion_coefficient=11.8e-6, initial_strength=250)
#     ]

#     initial_temp = 20  # Initial temperature in Celsius
#     final_temp = 100  # Final temperature in Celsius

#     for metal in metals:
#         metal.calculate_properties(initial_temp, final_temp)
#         print(metal.generate_report())

# if __name__ == "__main__":
#     main()


class Metal:
    def __init__(self, name, density, thermal_conductivity, thermal_expansion_coefficient, youngs_modulus, initial_temperature, initial_length):
        if density <= 0 or thermal_conductivity < 0 or thermal_expansion_coefficient < 0 or youngs_modulus <= 0 or initial_length <= 0:
            raise ValueError("Density, thermal conductivity, thermal expansion coefficient, Young's modulus, and initial length must be positive values.")
        
        self.name = name
        self.density = density
        self.thermal_conductivity = thermal_conductivity
        self.thermal_expansion_coefficient = thermal_expansion_coefficient
        self.youngs_modulus = youngs_modulus
        self.initial_temperature = initial_temperature
        self.initial_length = initial_length

    def calculate_expansion(self, temperature_change):
        """Calculate the expansion of the metal due to temperature change."""
        return self.thermal_expansion_coefficient * self.initial_length * temperature_change

    def calculate_strength_change(self, temperature_change):
        """Calculate the change in strength of the metal due to temperature change."""
        return -0.1 * self.youngs_modulus * temperature_change

    def generate_report(self, temperature_change):
        """Generate a report summarizing the metal's original and modified properties."""
        expansion = self.calculate_expansion(temperature_change)
        strength_change = self.calculate_strength_change(temperature_change)

        report = (
            f"Metal: {self.name}\n"
            f"Original Properties:\n"
            f"  Density: {self.density} kg/m³\n"
            f"  Thermal Conductivity: {self.thermal_conductivity} W/m·K\n"
            f"  Young's Modulus: {self.youngs_modulus} Pa\n"
            f"  Initial Temperature: {self.initial_temperature} °C\n"
            f"  Initial Length: {self.initial_length} m\n"
            f"\nModified Properties:\n"
            f"  Expansion: {expansion:.6f} m\n"
            f"  New Length: {self.initial_length + expansion:.6f} m\n"
            f"  Change in Strength: {strength_change:.2f} Pa\n"
            f"  New Strength: {self.youngs_modulus + strength_change:.2f} Pa\n"
        )

        return report


def main():
    metals = [
        Metal("Aluminum", 2700, 237, 0.000023, 70000000000, 20, 1),
        Metal("Copper", 8960, 386, 0.000017, 110000000000, 20, 1),
        Metal("Steel", 7850, 50, 0.000012, 200000000000, 20, 1),
    ]

    temperature_change = 100  # Celsius

    for metal in metals:
        report = metal.generate_report(temperature_change)
        print(report)
        print("\n")


if __name__ == "__main__":
    main()
