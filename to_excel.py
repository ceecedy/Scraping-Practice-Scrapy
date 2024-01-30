import pandas as pd  

# you should put your own json path here...
json_path = 'your_json_path'

# read the json data via pandas. 
json_data = pd.read_json(json_path)

# convert the json data to excel 
json_data.to_excel('booklists.xlsx', index = False, engine = 'openpyxl')
