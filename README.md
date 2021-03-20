# 🎵 Spyify 🔍

Logging of Spotify friend activity. Serving as a substitute for [missing Web API functionality](https://github.com/spotify/web-api/issues/83)

## Update 20/03/21

Since I made this, the app has changed and there is now a dedicated internal API call that fetches friend activity. This is used in this project: https://github.com/valeriangalliat/spotify-buddylist

This renders most of my project obsolete, and I would recommend using or implementing something like the above if you want to track Spotify friend activity.

## What is this

As of the creation of this project, the [Spotify Web API](https://developer.spotify.com/documentation/web-api/) has no endpoint for "Friend Activity".
Spyify aims to awkwardly plug that gap by intercepting https requests of the [Spotify Desktop Client](https://www.spotify.com/uk/download/other/).

### Who is it for

Anybody that wants to spy on their friends' listening habits. I think there is some fun analysis that could be done on the aggregated data.

### How is it done

This repo contains a script that, when provided as a parameter to `mitmproxy`, will log all friend activity on a local Spotify desktop client. 
Friend activity is stored in CSV files, one file per day.

### What about privacy stuff

[This thread](https://github.com/spotify/web-api/issues/83#issuecomment-311495141) documents the reasoning for not having this friend activity in the Spotify API.
The reasoning boils down to 'Spotify currently has no mechanism for users to consent to letting *applications* see what you're listening to'.
Personally I feel that if you consent to making this information public, you implicitly consent to that data being recorded, so for that reason I don't have a problem sharing this repo.

## Usage

*Please don't try to run Spyify unless you understand the security implications of trusting a certificate authority.*

If you'd like to run Spyify, clone the repo and do the following:

1. `pip install mitmproxy`
1. follow steps to [Trust mitmproxy certificate](https://docs.mitmproxy.org/stable/concepts-certificates/)
1. `./run.sh`
1. set system proxy to `localhost:8080`

## Problems

- The desktop application seems to stop updating friend activity after a few hours of inactivity, you will need to employ some way of keeping the app active if you want to use this for extended periods of time
