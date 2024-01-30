# Scraping Practice
The Booklists data is used as a practice when learning scrapy. This practice and tutorial is from Freecodecamp. 

The other spider created is a self-practice demonstration of skills in scrapy. 

## Step 1 - Install & activate your python virtual environment (If you want to do it in venv)
Then to activate it so that any new modules that are installed are installed into this virtual environment:

`source venv/bin/activate`

## Step 2 - Install the required python modules
To install the required modules for this python project to run you need to install the required python modules using the following command:

`pip install -r requirements.txt`


## Step 3 - Add your ScrapeOps API key to the settings.py file (if you don't want to use Scrapyd)
You can signup for an ScrapeOps API key at https://scrapeops.io

Then add your API key to the settings.py file.
`SCRAPEOPS_API_KEY = 'YOUR_API_KEY_HERE'` 

## Step 4 - Run the project/ Follow the course
Once the required python modules are installed you should be able to view/run the Python Scrapy Spider with the following command (from within the project folder):

Cd into the project spiders: `cd bookscraper`

View the project spiders: `scrapy list`

Run the project spider: `scrapy crawl bookspider`

# Helpful Dubugging 
If you have issues running the `pip install -r requirements.txt` command this can be due to some things not being up to date on your computer. 

Running the following may solve some of these issues:

`pip install --upgrade pip`

The following error: `NotADirectoryError: [Errno 20] Not a directory: 'pkg-config'` might be solvable by running:
`export PKG_CONFIG=/path/to/pkg-config`
