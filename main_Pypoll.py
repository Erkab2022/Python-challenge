# Store the file path associated with the file
import os
import csv 
#budget_data = os.path.join('..','Resources','budget_data.csv')
election_data = os.path.join('..','Resources','election_data.csv')
# C:\Users\17639\Documents\ARCC\UVM Bootcamp\Courses support\Activity 3\Python challenge\Starter_Code\PyPoll\Resources\election_data.csv

#Create Lists to store data
Ballot_ID =[]
County = []
Candidate = []

#Open the csv file
with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ',')
    #Skip the header
    next(csvreader,None)
    for row in csvreader:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

#Zip lists together
election_data = list(zip(Ballot_ID,County,Candidate))
#print(election_data)

print("Election Result")
print("----------------------")
print(f'{"Total Votes: " + str(len(election_data))}')
candidate_list=[]
for candidate in election_data:
    if election_data.count(candidate)> 1:
        if candidate not in candidate_list:
            candidate_list.append(candidate)
print(candidate_list)
    