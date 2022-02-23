import os
import requests
from bs4 import BeautifulSoup

os.system("clear")



def extract_jobs(word):
  headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
  ro_url = f"https://remoteok.io/remote-{word}-jobs"
  result = requests.get(ro_url, headers=headers)
  soup = BeautifulSoup(result.text, 'html.parser')
  jobs = []
  pagination_list = []
  if soup.find("table", {"id":"jobsboard"}):
    pagination_list = soup.find("table", {"id":"jobsboard"}).find_all("tr", {"class":"job"})
  for item in pagination_list[:-1]:
    link = "https://remoteok.com" + item.find("a", {"class":"preventLink"})["href"]
    title = item.find("h2", {"itemprop":"title"}).text.strip().strip('\n')
    company = item.find("h3", {"itemprop":"name"}).text.strip().strip('\n')
    kwargs = item.find_all("div", {"class":"location"})
    other_info = ""
    for info in kwargs:
      info = info.text.strip().strip('\n')
      if other_info == "":
        other_info += info
      else:
        other_info = other_info+" / "+info
    when = item.find("td", {"class":"time"}).text.strip().strip('\n')
    jobs.append({"title":title, "company":company, "when":when, "other_info":other_info, "link":link})
  return jobs
      