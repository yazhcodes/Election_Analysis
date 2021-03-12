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

# Print results
print("**********************")
print(f"A total number of {total_votes} have been cast.")
print(f"List of candidates : {candidates}")
print("\nTotal number of votes for each candidate : ")
for i in candidate_dict.items():
    print(f"\t{i[0]} has received {i[1]} votes.")
print(f"\nAnd the winner is {winner}..!!")
print("**********************")

#Record the Results
# with open(election_report_path,"w") as election_report:
#     election_report.write("Counties in the Election!\n")
#     election_report.write("-------------------------\n")
#     election_report.write("Arapahoe\nDenver\nJefferson")