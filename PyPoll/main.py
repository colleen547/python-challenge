"""PyPoll Homework"""

# Import OS module to create file paths across operating system
import os

# Import Module for reading CSV file
import csv

# Set path to collect data from the Resources folder
election_data = os.path.join("Resources","election_data.csv")

# Create a dictionary placeholder
candidate_dict = {}

# Open the data file
with open (election_data) as election_data:
    csv_reader = csv.reader(election_data)

# Read the data
    csvreader = csv.reader(election_data)

    # Read the header
    csv_header = next(csvreader)
    # Initialize the total votes
    total_votes = 0

    # Loop through the data file
    for row in csvreader:
            candidate = row[2]
            total_votes +=1

            # If the candidate is in the dictionary add to vote count
            if candidate in candidate_dict:
                vote = candidate_dict.get(candidate)
                vote +=1
                candidate_dict[candidate] = vote

            #otherwise add the candidate and set the vote to 1
            else:
                candidate_dict[candidate] = 1

    # Initialize the winner variables
    winner = ""
    winner_votes = 0

    # Set the path for the txt file
    output_path=os.path.join("Outputs", "PyPoll_output.txt")

    # Open the file
    with open (output_path, 'w', newline='') as textfile:
        
        # Print to the terminal
        print(f"Election Results")
        print("-------------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------------")

# Write to the textfile
        textfile.write("Election Results\n")
        textfile.write("-------------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("-------------------------------\n")

# Loop through the candidates
        for candidate in candidate_dict:
            votes = candidate_dict[candidate]
            if votes > winner_votes:
                winner = candidate
                winner_votes = votes
            print(f"{candidate}: {100*votes/total_votes:.3f}% ({votes})")
            # Write to textfile
            textfile.write(f"{candidate}: {100*votes/total_votes:.3f}% ({votes})\n")
    
        print("-------------------------------")
        print(f"Winner: {winner}")
        print("-------------------------------")

        # Write to the textfile
        textfile.write("-------------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("-------------------------------\n")
