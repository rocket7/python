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
    Class to represent artist details

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


def find_object(field, object_list):
    """
    Check object list to see if an object with 'name' attribute equals 'field' exist and return if true

    :param field:
    :param object_list:
    :return:
    """
    for item in object_list:
        if item.name == field:
            return item
    return None



def load_data():
    new_album = None
    new_artist = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of artist, album, year, song title
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field ))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We have just read details for new artist
                # Retrieve artist object if there is one
                # otherwise create a new artist object and add to artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field,new_album)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # we have just read a new album for current artist
                # retrieve the album object if there is one
                # otherwise create a new album object
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # # After reading the last line of a text file, we will have and artist and album
        # # process them now
        # if new_artist is not None:
        #     if new_album is not None:
        #         new_artist.add_album(new_album)
        #     artist_list.append(new_artist)

    return artist_list


def checkfile_album_output(artist_list):

    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)




if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists ".format(len(artists)))

    checkfile_album_output(artists)
