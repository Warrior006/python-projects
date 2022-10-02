# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup as bs

userRequest = input("Enter the name of GitHub user: ")
url = 'https://github.com/' + userRequest

requestURL = requests.get(url)
containerHTML = bs(requestURL.content, 'html.parser')

profileIMG = containerHTML.find('img', {'alt': 'Avatar'})['src']
profileFullName = containerHTML.find('span', {'class': 'p-name vcard-fullname d-block overflow-hidden'}).get_text()
profileUserName = containerHTML.find('span', {'class': 'p-nickname vcard-username d-block'}).get_text()
profileLocation = containerHTML.find('span', {'class': 'p-label'}).get_text()
profileNumRepository = containerHTML.find('span', {'class': 'Counter'}).get_text()

print(f"Github URL profile image: {profileIMG}")
print(f"Fullname: {profileFullName}")
print(f"Github Username: {profileUserName}")
print(f"Location: {profileLocation}")
print(f"Number of repositories: {profileNumRepository}")
