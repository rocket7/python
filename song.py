class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the 'duration' attribute.
                Will defaulkt to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

        # AVOID CIRCULAR REFERENCES - REMOVE ARTIST IN SONG
        #

# help(Song.__doc__)
# help(Song.__init__.__doc__)
#
# help(Song)
# print(Song.__doc__)

class Album:
    """
    Class to represent a Album, using it's track list

    Attributes:
        album name (str): The name of the album
        year (int): The year of the album
        artist: (Artist): The artist responsible for the album.  If not specified will default to "Various Artists"
        tracks (List(Songs)): A list of songs on the album

    Methods:
          addSong: Used to add a new song to an album track list


    """


    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []


    def add_song(self, song, position=None):
        """
        addSong: Used to add a new song to an album track list

        :param song: Song to add
        :param position: (Optional [int]): The position of song to be added - inserting between songs if neccessary
        :return:
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """
    Basic class to store artist details

    Attributes:
        name (str):  name of artist
        albums (List[Album]):  list of albums by artist

    """
    def __init__(self, name):
        """
        Album Constructor
        :param name:
        """
        self.name = name
        self.albums = []


    def add_album(self, album):
         """
         Add Album Object to List

         :param album: Album object to add to the list
         :return:
         """
         self.albums.append(album)


def load_data():
    new_album = None
    new_artist = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of artist, album, year, song title
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field )

if __name__ == '__main__':
    load_data()
