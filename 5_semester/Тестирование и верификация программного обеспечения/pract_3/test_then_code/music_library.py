class Track:
    def __init__(self, title, artist, genre=None, year=None, duration=None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.duration = duration


class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        """Добавление трека в библиотеку с проверкой на дубликаты"""
        for existing_track in self.tracks:
            if (existing_track.title.lower() == track.title.lower() and
                existing_track.artist.lower() == track.artist.lower() and
                existing_track.genre == track.genre and
                existing_track.year == track.year and
                existing_track.duration == track.duration):
                return
        self.tracks.append(track)

    def find_by_title(self, title):
        """Поиск треков по названию"""
        title_lower = title.lower()
        return [track for track in self.tracks if title_lower in track.title.lower()]

    def find_by_artist(self, artist):
        """Поиск треков по артисту"""
        artist_lower = artist.lower()
        return [track for track in self.tracks if artist_lower in track.artist.lower()]

    def find_by_genre(self, genre):
        """Поиск треков по жанру"""
        genre_lower = genre.lower()
        return [track for track in self.tracks if track.genre and genre_lower in track.genre.lower()]

    def edit_track_metadata(self, title, **kwargs):
        """Редактирование метаданных трека."""
        tracks_to_edit = self.find_by_title(title)

        for track in tracks_to_edit:
            for key, value in kwargs.items():
                if hasattr(track, key) and value is not None:
                    setattr(track, key, value)