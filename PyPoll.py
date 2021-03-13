import csv
import os
election_data_path = os.path.join("Course Work","Election_Analysis","Resources","election_results.csv")
election_report_path = os.path.join("Course Work","Election_Analysis","analysis","election_analysis.txt")

total_votes = 0
candidate_dict = {}
candidates_summary = ""

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

#Find winner
max_vote = max(candidate_dict.values())
for i in candidate_dict.items():
    if i[1] == max_vote:
        winner = i[0]
        winning_vote_count = i[1]
        winning_percentage = i[1]/total_votes*100

#Prepare summary
overall_summary = (
        f"\nElection Results\n"
        f"-------------------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"-------------------------------------"
        )
for i in candidate_dict.items():
    if candidates_summary:
        candidates_summary += "\n"
    candidates_summary += (f"{i[0]}: {(i[1]/total_votes*100):.1f}% ({i[1]})")
winning_summary = (
        f"-------------------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_vote_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------"
        )

# Print results
print(overall_summary)
print(candidates_summary)
print(winning_summary)

#Record the Results
with open(election_report_path,"w") as election_report:
    election_report.write(f"{overall_summary}\n{candidates_summary}\n{winning_summary}")