import requests
from bs4 import BeautifulSoup
from API.db import Add_new_job, SearchIn_JobSearch_db
from API.utils import Random_user_agent, URL_to_bs64, bs64_to_URL


def JobSearch(query):
    '''Search in JobSearch database and return results'''
    
    # Query and return results
    results = SearchIn_JobSearch_db(query)
    
    if len(results) == 0:
        return 'Not found'

    else:
        data = []
        
        # Append results to data list
        for result in results:
            data.append(
                {
                    'job_title' : result[0],
                    'more_details' : bs64_to_URL(result[1]),
                    'company_name' : result[2],
                    'published_date' : result[3],
                    'location' : result[4],
                    'contract' : result[5].split('\n') if result[5] else None
                }
            )
        
        return data


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
    
    # If not found
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
        for title, url, company, date, city, contract, _ in zip(job_titles, more_details_urls,
            company_names, published_dates, cities, contracts, range(0, 7)):
            
            data.append(
                {
                    'job_title'  : title.strip(),
                    'company_name' : company.strip(),
                    'city' : city.strip(),
                    'contract' : contract.strip().split('\n'),
                    'published_date' : date.strip(),
                    'more_details' : url.strip()
                }
            )

            # Add each job to JobSearch database
            try:
                Add_new_job(title=title.strip(), url=url.strip(), comp_name=company.strip(),
                            date=date.strip(), city=city.strip(), contract=contract.strip())

            except Exception as e:
                print(e)

        return data


def Yarijob(query):
    '''Search and return results from yarijob.ir using web scraping'''

    # Prepare url
    url = f'https://yarijob.ir/jobs?searchInput={query}'
    # Make a request
    page = requests.get(url, headers=Random_user_agent()).text

    # Read the page
    soup = BeautifulSoup(page, 'lxml')

    # If not found
    if soup.find('span', 'noResultMessage'):
        return 'Not found'
    
    else:
        # Find all data
        find_job_titles = soup.find_all('h3', {'class' : 'listItemTitle'})
        find_company_names = soup.find_all('span', {'class' : 'initialDir'})
        find_published_dates = soup.find_all('span', {'class' : 'jobListPassedDays'})
        find_cities = soup.find_all('li', class_='jobListMetaItem')
        find_contracts = soup.find_all('li', {'class' : 'jobListMetaItem last'})

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
            more_details_urls.append('https://yarijob.ir' + url.a['href'])
        
        # Append company name
        for name in find_company_names:
            company_names.append(name.text)

        # Append published date
        for date in find_published_dates:
            published_dates.append(date.text)

        # Append city
        for city in find_cities:
            if 'icon-mapmarker-alt' in city.i['class']:
                cities.append(city.text)

        # Append contract
        for contract in find_contracts:
            if 'icon-handshake' in city.i['class']:
                contracts.append(contract.text)

        data = []

        # Append each job to data list
        for title, url, company, date, city, contract, _ in zip(job_titles, more_details_urls,
            company_names, published_dates, cities, contracts, range(0, 7)):
            
            data.append(
                {
                    'job_title'  : title.replace('\n', '').strip(),
                    'company_name' : company.replace('\n', '').strip(),
                    'city' : city.replace('\n', '').strip().split('،')[1].replace(' ', ''),
                    'contract' : contract.replace('\n', '').strip().replace(' ', '').split('،'),
                    'published_date' : date.replace('\n', '').strip(),
                    'more_details' : url.replace('\n', '').strip()
                }
            )

            # Add each job to JobSearch database
            try:
                Add_new_job(title=title.replace('\n', '').strip(), url=url.replace('\n', '').strip(),
                             comp_name=company.replace('\n', '').strip(), date=date.replace('\n', '').strip(), 
                             city=city.replace('\n', '').strip().split('،')[1].replace(' ', ''))

            except Exception as e:
                print(e)

        return data


def Karboom(query):
    '''Search and return results from karboom.io using web scraping'''

    # Prepare url
    url = f'https://karboom.io/jobs?q={query}'
    # Make a request
    page = requests.get(url, headers=Random_user_agent()).text

    # Read the page
    soup = BeautifulSoup(page, 'lxml')

    # If not found
    if soup.find('div', {'class' : 'col-md-8 col-md-offset-2 kb-shadow m-t-35 p-t-30 p-b-30 text-center'}):
        return 'Not found'

    else:
        # Find all data
        find_job_titles = soup.find_all('h3', {'class' : 'sm-title-size ellipsis-text width-100 m-0'})
        find_company_names = soup.find_all('span', {'class' : 'company-name ellipsis-text m-0'})
        find_published_dates = soup.find_all('p', {'class' : 'date sm-text-size kb-text-gray-light m-0'})
        find_cities = soup.find_all('span', class_='pull-right')

        job_titles = []
        more_details_urls = []
        company_names = []
        published_dates = []
        cities = []

        # Append job title
        for title in find_job_titles:
            job_titles.append(title.a.text)

        # Append job more details url
        for url in find_job_titles:
            more_details_urls.append(url.a['href'])

        # Append company name
        for name in find_company_names:
            company_names.append(name.text)

        # Append published date
        for date in find_published_dates:
            published_dates.append(date.text)

        # Append city
        for city in find_cities:
            cities.append(city.text)

        data = []

        # Append each job to data list
        for title, url, company, date, city, _ in zip(job_titles, more_details_urls,
            company_names, published_dates, cities, range(0, 7)):
            
            data.append(
                {
                    'job_title'  : title.strip(),
                    'company_name' : company.strip(),
                    'city' : city.strip(),
                    'published_date' : date.strip(),
                    'more_details' : url.strip()
                }
            )

            # Add each job to JobSearch database
            try:
                Add_new_job(title=title.strip(), url=URL_to_bs64(url), comp_name=company.strip(),
                            date=date.strip(), city=city.strip())
        
            except Exception as e:
                print(e)

        return data


def JobInja(query):
    '''Search and return results from jobinja.ir using web scraping'''

    # Prepare url
    url = f'https://jobinja.ir/jobs?filters%5Bkeywords%5D%5B%5D={query}'
    # Make a request
    page = requests.get(url, headers=Random_user_agent()).text

    # Read the page
    soup = BeautifulSoup(page, 'lxml')

    # If not found
    if soup.find('div', {'class' : 'c-jobSearch__noResult'}):
        return 'Not found'

    else:
        # Find all data
        find_job_titles = soup.find_all('a', {'class' : 'c-jobListView__titleLink'})
        find_published_dates = soup.find_all('span', class_='c-jobListView__passedDays')
        find_compNames_cities_contract = soup.find_all('li', {'class' : 'c-jobListView__metaItem'})

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
            more_details_urls.append(url['href'])

        # Append company name
        for name in find_compNames_cities_contract:
            if 'c-icon--construction' == name.i['class'][3]:
                company_names.append(name.text)

        # Append published date
        for date in find_published_dates:
            published_dates.append(date.text)

        # Append city
        for city in find_compNames_cities_contract:
            if 'c-icon--place' == city.i['class'][3]:
                cities.append(city.text)
        
        # Append contract
        for contract in find_compNames_cities_contract:
            if 'c-icon--resume' == contract.i['class'][3]:
                contracts.append(contract.span.span.text)

        data = []

        # Append each job to data list
        for title, url, company, date, city, contract, _ in zip(job_titles, more_details_urls,
            company_names, published_dates, cities, contracts, range(0, 7)):
            
            data.append(
                {
                    'job_title'  : title.strip(),
                    'company_name' : company.strip(),
                    'city' : city.strip(),
                    'contract' : contract.strip().replace('\n', '').replace('             ', ''),
                    'published_date' : date.strip(),
                    'more_details' : url.strip()
                }
            )

            # Add each job to JobSearch database
            try:
                Add_new_job(title=title.strip(), url=URL_to_bs64(url), comp_name=company.strip(),
                            date=date.strip(), city=city.strip(), 
                            contract=contract.strip().replace('\n', '').replace('             ', ''))
        
            except Exception as e:
                print(e)

        return data


def Linkedin(query):
    '''Search and return results from Linkedin.com using web scraping'''

    # Prepare url
    url = f'https://www.linkedin.com/jobs/search?keywords={query}'
    # Make a request
    page = requests.get(url, headers=Random_user_agent()).text

    # Read the page
    soup = BeautifulSoup(page, 'lxml')

    # If not found
    if soup.find('p', {'class' : 'no-results__subheading'}):
        return 'Not found'

    else:
        # Find all data
        find_job_titles = soup.find_all('a', {'class' : 'base-card__full-link'})
        find_company_names = soup.find_all('a', {'data-tracking-control-name' : 'public_jobs_jserp-result_job-search-card-subtitle'})
        find_published_dates = soup.find_all('time', {'class' : 'job-search-card__listdate--new'})
        find_locations = soup.find_all('span', class_='job-search-card__location')

        job_titles = []
        more_details_urls = []
        company_names = []
        published_dates = []
        locations = []

        # Append job title
        for title in find_job_titles:
            job_titles.append(title.text)

        # Append job more details url
        for url in find_job_titles:
            more_details_urls.append(url['href'])
        
        # Append company name
        for name in find_company_names:
            company_names.append(name.text)

        # Append published date
        for date in find_published_dates:
            published_dates.append(date.text)

        # Append city
        for location in find_locations:
            locations.append(location.text)

        data = []

        # Append each job to data list
        for title, url, company, date, location, _ in zip(job_titles, more_details_urls,
            company_names, published_dates, locations, range(0, 7)):
            
            data.append(
                {
                    'job_title'  : title.strip(),
                    'company_name' : company.strip(),
                    'location' : location.strip(),
                    'published_date' : date.strip(),
                    'more_details' : url.strip()
                }
            )

            # Add each job to JobSearch database
            try:
                Add_new_job(title=title.strip(), url=URL_to_bs64(url), comp_name=company.strip(),
                            date=date.strip(), city=location.strip())
        
            except Exception as e:
                print(e)

        return data