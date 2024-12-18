// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQCvt4bP8Zj2NB4YMewfHAExqJjN421Ut9KcOgxlVl6kcgaXNdHhOzfqUDLr94qJpdx1rOGjostrPlL2AC4LQEQQU5kQXrsyp3bDORnb2jp_kjqcv0CGIbUdoBiW53J9Vc-b6mFKD2r_-ReBMB2bPf_2J08nEbOZCXM9_7t0xTZIf43MLPMQ4OjH-lRgo7Izm_NhdMYUOOkqcbnNhyZsnj6wL6TtURpgC8I9N3ka2pQ-r8EWLTs2elhkyiwlmBi1frmr3waqe2vM1c5dxZJQZ92IlltsrsxCAB-6';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

async function getTopTracks(){
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
  )).items;
}

const topTracks = getTopTracks();
console.log(
  topTracks?.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);