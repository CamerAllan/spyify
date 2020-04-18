# 🎵 Spyify 🔍

Logging of Spotify friend activity. Serving as a substitute for [missing Web API functionality](https://github.com/spotify/web-api/issues/83)

## What is this

As of the creation of this project, the [Spotify Web API](https://developer.spotify.com/documentation/web-api/) has no endpoint for "Friend Activity".
Spyify aims to awkwardly plug that gap by intercepting https requests of the [Spotify Desktop Client](https://www.spotify.com/uk/download/other/).

### Who is it for

Anybody that wants to spy on their friends' listening habits. I think there is some fun analysis that could be done on the aggregated data.

### What about privacy stuff

The friend activity is already available to users through the desktop client UI.
[This] comment summarises the reason for the missing functionality - it comes down to 'there is currently no mechanism for users to consent to letting apps see what you're listening to'.
[This comment](https://github.com/spotify/web-api/issues/83#issuecomment-311495141) raises a counterpoint which aligns with my views, therefore I have no problem making this project public.

## Usage

Hopefully this will be nicely packaged up in the future.
For now, clone the repo and run the following:
1. `pip install mitmproxy`
1. `source env/bin/activate`
1. `mitmdump -s ./src/spyipy.py`
1. `Set OS-level proxy to localhost:8080` (hope to reduce this to just Spotify proxy)
