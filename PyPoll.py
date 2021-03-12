# Data to be retrieved
import csv
import os
election_data_path = os.path.join("Course Work","Election_Analysis","Resources","election_results.csv")
election_report_path = os.path.join("Course Work","Election_Analysis","analysis","election_analysis.txt")

total_votes = 0
candidate_dict = {}

# Retrieve data from file
with open(election_data_path,"r") as election_data:
    election_data_reader = csv.reader(election_data)
    header = next(election_data_reader)
    for i in election_data_reader:
        total_votes += 1
        if i[2] not in candidate_dict:
            candidate_dict[i[2]] = 1
        else:
             candidate_dict[i[2]] += 1

# Convert candidate list into string
num = len(candidate_dict)
for i in range(num):
    if i == 0:
        candidates = list(candidate_dict)[i]
    elif i != num-1:
        candidates = candidates + ", " + list(candidate_dict)[i]
    else:
        candidates = candidates + " & " + list(candidate_dict)[i]

#Find winner
max_vote = max(candidate_dict.values())
for i in candidate_dict.items():
    if i[1] == max_vote:
        winner = i[0]
        winning_vote_count = i[1]
        winning_percentage = i[1]/total_votes*100

# Print results
for i in candidate_dict.items():
    print(f"{i[0]}: {(i[1]/total_votes*100):.1f}% ({i[1]})\n")
print("------------------------")
print(f"Winner: {winner}")
print(f"Winning Vote Count: {winning_vote_count}")
print(f"Winning Percentage: {winning_percentage:.1f}%")
print("------------------------")

#Record the Results
# with open(election_report_path,"w") as election_report:
#     election_report.write("Counties in the Election!\n")
#     election_report.write("-------------------------\n")
#     election_report.write("Arapahoe\nDenver\nJefferson")