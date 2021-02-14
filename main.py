from flask import Flask, render_template, request, redirect

app = Flask("han's Scrapper")

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

  else:
    return redirect("/")
  # use {{searchby}} in template
  print(word)
  return render_template("report.html", searchby = word) 



app.run(host="0.0.0.0") # 0.0.0.0 is repl's host