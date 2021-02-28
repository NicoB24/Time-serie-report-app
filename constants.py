peak_values_and_dates = [['Jan 24, 2021, 11:08', 'Jan 25, 2021, 14:08', 'Jan 25, 2021, 16:49', 
                          'Jan 25, 2021, 17:49', 'Jan 25, 2021, 18:12'], ['214','14','869','32','7']]

slope_changes_and_dates = [['Jan 24, 2021, 11:20', 'Jan 25, 2021, 03:34', 'Jan 25, 2021, 10:05', 
                            'Jan 25, 2021, 19:55', 'Jan 26, 2021, 10:01'], ['Positive', 'Negative', 'Positive', 'Negative', 'Positive']]

insights = (
    'From the exploratory data analysis, i saw that the data is from a time series, ' + 
    'and the timestamps columns was string data type. Also in this column, there was a NaN ' +
    'and a bad string. This may be due to a ' +
    'lack of validation in the data entry, or a typo. ' + 
    'When i graphed the data, i saw some peak and changes in the slopes. ' + 
    'Because i dont have any backround of this data, i dont know if this peaks ' +
    'are possibles or if they are outliers, ' +
    'because this values significantly differ from the patterns and trends of the other values ' + 
    'in the time series. ' +
    'From the boxplot graphics, i saw that the Jan 25 has the biggest range ' + 
    'of values and the biggest median. Between the 14 and 21 hours, the interquartile range is the biggest. ' + 
    'The bar plot graphics provides similar information information (values per day and hour).'
)