import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # stire the url of the api call
r = requests.get(url)  # use request to make the call,call get() and pass it the url,store the response object in the variable r
print("Status code:",r.status_code) # response obj r has an attribute status_code which tells us whether the request was successful(200)
# store API response in a variable
response_dict = r.json() # api returns the information in JSON format,so we use json() method to convert the information to a python dictionary
# Process results
print(response_dict.keys()) # print the keys of python dictionary

print("Total repositories:",response_dict['total_count'])

# explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))
# examine the first repository
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for i in sorted(repo_dict.keys()):
    print(i)
print("\nSelected information about first repository:") # here print out the values for a number of keys from the first repository's dictionary
print('Name:',repo_dict['name'])
print('Owner:',repo_dict['owner']['login'])  # owner to access the owner and owner's login name
print('Stars:',repo_dict['stargazers_count'])  # how many stars the project has earned
print('Repository:',repo_dict['html_url']) # url for the project's github repository
print('Created:',repo_dict['created_at'])  # show when it was created
print('Updated:',repo_dict['updated_at']) # show when it was updated
print('Description',repo_dict['description']) # print the repository's description

for i in repo_dicts: # loop through all the dictionaries in repo_dicts
    print('Name:', i['name'])
    print('Owner:', i['owner']['login'])  # owner to access the owner and owner's login name
    print('Stars:', i['stargazers_count'])  # how many stars the project has earned
    print('Repository:', i['html_url'])  # url for the project's github repository
    print('Created:', i['created_at'])  # show when it was created
    print('Updated:', i['updated_at'])  # show when it was updated
    print('Description', i['description'])  # print the repository's description

name,stars = [],[]
for i in repo_dicts:
    names.append(i['name'])
    stars.append(i['stargazers_count'])
