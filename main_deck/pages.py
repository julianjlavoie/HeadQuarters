'''
Title: HeadQuarters
Author: Julian Lavoie
Date: 2024-06-05
Description: A central location for my life data.
File_Description: The bluprint for MainDeck. Includes the routing info
'''

from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    ''' The home page '''
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    ''' The about me page '''
    return render_template("pages/about.html")

@bp.route("/logs")
def logs():
    ''' The logs page '''
    return render_template("pages/logs.html")
