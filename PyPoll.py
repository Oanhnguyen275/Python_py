import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        print(". ", end=""),

        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results 
with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save to the text file
    txt_file.write(winning_candidate_summary)
