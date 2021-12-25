import os
from flask import Blueprint, render_template, redirect, request
from . import Session
from .models import Song

views = Blueprint('views', __name__)


@views.route('/')
def index():
	"""Index page route handler.
	
	GET: Landing page: "Index page"
	"""
	session = Session()
	songs = session.query(Song).all()

	songs_to_send = []	
	for i in range(0, len(songs), 3):
		songs_to_send.append(songs[i:i+3])
	return render_template('index.html', preproc_songs=songs_to_send)


def get_last_id():
	"""Return id of the last object in database. If database is empty return 1."""
	session = Session()

	try:
		return session.query(Song).all()[-1].id_ + 1
	except:
		return 1


def get_current_dir():
	"""Return current path direction."""
	return os.path.dirname(os.path.realpath(__file__))


@views.route('/add_song', methods = ['POST', 'GET'])
def add_song():
	"""Add song page route handler.
	
	GET: Landing page: "Add song page".
	POST: Add a new song to the database. Redirect to "Index page".
	"""
	if request.method == 'POST':
		songname = request.form['songname']
		author = request.form['songauthor']
		lyrics = request.form['lyrics']
		song = request.files['song']

		new_song = Song()
		new_song.songname = songname
		new_song.author = author
		new_song.lyrics = lyrics
		song.save(os.path.join(get_current_dir()+ '/static/audio', str(get_last_id()) + '.mp3'))

		try:
			session = Session()
			session.add(new_song)
			session.commit()
			return redirect('/')
		except:
			return "Error with add new song"

	elif request.method == 'GET':
		return render_template('add_song.html')


@views.route('/about')
def about():
	"""About site page route handler.
	
	GET: Landing page: "About page"
	"""
	return render_template('about_us.html')


@views.route('/about_song/<int:song_id>')
def about_song(song_id):
	"""About song page route handler.
	
	GET: Landing page: "About song page"
	"""
	session = Session()

	try:
		song = session.query(Song).filter(Song.id_ == song_id).first()
		if song is None:
			return "Unable to get info about non-existent song."
		return render_template('about_song.html', song=song)
	except:
		return "Failed to load song info"


@views.route('/like/<int:song_id>')
def like_song(song_id):
	"""Like song route handler.
	
	GET: Increment song's like counter in database. Redirect to "Current song page".
	"""
	try:
		session = Session()
		song_to_like = session.query(Song).filter(Song.id_ == song_id).first()
		if song_to_like is None:
			return "Unable to like non-existent song."
		song_to_like.likes += 1
		session.commit()
		return redirect(f'/about_song/{song_id}')
	except:
		return "Failed to like song."


@views.route('/delete/<int:song_id>')
def delete_song(song_id):
	"""Delete song route handler.
	
	GET: Delete song from database. Redirect to "Index page".
	"""
	try:
		session = Session()
		song_to_delete = session.query(Song).filter(Song.id_ == song_id).first()
		if song_to_delete is None:
			return "Unable to delete info about non-existent song."
		session.delete(song_to_delete)
		session.commit()
		os.remove(os.path.join(get_current_dir() + '/static/audio', str(song_id) + '.mp3'))
		return redirect('/')
	except:
		return "Failed to delete song."


@views.route('/update/<int:song_id>', methods=['GET', 'POST'])
def update_song(song_id):
	"""Update song page route handler.
	
	GET: Landing page: "Update song page".
	POST: Update information about song in the database. Redirect to "Index page".
	"""
	if request.method == 'POST':
		songname = request.form['songname']
		author = request.form['songauthor']
		lyrics = request.form['lyrics']

		try:
			session = Session()
			song_to_update = session.query(Song).filter(Song.id_ == song_id).first()
			song_to_update.songname = songname
			song_to_update.author = author
			song_to_update.lyrics = lyrics
			session.commit()
			return redirect('/')
		except:
			return "Failde to update song."
	elif request.method == 'GET':
		session = Session()
		song = session.query(Song).filter(Song.id_ == song_id).first()
		return render_template('update_song.html', song=song)