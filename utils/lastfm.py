import pylast
from utils.config import API_KEY, API_SECRET, LAST_FM_USERNAME

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def get_recent_track() -> pylast.Track:
    recent_track = network.get_user(LAST_FM_USERNAME).get_recent_tracks(limit=1, now_playing=True)
    return recent_track[0].track

def get_current_track():
    return network.get_user(LAST_FM_USERNAME).get_now_playing()

def get_lastfm_cover_uri(track: pylast.Track) -> str | None:
    try:
        uri = track.get_cover_image(2)
        if uri == "https://lastfm-img.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png": # пиздец.
            return None
        else:
            return uri
    except:
        return None
    
def get_lastfm_uri(track: pylast.Track) -> str | None:
    try:
        return track.get_url()
    except:
        return None