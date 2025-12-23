import unittest
from music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        """Подготовка объектов для тестов"""
        self.library = MusicLibrary()
        self.track_1 = Track(
            title="Конь",
            artist="Любэ",
            genre="Фолк-рок",
            year=1994,
            duration=218
        )
        self.track_2 = Track(
            title="А зори здесь тихие",
            artist="Любэ",
            genre="Русская эстрада",
            year=2015,
            duration=214
        )
        self.track_3 = Track(
            title="Кукла колдуна",
            artist="Король и Шут",
            genre="Фолк-рок",
            year=1998,
            duration=203
        )
        self.track_4 = Track(
            title="Кукла",
            artist="Иванушки International",
            genre="Поп",
            year=1997,
            duration=314
        )

    def test_add_track(self):
        """Тест на добавление трека в библиотеку"""
        self.library.add_track(self.track_1)
        self.assertIn(self.track_1, self.library.tracks)
        self.assertEqual(len(self.library.tracks), 1)

    def test_add_multiple_tracks(self):
        """Тест на добавление нескольких треков"""
        self.library.add_track(self.track_1)
        self.library.add_track(self.track_2)
        self.assertEqual(len(self.library.tracks), 2)
        self.assertIn(self.track_1, self.library.tracks)
        self.assertIn(self.track_2, self.library.tracks)

    def test_add_copy_track(self):
        """Тест на добавление уже существующего трека"""
        self.library.add_track(self.track_1)
        self.library.add_track(self.track_1)
        self.assertEqual(len(self.library.tracks), 1)

    def test_find_track_by_title_exact_match(self):
        """Тест на поиск трека по точному названию"""
        self.library.add_track(self.track_1)
        self.library.add_track(self.track_2)

        found_tracks = self.library.find_by_title("Конь")
        self.assertIn(self.track_1, found_tracks)
        self.assertEqual(len(found_tracks), 1)

    def test_find_track_by_title_partial_match(self):
        """Тест на поиск по части названия"""
        self.library.add_track(self.track_2)
        self.library.add_track(self.track_3)
        self.library.add_track(self.track_4)

        found_tracks = self.library.find_by_title("Кукла")
        self.assertIn(self.track_3, found_tracks)
        self.assertIn(self.track_4, found_tracks)
        self.assertEqual(len(found_tracks), 2)

    def test_find_track_by_title_case_insensitive(self):
        """Тест на поиск без учёта регистра"""
        self.library.add_track(self.track_2)

        found_tracks = self.library.find_by_title("а зори здесь тихие")
        self.assertIn(self.track_2, found_tracks)
        self.assertEqual(len(found_tracks), 1)

    def test_find_track_by_title_not_found(self):
        """Тест на поиск несуществующего трека"""
        self.library.add_track(self.track_1)

        found_tracks = self.library.find_by_title("Несуществующая песня")
        self.assertEqual(len(found_tracks), 0)

    def test_find_by_artist(self):
        """Тест поиска по артисту"""
        self.library.add_track(self.track_1)
        self.library.add_track(self.track_2)
        self.library.add_track(self.track_3)

        found_tracks = self.library.find_by_artist("Любэ")
        self.assertIn(self.track_1, found_tracks)
        self.assertIn(self.track_2, found_tracks)
        self.assertEqual(len(found_tracks), 2)

    def test_find_by_genre(self):
        """Тест поиска по жанру"""
        self.library.add_track(self.track_1)
        self.library.add_track(self.track_3)
        self.library.add_track(self.track_4)

        found_tracks = self.library.find_by_genre("Рок")
        self.assertIn(self.track_1, found_tracks)
        self.assertIn(self.track_3, found_tracks)
        self.assertEqual(len(found_tracks), 2)

    def test_edit_track_metadata_artist(self):
        """Тест на редактирование артиста"""
        self.library.add_track(self.track_2)

        new_artist = "Любэ, Алексей Филатов"
        self.library.edit_track_metadata(self.track_2.title, artist=new_artist)

        updated_track = self.library.find_by_title("А зори здесь тихие")[0]
        self.assertEqual(updated_track.artist, new_artist)

    def test_edit_track_metadata_genre(self):
        """Тест на редактирование жанра"""
        self.library.add_track(self.track_4)

        new_genre = "Поп-музыка"
        self.library.edit_track_metadata(self.track_4.title, genre=new_genre)

        updated_track = self.library.find_by_title("Кукла")[0]
        self.assertEqual(updated_track.genre, new_genre)

    def test_edit_track_metadata_multiple_fields(self):
        """Тест на редактирование нескольких полей одновременно"""
        self.library.add_track(self.track_1)

        self.library.edit_track_metadata(
            self.track_1.title,
            genre="Эстрада, фолк-рок",
            year=1995,
            duration=246
        )
        updated_track = self.library.find_by_title("Конь")[0]
        self.assertEqual(updated_track.genre, "Эстрада, фолк-рок")
        self.assertEqual(updated_track.year, 1995)
        self.assertEqual(updated_track.duration, 246)


if __name__ == '__main__':
    unittest.main()