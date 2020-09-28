import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

"""
This function will determine if there have been any publications of a given disease in a given number of days.
"""

def disease_publications(disease_tuple, num_days):

    disease_name, url = disease_tuple
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features='xml')

    items = soup.findAll('item')

#Extract publishing dates of the clinical trials:
    extracted_publishing_dates = []
    for item in items:
        extracted_publishing_date = {}
        extracted_publishing_date['pubDate'] = item.pubDate.text
        extracted_publishing_dates.append(extracted_publishing_date)


#Reformat the dates so that we can calculate the days between publications:
    datetimes = []
    for extracted_publishing_date in extracted_publishing_dates:
        alz_item_date = extracted_publishing_date['pubDate']
        datetimes.append(datetime.strptime(alz_item_date, '%a, %d %b %Y %H:%M:%S %Z'))

    datetimes = sorted(datetimes)

#Determine the days between publications.
#If there exists a gap in days between publications that is greater than the given number of days, it will return True.
#If not, it will return False.

    for i in range(0, len(datetimes)-1):
        days = datetimes[i+1] - datetimes[i] #Assuming 1 day is a number change in the date, not necessarily 24 hours.
        if days > timedelta(days=num_days):
            return True
    return False

#Sample usage
url = 'https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d=14&lup_d=&sel_rss=new14&cond=Alzheimer+Disease&count=10000'
input = ('Alzheimers', url)
num_days = 2  # 2 days
is_good = disease_publications(input, num_days)
if is_good == True:
    print('There has been a %s day period where there were no publications' % num_days)
else:
    print('There has not been a %s day period where there were no publications' % num_days)