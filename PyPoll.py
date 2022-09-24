#The data we need to retrieve.

#Use modules to join path and open a csv file.
import os
import csv

#Assign a variabel for the file to load, and the path.
csvpath = os.path.join('Resources3','election_results.csv')

#assign a variable to save to the path
textpath= os.path.join('analysis', 'Election_Analysis.txt')

#The total number of votes cast
totalvotes = 0

#Candidate Options
candidate_options=[]

#Declare empty dictionary for candidates and their votes
candidate_votes={}

#Declaring variable for winning candidate and count tracker
winning_candidate = ""
winning_count=0
winning_percentage =0

#Open the elextion results and read the file
with open(csvpath) as election_data:
    file_reader = csv.reader(election_data)

    #next() is used to skip the first line of the csv file aka headers
    headers=next(file_reader)

    #2. A complete list of candidates
    #Print each rwo in the csv file
    for row in file_reader:
        #Add tp the total vote count
        totalvotes+=1

        #print candidate name from each row
        candidate_names=row[2]

        if candidate_names not in candidate_options:
            #Add the candidate name to the list
            candidate_options.append(candidate_names)
            #Begin tracking the candidates votes
            candidate_votes[candidate_names] =0
        #Add to the count of votes for each row, placed outside the if statement
        candidate_votes[candidate_names] +=1
    
    #3. The percentage of votes each candidate won
    #Iterate through cnadidate list
    for candidate_names in candidate_votes:
        #Retrieve vote count of candidate
        votes= candidate_votes[candidate_names]
        #Calculate percentage of votes
        vote_percentage = float(votes) / float(totalvotes) * 100

        #Determine if the votes are greater than the winning count.
        if votes > winning_count and vote_percentage > winning_percentage:
            #if true then set winning variables
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_names

        print(f"{candidate_names}: {vote_percentage:.1f}% ({votes:,} votes)\n ")

    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}\n"
        f"---------------------------------\n")
    print(winning_candidate_summary)


    

#print the candidate list
#print(candidate_votes)

