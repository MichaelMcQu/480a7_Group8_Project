import csv
from pydriller import Repository
from datetime import datetime

def find_commit_frequency(repo_url, since, to, output_csv):
    # Dictionary to store commit counts: {(author, date): count}
    commit_counts = {}

    for commit in Repository(repo_url, since=dt1, to=dt2).traverse_commits():
        author = commit.author.name
        date = commit.author_date.strftime('%Y-%m-%d')  # commit date (day granularity)
        key = (author, date)
        commit_counts[key] = commit_counts.get(key, 0) + 1

    # Write results to CSV
    with open(output_csv, 'w', newline='') as file:
        fieldnames = ['Author', 'Date', 'CommitCount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for (author, date), count in commit_counts.items():
            writer.writerow({
                'Author': author,
                'Date': date,
                'CommitCount': count
            })

if __name__ == "__main__":
    # cloudfoundary commit frequency
    dt1 = datetime(2018, 1, 1)
    dt2 = datetime(2019, 1, 1)
    repo_url = 'https://github.com/cloudfoundry/bosh'
    output_csv = 'cloudfoundary_commit_frequency_2018.csv'

    find_commit_frequency(repo_url, dt1, dt2, output_csv)

    dt1 = datetime(2021, 1, 1)
    dt2 = datetime(2022, 1, 1)
    output_csv = 'cloudfoundary_commit_frequency_2021.csv'

    find_commit_frequency(repo_url, dt1, dt2, output_csv)