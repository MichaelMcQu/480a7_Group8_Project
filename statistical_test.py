import pandas as pd
from scipy.stats import shapiro

df = pd.read_csv("data/cloudfoundary_commit_frequency_2018.csv")

values = df["CommitCount"].values # seeing if commit frequency is normally distributed

stat, p = shapiro(values) # testing to see if this is normally distributed or not

print("Shapiro-Wilk Test:") # this test will tell us if we should run a t-test or a mann-whitney test
print(f"Statistic = {stat}")
print(f"P-value   = {p}")

if p > 0.05:
    print("Fail to reject null hypothesis data is normally distributed.")
else:
    print("Reject null hypothesis data is not normally distributed.")
