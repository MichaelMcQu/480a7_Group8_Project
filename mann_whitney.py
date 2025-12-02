from scipy.stats import mannwhitneyu
import pandas as pd

def mann_whitney_test(csv1, csv2, column):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    values1 = df1[column].values
    values2 = df2[column].values

    stat, p = mannwhitneyu(values1, values2, alternative='two-sided')

    print(f"Mann-Whitney U Test comparing {csv1} vs {csv2} for '{column}':")
    print(f"Statistic = {stat}")
    print(f"P-value   = {p}\n")

    if p < 0.05:
        print("Result: Significant difference between the two samples.\n")
    else:
        print("Result: No significant difference between the two samples.\n")

if __name__ == "__main__":
    mann_whitney_test("data/cloudfoundary_commit_frequency_2018.csv", "data/cloudfoundary_commit_frequency_2021.csv", "CommitCount")

    mann_whitney_test("data/cloudfoundary_merge_time_2018.csv", "data/cloudfoundary_merge_time_2021.csv", "TimeToMergeHours")
