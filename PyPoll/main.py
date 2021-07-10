#Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#In addition, 
# your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

#set path for file
pyPool_csv = './Resources/election_data.csv'

#create variables
total_votes=0
candidates=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0


with open(pyPool_csv, encoding="utf-8") as csvfile: 
    csv_reader = csv.reader(csvfile,delimiter=",") 
    csv_header = next(csv_reader)
    #print(csv_header)

    for row in csv_reader: 

        # Count the Voter ID's and store in variable  
        total_votes +=1

        # Count the times the candidate's name appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1
    
    
#Print the total number of votes cast
print(total_votes)


# print the total number of votes each candidate won
print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)

# print the percentage of votes each candidate won
khan_percent = (khan_votes/total_votes) *100
print(f" Khan: \t \t {khan_percent} % ({khan_votes} votes)")
correy_percent = (correy_votes/total_votes) * 100
print(f" Correy: \t {correy_percent} % ({correy_votes} votes)")
li_percent = (li_votes/total_votes)* 100
print(f" Li: \t \t {li_percent} % ({li_votes} votes)")
otooley_percent = (otooley_votes/total_votes) * 100
print(f" O'Tooley: \t {otooley_percent} % ({otooley_votes} votes)")



#print the winner of the election based on popular vote.
#make dictionary where the candidate is a key and the number of votes is the attribute, find the max number of votes and print the key using .get
candidates=["Khan", "Correy", "Li", "O'Tooley"]
votes=[khan_votes, correy_votes, li_votes, otooley_votes]
dict_candidates=dict(zip(candidates, votes))
print(dict_candidates)
winner=max(dict_candidates, key=dict_candidates.get)
print(f"The Winner is {winner}")





