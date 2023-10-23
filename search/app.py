from flask import Flask, app, redirect, render_template
import requests

app = Flask(__name__)

@app.route("/index.html", methods=["GET", "POST"])
def lucky():
    """Get http response from Google I'm feeling lucky"""
    if requests.method == "POST":
        
        # Make a url
        url = "https://google.com/search"
        
        # Get data
        query = requests.form("q")
        luckyQuerry = requests.form("btnI")
        
        if query:
            url = url + "?q=" + {query}
        if luckyQuerry:
            url = url + "&btnI=I'm Feeling Lucky"
            
        return redirect(f"/{url}")
    return render_template("/index.html")