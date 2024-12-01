from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('pages/index.html')

@main.route('/add-song', methods=['POST'])
def add_song():
	pass