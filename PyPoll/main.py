import os
import csv

#define the current dictionary
current_dir = os.getcwd()
#define the path to the CSV file
csvpath = os.path.join (current_dir,"Resources","election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
candidate_votes = 0
winner = ""
percentage_vote = 0

#open and read the CSV file
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the head row
    header = next(csvreader)

    #process each row in CSV file
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        #if the candidate is in the dictionary,increment the vote count
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        #if not,add it to the dictionary as 1 vote
        else:
            candidates[candidate] = 1
        
  
# determine the winner of the election
max_votes=0
for candidate,votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("Election Results:")
print(f"The total votes are  {total_votes}.")
for candidate,votes in candidates.items():
    percentage_vote = (votes / total_votes) * 100
    print(f"{candidate}: {percentage_vote:.3f}% ({votes} votes)")
print(f"The winner of the election based on popular vote is {winner}.")





        

        
