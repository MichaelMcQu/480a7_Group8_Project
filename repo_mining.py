import csv
from pydriller import Repository
from datetime import datetime

def find_time_to_merge(repo_url, since, to, output_csv):
    with open(output_csv, 'w', newline='') as file:
        fieldnames = ['MergeHash', 'MergeDate', 'Author', 'TimeToMergeHours', 'FilesMerged']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for commit in Repository(repo_url, since=since, to=to).traverse_commits():
            if len(commit.parents) > 1:
                merge_date = commit.author_date
                merged_parent_hash = commit.parents[1]

                branch_start_date = None 
                for c in Repository(repo_url).traverse_commits(): # looks for beginning of the branch to help calculate times
                    if c.hash == merged_parent_hash:
                        branch_start_date = c.author_date
                        break

                files_merged = set() 
                reached_tip = False
                for c in Repository(repo_url).traverse_commits(): # looks through the branch to find all files changed
                    if c.hash == merged_parent_hash:
                        reached_tip = True
                    if reached_tip:
                        for f in c.modified_files:
                            if f.new_path:
                                files_merged.add(f.new_path)
                            elif f.old_path:
                                files_merged.add(f.old_path)
                        if len(c.parents) == 0: # edge case
                            break
                        if c.hash == commit.parents[1]:
                            merged_parent_hash = c.parents[0] if c.parents else None

                time_to_merge = (
                    (merge_date - branch_start_date).total_seconds() / 3600.0
                    if branch_start_date else None
                )

                writer.writerow({
                    'MergeHash': commit.hash,
                    'MergeDate': merge_date.strftime('%Y-%m-%d %H:%M'),
                    'Author': commit.author.name,
                    'TimeToMergeHours': round(time_to_merge, 2) if time_to_merge else '',
                    'FilesMerged': ','.join(files_merged)
                })

