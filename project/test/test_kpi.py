import pytest
import os
import pandas as pd
from kpi import file_list, read_df, count_labels

def test_files_count():
    files = os.listdir(os.curdir)
    csvs = list(filter(lambda csv: str(csv)[-3:] == 'csv', files))
    assert len(csvs) == 3
    assert csvs[0] == file_list[0]
    assert csvs[1] == file_list[1]
    assert csvs[2] == file_list[2]

def test_read_df():
    assert read_df(file_list[0]).shape[1] == 15
    assert read_df(file_list[1]).shape[1] == 15
    assert read_df(file_list[2]).shape[1] == 5

def test_companies():
    for file in file_list:
        df = pd.read_csv(file_list[0])
        assert len(list(df['Labels'].unique())) == 3
        assert 'lht' in df['Labels'].unique()
        assert 'os' in df['Labels'].unique()
        assert 'bo' in df['Labels'].unique()
