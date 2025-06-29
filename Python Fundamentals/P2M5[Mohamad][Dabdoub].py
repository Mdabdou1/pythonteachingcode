# Final Project - Element_Quiz
# Author: Mohamad Dabdoub

# Step 1: Download the file (for Jupyter only — skip this line in pure Python scripts)
# !curl -o elements1_20.txt https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt

# Step 2: Load first 20 element names into a list
elements_file = open("elements1_20.txt", "r")
first_20_elements = []

line = elements_file.readline()
while line:
    element = line.strip().lower()
    if element:
        first_20_elements.append(element)
    line = elements_file.readline()

elements_file.close()


# Step 3: Define get_names function
def get_names():
    print("Welcome Mohamad Dabdoub! List any 5 of the first 20 elements in the Period Table:")
    user_elements = []
    while len(user_elements) < 5:
        element_input = input("Enter the name of an element: ").strip().lower()
        if element_input == "":
            print("No empty input allowed.")
        elif element_input in user_elements:
            print(f"{element_input.title()} was already entered")
        else:
            user_elements.append(element_input)
    return user_elements


# Step 4: Main Quiz Logic
user_inputs = get_names()

correct = []
incorrect = []

for element in user_inputs:
    if element in first_20_elements:
        correct.append(element.title())
    else:
        incorrect.append(element.title())

# Step 5: Calculate score
score = len(correct) * 20

# Step 6: Output results
print(f"\n{score} % correct")
if correct:
    print("Found:", " ".join(correct))
if incorrect:
    print("Not Found:", " ".join(incorrect))
