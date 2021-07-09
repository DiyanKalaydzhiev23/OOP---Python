from Spotify.album import Album
from Spotify.song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name and not album.published:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
            elif album_name == album.name and album.published:
                return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        albums = '\n'.join([album.details() for album in self.albums])
        return f"Band {self.name}\n{albums}\n"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
