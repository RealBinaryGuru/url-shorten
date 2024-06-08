import string
import random
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .utils import urlShortener
from flask import Blueprint, render_template, request, redirect, url_for, flash


bp = Blueprint('main', __name__)
url_shortener = urlShortener()
        
@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("original_url")
        if original_url:
            short_url = url_shortener.convert_long_to_short_url(original_url)
            print("\n\n")
            print("Here is the short URL: " + short_url) 
            print("\n\n")
            flash(f'SHORT URL CREATED: {short_url}')
            return render_template("output.html", short_url=short_url, original_url=original_url)
        
        else:
            flash("Please enter a valid URL.")
            return redirect(url_for('main.index'))
        
    return render_template("index.html")

@bp.route("/<short_url>")
def redirect_to_url(short_url):
    original_url = url_shortener.get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        flash("Invalid URL")
        return redirect(url_for("main.index"))

