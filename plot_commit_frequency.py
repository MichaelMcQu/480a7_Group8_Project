import pandas as pd
import matplotlib.pyplot as plt

def plot_commit_frequency_by_month(csv1, csv2=None, label1='Repo 1', label2='Repo 2'):
    def process_csv(csv):
        df = pd.read_csv(csv)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        monthly_counts = df.groupby('Month')['CommitCount'].sum() # count commits monthly
        return monthly_counts 

    monthly1 = process_csv(csv1)

    plt.figure(figsize=(10, 6))
    plt.plot(monthly1.index, monthly1.values, label=label1, color='steelblue', linewidth=2)

    if csv2:
        monthly2 = process_csv(csv2)
        plt.plot(monthly2.index, monthly2.values, label=label2, color='darkorange', linewidth=2)

    # Labels and title
    plt.title('Commit Frequency by Month', fontsize=14)
    plt.xlabel('Month')
    plt.ylabel('Total Commits')
    plt.xticks(range(1, 13),
               ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # cloudfoundary commit frequency
    plot_commit_frequency_by_month(
    'data/cloudfoundary_commit_frequency_2018.csv',
    'data/cloudfoundary_commit_frequency_2021.csv',
    label1='cloudfoundary 2018–2019',
    label2='cloudfoundary 2021–2022'
    )