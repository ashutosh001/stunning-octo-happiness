# Welcome to the Depths of Octo-Sharks - Aquatic Python Thrills!

class OctoShark:
    def __init__(self, name):
        self.name = name

    def aquatic_tentacle_swirl(self):
        print(f"{self.name} performs a mesmerizing tentacle swirl underwater. A dance of the Octo-Shark realm!")

    def ink_surge_attack(self, target):
        print(f"Danger! {self.name} unleashes a surge of ink at {target}. A tactical move in the depths!")

    def deep_sea_octo_shark_magic(self):
        print(f"{self.name} taps into deep-sea octo-shark magic. Mystical currents and aquatic wonders!")

# Let's summon the Octo-Shark squad and embark on an Aquatic Python Thrill!

octo_shark_squad = []

for i in range(1, 101):
    octo_shark_name = f"OctoShark{i}"
    octo_shark = OctoShark(octo_shark_name)
    octo_shark_squad.append(octo_shark)

# Time for the Depths of Octo-Sharks Aquatic Python Thrills!

for octo_shark in octo_shark_squad:
    octo_shark.aquatic_tentacle_swirl()
    octo_shark.ink_surge_attack("Prey")
    octo_shark.deep_sea_octo_shark_magic()
    print("-" * 45)

print("The Depths of Octo-Sharks Aquatic Python Thrill was an oceanic spectacle!")
