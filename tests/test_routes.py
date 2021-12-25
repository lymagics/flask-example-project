import unittest 
import requests
from website import create_app, Session
from website.views import get_last_id
from website.models import Song


class TestApplication(unittest.TestCase):
	"""Class includes tests for application routes."""
	API_URL = "http://127.0.0.1:5000"
	
	app = create_app().test_client()
	session = Session()
	last_id = get_last_id()

	INDEX_URL = f"{API_URL}/"
	ABOUT_URL = f"{API_URL}/about"
	ADD_SONG = f"{API_URL}/add_song"
	SONG_INFO = f"{API_URL}/about_song/{last_id}"
	LIKE_SONG = f"{API_URL}/like/{last_id}"
	UPDATE_SONG = f"{API_URL}/update/{last_id}"
	DELETE_SONG = f"{API_URL}/delete/{last_id}"

	def test_1_add_song_post(self):
		"""Test for add song page post method."""
		query = {
				'songname': 'test_song',
				'songauthor': 'test_author',
				'lyrics': 'test_lyrics',
		}

		song = open('tests/test_audio.mp3', 'rb')

		query['song'] = song

		r = TestApplication.app.post(TestApplication.ADD_SONG, data=query)
		song.close()
		self.assertEqual(r.status_code, 302)

	def test_2_index_get(self):
		"""Test for index page get method."""
		r = TestApplication.app.get(TestApplication.INDEX_URL)
		self.assertEqual(r.status_code, 200)

	def test_3_about_get(self):
		"""Test for about page get method."""
		r = TestApplication.app.get(TestApplication.ABOUT_URL)
		self.assertEqual(r.status_code, 200)

	def test_4_add_song_get(self):
		"""Test for add song page get method."""
		r = TestApplication.app.get(TestApplication.ADD_SONG)
		self.assertEqual(r.status_code, 200)

	def test_5_about_song_get(self):
		"""Test for about song get method."""
		r = TestApplication.app.get(TestApplication.SONG_INFO)
		self.assertEqual(r.status_code, 200)

	def test_6_like_song_get(self):
		"""Test for like song page get method."""
		r = TestApplication.app.get(TestApplication.LIKE_SONG)
		self.assertEqual(r.status_code, 302)

	def test_7_update_song_get(self):
		"""Test for update song get method."""
		r = TestApplication.app.get(TestApplication.UPDATE_SONG)
		self.assertEqual(r.status_code, 200)

	def test_8_update_song_post(self):
		"""Test for update song post method."""
		data = {
			'songname': 'new_name',
			'songauthor': 'new_author',
			'lyrics': 'new_lyrics'
		}

		r = TestApplication.app.post(TestApplication.UPDATE_SONG, data=data)
		self.assertEqual(r.status_code, 302)

	def test_9_delete_get(self):
		"""Test for delete song get method."""
		r = TestApplication.app.get(TestApplication.DELETE_SONG)
		self.assertEqual(r.status_code, 302)
