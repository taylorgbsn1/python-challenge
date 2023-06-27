# import os module for operating system and file handling function
import os

# import module for csv files 
import csv 

# use os.path.join to form a path to csv file
fileload = os.path.join("election_data.csv")

# file to hold the output of the election analysis
outputfile = os.path.join("electionAnalysis.txt")

# variables 
totalVotes = 0 # initialize number of votes to 0
candidates = [] # list that holds name of the candidates 
candidateVotes = {} # dictionary that holds the votes each candidate receives
winningCount = 0 # variable holds the winning counts
winningCandidate = "" # variable to hold winning candidate 



# read the csv file 
with open(fileload) as electionData:
    #create a csv reader object
    csvreader = csv.reader(electionData)

    # read the header row
    header = next(csvreader)

    # rows will be lists where
       # index 0 is Ballot ID
       # index 1 is County
       # index 2 is Candidate  

    # for each row 
    for row in csvreader:
        # add on to the total votes 
        totalVotes += 1 # same as saying totalVotes = totalVotes + 1

        # check to see if candidate is in the list of candidates 
        if row[2] not in candidates:
              # if the candidate is not in the list, add candidate to the list of candidates
              candidates.append(row[2])

              # add the value to the dictionary as well
              # {"key": value}
              # start the count at 1 for the votes 
              candidateVotes[row[2]] = 1

        else:
              # the candidate is in the list of candidates
              # add a vote to the candidates count
              candidateVotes[row[2]] += 1

# print(candidateVotes)
voteOutput = ""

for candidate in candidateVotes:
    # get the vote count and percentage 
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100 
    voteOutput += f"\t{candidate}: {votePct:.2f}% \n"

    # compare the votes to the winning count
    if votes > winningCount:
          # update the votes to the new winning count 
          winningCount = votes
          # update the winning candidate 
          winningCandidate = candidate

winningCandidateOutput = f"\t\tWinner: {winningCandidate}\n----------------------------- "
    


              

      



# start generating the output
output = (
    f"\n\nElection Results\n"
    f"-----------------------------\n"
    f"\t Total Votes: {totalVotes:,}\n"
    f"-----------------------------\n"
    f"{voteOutput}"
    f"-------------------------------\n"
    f"{winningCandidateOutput}"
)

# print the output to terminal
print(output)

# export the output to the text file 
with open(outputfile, "w") as textfile:
         textfile.write(output)