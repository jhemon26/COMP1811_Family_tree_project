'''
Jahid Emon & Hugo Piper's work.
Family tree project 1.
Paradigms of Programming
26/10/2024
Year 1, term 1 graded coursework.
'''

import datetime
from datetime import date
import sys #Importing sys so that exiting the program works as intended.

class FamilyMember:
    
    def __init__(self, first_name, last_name, birthday, death):
        '''
        The __init__ method initializes each instance with a;
        firstname, lastname, birthday & death date.
        empty lists for the parents/children are also created.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.parents = []
        self.children = []
        self.spouse = None
        self.death = death
    
    def calculate_age(self, print_age= False):
        '''
        Calculates the age of a member based on their date of birth.
        Also determines if a member is dead or alive and prints their death date (if dead).
        '''
        age = ()
        
        birth_date = datetime.datetime.strptime(self.birthday, "%d-%m-%Y")
        if self.death == "Still Alive":
                death_date = date.today()
        else:
            death_date = datetime.datetime.strptime(self.death, "%d-%m-%Y")
        age = death_date.year - birth_date.year
        
        if print_age:
            print(f"\nAge of {self.first_name} {self.last_name}: {age} years")
            print(f"Date of Birth: {self.birthday}.")
            if self.death != "Still Alive": 
                print(f"Date of Death: {self.death}")
            else:
                print("Still Alive.")
        return age  

    def average_age_of_death():
        '''
        - Gathers everyone who is dead (!= 'Still Alive')
        - Uses a lambda function to sort all the dead members from oldest to youngest and prints them to the terminal.
        - Calculates  the average age by additioning the age of all the dead members and dividing the total by the quanitity of dead members.
        '''
        deceased_members = []
    
        # Collect each deceased family member's age at death
        for member in family_members.values():
            if member.death != "Still Alive":
                age_at_death = member.calculate_age()
                deceased_members.append((member.first_name + " " + member.last_name, age_at_death))
    
        # Check if we have deceased members to calculate the average
        if deceased_members:
            # Sort by age at death in descending order
            deceased_members.sort(key=lambda x: x[1], reverse=True)
        
            # Display each deceased member's age at death
            print("\nDeceased family members sorted by age at death (oldest to youngest):")
            for name, age in deceased_members:
                print(f"{name} died at age {age}.")
        
            # Calculate and display the average age of death
            average_age = sum(age for _, age in deceased_members) / len(deceased_members)
            print(f"\nAverage age of death: {average_age:.2f} years")
        else:
            print("\nNo deceased family members to calculate average age of death.")

    def average_number_of_children():
        """
        This method displays a list of each family member showing if they have children and the final average 
        number of children per person who has children.
        """
        total_children = 0
        people_with_children = 0
        total_people = len(family_members)
    
        print("\nFamily Members and Their Number of Children:\n")
    
        # Loop through each family member and count their children
        for member in family_members.values():
            num_children = len(member.children)
            total_children += num_children  # Add to total children count
            if num_children > 0:
                people_with_children += 1  # Count this person if they have children
                print(f"{member.first_name} {member.last_name}: {num_children} children")
            else:
                print(f"{member.first_name} {member.last_name}: No children")
    
        # Calculate and display the average number of children per person with children
        if people_with_children > 0:
            average_children = total_children / people_with_children
            print(f"\n\nAverage number of children per person with children: {average_children:.2f}")
            average_children = total_children / total_people
            print(f"\nAverage number of children per person in the entire family: {average_children:.2f}")
        else:
            print("\nNo family members with children to calculate the average.")
    
    
    def add_parent(self, parent):
        '''
        This function links the family member entered to a parent.
        For instance: if you have a family member Collin and you call collin.add_parent(henry), it links Henry as Collin's parent and vice versa.
        '''
        self.parents.append(parent)
        parent.children.append(self)
        
        
    # Display siblings of the Family member.
    def get_siblings(self, print_siblings=True):

        siblings = []
    
        # Check if parents list is empty to avoid index error
        if not self.parents:
            if print_siblings:
                print("\nNo parents listed, so no siblings.")
            return siblings

        # Check if there is only one child under the parent
        if len(self.parents[0].children) == 1:
            if print_siblings:
                print("\nNo siblings listed.")
            return siblings

        # If parents exist, proceed to find siblings
        if self.parents:
            for sibling in self.parents[0].children:
                if sibling != self:
                    siblings.append(sibling)

            # Print siblings only if requested
            if print_siblings:
                print("\nSiblings:")
                for sibling in siblings:
                    print(f" - {sibling.first_name} {sibling.last_name}")

        return siblings



    def get_grandparents(self):
        '''
        This method links the family member entered to a grandparent.
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
        This method finds and returns the grandchildren of the family member
        by finding the children of a family member's children.
        It uses a set to avoid duplicates.
        '''
        grandchildren = set()
        for child in self.children:
            grandchildren.update(child.children)  # Use 'update' to add all children of each child
        return list(grandchildren)  # Convert set back to list before returning
    
    def get_cousins(self):
        '''
        Finds and prints the cousins of the family member by checking the children of the members parents' siblings.
        '''
        cousins = set()
        
        if self.parents:
            for parent in self.parents:
                siblings = parent.get_siblings(print_siblings=False)  # Retrieve the siblings list
                for sibling in siblings:
                    cousins.update(sibling.children)
        
        if cousins:
            print("\nCousins:")
            for cousin in cousins:
                print(f" - {cousin.first_name} {cousin.last_name}")
        else:
            print("\nNo cousins listed.\n")


    def display_immediate_family_info(self, childcount):
        '''
        This method displays a members immediate family information.
        This includes: Parents & Children of a member.
        The siblings are displayed in another method.
        This method also includes Feature F3B: Find the number of children for each individual
        '''
         # Find spouse by checking the other parent of each child
        spouse = None
        for child in self.children:
            for parent in child.parents:
                if parent != self:
                    spouse = parent
                    break
            if spouse:
                break
    
        # Display spouse if one is found
        if spouse:
            print(f"\nSpouse: {spouse.first_name} {spouse.last_name}")
        else:
            print("\nNo spouse listed.")

        # Display parents if they exist
        if self.parents:
            print("\nParents:")
            for parent in self.parents:
                print(f" - {parent.first_name} {parent.last_name}")
        else:
            print("\nNo parents listed.")
    
        # Display children if they exist
        childcount = 0
        if self.children:
            print("\n\nChildren:")
            for child in self.children:
                childcount += 1
                print(f" - {child.first_name} {child.last_name}") #Displays a members child name and surname
            print(f"\n{self.first_name} {self.last_name} has {childcount} children.") #Displays the amount of children for a member
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

       # Grandchildren
        grandchildren = self.get_grandchildren()
        if grandchildren:
              print("\nGrandchildren:")
              for grandchild in grandchildren:  # Use a single item variable for iteration
                 print(f" - {grandchild.first_name} {grandchild.last_name}")  # Correctly reference grandchild
        else:
            print("\nNo grandchildren listed.")


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
margret = FamilyMember("Margret", "Doyle", "06-04-1922", "14-07-1989")
albert = FamilyMember("Albert", "Adams", "23-02-1914", "30-10-1984")
janet = FamilyMember("Janet", "Fisher", "13-05-1922", "11-02-1994")
nicholas = FamilyMember("Nicholas", "Porter", "20-03-1919", "07-08-1997")
sally = FamilyMember("Sally", "Smith", "16-10-1924", "24-04-2018")
william = FamilyMember("William", "Jones", "08-11-1923", "09-10-2001")
peggy = FamilyMember("Peggy", "Fring", "31-12-1929", "06-07-2022")
gus = FamilyMember("Gus", "Clark", "18-07-1918", "18-07-1989")

# Generation 2 (Parents)
olivia = FamilyMember("Olivia", "Adams", "27-09-1942", "10-02-2012")
joshua = FamilyMember("Joshua", "Porter", "10-07-1945", "14-06-2010")
linda = FamilyMember("Linda", "Jones", "01-01-1946", "21-08-2018")
henry = FamilyMember("Henry", "Clark", "14-03-1949", "28-10-2020")
doris = FamilyMember("Doris", "Jenkins", "06-04-1951", "Still Alive")

# Generation 3 (Children)
charlotte = FamilyMember("Charlotte", "West", "09-09-1969", "Still Alive")
jake = FamilyMember("Jake", "Porter", "29-09-1972", "Still Alive")
sam = FamilyMember("Sam", "Porter", "05-04-1970", "Still Alive")
gracie = FamilyMember("Gracie", "Porter", "10-07-1974", "Still Alive")
collin = FamilyMember("Collin", "Clark", "16-09-1976", "12-03-2020")
ellie = FamilyMember("Ellie", "Clark", "11-11-1978", "Still Alive")
liliana = FamilyMember("Liliana", "Clark", "28-08-1968", "Still Alive")

#todo change dates of birth

# Generation 4 (Grandchildren)
penny = FamilyMember("Penny", "Porter", "01-02-2002", "Still Alive")
micheal = FamilyMember("Micheal", "Porter", "08-12-2004", "Still Alive")
robert = FamilyMember("Robert", "Clark", "01-05-2005", "28-03-2022")
niko = FamilyMember("Niko", "Clark", "01-05-2005", "Still Alive")
willow = FamilyMember("Willow", "Clark", "27-11-2007", "Still Alive")

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



'''
 Dictionary to store all the family members to call them in an easier fashion via the code
'''
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
    Options include listing family members, viewing birthdays, calculating death dates, finding relatives, exiting the program & returning to the main menu..
    """
    while True:
        # Get user input
        name = input(
            "\n-------------------------------------------\n"
            "\n- Enter the full name of the family member (ex: 'Robert Clark')\n"
            "- Type 'list' for a list of family members\n"
            "- Type 'birthdays' for a list of birthdays\n"
            "- Type 'death' for a calculation of the average age of death within the family\n"
            "- Type 'children' to view the average amount of children per person within the family\n"
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
            sorted_birthdays = sorted(family_members.items(), key=lambda x: datetime.datetime.strptime(x[1].birthday, "%d-%m-%Y").strftime("%m-%d"))
            for family_name, member in sorted_birthdays:
                print(f"{family_name:.<20}{member.birthday} ")
            continue

        elif name == 'Death':
            FamilyMember.average_age_of_death()
            continue  # Skip the rest of the loop for this iteration

        elif name == 'Children':
            FamilyMember.average_age_of_children()
            continue


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
                    "\n--------------------\n"
                    f"\nPlease select what info you would like to see about {name}\n\n"
                    "1. View Close Family\n"
                    "2. View Extended Family\n"
                    "3. View Siblings\n"
                    "4. View Cousins\n"
                    "5. View Age, Date of Birth & Date of Death\n\n" 
                    "6. Return to Main Menu\n"
                    "0. Quit\n\n> "
                ))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue

            # Perform actions based on user selection
            if selection == 1:
                member.display_immediate_family_info(0)
                member.get_siblings()
            elif selection == 2:
                member.display_immediate_family_info(0)
                member.display_extended_family_info()
                member.get_siblings()
            elif selection == 3:
                member.get_siblings()
            elif selection == 4:
                cousin = member.get_cousins()
            elif selection == 5:
                  member.calculate_age(print_age=True) # Runs the calculate_age method
            elif selection == 6:
                break #returns to the main menu
            elif selection == 0:
                print("User decided to exit. Exiting...")
                sys.exit()  # Immediately terminate the program
            else:
                print("Invalid selection. Please choose a valid option.")
                continue

            #Allow user to view more info about a member, return to the main menu or exit the program.
            asking_user_again = input("\n->Do you want to see more information about this family member?\n"   # Continue to ask for more info about this family member
                                    
                                      "\n>Type 'YES' to View the Information List again.\n"
                                      ">Type 'RETURN' to Return to the Main Menu. \n"
                                      ">Type 'EXIT' to Exit the Program. \n\n> "
            ).strip().upper()     # to avoid case sensitivity and any white spaces.

            
            
            if asking_user_again == "YES":    # if yes then show to list again.
                continue
            elif asking_user_again == "RETURN":  # if return then go back to the main menu.
                return main()
            elif asking_user_again == "EXIT": # if exit then exit the system.
                print("User decided to exit. Exiting...")
                sys.exit()  # Immediately terminate the program
            else:
                print("Invalid option. Please enter 'YES', 'RETURN', or 'EXIT'.")
                continue  # Ask again if the input is invalid

# Runs the main program
main()
