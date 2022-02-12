import requests
from bs4 import BeautifulSoup
from API.utils import Random_user_agent


def Eestekhdam(query):
    '''Search and return results from e-estekhdam.com using web scraping'''

    # Input query
    query = f'استخدام-برای-{query}'
    # Prepare url
    url = f'https://www.e-estekhdam.com/search/{query}'
    
    # Make a request
    page = requests.get(url, headers=Random_user_agent()).text
    # Read the page
    soup = BeautifulSoup(page, 'lxml')

    if soup.find('div', 'alert2 alert2-warning font-size-14'):
        return 'Not found'
    
    else:
        # Find all data
        find_job_titles = soup.find_all('a', {'class' : 'title vertical-top display-inline'})
        find_company_names = soup.find_all('div', {'class' : 'company'})
        find_published_dates = soup.find_all('div', {'class' : 'date'})
        find_cities = soup.find_all('div', {'class' : 'provinces'})
        find_contracts = soup.find_all('div', {'class' : 'contract'})

        # Append all data to each list
        job_titles = []
        more_details_urls = []
        company_names = []
        published_dates = []
        cities = []
        contracts = []

        # Append job title
        for title in find_job_titles:
            job_titles.append(title.text)

        # Append job more details url
        for url in find_job_titles:
            more_details_urls.append('https://www.e-estekhdam.com' + url['href'])
        
        # Append company name
        for name in find_company_names:
            company_names.append(name.text)

        # Append published date
        for date in find_published_dates:
            published_dates.append(date.text)

        # Append city
        for city in find_cities:
            cities.append(city.text)

        # Append contract
        for contract in find_contracts:
            contracts.append(contract.text)

        data = []
        
        # Append each job to data list
        for title, url, company, date, city, contract in zip(job_titles, more_details_urls,
            company_names, published_dates, cities, contracts):
            
            data.append(
                {
                    'job_title'  : title.strip(),
                    'company_name' : company.strip(),
                    'city' : city.strip(),
                    'contract' : contract.strip(),
                    'published_date' : date.strip(),
                    'more_details' : url.strip()
                }
            )

        return data



