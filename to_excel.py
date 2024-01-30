import pandas as pd  

json_path = '/Users/macintoshcider/Documents/Programming/Python/Scraping-Practice-Scrapy/bookscraper/bookscraper/booklists.json'

# read the json data via pandas. 
json_data = pd.read_json(json_path)

# convert the json data to excel 
json_data.to_excel('booklists.xlsx', index = False, engine = 'openpyxl')