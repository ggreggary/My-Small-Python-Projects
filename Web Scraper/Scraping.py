import requests
import BeautifulSoup

req = requests.get("https://www.yahoo.com/now/shibaswap-"
                   "explained-everything-know-shiba-200057559"
                   ".html")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

#The code above simply prints out the source code of a webpage.
