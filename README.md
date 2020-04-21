# 🎵 Spyify 🔍

Logging of Spotify friend activity. Serving as a substitute for [missing Web API functionality](https://github.com/spotify/web-api/issues/83)

## What is this

As of the creation of this project, the [Spotify Web API](https://developer.spotify.com/documentation/web-api/) has no endpoint for "Friend Activity".
Spyify aims to awkwardly plug that gap by intercepting https requests of the [Spotify Desktop Client](https://www.spotify.com/uk/download/other/).

### Who is it for

Anybody that wants to spy on their friends' listening habits. I think there is some fun analysis that could be done on the aggregated data.

### How is it done

This repo contains a script that, when given as a parameter to `mitmproxy`, will log all friend activity on a local Spotify desktop client. 
Friend activity is stored in CSV files, separated by day.

### What about privacy stuff

Friend activity is available to users through the desktop client UI.
[This] comment gives an explanation as to why this functionality is missing - it comes down to 'there is currently no mechanism for users to consent to letting *applicatins* see what you're listening to'.
[This comment](https://github.com/spotify/web-api/issues/83#issuecomment-311495141) raises a counterpoint - *'if you're explicitly consenting to making these details public, it would imply that you're also consenting to allowing others the ability to read and record that information.'*. 
I'm happy enough with this reasoning that I have no problem sharing this project.

## Usage

*Don't try to run Spyify* unless you understand the security implications of trusting a certificate authority.

**Don't try to run Spyify**.

If you'd like to run Spyify, clone the repo and do the following:

1. `pip install mitmproxy`
1. follow steps to [Trust mitmproxy certificate](https://docs.mitmproxy.org/stable/concepts-certificates/)
1. `./run.sh`
1. set system proxy to `localhost:8080`
