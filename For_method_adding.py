    
import pprint
import datetime
from datetime import date

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
    def __init__(self, first_name, last_name, birthday, death):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.parents = []
        self.children = []
        
        self.death = death
        self.calculate_age()
        
        
    def calculate_age(self, print_age= False):
        age = ()
        
        
        birth_date = datetime.datetime.strptime(self.birthday, "%d-%m-%Y")
        if self.death == "Still Alive":
                death_date = date.today()
        else:
            death_date = datetime.datetime.strptime(self.death, "%d-%m-%Y")
        age = death_date.year - birth_date.year
        
        if print_age:
            print(f"Age of {self.first_name} {self.last_name}: {age} years")
            print(f"Date of Birth: {self.birthday}.")
            if self.death != "Still Alive": 
                print(f"Date of Death: {self.death}")
            else:
                print("Still Alive.")
        return age    
            
        
        
        
        
        
        
        
        
        

    def add_parent(self, parent):
        '''
        This function links the family member entered to a parent.
        For instance: if you have a family member Collin and you call collin.add_parent(henry), it links Henry as Collin's parent and vice versa.
        '''
        self.parents.append(parent)
        parent.children.append(self)
        
        
        
    
    # Display siblings of the Family member.
    def get_siblings(self, print_siblings=True):   #print_siblings will determine if the siblings will be print or not.
        
        siblings = set()  # used set so that it avoids duplicates as we are accessing siblings from multiple parents.
    
        if self.parents:   #if the family member has parents.
            
            for parent in self.parents:       # it will go through each parent> to child th parent's children and add them to the siblings set.
                for sibling in parent.children:  # Parent's children are the siblings.
                    if sibling != self:  # using != to cut off the searched family member from the list of siblings.
                        siblings.add(sibling)    # when got the siblings, add(s.) will add it to the siblings set.
        
        
        
        # Now we will use if print_siblings to determine if the siblings will be printed or not to avoid printing unwanted print-
        #-statements while calling the method onto the get_cousins method.
        if print_siblings:
            if siblings: #if siblings are found then print.
                print("\nSiblings:")
                for sibling in siblings:   # for individual sibling in the siblings set, using an f-string to print the F&L name.
                    print(f" - {sibling.first_name} {sibling.last_name}")
            else:
                print("\nNo siblings found.") 
        return list(siblings)  # Return the siblings as a list so that it can be used in other methods.
               
               
     # Display cousins of the Family member.               
    def get_cousins(self):
        
        cousins = set()  # used set s0 that it avoids duplicates as we are accessing cousins from multiple parents.
        if self.parents: # if the family member has parents.
            for parent in self.parents:  # it will check through each parent.
                siblings = parent.get_siblings(print_siblings=False)  # Used the get_siblings method to get the siblings of the parent
                # print_siblings=False to avoid printing the siblings of the parent.
                for sibling in siblings:  # for each sibling in the siblings list.
                    cousins.update(sibling.children)  # Add the children of each sibling to the cousins set.
    
        if cousins:   # if cousins are found then print. 
                print("\nCousins:")
                for cousin in cousins:
                    print(f" - {cousin.first_name} {cousin.last_name}")
        else:
            print("\nNo cousins listed.\n")   
        
        
        
        
     # Display grandparents of the Family member.   
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
    
    
    # Display grandchildren of the Family member.
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
    
    
    # Display the immediate family of the Family member.
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
            
            
        # Display grandparents
    def display_extended_family_info(self):
        '''
        This function will display the extended family information.
        It finds the member's grandparents, aunts, uncles, and cousins.
        '''
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
            if parent.parents:
                for grandparent in parent.parents:
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
nicholas = FamilyMember("Nicholas", "Porter", "20-03-1919", "07-08-1987")
sally = FamilyMember("Sally", "Smith", "16-10-1924", "24-04-2006")
william = FamilyMember("William", "Jones", "08-11-1923", "09-10-2001")
peggy = FamilyMember("Peggy", "Fring", "31-12-1929", "06-07-2010")
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
    "Micheal Porter": micheal,
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

    name = input("\n\nEnter the full name of the family member (ex: 'Robert Clark'), type 'list' for a list of family members, type exit to exit:\n> ").strip().title() #STRIP removes excess spaces, #TITLE capitalizes the start of each word to avoid incorrect entries.
   
    # name = "Robert Clark"  For debuggig purposes onlu (remove when no needed)
    
    if str(name) == 'List':
        print("\nAvailable family members:\n")
        for family_name in family_members.keys():
            print(family_name)  # Print all available names
        
        # Prompt user again after displaying the list
        name = input("\n\nEnter the full name of the family member (ex: 'Robert Clark'), type 'list' for a list of family members, type exit to exit:\n> ").strip().title()
        
        if name == 'Exit':
            quit("User decided to exit. Exiting...")
        member = family_members.get(name)
    elif str(name) == 'Exit':
        quit('User decided to exit. Exiting...')
    else:
        member = family_members.get(name)

    if member:
        selection = int(input(f"\nPlease select what info you would like to see about or you can type return to go to the previous menu {name}\n\n1. View Close Family\n2. View extended family\n3. View siblings\n4. View cousins\n5. Exit\n6. View Age, DoB Or Death date \n0. Return\n>"))
        
        # IF statements to determine what the user selected 
        if selection == 1:
            # Feature F1A Return close family if they exist
            member.display_immediate_family_info()
        
            
        elif selection == 2:
            # Feature F2B Return immediate AND extended family if they exist
            member.display_immediate_family_info()
            member.display_extended_family_info()  
             
        elif selection == 3:
            # Get and print siblings
            siblings = member.get_siblings()
            
        elif selection == 4:
            # Get and print cousins
            cousins = member.get_cousins()
              
        elif selection == 5: exit()
        #elif selection == 6:
        #  return main()    i wanted to make a return function but i will work on it later 
        
        elif selection == 6:
            member.calculate_age(print_age=True)
        
        else:
            print("You did not enter a valid selection.")
    else:
        print("Family member not found. Please check the spelling and format (e.g., 'First Last').")
        
    # Re-run main to allow another query
    main()

# Run the program
main()