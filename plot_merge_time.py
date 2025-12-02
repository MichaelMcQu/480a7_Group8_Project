import pandas as pd
import matplotlib.pyplot as plt


def boxplot_merge_time_by_yearmonth(csv1, csv2, label1='Repo 1', label2='Repo 2'):
    def process_csv(csv):
        df = pd.read_csv(csv)

        df['MergeDate'] = pd.to_datetime(df['MergeDate'], errors='coerce')
        df['TimeToMergeHours'] = pd.to_numeric(
            df['TimeToMergeHours'], errors='coerce')

        df['YearMonth'] = df['MergeDate'].dt.to_period('M').astype(str)

        df['Month'] = df['MergeDate'].dt.month
        df = df[~((df['Month'] == 1) & (df['MergeDate'].dt.day == 1))]

        return df[['YearMonth', 'TimeToMergeHours']]

    # Process both repos
    df1 = process_csv(csv1)
    df2 = process_csv(csv2)

    # Group by YearMonth
    ym_groups_1 = df1.groupby('YearMonth')['TimeToMergeHours'].apply(
        lambda x: x.dropna().values)
    ym_groups_2 = df2.groupby('YearMonth')['TimeToMergeHours'].apply(
        lambda x: x.dropna().values)

    labels_1 = list(ym_groups_1.index)
    labels_2 = list(ym_groups_2.index)

    # Combine timeline
    all_labels = sorted(set(labels_1 + labels_2))

    combined_data_1 = []
    combined_data_2 = []

    for label in all_labels:
        combined_data_1.append(
            df1[df1['YearMonth'] == label]['TimeToMergeHours'].dropna().values)
        combined_data_2.append(
            df2[df2['YearMonth'] == label]['TimeToMergeHours'].dropna().values)

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

    plt.ylabel("Time to Merge (hours)")
    plt.title("Merge Time Distribution by Year–Month")
    plt.grid(axis='y', linestyle='--', alpha=0.4)

    plt.legend([label1, label2])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    boxplot_merge_time_by_yearmonth(
        'data/cloudfoundary_merge_time_2018.csv',
        'data/cloudfoundary_merge_time_2021.csv',
        label1='cloudfoundary 2018–2019',
        label2='cloudfoundary 2021–2022'
    )
