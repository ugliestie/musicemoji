import pylast
from utils.config import API_KEY, API_SECRET, LAST_FM_USERNAME

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def get_recent_track():
    recent_track = network.get_user(LAST_FM_USERNAME).get_recent_tracks(limit=1, now_playing=True)
    return recent_track[0].track

def get_lastfm_uri(track: pylast.Track):
    try:
        return track.get_cover_image(0)
    except:
        return None