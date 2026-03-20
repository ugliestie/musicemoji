from urllib.request import urlopen
from urllib.parse import quote
import json
import pylast
from difflib import SequenceMatcher

def get_itunes_uri(track: pylast.Track):
    try:
        url = f"https://itunes.apple.com/search?term={quote(str(track))}&media=music&entity=musicTrack&limit=3"
        response = urlopen(url)
        data = json.loads(response.read())
        matches = []
        for n in data['results']:
            matches.append(SequenceMatcher(None, track.title, n['trackName']).ratio())
        return data['results'][matches.index(max(matches))]['artworkUrl100']
    except:
        return None