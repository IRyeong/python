import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

def extract_max_page(word):
  so_url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  result = requests.get(so_url)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", {"class":"s-pagination"})
  pagination_list = pagination.find_all("a")
  max_page = len(pagination_list)
  return max_page

def extract_jobs(word):
  max_page = extract_max_page(word)
  jobs = []
  for page in range(max_page):
    so_url = f"https://stackoverflow.com/jobs?r=true&q={word}&pg={page}"
    result = requests.get(so_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination_list = soup.find("div", {"class":"listResults"}).find_all("div", {"class":"-job"})
    for item in pagination_list[:-1]:
      title = item.find("a", {"class":"s-link"}).text
      link = "https://stackoverflow.com" + item.find("a", {"class":"s-link"})["href"]
      company, location = item.find("h3").text.split("•")
      company = company.strip()
      location = location.strip()
      when, *kwargs = item.find("ul", {"class":"mt4"}).find_all("li")
      when = when.text
      other_info = ""
      other_info += location
      for info in kwargs:
        info = info.text
        other_info = other_info+" / "+info
      jobs.append({"title":title, "company":company, "when":when, "other_info":other_info, "link":link})
  return jobs
      
