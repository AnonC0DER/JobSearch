import random
import base64


def Random_user_agent():
    '''Get random user agent'''
    
    file = open('API/user_agents/user_agents.txt', 'r')
    data = file.read()

    user_agents = data.split('\n') 

    User_agents_list = []
    for user in user_agents:
        try:
            User_agents_list.append(user)
        except:
            pass
        
    return {'User-Agent' : random.choice(User_agents_list)}


def URL_to_bs64(url):
    '''Get url and return the bs64 url bytes'''
    
    url = url.strip().encode('ascii')
    url = base64.b64encode(url)
    url = url.decode('ascii')

    return url


def bs64_to_URL(bs64):
    '''Get bs64 bytes and return the url'''
    
    try:
        base64_bytes = bs64.encode('ascii')  
        url_bytes = base64.b64decode(base64_bytes)
        url = url_bytes.decode('ascii')

        return url
    
    # If the given variable is not bs64 bytes, return it
    except:
        return bs64