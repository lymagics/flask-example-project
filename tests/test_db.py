from website import Session
from website.models import Song 


class TestDatabase:
	"""Class includes tests for database."""
	def __init__(self, session):
		self.session = session()

	def test_insert(self):
		"""INSERT test function."""
		try:
		    new_song = Song(id_=0, songname='High', author='DJ', lyrics="some lyrics")
		    self.session.add(new_song)
		    self.session.commit()
		    print('Test insert ended successfully')
		except Exception as ex:
		    print(f'Test insert failed: {ex}')

	def test_update(self):
		"""UPDATE test function."""
		try:
			song_to_update = self.session.query(Song).filter(Song.songname == 'High').first()
			song_to_update.songname = 'UpdateHigh'
			self.session.commit()
			print('Test update ended successfully')
		except Exception as ex:
			print(f'Test update failed: {ex}')

	def test_select(self):
		"""SELECT test function."""
		try:
			song = self.session.query(Song).filter(Song.songname == 'UpdateHigh').first()
			if song.author == 'DJ':
				print('Test select ended successfully')
		except Exception as ex:
			print(f'Test select failed: {ex}')

	def test_delete(self):
		"""DELETE test function."""
		try:
			song_to_delete = self.session.query(Song).filter(Song.songname == 'UpdateHigh').first()
			self.session.delete(song_to_delete)
			self.session.commit()
			print('Test delete ended successfully')
		except Exception as ex:
			print(f'Test delete failed: {ex}')


if __name__ == '__main__':
	test = TestDatabase(Session)
	test.test_insert()
	test.test_update()
	test.test_select()
	test.test_delete()


	
