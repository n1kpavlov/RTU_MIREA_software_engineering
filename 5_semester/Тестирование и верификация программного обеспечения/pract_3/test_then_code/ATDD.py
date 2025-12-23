import unittest
from music_library import MusicLibrary, Track


class TestMusicLibraryAcceptance(unittest.TestCase):
    def setUp(self):
        self.library = MusicLibrary()

        self.tracks = [
            Track("Конь", "Любэ", "Фолк-рок", 1994, 218),
            Track("А зори здесь тихие", "Любэ", "Русская эстрада", 2015, 214),
            Track("Кукла колдуна", "Король и Шут", "Фолк-рок", 1998, 203),
            Track("Кукла", "Иванушки International", "Поп", 1997, 314)
        ]

    def test_acceptance_add_track_to_library(self):
        """Сценарий: Пользователь добавляет трек в библиотеку"""
        # Given - пользователь хочет добавить песню "Конь" группы Любэ
        new_track = Track("Конь", "Любэ", "Фолк-рок", 1994, 218)

        # When - пользователь добавляет трек в библиотеку
        self.library.add_track(new_track)

        # Then - трек успешно добавлен и доступен для поиска
        found_tracks = self.library.find_by_title("Конь")
        self.assertIn(new_track, found_tracks)
        self.assertEqual(len(found_tracks), 1)

    def test_acceptance_find_all_songs_by_artist(self):
        """Сценарий: Пользователь ищет все песни группы Любэ"""
        # Given - в библиотеке есть несколько песен разных артистов
        for track in self.tracks:
            self.library.add_track(track)

        # When - пользователь ищет все треки группы "Любэ"
        lyube_tracks = self.library.find_by_artist("Любэ")

        # Then - система возвращает все песни этого артиста
        self.assertEqual(len(lyube_tracks), 2)
        titles = set(track.title for track in lyube_tracks)
        expected_titles = {"Конь", "А зори здесь тихие"}
        self.assertEqual(titles, expected_titles)

    def test_acceptance_filter_songs_by_genre(self):
        """Сценарий: Пользователь фильтрует песни по жанру Фолк-рок"""
        # Given - библиотека содержит песни разных жанров
        for track in self.tracks:
            self.library.add_track(track)

        # When - пользователь выбирает жанр "Фолк-рок"
        folk_rock_tracks = self.library.find_by_genre("Фолк-рок")

        # Then - система показывает все треки этого жанра
        self.assertEqual(len(folk_rock_tracks), 2)
        artists = set(track.artist for track in folk_rock_tracks)
        self.assertEqual(artists, {"Любэ", "Король и Шут"})

    def test_acceptance_search_songs_with_similar_titles(self):
        """Сценарий: Пользователь ищет песни с похожими названиями"""
        # Given - в библиотеке есть песни с похожими названиями
        for track in self.tracks:
            self.library.add_track(track)

        # When - пользователь ищет по части названия "Кукла"
        doll_tracks = self.library.find_by_title("Кукла")

        # Then - система находит все подходящие треки
        self.assertEqual(len(doll_tracks), 2)
        titles = set(track.title for track in doll_tracks)
        expected_titles = {"Кукла колдуна", "Кукла"}
        self.assertEqual(titles, expected_titles)

    def test_acceptance_correct_track_metadata(self):
        """Сценарий: Администратор исправляет информацию о треке"""
        # Given - в библиотеке есть трек с неполной информацией
        track = Track("Конь", "Любэ", None, None, 218)
        self.library.add_track(track)

        # When - администратор обновляет метаданные трека
        self.library.edit_track_metadata(
            title="Конь",
            genre="Фолк-рок, военная песня",
            year=1994,
            duration=220
        )

        # Then - информация успешно обновляется
        updated_track = self.library.find_by_title("Конь")[0]
        self.assertEqual(updated_track.genre, "Фолк-рок, военная песня")
        self.assertEqual(updated_track.year, 1994)
        self.assertEqual(updated_track.duration, 220)

    def test_acceptance_case_insensitive_search(self):
        """Сценарий: Пользователь ищет песни без учёта регистра"""
        # Given - в библиотеке есть песни с разным регистром в названиях
        for track in self.tracks:
            self.library.add_track(track)

        # When - пользователь ищет "а зори здесь тихие" в нижнем регистре
        found_tracks = self.library.find_by_title("а зори здесь тихие")

        # Then - система находит песнь независимо от регистра
        self.assertEqual(len(found_tracks), 1)
        self.assertEqual(found_tracks[0].title, "А зори здесь тихие")

    def test_acceptance_prevent_duplicate_tracks(self):
        """Сценарий: Система предотвращает добавление дубликатов"""
        # Given - в библиотеке уже есть песня "Конь"
        original_track = Track("Конь", "Любэ", "Фолк-рок", 1994, 218)
        self.library.add_track(original_track)

        # When - пользователь пытается добавить тот же трек повторно
        duplicate_track = Track("Конь", "Любэ", "Фолк-рок", 1994, 218)
        self.library.add_track(duplicate_track)

        # Then - система отклоняет дубликат
        self.assertEqual(len(self.library.tracks), 1)


if __name__ == '__main__':
    unittest.main()