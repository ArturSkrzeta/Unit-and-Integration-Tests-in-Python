# script counts items with status:
# created within the created.csv file
# closed within the closed.csv file
# on hold within the Weekly IT KPI.csv

import pandas as pd

file_list = [
    'closed.csv',
    'created.csv',
    'Weekly IT KPI.csv'
]

status_list = [
    'closed',
    'created',
    'on hold'
]

def read_df(file):
    return pd.read_csv(file)

def count_labels(df, status_name):
    unique_items = df['Labels'].unique()

    if len(unique_items) == 3 and ('lht' in unique_items and 'bo' in unique_items and 'os' in unique_items):

        if status_name != 'on hold':
            print('- - - ' + status_name + ' - - -')
            print(df['Labels'].value_counts())
        elif status_name == 'on hold':
            filt = (df['Status'] == 'On hold')
            print('- - - ' + status_name + ' - - -')
            print(df.loc[filt]['Labels'].value_counts())
        else:
            print("some unexpected items im Labels column for status: " + status_name)


def main():

    for file in file_list:
        df = read_df(file)
        if file == 'created.csv':
            count_labels(df,status_list[0])
        elif file == 'closed.csv':
            count_labels(df,status_list[1])
        elif file == 'Weekly IT KPI.csv':
            count_labels(df,status_list[2])

if __name__ == '__main__':
    main()
