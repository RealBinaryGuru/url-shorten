from flask import Blueprint, render_template, request, redirect, url_for, flash
from .utils import urlShortener
from flask import Blueprint, render_template, request, redirect, url_for, flash


bp = Blueprint('main', __name__)
url_shortener = urlShortener()
        
@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@bp.route("/<short_url>")
def redirect_to_url(short_url):
    original_url = url_shortener.get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        flash("Invalid URL")
        return redirect(url_for("main.index"))

