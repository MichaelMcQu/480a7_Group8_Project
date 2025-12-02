import pandas as pd
import matplotlib.pyplot as plt


def boxplot_commit_frequency(csv1, csv2=None, label1='Repo 1', label2='Repo 2'):
    def process_csv(csv):
        df = pd.read_csv(csv)
        df['Date'] = pd.to_datetime(df['Date'])
        df['YearMonth'] = df['Date'].dt.to_period(
            'M').astype(str)  # this is representing year/month in this format YYYY-MM"2018-03"
        return df[['YearMonth', 'CommitCount']]

    df1 = process_csv(csv1)
    ym_groups_1 = df1.groupby('YearMonth')['CommitCount'].apply(
        lambda x: x.dropna().values)

    labels = list(ym_groups_1.index)
    data = list(ym_groups_1.values)

    if csv2:
        df2 = process_csv(csv2)
        ym_groups_2 = df2.groupby('YearMonth')['CommitCount'].apply(
            lambda x: x.dropna().values)

        labels_2 = list(ym_groups_2.index)
        data_2 = list(ym_groups_2.values)

        # Ensure both repos align into a combined timeline
        all_labels = sorted(set(labels + labels_2))
        combined_data_1 = []
        combined_data_2 = []

        for label in all_labels:
            combined_data_1.append(
                df1[df1['YearMonth'] == label]['CommitCount'].dropna().values)
            combined_data_2.append(
                df2[df2['YearMonth'] == label]['CommitCount'].dropna().values)

        plt.figure(figsize=(18, 7))

        positions_1 = range(1, len(all_labels) + 1)
        positions_2 = [p + 0.35 for p in positions_1]

        plt.boxplot(
            combined_data_1,
            positions=positions_1,
            widths=0.3,
            showfliers=False
        )

        plt.boxplot(
            combined_data_2,
            positions=positions_2,
            widths=0.3,
            showfliers=False
        )

        plt.xticks(
            [p + 0.17 for p in positions_1],
            all_labels,
            rotation=45,
            ha='right'
        )

        plt.legend([label1, label2])

    plt.ylabel("Commits per day")
    plt.title("Commit Frequency Distribution by Year–Month")
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    boxplot_commit_frequency(
        'data/cloudfoundary_commit_frequency_2018.csv',
        'data/cloudfoundary_commit_frequency_2021.csv',
        label1='cloudfoundary 2018–2019',
        label2='cloudfoundary 2021–2022'
    )
