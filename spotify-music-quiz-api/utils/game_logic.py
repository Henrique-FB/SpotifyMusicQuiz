from typing import List

def update_artists(playlists: List[dict]) -> List[dict]:
    #artists =  {'name': 'artist_name', 'id': 'artist_id'}
    artists = []
    for playlist in playlists:
        for item in playlist['tracks']:
            for artist in item['track']['artists']:
                if artist not in artists:
                    artists.append(artist)
    return artists

def define_artist_overlap(room_info: dict) -> List[str]:
    first_user = next(iter(room_info['users'].values()), None)
    artist_intersection = set([artist['id'] for artist in first_user['artists']])
    
    for user in list(room_info['users'].values())[1:]:
        artist_intersection &= set([artist['id'] for artist in user['artists']])
    
    return list(artist_intersection)


