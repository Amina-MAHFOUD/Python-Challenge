import os
import csv
import pandas as pd
from collections import Counter

# Load the dataset
data = pd.read_csv(r'C:\Users\azerty\Desktop\Data Boot Camp\Challenges\Challenge 3\Python-Challenge\PyPoll\Resources\election_data.csv')

# Calculate the total number of votes cast
total_votes = len(data)

# Get a complete list of candidates who received votes
candidates = data['Candidate'].unique()

# Calculate the total number of votes each candidate won
vote_counts = Counter(data['Candidate'])

# Calculate the percentage of votes each candidate won
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in vote_counts.items()}

# Determine the winner of the election based on popular vote
winner = max(vote_counts, key=vote_counts.get)

# Prepare the results in the desired format
results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate, votes in vote_counts.items():
    percentage = vote_percentages[candidate]
    results += f"{candidate}: {percentage:.2f}% ({votes})\n"
results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
with open('election_results.txt', 'w') as file:
    file.write(results)

# Define Path to Analysis folder:
folder_path = 'c:/Users/azerty/Desktop/Data Boot Camp/Challenges/Challenge 3/Python-Challenge/PyPoll/Analysis'

file_path = os.path.join(folder_path, 'election_results.txt')

# Write the analysis to a text file
with open(file_path, 'w') as textfile:
    textfile.write(results)
