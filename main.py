import json

# Function to write data to JSON file
def write_to_json(data, json_file_path, password):
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file)
        print(f"User input has been written to {json_file_path}.")

# Function to read data from JSON file
def read_from_json(json_file_path, password):
    with open(json_file_path, "r") as json_file:
        stored_data = json.load(json_file)
        if password in stored_data:
            return stored_data[password]
        else:
            return None

# Get user input
user_input = input("Enter some text: ")
password = input("Enter a password to protect your data: ")

# Create a dictionary to store the user input
data = {password: user_input}

# Specify the JSON file path
json_file_path = "data.json"

# Write the data to the JSON file
write_to_json(data, json_file_path, password)

cmd = input("Enter the password to access the data: ")

# Check if the entered password matches and print the stored data
stored_data = read_from_json(json_file_path, cmd)
if stored_data is not None:
    print(f"Data protected with password '{cmd}' is: {stored_data}")
else:
    print("Incorrect password. Access denied.")
