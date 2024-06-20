'''
Title: HeadQuarters
Author: Julian Lavoie
Date: 2024-06-05
Description: A central location for my life data.
File_Description: The entry point of the Web Platform
'''

from flask import Flask

from main_deck import pages

def create_app():
    ''' create apps '''
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    return app
