# SoftwareDeveloper class is inspired from the builder class from https://www.oodesign.com/builder-pattern
# It is close to, but not really an abstract interface and does have add_trait functional method.
class SoftwareDeveloper:

    def __init__(self):
        self.traits = []

    def add_trait(self, trait):
        self.traits.append(trait)


# TraitBuilder is my attempt at a Concrete Builder in Python.
# This class does most of the work constructing traits inheriting from SoftwareBuilder class
class TraitBuilder(SoftwareDeveloper):

    def build_traits(self):
        # Adding Curiosity
        self.add_trait("Curiosity: Research new technologies, learn new skills, improve your understanding.")
        # Adding Communication
        self.add_trait("Communication: Communicate clearly, listen actively, verify your understanding.")
        # Adding Determination
        self.add_trait("Determination: Follow through, break problems down, drive towards solutions.")

    def describe_trait(self):
        trait_num = 1
        print("\nSkilled software developers have the following important traits :")
        for trait in self.traits:
            print("{}: {}".format(trait_num, trait))
            trait_num += 1


def main():

    developer = TraitBuilder()
    developer.build_traits()
    developer.describe_trait()

    print("\n---NOTES---\n"
          " * This program is inspired from the Builder Pattern from https://www.oodesign.com/builder-pattern\n"
          " * SoftwareDeveloper is the Builder class and works like a psuedo interface.\n"
          " * TraitBuilder is the Concrete Builder class and inherits methods defined in SoftwareDeveloper.\n"
          " * The main method is the Director and the Product is the developer object.")
    print("-----------")
    print("\nHere is the programs logical flow and how it follows the builder pattern :")
    print("1: New object of TraitBuilder is created called developer.")
    print("2: The developer.build_traits() method add the traits of Curiosity, Communication, and Determination.")
    print("3: The developer.describe_trait() method formats and prints the traits and their descriptions.")


if __name__ == '__main__': main()



