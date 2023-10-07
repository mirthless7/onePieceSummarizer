import pandas as pd


page = pd.read_csv('https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/bible.csv', delimiter='\t')
print(page['quote', 1])

print(page)