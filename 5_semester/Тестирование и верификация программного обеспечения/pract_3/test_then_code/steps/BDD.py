from behave import given, when, then
from music_library import MusicLibrary, Track


@given('в библиотеке есть треки:')
def step_impl(context):
    context.library = MusicLibrary()
    for row in context.table:
        title = row['Название']
        artist = row['Артист']
        genre = row.get('Жанр', None)
        year = int(row['год']) if row.get('год') else None
        duration = int(row['длительность']) if row.get('длительность') else None

        track = Track(title, artist, genre, year, duration)
        context.library.add_track(track)


@when('я ищу треки по названию "{title}"')
def step_impl(context, title):
    context.found_tracks = context.library.find_by_title(title)


@then('я должен найти {count:d} трек')
def step_impl(context, count):
    assert len(context.found_tracks) == count, f"Ожидалось {count} треков, но найдено {len(context.found_tracks)}"


@then('среди найденных должны быть "{title}"')
def step_impl(context, title):
    titles = [track.title for track in context.found_tracks]
    assert title in titles, f"Трек '{title}' не найден среди {titles}"