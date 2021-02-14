from flask import Flask, render_template, request, redirect, send_file
from stack_scrapper import get_jobs
from export import save_file
import pdfkit

app = Flask("han's Scrapper")

# fake db
db = {}

@app.route("/") # only read function
def home():
  return render_template("home.html")

# @app.route("/<username>") # dynamic url
# def contact(username):
#   return f"Hello your name is {username} "

#use request, get word

@app.route("/report")
def report():
  
  word = request.args.get('word')

  if word:
    # lowcase in alphabet
    word = word.lower()
    fromDB = db.get(word)
    if fromDB:
      jobs = fromDB
    else:
      jobs = get_jobs(word)
      db[word] = jobs

  else:
    return redirect("/")
  # use {{searchby}} in template
  print(word)
  return render_template(
    "report.html"
    , searchby = word
    , resultsNumber = len(jobs)
    , jobs = jobs
    ) 


@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
      word = word.lower()
    jobs = db.get(word)

    if not jobs:
      raise Exception()

    save_file(jobs)

    return send_file("jobs.csv")


  except:
    return redirect("/")

@app.route("/exportPDF")
def exportPDF():
  pdfkit.from_url('')

  

app.run(host="0.0.0.0") # 0.0.0.0 is repl's host