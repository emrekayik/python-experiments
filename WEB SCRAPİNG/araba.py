import requests
from bs4 import BeautifulSoup
url = "https://www.sahibinden.com/otomobil/erzincan"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
pages = len(soup.find_all("table",attrs={"id":"searchResultsTable"})[0].find_all("td")) - 2
totalJobs = 0
for pageNumber in range(1,pages + 1):
    pageRequest = requests.get("https://www.sahibinden.com/otomobil/erzincan?pagingOffset=" + str(pageNumber))
    pageSource = BeautifulSoup(pageRequest.content,"html.parser")
    jobs = pageSource.find("tbody",attrs={"class":"searchResultsRowClass"}).find_all("tr")
    # Tüm işleri çektik, döngü ile ilan detaylarını alalım.
    for job in jobs:
        name = job.h2.find("a", attrs={"class":"classifiedTitle"}).text
        location = job.find("td",attrs={"class":"searchResultsTagAttributeValue"}).text
        company = job.find("td",attrs={"class":"searchResultsAttributeValue"}).text
        publish_time = job.find("searchResultsPriceValue").text
        totalJobs += 1
        print(name,company,location,publish_time,sep="\n")
        print("-"*60)

print("Total {} jobs found.".format(totalJobs))
