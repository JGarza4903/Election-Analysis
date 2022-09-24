#The data we need to retrieve.

#Use modules to join path and open a csv file.
from distutils import text_file
import os
import csv

#Assign a variabel for the file to load, and the path.
csvpath = os.path.join('Resources3','election_results.csv')

#assign a variable to save to the path
file_to_save= os.path.join('analysis', 'Election_Analysis.txt')

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

    #save the results to our text file
    with open(file_to_save,"w") as txt_file:
        election_results=(
            f"\nElection Results\n"
            f"------------------------\n"
            #total votes formatted with the thousandths separator
            f"Total Votes: {totalvotes:,}\n"
            f"-------------------------")
        print(election_results, end="")
        #save the final vote count to the text file
        txt_file.write(election_results)
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

            #print(f"{candidate_names}: {vote_percentage:.1f}% ({votes:,} votes)\n ")

        winning_candidate_summary = (
            f"---------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.2f}\n"
            f"---------------------------------\n")
        #print(winning_candidate_summary)



            
            



