# Store the file path associated with the file
import os
import csv 
#budget_data = os.path.join('..','Resources','budget_data.csv')
election_data = os.path.join('C:/Users/17639/Desktop/Python-challenge/PyPoll/Resources/election_data.csv')

#Create Lists to store data
total_votes = 0

candidate = []
candidate_votes = {}
winning_candidate =  ""
winning_counter = 0

#Open the csv file
with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ',')
    #Skip the header
    next(csvreader,None)
    for row in csvreader:
        total_votes += 1

        candidate_name  = row[2]
        if candidate_name not in candidate: 
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

print(election_data)
output = os.path.join('C:/Users/17639/Documents/ARCC/UVM Bootcamp/Courses support/Activity 3/Python-challenge/PyPoll/Resources/election.txt')

with open(output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n"
    )
    print(election_data)

    txt_file.write(election_results)

    
    for candi in candidate_votes:
        vote =candidate_votes.get(candi)
        percentage_votes = float(vote) / float(total_votes) * 100
        
    
        if (vote > winning_counter):
            winning_counter = vote
            winning_candidate = candi

        vote_output = f"{candi}: {percentage_votes:.3f}% ({vote})\n"
        print(vote_output)

        txt_file.write(vote_output)


    summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n"

    )

    print(summary)
    txt_file.write(summary)