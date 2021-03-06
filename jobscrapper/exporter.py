import csv

def save_to_file(jobs):
  file = open(f"jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "posted", "info", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return