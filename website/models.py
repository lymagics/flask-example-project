from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text

from . import Base


class Song(Base):
    """A database table to represent a song.

    id_ : int Song identificator in database.
    songname : string Name of a song.
    author : string Name of a song's author.
    lyrics : string Song's lyrics.
    likes : int Number of song's likes.
    """
    __tablename__ = 'songs'
    id_ = Column(Integer(), primary_key=True)
    songname = Column(String(20), nullable=False)
    author = Column(String(20), nullable=False)
    lyrics = Column(Text(), nullable=False)
    likes = Column(Integer(), default=0)

    def __repr__(self):
        return f'<Songname {self.songname} Song author {self.author}>'