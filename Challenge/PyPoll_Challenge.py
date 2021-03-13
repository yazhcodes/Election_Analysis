# Add our dependencies.
import csv
import os

# Add file path variables
election_data_path = os.path.join("Course Work","Election_Analysis","Challenge","election_results.csv")
election_result_path = os.path.join("Course Work","Election_Analysis","Challenge","election_analysis.txt")

# Initialize variables for analysis
total_votes = 0
candidate_dict = {}
candidates_summary = ""
county_dict = {}
county_summary = ""

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
        if i[1] not in county_dict:
            county_dict[i[1]] = 1
        else:
            county_dict[i[1]] += 1

# Find winner
winner_votes = max(candidate_dict.values())
for i in candidate_dict.items():
    if i[1] == winner_votes:
        winner = i[0]
        winner_percent = winner_votes/total_votes * 100

# Find County with largest vote turnout
largest_county_votes = max(county_dict.values())
for i in county_dict.items():
    if i[1] == largest_county_votes:
        largest_county = i[0]
        largest_county_percent = largest_county_votes/total_votes * 100

#Prepare summary
divider = "----------------------------------------"
overall_summary = (
        f"\nELECTION RESULTS\n"
        f"{divider}\n"
        f"Total Votes:  {total_votes:,}\n"
        f"{divider}"
        )
for i in county_dict.items():
    if not county_summary:
        county_summary = "County Votes:\n"
    else:
        county_summary += "\n"
    county_summary += (f"{i[0]}: {(i[1]/total_votes*100):.1f}% ({i[1]:,})")
largest_county_summary = (
        f"{divider}\n"
        f"Largest County Turnout: {largest_county}\n"
        f"{divider}"
        )
for i in candidate_dict.items():
    if candidates_summary:
        candidates_summary += "\n"
    candidates_summary += (f"{i[0]}: {(i[1]/total_votes*100):.1f}% ({i[1]:,})")
winning_summary = (
        f"{divider}\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winner_votes:,}\n"
        f"Winning Percentage: {winner_percent:.1f}%\n"
        f"{divider}"
        )

# Print results
print(f"{overall_summary}\n{county_summary}\n{largest_county_summary}\n{candidates_summary}\n{winning_summary}")

#Record the Results
with open(election_result_path,"w") as election_result:
    election_result.write(f"{overall_summary}\n{county_summary}\n{largest_county_summary}\n{candidates_summary}\n{winning_summary}")