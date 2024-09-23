import csv
import os

# Initialize variables
total_months = 0
net_total = 0
previous_profit_losses = 0
changes = []
dates = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(r'C:\Users\azerty\Desktop\Data Boot Camp\Challenges\Challenge 3\Python-Challenge\PyBank\Resources\budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        net_total += int(row[1])

        # Calculate the changes in "Profit/Losses"
        if total_months > 1:
            change = int(row[1]) - previous_profit_losses
            changes.append(change)
            dates.append(row[0])

            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        previous_profit_losses = int(row[1])

# Calculate the average change
average_change = sum(changes) / len(changes)

# Prepare the analysis results
analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Define Path to Analysis folder:
folder_path = 'c:/Users/azerty/Desktop/Data Boot Camp/Challenges/Challenge 3/Python-Challenge/PyBank/Analysis'

file_path = os.path.join(folder_path, 'financial_analysis.txt')

# Write the analysis to a text file
with open(file_path, 'w') as textfile:
    textfile.write(analysis)


# Print the analysis to the console as well
print(analysis)