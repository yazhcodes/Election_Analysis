# Election_Analysis

## Overview of Election Audit

   A Colorado Board of Elections employee has sought out help in auditing the results of a recent local congressional election.

## Election-Audit Results

* A total of **369,711** votes were cast in this congressional election.
* The election was held in three counties  - Jefferson, Denver & Arapahoe. And here's a breakdown of the voters turnout in each of these counties.

    | County     | Total Votes  | Percentage of Votes  |
    | ---------- | -----------: | -------------------: |
    | Jefferson  | 38,855       | 10.5%                |
    | Denver     | 306,055      | 82.8%                |
    | Arapahoe   | 24,801       | 6.7%                 |
    
* **Denver** had the largest votes turnout, accounting to 83% of the total votes! 
* Three candidates, Charles Casper Stockham, Diana DeGette & Raymon Anthony Doane, ran in the election. The votes they received from all counties are:

    | Candidate                | Total Votes  | Percentage of Votes  |
    | ------------------------ | -----------: | -------------------: |
    | Charles Casper Stockham  | 85,213       | 23.0%                |
    | **Diana DeGette **       | 272,892      | 73.8%                |
    | Raymon Anthony Doane     | 11,606       | 3.1%                 |

* The clear winner of the election was **Diana DeGette** who led by a whopping 74%, receiving a total of 272,892 votes from all three counties.

## Election-Audit Summary 

   My Python code reads the voting data (369,711 records to be exact) from a .csv file and instantly provides the election results. Although it took me almost 5 hours to build the script from scratch, the good news is that this script can be reused for all upcoming elections that capture voting data in a similar format (i.e., Ballot ID, County, Candidate).  The script requires only two minor modifications where it points to the location of the data file and to that of the results file.

`
election_data_path = os.path.join("Course Work","Election_Analysis","Resources","election_results.csv")
election_result_path = os.path.join("Course Work","Election_Analysis","Challenge","election_analysis.txt")
`
