'''
Jahid Emon & Hugo Piper's work.
Family tree project 1.
Paradigms of Programming
26/10/2024


TODO: Add date of death and calcuate it, Use DOCSTRINGS for better marks, test for bugs and fix, update layout of certain things for better readability
'''


from datetime import datetime

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
        
        
    # Display siblings of the Family member.
    def get_siblings(self):
        if len(self.parents[0].children) == 1: print("\nNo siblings listed."); exit
        if self.parents: #if parents exist
            print("\nSiblings:")
            for sibling in self.parents[0].children:
                if sibling != self:
                    print(f" - {sibling.first_name} {sibling.last_name}")


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

    def display_immediate_family_info(self):
    # Display parents if they exist
        if self.parents:
            print("\nParents:")
            for parent in self.parents:
                print(f" - {parent.first_name} {parent.last_name}")
        else:
            print("\nNo parents listed.")
    
        # Display children if they exist
        if self.children:
            print("\nChildren:")
            for child in self.children:
                print(f" - {child.first_name} {child.last_name}")
        else:
            print("\nNo children listed.")

    def display_extended_family_info(self):
        '''
        This function will display the extended family information.
        It finds the member's grandparents, aunts, uncles, and cousins.
        '''
        # Display grandparents
        grandparents = self.get_grandparents()
        if grandparents:
            print("\nGrandparents:")
        for grandparent in grandparents:
            print(f" - {grandparent.first_name} {grandparent.last_name}")
        else:
            print("\nNo grandparents listed.")

        # Aunts and Uncles
        aunts_uncles = set()
        for parent in self.parents:
            # Check if the parent has grandparents (parents of their own)
            if parent.parents: #if parents paents (grandparents) exist
                for grandparent in parent.parents: #counts the amount of parents parents (grandparents)
                    for sibling in grandparent.children:  # Grandparent's children are the parent and aunts/uncles
                        if sibling != parent:  # Exclude the parent themselves
                            aunts_uncles.add(sibling)

        if aunts_uncles:
            print("\nAunts and Uncles:")
            for aunt_uncle in aunts_uncles:
                print(f" - {aunt_uncle.first_name} {aunt_uncle.last_name}")
        else:
            print("\nNo aunts or uncles listed.")

        # Cousins (children of aunts/uncles only)
        cousins = set()
        for aunt_uncle in aunts_uncles:
            cousins.update(aunt_uncle.children)  # Collect children of each aunt or uncle

        if cousins:
            print("\nCousins:")
            for cousin in cousins:
                print(f" - {cousin.first_name} {cousin.last_name}")
        else:
            print("\nNo cousins listed.\n")

         
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



# Dictionary to store all the family members
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
    "Micheal Porter": micheal,
    "Robert Clark": robert,
    "Niko Clark": niko,
    "Willow Clark": willow,
}


def main():
    """
    This function retrieves and displays information about a family member based on the user’s input.
    Options include listing family members, viewing birthdays, or exiting the program.
    """
    while True:
        # Get user input
        name = input(
            "\n\n- Enter the full name of the family member (ex: 'Robert Clark')\n"
            "- Type 'list' for a list of family members\n"
            "- Type 'birthdays' for a list of birthdays\n"
            "- Type 'exit' to exit\n\n> "
        ).strip().title()

        # Handle special commands: list, birthdays, and exit
        if name == 'List':
            print("\nAvailable family members:\n")
            for family_name in family_members.keys():
                print(family_name)
            continue  # Go back to the start of the loop for the next input

        elif name == 'Birthdays':
            print("\nHere are the family members' birthdays in day/month order:\n")
            # Sorts family members by birth day and month, ignoring the year. This uses a sorted function to sort the data that the 'lambda' function extracts (lambda is used to extract the birth day data and the birth month data)
            sorted_birthdays = sorted(family_members.items(), key=lambda x: datetime.strptime(x[1].birthday, "%d-%m-%Y").strftime("%m-%d"))
            for family_name, member in sorted_birthdays:
                #string formatting has been used here to neatly present the list of birthdays
                print(f"{family_name:.<20}{member.birthday} ")
            continue # Go back to the start of the loop for the next input

        elif name == 'Exit':
            print("User decided to exit. Exiting...")
            break  # Exit the loop and end the program

        # Check if the entered name matches a family member
        member = family_members.get(name)
        if not member:
            print("Family member not found. Please check the spelling and format (e.g., 'First Last').")
            continue  # Go back to the start of the loop for the next input

        # Display options for the selected member
        while True:
            try:
                selection = int(input(
                    f"\nPlease select what info you would like to see about {name} or type '6' to return to the main menu\n"
                    "1. View Close Family\n"
                    "2. View Extended Family\n"
                    "3. View Siblings\n"
                    "4. View Cousins\n"
                    "5. Exit\n"
                    "6. Return to main menu\n> "
                ))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue

            # Perform actions based on user selection
            if selection == 1:
                member.display_immediate_family_info()
            elif selection == 2:
                member.display_immediate_family_info()
                member.display_extended_family_info()
            elif selection == 3:
                member.get_siblings()
            elif selection == 4:
                member.display_extended_family_info()  # Assuming cousins are included in extended family
            elif selection == 5:
                print("User decided to exit. Exiting...")
                quit() # End the program
            elif selection == 6:
                break  # Return to the main menu
            else:
                print("Invalid selection. Please choose a valid option.")

# Runs the main program
main()
