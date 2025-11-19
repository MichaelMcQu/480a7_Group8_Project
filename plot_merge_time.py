import pandas as pd
import matplotlib.pyplot as plt

def plot_merge_time_by_month(csv1, csv2, label1='Repo 1', label2='Repo 2'):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    df1['MergeDate'] = pd.to_datetime(df1['MergeDate'])
    df2['MergeDate'] = pd.to_datetime(df2['MergeDate'])
    df1['TimeToMergeHours'] = pd.to_numeric(df1['TimeToMergeHours'], errors='coerce')
    df2['TimeToMergeHours'] = pd.to_numeric(df2['TimeToMergeHours'], errors='coerce')

    df1['Month'] = df1['MergeDate'].dt.month
    df2['Month'] = df2['MergeDate'].dt.month

    # using this so we dont get jan 1 of the next year
    df1 = df1[~((df1['Month'] == 1) & (df1['MergeDate'].dt.day == 1))]
    df2 = df2[~((df2['Month'] == 1) & (df2['MergeDate'].dt.day == 1))]

    avg1 = df1.groupby('Month')['TimeToMergeHours'].mean()
    avg2 = df2.groupby('Month')['TimeToMergeHours'].mean()

    plt.figure(figsize=(10, 6))
    plt.plot(avg1.index, avg1.values, label=label1, color='steelblue', linewidth=2)
    plt.plot(avg2.index, avg2.values, label=label2, color='darkorange', linewidth=2)

    plt.title('Average Time to Merge by Month', fontsize=14)
    plt.xlabel('Month')
    plt.ylabel('Average Time to Merge (hours)')
    plt.xticks(range(1, 13),
               ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # cloudfoundary
    plot_merge_time_by_month(
    'Data/cloudfoundary_merge_time_2018.csv',
    'Data/cloudfoundary_merge_time_2021.csv',
    label1='cloudfoundary 2018–2019',
    label2='cloudfoundary 2021–2022'
    )

    # electron
    plot_merge_time_by_month(
    'Data/electron_merge_time_2018.csv',
    'Data/electron_merge_time_2021.csv',
    label1='electron 2018–2019',
    label2='electron 2021–2022'
    )

    plot_merge_time_by_month(
    'Data/architect_merge_time_2018.csv',
    'Data/architect_merge_time_2021.csv',
    label1='Architect 2018–2019',
    label2='Architect 2021–2022'
    )