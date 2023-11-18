import requests
import re
def request(url):
    try:
        get_response = requests.get("https://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass
    
    
target_url = "zsecurity.org"
response = request(target_url)
href_links = re.findall('(?:href=")(.*?)"', response.content) 


print(href_links)   
