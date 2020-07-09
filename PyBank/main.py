"""PyBank Homework"""

# Import OS module (This allows us to create file paths across operating systems)
import os
# Module for reading CSV file
import csv
import sys 
import datetime

# Path to collect data from the Resources folder
filetoload = os.path.join("Resources","budget_data.csv")

# Create Variables
total_months = 0
total_net = 0
# Create Lists
months_list = []
netchange_list = []

with open (filetoload) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    firstrow = next(csvreader)

    # Total number of months in CSV file
    total_months = total_months + 1

    # Net total amount of "Profit/Losses" over the entire period
    total_net = total_net + int(firstrow [1])
    previous_net = int(firstrow [1])
    
    for row in csvreader:
    # The total number of months included in the dataset
        total_months = total_months + 1
    # The net total amount of "Profit/Losses" over the entire period    
        total_net = total_net + int(row [1])
    # The average of the changes in "Profit/Losses" over the entire period    
        change = int(row[1])-previous_net
        previous_net = int(row [1])
        netchange_list = netchange_list + [change]
        months_list = months_list + [row[0]]
                
# The average of the changes in "Profit/Losses" over the entire period as average_net
average_net = round(sum(netchange_list)/len(netchange_list),2)

# The greatest increase in profits (date and amount) over the entire period
greatest_incr_value = max(netchange_list)
greatest_incr_month = months_list[netchange_list.index(max(netchange_list))]

# The greatest decrease in losses (date and amount) over the entire period
greatest_decr_value = min(netchange_list)
greatest_decr_month = months_list[netchange_list.index(min(netchange_list))]

# Print Results
print("Financial Analysis")
print("---------------------------")
print (f"Total Months: {total_months}")
print (f"Total: ${total_net}")
print (f"Average Change: ${average_net}")
print (f"Greatest Increase in Profits: {greatest_incr_month} (${greatest_incr_value})")
print (f"Greatest Decrease in Profits: {greatest_decr_month} (${greatest_decr_value})")

# Set the path for the txt file
output_path=os.path.join("Outputs", "PyBank_output.txt")

# Open the file
with open (output_path, 'w', newline='') as textfile:

# Write to the textfile
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_net}\n")
    textfile.write(f"Average Change: ${average_net}")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_incr_month} (${greatest_incr_value})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decr_month} (${greatest_decr_value})\n")
