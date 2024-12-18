import requests

# Authorization token that must have been created previously
token = "BQCvt4bP8Zj2NB4YMewfHAExqJjN421Ut9KcOgxlVl6kcgaXNdHhOzfqUDLr94qJpdx1rOGjostrPlL2AC4LQEQQU5kQXrsyp3bDORnb2jp_kjqcv0CGIbUdoBiW53J9Vc-b6mFKD2r_-ReBMB2bPf_2J08nEbOZCXM9_7t0xTZIf43MLPMQ4OjH-lRgo7Izm_NhdMYUOOkqcbnNhyZsnj6wL6TtURpgC8I9N3ka2pQ-r8EWLTs2elhkyiwlmBi1frmr3waqe2vM1c5dxZJQZ92IlltsrsxCAB-6"

def fetch_web_api(endpoint, method="GET", body=None):
    url = f"https://api.spotify.com/{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=body)
    else:
        raise ValueError("Unsupported HTTP method")
    
    response.raise_for_status()  # Raise an error for HTTP issues
    return response.json()

def get_top_tracks():
    # Endpoint reference: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    endpoint = "v1/me/top/tracks?time_range=long_term&limit=50"
    response = fetch_web_api(endpoint)
    return response.get("items", [])

# Fetch and print the top tracks
top_tracks = get_top_tracks()

for track in top_tracks:
    name = track["name"]
    artists = ", ".join(artist["name"] for artist in track["artists"])
    print(f"{name} by {artists}")
