class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for song in self.songs:
            if song.name == song_name and not self.published:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
            elif song_name == song.name and self.published:
                return f"Cannot remove songs. Album is published."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        songs = '\n'.join([f"== {song.get_info()}" for song in self.songs])
        return f"Album {self.name}\n{songs}\n"
