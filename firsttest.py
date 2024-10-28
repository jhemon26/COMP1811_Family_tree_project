'''
Jahid Emon & Hugo Piper's work.
Family tree project 1.
Paradigms of Programming
26/10/2024

PROGRESS:
- Family tree created in Lucidchart with names, relationships and DOB's. Jahid Emon & Hugo Piper
- The family tree has been implemented into the program in the form of a list. Hugo Piper
- FEATURE 1 COMPLETE: Basic family tree query structure: The program is able to retrieve specific data from a family members when a user enters a family members name: DOB, Parents, Grandparents, Children & Grandchildren. Programmed by Hugo

TODO:Implement a system where the user can select what family members they would like to view (close family, distant family (uncles, cousins...etc)), Feature 2a, Feature 2b, Feature 2c, Feature 3a, Feature 3b
'''

class FamilyMember:
    '''
    The __init__ method initializes each instance with a;
     firstname, lastname, a birthday & empty lists for the parents/children.
    '''
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.parents = []
        self.children = []

    def add_parent(self, parent):
        '''
        This function links the family member entered to a parent.
        For instance: if you have a family member Collin and you call collin.add_parent(henry), it links Henry as Collin's parent and vice versa.
        '''
        self.parents.append(parent)
        parent.children.append(self)

    def get_grandparents(self):
        '''
        This function links the family member entered to a grandparent.
        For instance: if you have a family member Collin, it finds Collins parents (Henry) then it retrieves Henry's parents
        (which will be the grandparents Peggy and Gus according to the family tree we made.)

        'grandparents.extend(parent.parents)' takes the list of each parent's parents and combines them into the grandparents list.
        '''
        grandparents = []
        for parent in self.parents:
            grandparents.extend(parent.parents)
        return grandparents

    def get_grandchildren(self):
        '''
        This function finds and returns the grandchildren of the family member
        by finding the children of a family member's children.
        It uses a set to avoid duplicates.
        '''
        grandchildren = set()
        for child in self.children:
            grandchildren.update(child.children)  # Use 'update' to add all children of each child
        return list(grandchildren)  # Convert set back to list before returning

    def display_family_info(self):
        '''
        This function displays the first name, last name, birthday, parents, grandparents, and children if there are any.
        We used an if statement so in the event the system can't find listed kids...etc of a family member we dont get an error or a crash (We'd lose marks!).
        '''
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Birthday: {self.birthday}")

        if self.parents:
            print("Parents:")
            for parent in self.parents:
                print(f" - {parent.first_name} {parent.last_name}")
        else:
            print("No parents listed.")

        grandparents = self.get_grandparents()
        if grandparents:
            print("Grandparents:")
            for grandparent in grandparents:
                print(f" - {grandparent.first_name} {grandparent.last_name}")
        else:
            print("No grandparents listed.")

        if self.children:
            print("Children:")
            for child in self.children:
                print(f" - {child.first_name} {child.last_name}")
        else:
            print("No children listed.")

        grandchildren = self.get_grandchildren()
        if grandchildren:
            print("Grandchildren:")
            for grandchild in grandchildren:
                print(f" - {grandchild.first_name} {grandchild.last_name}")
        else:
            print("No grandchildren listed.")

'''
Below are instances of FamilyMember
'''
# Generation 1 (Grandparents)
margret = FamilyMember("Margret", "Doyle", "06-04-1922")
albert = FamilyMember("Albert", "Adams", "23-02-1914")
janet = FamilyMember("Janet", "Fisher", "13-05-1922")
nicholas = FamilyMember("Nicholas", "Porter", "20-03-1919")
sally = FamilyMember("Sally", "Smith", "16-10-1924")
william = FamilyMember("William", "Jones", "08-11-1923")
peggy = FamilyMember("Peggy", "Fring", "31-12-1929")
gus = FamilyMember("Gus", "Clark", "18-07-1918")

# Generation 2 (Parents)
olivia = FamilyMember("Olivia", "Adams", "27-09-1942")
joshua = FamilyMember("Joshua", "Porter", "10-07-1945")
linda = FamilyMember("Linda", "Jones", "01-01-1946")
henry = FamilyMember("Henry", "Clark", "14-03-1949")
doris = FamilyMember("Doris", "Jenkins", "06-04-1951")

# Generation 3 (Children)
charlotte = FamilyMember("Charlotte", "West", "09-09-1969")
jake = FamilyMember("Jake", "Porter", "29-09-1972")
sam = FamilyMember("Sam", "Porter", "05-04-1970")
gracie = FamilyMember("Gracie", "Porter", "10-07-1974")
collin = FamilyMember("Collin", "Clark", "16-09-1976")
ellie = FamilyMember("Ellie", "Clark", "11-11-1978")
liliana = FamilyMember("Liliana", "Clark", "28-08-1968")

#todo change dates of birth

# Generation 4 (Grandchildren)
penny = FamilyMember("Penny", "Porter", "01-02-2002")
micheal = FamilyMember("Micheal", "Porter", "08-12-2004")
robert = FamilyMember("Robert", "Clark", "01-05-2005")
niko = FamilyMember("Niko", "Clark", "01-05-2005")
willow = FamilyMember("Willow", "Clark", "27-11-2007")

'''
Setting up relationships for each generation below:
'''
# Linking generation 1 (grandparents) to generation 2 (parents)
olivia.add_parent(margret)
olivia.add_parent(albert)
joshua.add_parent(janet)
joshua.add_parent(nicholas)
linda.add_parent(sally)
linda.add_parent(william)
henry.add_parent(peggy)
henry.add_parent(gus)

# Linking generation 2 (parents) to generation 3 (children)
jake.add_parent(olivia)
jake.add_parent(joshua)
sam.add_parent(olivia)
sam.add_parent(joshua)
gracie.add_parent(olivia)
gracie.add_parent(joshua)
collin.add_parent(linda)
collin.add_parent(henry)
ellie.add_parent(linda)
ellie.add_parent(henry)
liliana.add_parent(henry)
liliana.add_parent(doris)

# Linking generation 3 (children) to generation 4 (grandchildren)
penny.add_parent(charlotte)
penny.add_parent(jake)
micheal.add_parent(charlotte)
micheal.add_parent(jake)
robert.add_parent(gracie)
robert.add_parent(collin)
niko.add_parent(gracie)
niko.add_parent(collin)
willow.add_parent(gracie)
willow.add_parent(collin)



# Dictionary to store family members
family_members = {
    "Margret Doyle": margret,
    "Albert Adams": albert,
    "Janet Fisher": janet,
    "Nicholas Porter": nicholas,
    "Sally Smith": sally,
    "William Jones": william,
    "Peggy Fring": peggy,
    "Gus Clark": gus,
    "Olivia Adams": olivia,
    "Joshua Porter": joshua,
    "Linda Jones": linda,
    "Henry Clark": henry,
    "Doris Jenkins": doris,
    "Charlotte West": charlotte,
    "Jake Porter": jake,
    "Sam Porter": sam,
    "Gracie Porter": gracie,
    "Collin Clark": collin,
    "Ellie Clark": ellie,
    "Liliana Clark": liliana,
    "Penny Porter": penny,
    "Micheal Micheal": micheal,
    "Robert Clark": robert,
    "Niko Clark": niko,
    "Willow Clark": willow,
}



def main():
    '''
    This function gets a family member's information (name, surname, birthdate, parents, grandparents, & kids) based on the name inputted by the user.
    IF the family member exists --> Display Family Info
    ELSE --> display "Family member not found."
    '''
    print("\nAvailable family members:\n")
    for name in family_members.keys():
        print(name)  # Print all available names.

    name = input("\nEnter the full name of the family member (e.g., 'Olivia Adams'):\n> ").strip().title() #STRIP removes excess spaces, #TITLE capitalizes the start of each word to avoid incorrect entries.
    member = family_members.get(name)
    if member:
      member.display_family_info()
    else:
      print("Family member not found. Please check the spelling and format (e.g., 'First Last').")


# Run the program
main()

