import requests

url = 'https://www.rb.cz/informacni-servis/kurzovni-listek'
response = requests.get(url)

print(response.status_code)





 

