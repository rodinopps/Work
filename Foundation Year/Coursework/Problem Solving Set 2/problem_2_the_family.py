# Problem 2 - Rodin Opuz
# The Family
# This is the family tree I decided to create. It is a dictionary with dictionaries and lists in it.
# I decided on the Breaking Bad family tree. It has three generations.
# I tried to completely finish.
# I chose it because it is my favourite show.
# It consists of 4 of the first generation. Mr White Sr, Mrs White, Mr Lambert and Mrs Lambert.
# It consists of 3 of the second generation. Walter Hartwell White Sr, Skyler White and Marie Schrader.
# It consists of 2 of the third generation. Walter Hartwell White Jr (Flynn) and Holly White.
# Each family member has a list of parents, children and siblings. If they do not have any of those, it is an empty list.
family_tree = {
    "Walter Hartwell White Sr": {
        "parents": ["Mr White Sr", "Mrs White"],
        "children": ["Walter Hartwell White Jr", "Holly White"],
        "siblings": []
    },
    "Skyler White": {
        "parents": ["Mr Lambert", "Mrs Lambert"],
        "children": ["Walter Hartwell White Jr", "Holly White"],
        "siblings": ["Marie Schrader"]
    },
    "Walter Hartwell White Jr": {
        "parents": ["Walter Hartwell White Sr", "Skyler White"],
        "children": [],
        "siblings": ["Holly White"]
    },
    "Holly White": {
        "parents": ["Walter Hartwell White Sr", "Skyler White"],
        "children": [],
        "siblings": ["Walter Hartwell White Jr"]
    },
    "Mr White Sr": {
        "parents": [],
        "children": ["Walter Hartwell White Sr"],
        "siblings": [],
    },
    "Mrs White": {
        "parents": [],
        "children": ["Walter Hartwell White Sr"],
        "siblings": []
    },
    "Mr Lambert": {
        "parents": [],
        "children": ["Skyler White", "Marie Schrader"],
        "siblings": []
    },
    "Mrs Lambert": {
        "parents": [],
        "children": ["Skyler White", "Marie Schrader"],
        "siblings": []
    },
    "Marie Schrader": {
        "parents": ["Mr Lambert", "Mrs Lambert"],
        "children": [],
        "siblings": ["Skyler White"]
    }
}



# This is used to output a list of the family member's children. If they do not have children, it just outputs an empty list.
def get_children(name): # This is a function that takes a name as a parameter.
    if name in family_tree: # If the name is in the dictionary, it will output the list of children.
        return family_tree[name]["children"] # This returns the children list from the family member dictionary from the family tree dictionary.
    else: # If the name was not a family member, it will output this instead.
        return f"There is no person called '{name}' in the family tree. " # This outputs the error message.



# This is used to output a list of the family member's siblings. If they do not have siblings, it just outputs an empty list.
def get_siblings(name): # This is a function that takes a name as a parameter.
    if name in family_tree: # If the name is in the dictionary, it will output the list of siblings.
        return family_tree[name]["siblings"] # This returns the sibling list from the family member dictionary from the family tree dictionary.
    else: # If there is not family member called the name, it will output this instead.
        return f"There is no person called '{name}' in the family tree. "  # This outputs the message that there is no person called the name in the family tree.



# This outputs the list of common ancestors between two people. If they have no common ancestors, it just outputs an empty list.
def find_common_ancestors(name1, name2): # This is a function that takes two names as parameters. 
    if name1 in family_tree and name2 in family_tree: # If the names are in the family tree, it will find the common ancestors and output it.
        
        name1_parents = family_tree[name1]["parents"] # This stores the first names parents.
        name2_parents = family_tree[name2]["parents"] # This stores the second names parents.
        
        name1_grandparents, name2_grandparents, common_parents, common_grandparents = [], [], [], [] # This creates four dictionaries.
        
        for i in name1_parents: # This goes through the list of the first name's parents.
            name1_grandparents.append(family_tree[i]["parents"]) # This appends the grandparents (parent's parents) of the first name to the list.
            if i in name2_parents: # If the first name's parent is in the list of the second name's parents, it runs the code below.
                common_parents.append(i) # It appends the common parent between the two names to the list.
                
        for i in name2_parents: # This goes through the list of the second name's parents.
            name2_grandparents.append(family_tree[i]["parents"]) # This appends the grandparents (parent's parents) of the second name to the list.

        for i in name1_grandparents: # This goes through the first name's grandparents.
            if i in name2_grandparents: # If the first name's grandparent is in the list of the second name's grandparents, it runs the code below.
                common_grandparents.append(i) # It appends the common grandparent between the two names to the list.

        return f"{common_parents}, {common_grandparents}" # Once the for loops have been finished, it outputs the common parents and the common grandparents (ancestors).
    
    else: # If the names are not in the family tree, it will run the code below.
        return "You have not entered names from the family tree. " # This outputs the error message.


                                
# This outputs True or False if the two people are related. 
def is_related(name1, name2): # This is a function that takes two names
    if name1 in family_tree and name2 in family_tree: # If both names are in the family tree, it will find if two of the names are related.
        
        parents = family_tree[name1]["parents"] == family_tree[name2]["parents"] and (family_tree[name1]["parents"] != [] and family_tree[name2]["parents"])  # This stores a boolean variable True or False depending on if the two names share the same parents.
        siblings = name1 in family_tree[name2]["siblings"] or name2 in family_tree[name1]["siblings"] # This stores a boolean variable True or False depending on if the two names are siblings.
        children = name1 in family_tree[name2]["children"] or name2 in family_tree[name1]["children"] # This stores a boolean variable True or False depending on if one of the names are the other's child. Child and Parent relationship.
        
        return parents or siblings or children # If any one of these are True, it will output as True.

    else: # If one of the names or both of the names are not in the family tree dictionary, it will output an error message.
        return "You have not entered names from the family tree. " # This is the error message that explains to the user how they have not entered a correct name.



# This outputs the family tree starting from the name.
def print_family_tree(name): # This is a function that takes a name as a parameter.
    if name in family_tree: # If the name is in the family tree, it will run the code below.
        print(f"{name}") # This prints the name of the person.
        
        if family_tree[name]["parents"] != []: # If the person has parents in the list and its not just empty, it will print out the parents. This checks if the person has parents.
            print(f"Parents: {', '.join(family_tree[name]['parents'])}") # This prints out the parents.
            
        if family_tree[name]["children"] != []: # If the person has children, it will print out the children.
            print(f"Children: {', '.join(family_tree[name]['children'])}") # This prints out the children.
            
        if family_tree[name]["siblings"] != []: # If the person has sublings, it will print out their siblings.
            print(f"Siblings: {', '.join(family_tree[name]['siblings'])}") # This prints out the siblings.
            
        for i in family_tree[name]["children"]: # This repeats the same for the children of the name. It is a for loop that uses recursion.
            print() # For readibility
            
            print_family_tree(i) # This calls the function with the parameter i (The current child).
    else: # If the name is not in the family tree, it will output the error message.
        return f"There is no person called '{name}' in the family tree. " # This outputs the error message.

# This is just different tests for each function. Examples of the output as shown in the document.
# The tests are labelled aswell just to make it easier for me.
print("get_children function")
print(get_children("Walter Hartwell White Sr"))
print()
print("get_siblings function")
print(get_siblings("Skyler White"))
print()
print("find_common_ancestors function")
print(find_common_ancestors("Walter Hartwell White Jr", "Holly White"))
print()
print("is_related function")
print(is_related("Mr White Sr", "Mrs Lambert"))
print()
print("is_related function")
print(is_related("Walter Hartwell White Sr", "Walter Hartwell White Jr"))
print()
print("print_family_tree function")
print_family_tree("Walter Hartwell White Sr")
