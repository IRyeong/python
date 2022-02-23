import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

def extract_jobs(word):
  wwr_url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  result = requests.get(wwr_url)
  soup = BeautifulSoup(result.text, 'html.parser')
  jobs = []
  total_list = soup.find_all("section", {"class":"jobs"})
  for list in total_list:
    pagination_list = list.find_all("li", {"class":"feature"})
    for item in pagination_list[:-1]:
      link = "https://weworkremotely.com" + item.find_all("a")[1]["href"]
      title = item.find("span", {"class":"title"}).text
      company = item.find_all("span", {"class":"company"})[0].text
      if item.find("span", {"class":"region"}):
        location = item.find("span", {"class":"region"}).text
      else:
        continue
      other_info = ""
      other_info += location
      other_info = other_info + " / " + (item.find_all("span", {"class":"company"})[1].text)
      temp = item.find("span", {"classs":"date"})
      if temp:
        when = temp.text
      else:
        when = "featured"
      jobs.append({"title":title, "company":company, "when":when, "other_info":other_info, "link":link})
  return jobs
      