# [] create The Weather


# Module 4 Required Coding Activity - The Weather
# Author: Mohamad Dabdoub

# Download the file (Jupyter only — skip this line in .py script)
# !curl -o mean_temp.txt https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv

# Step 1: Open file in append mode and add Rio
with open("mean_temp.txt", "a+") as mean_temps:
    mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")

# Step 2: Reopen file for reading
mean_temps = open("mean_temp.txt", "r")

# Step 3: Read and split headings
headings = mean_temps.readline()
headings_list = headings.strip().split(",")

# Step 4: Print name
print("Mohamad Dabdoub\n")

# Step 5: Read city data line by line
line = mean_temps.readline()
while line:
    city_data = line.strip().split(",")
    city = city_data[0]
    temp_high = city_data[2]
    print(f"City of {city} {headings_list[2]} is {temp_high} Celsius")
    line = mean_temps.readline()

# Step 6: Close file
mean_temps.close()

