import re 
url = input("URL: ")
username = re.sub(r"^(https?)?://(www\.)?twitter\.com/","",url)
print(username)
