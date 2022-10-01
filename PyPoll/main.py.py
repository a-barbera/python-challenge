#import modules
import os
import csv
import enum

pypoll_csv = os.path.join("Resources", "election_data.csv")

#initiate global variables

count = 0
total_votes = 0
votes = []
candidates = []

#write to txt file
with open('Analysis/PyPoll_Election_Results.txt', 'w') as f:
    
    #open and read CSV
    with open(pypoll_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        #skip the header row:
        csv_header = next(csv_reader)
    
        for row in csv_reader:
            total_votes = total_votes + 1 
        
            if row[2] not in candidates:
                candidates.append(row[2])
                votes.append(1)
            else:
                index = candidates.index(row[2])
                votes[index] = votes[index] + 1 #incrementing the index of the candidate
    
        print(" ")
        print(" ")
        print("Election Results")
        print('-------------------------')
        print(f"Total Votes: {total_votes}")
        print('-------------------------')
        
        #write to the text file:
        f.write(" ")
        f.write("\n")
        f.write(" ")
        f.write("\n")
        f.write("Election Results")
        f.write("\n")
        f.write('-------------------------')
        f.write("\n")
        f.write(f"Total Votes: {total_votes}")
        f.write("\n")
        f.write('-------------------------')
        f.write("\n")
       
        max_votes = 0     
            
        for index,x in enumerate(candidates):
            #index stands for the candidate
            percentage = round((votes[index] / total_votes) * 100, 3)
            print(f"{candidates[index]}:  {percentage}% ({votes[index]})")
            #write to txt file:
            f.write(f"{candidates[index]}:  {percentage}% ({votes[index]})")
            f.write("\n")
            
            if votes[index] > max_votes:
                max_index = index
                max_votes = votes[index]
        
        print('-------------------------')        
        print(f"Winner: {candidates[max_index]}")
        print('-------------------------')
        
        #write to txt file:
        
        f.write('-------------------------')
        f.write("\n")        
        f.write(f"Winner: {candidates[max_index]}")
        f.write("\n")
        f.write('-------------------------')
    