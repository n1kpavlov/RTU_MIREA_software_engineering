import unittest
from music_library import MusicLibrary, Track
from SDD_specifications import TRACK_METADATA, SEARCH_RESULTS


class TestMusicLibrarySDD(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой библиотеки на основе таблицы метаданных"""
        self.library = MusicLibrary()

        for track_data in TRACK_METADATA:
            track = Track(
                title=track_data['title'],
                artist=track_data['artist'],
                genre=track_data['genre'],
                year=track_data['year'],
                duration=track_data['duration']
            )
            self.library.add_track(track)

    def test_search_by_title_specifications(self):
        """Поиск по названию на основе таблицы спецификаций"""
        title_search_cases = [case for case in SEARCH_RESULTS if case['search_type'] == 'by_title']

        for search_case in title_search_cases:
            with self.subTest(query=search_case['query']):
                results = self.library.find_by_title(search_case['query'])
                result_titles = [track.title for track in results]

                self.assertEqual(set(result_titles), set(search_case['expected_titles']))

    def test_search_by_artist_specifications(self):
        """Поиск по артисту на основе таблицы спецификаций"""
        artist_search_cases = [case for case in SEARCH_RESULTS if case['search_type'] == 'by_artist']

        for search_case in artist_search_cases:
            with self.subTest(query=search_case['query']):
                results = self.library.find_by_artist(search_case['query'])
                result_titles = [track.title for track in results]

                self.assertEqual(set(result_titles), set(search_case['expected_titles']))

    def test_search_by_genre_specifications(self):
        """Поиск по жанру на основе таблицы спецификаций"""
        genre_search_cases = [case for case in SEARCH_RESULTS if case['search_type'] == 'by_genre']

        for search_case in genre_search_cases:
            with self.subTest(query=search_case['query']):
                results = self.library.find_by_genre(search_case['query'])
                result_titles = [track.title for track in results]

                self.assertEqual(set(result_titles), set(search_case['expected_titles']))


if __name__ == '__main__':
    unittest.main()