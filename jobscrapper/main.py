from so import extract_jobs as so_extract_jobs
from ro import extract_jobs as ro_extract_jobs
from wwr import extract_jobs as wwr_extract_jobs
from exporter import save_to_file
from flask import Flask, render_template, request, redirect, send_file

app = Flask("_YOLO_")

fakeDB = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  jobs = []
  if word:
    word = word.lower()
    fromDb = fakeDB.get(word)
    if fromDb:
      print("dsflsjdfsdaf")
      jobs=fakeDB[word]
    else:
      if so_extract_jobs:
        jobs += so_extract_jobs(word)
      if wwr_extract_jobs:
        jobs += wwr_extract_jobs(word)
      if ro_extract_jobs:
        jobs += ro_extract_jobs(word)
      fakeDB[word] = jobs
  else:
    redirect("/")
  return render_template('jobs.html', 
  resultsNumber = len(jobs),
  searchingBy = word,
  jobs = jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception
    word = word.lower()
    jobs = fakeDB.get(word)
    if not jobs:
      raise Exception
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    print("failed")
    return redirect("/")

app.run(host="0.0.0.0")
