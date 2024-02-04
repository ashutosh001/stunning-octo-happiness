# Welcome to the Polar OctoFrost - Arctic Python Adventure!

class PolarOcto:
    def __init__(self, name):
        self.name = name

    def icy_tentacle_twirl(self):
        print(f"{self.name} gracefully twirls its icy tentacles. A dance of frost and elegance!")

    def frosty_ink_blast(self, target):
        print(f"Watch out! {self.name} releases a burst of frosty ink at {target}. Subzero surprise!")

    def arctic_octo_magic(self):
        print(f"{self.name} practices ancient arctic octo-magic. Conjuring frost and snowstorms!")

# Let's summon the Polar OctoFrost clan and let the Arctic Python Adventure unfold!

polar_octofrost_clan = []

for i in range(1, 101):
    polar_octo_name = f"PolarOcto{i}"
    polar_octo = PolarOcto(polar_octo_name)
    polar_octofrost_clan.append(polar_octo)

# Time for the Polar OctoFrost Arctic Python Adventure!

for polar_octo in polar_octofrost_clan:
    polar_octo.icy_tentacle_twirl()
    polar_octo.frosty_ink_blast("Seal")
    polar_octo.arctic_octo_magic()
    print("-" * 40)

print("The Polar OctoFrost Arctic Python Adventure was an icy marvel!")
