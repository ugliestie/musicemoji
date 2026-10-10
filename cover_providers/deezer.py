import json
from difflib import SequenceMatcher
from urllib.parse import quote
from urllib.request import urlopen

from pylast import Track


def get_deezer_uri(track: Track) -> str | None:
    try:
        url = f"https://api.deezer.com/search/track?q={quote(str(track))}&limit=3"
        response = urlopen(url)
        data = json.loads(response.read())
        matches = []
        for n in data['data']:
            matches.append(SequenceMatcher(None, track.title, n['title']).ratio())
        return data['data'][matches.index(max(matches))]['album']['cover_medium']
    except:
        return None