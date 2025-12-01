import pandas as pd
from scipy.stats import shapiro

def shaprio_test_commit_frequency(csv):
    df = pd.read_csv(csv)

    values = df["CommitCount"].values # seeing if commit frequency is normally distributed

    stat, p = shapiro(values) # testing to see if this is normally distributed or not

    print(f'Shapiro-Wilk Test for {csv}:') # this test will tell us if we should run a t-test or a mann-whitney test
    print(f"Statistic = {stat}")
    print(f"P-value   = {p}")

    if p > 0.05:
        print("Fail to reject null hypothesis, data is normally distributed. You should use a t-test\n")
    else:
        print("Reject null hypothesis, data is not normally distributed. You should use a Mann-Whitney test\n")

def shaprio_test_merge_time(csv):
    df = pd.read_csv(csv)

    values = df["TimeToMergeHours"].values
    stat, p = shapiro(values)

    print(f'Shapiro-Wilk Test for {csv}:') 
    print(f"Statistic = {stat}")
    print(f"P-value   = {p}")

    if p > 0.05:
        print("Fail to reject null hypothesis, data is normally distributed. You should use a t-test\n")
    else:
        print("Reject null hypothesis, data is not normally distributed. You should use a Mann-Whitney test\n")


if __name__ == "__main__":
    shaprio_test_commit_frequency("data/cloudfoundary_commit_frequency_2018.csv")
    shaprio_test_commit_frequency("data/cloudfoundary_commit_frequency_2021.csv")
    
    shaprio_test_merge_time("data/cloudfoundary_merge_time_2018.csv")
    shaprio_test_merge_time("data/cloudfoundary_merge_time_2021.csv")
