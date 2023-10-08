import pandas as pd
import csv


page = pd.read_csv('https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/bible.csv', delimiter='\t')

print(page.iloc[3:5+1, 0].values.tolist())

print(page)