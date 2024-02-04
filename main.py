# Welcome to the OctoVerse - Octopus Python Party!

class Octopus:
    def __init__(self, name):
        self.name = name

    def tentacle_dance(self):
        print(f"{self.name} is doing the Tentacle Dance. It's a hit in the ocean dance floors!")

    def ink_attack(self, target):
        print(f"Beware! {self.name} squirts ink at {target}. A master of camouflage!")

    def octo_magic(self):
        print(f"{self.name} is practicing ancient octo-magic. Cephalopod sorcery at its finest!")

# Let's summon some octopuses and make them perform!

octopus_party = []

for i in range(1, 101):
    octopus_name = f"Octo{i}"
    octo = Octopus(octopus_name)
    octopus_party.append(octo)

# Time for the octopus extravaganza!

for octo in octopus_party:
    octo.tentacle_dance()
    octo.ink_attack("Predator")
    octo.octo_magic()
    print("-" * 30)

print("The OctoVerse Python Party was a blast!")
