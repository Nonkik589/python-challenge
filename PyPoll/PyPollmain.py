import os
import csv

#Opening the CSV File
path = os.path.abspath(os.path.dirname(__file__))
csvpath = os.path.join(path, "../Data/election_data.csv")

#Initialize Variables
row_total = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0



  

#Reading the file and Grabbing Important Info
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)

    

    for row in csvreader:
      #Count every row as a vote
      row_total += 1

      vote = row [2]

      if vote == "Charles Casper Stockham":
        charles_votes += 1
      
      elif (vote == "Diana DeGette"):
        diana_votes += 1
      
      else:
        raymon_votes += 1
  


winnerdictionary = {charles_votes: "Charles Casper Stockham",
             diana_votes: "Diana DeGette",
               raymon_votes: "Raymon Anthony Doane"}

#mathlist = [charles_votes, diana_votes, raymon_votes]

charlesper = round((charles_votes / row_total) * 100)
dianaper = round((diana_votes / row_total) * 100)
raymonper = round((raymon_votes / row_total) * 100)
winner = max(winnerdictionary)

print(f"The Total Votes are: {row_total}")
print(f"Charles received: {charlesper}% {charles_votes} of the votes")
print(f"Diana received: {dianaper}% {diana_votes} of the votes")
print(f"Raymon received: {raymonper}% {raymon_votes} of the votes")

if winner==charles_votes:
  print("Winner: Charles Casper Stockham")

elif winner==diana_votes:
  print("Winner: Diana DeGette")

else:
  print("Winner: Raymon Anthony Doane")

      



output_path = os.path.join(path, "../Analysis/PyPollAnalysis.csv")

with open (output_path, 'w') as csv_out_file:
    
    csvwriter = csv.writer(csv_out_file, delimiter=' ')
   
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------"])
    csvwriter.writerow([f"Charles received: {charlesper}% {charles_votes} of the votes"])
    csvwriter.writerow([f"Diana received: {dianaper}% {diana_votes} of the votes"])
    csvwriter.writerow([f"Raymon received: {raymonper}% {raymon_votes} of the votes"])
    csvwriter.writerow(["-----------------------"])
    
    if winner==charles_votes:
      csvwriter.writerow([f"Winner: Charles Casper Stockham"])
    elif winner==diana_votes:
      csvwriter.writerow([f"Winner: Diana DeGette"])
    else:
      csvwriter.writerow([f"Winner: Raymon Anthony Doane"])