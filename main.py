import flask, render_template

@static_method
def home():
  return render_template("home.html")
