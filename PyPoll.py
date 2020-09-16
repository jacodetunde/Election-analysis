# Add our dependencies
import csv
import os
# Assign a variable to laod a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file
# Set total votes counter to Zero
total_votes = 0
# Candidate options and candidate votes 
candidate_options =[]
# Declare empty dictionary
candidate_votes ={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row 
    headers = next(file_reader)
    
# print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Print candidate from each row
        candidate_name  = row[2]
        
        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:

         # Add  the candidate name to the candidate option   
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
        candidate_votes[candidate_name]  += 1 
# Determine the percentage of votes for each candidate by looping through the counts 
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)* 100   
# Print the candidate list
    # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count =vote and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidates's name 
            winning_candidate = candidate_name
# To do: print out the winning candidate,vote count and percentage to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  
    winning_candidate_summary = (
        f"----------------------\n"
        f" Winner: {winning_candidate}\n"
        f" Winning Vote Count: { winning_count:,}\n"
        f" Winning Percentage: { winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
          
    