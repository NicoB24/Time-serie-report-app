import pandas as pd
from datetime import datetime
import pickle

class Data:
    def __init__(self):
        with open('data/test_data.pkl', 'rb') as handle:
            data = pickle.load(handle)
        self.data = data

    def retrieve_prepared_data(self):
        self.data = self.data.dropna()
        self.data = self.data[self.data.Timestamps != 'Data Sucia']
        self.data['Timestamps'] = pd.to_datetime(self.data['Timestamps'], utc=True)
        return self.data

    def retrieve_splitted_date_data(self):
        splitted_data = self.retrieve_prepared_data().set_index('Timestamps')
        splitted_data['day'] = splitted_data.index.day
        splitted_data['hour'] = splitted_data.index.hour
        return splitted_data

    def retrieve_peak_values_and_dates(self):
        return [['Jan 24, 2021, 11:08', 'Jan 25, 2021, 14:08', 'Jan 25, 2021, 16:49', 
                 'Jan 25, 2021, 17:49', 'Jan 25, 2021, 18:12'], ['214','14','869','32','7']]

    def retrieve_slope_changes_and_dates(self):
        return [['Jan 24, 2021, 11:20', 'Jan 25, 2021, 03:34', 'Jan 25, 2021, 10:05', 
                 'Jan 25, 2021, 19:55', 'Jan 26, 2021, 10:01'], ['Positive', 'Negative', 'Positive', 'Negative', 'Positive']]
