import random

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