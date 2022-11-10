#Script for PyPoll
# Import the necessary dependencies for os.path.join()
import os
import csv


#read in a .csv file
csv_file = os.path.join("Resources", "election_data.csv")

#create lists

total = 0
candidate_list = []
candidate_name = []
vote_count = 0
percent_vote = []
candidate_vote = {}



# open csv as Reader
with open(csv_file) as csv_poll:
    csv_reader=csv.reader(csv_poll, delimiter=",")
    csv_header=next(csv_reader)
    print(f"Header:{csv_header}")

    #The total number of votes cast
    for row in csv_reader:
        vote_count +=1
        total +=int(row[0])
    #candidate list from candidates in file (appending-an-id-to-a-list-if-not-already-present-in-a-string)
        candidate_name = row [2]
        #if statement required adding name to list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
            


    #A complete list of candidates who received votes

    #The percentage of votes each candidate won

    #The total number of votes each candidate won

    #The winner of the election based on popular vote

#Print statements
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {vote_count}")
print(f"----------------------------")