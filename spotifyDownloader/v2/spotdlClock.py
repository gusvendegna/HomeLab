import os
import time
import subprocess

playlists = ["https://open.spotify.com/playlist/1K91E1HtWp0PKjgMtuovHO?si=dfd0c507ca9048d1",
            "https://open.spotify.com/playlist/4iLrgpUfRpBj45tvnEa0lC?si=f66301f588184052",
            "https://open.spotify.com/playlist/1LXHvZJhuMNezUNZI9ub9U?si=bc52087277f64b70",
            "https://open.spotify.com/playlist/7gnhk765qTbXoGkGHTN35u?si=154712f5a28b49ed",
            "https://open.spotify.com/playlist/6chwePfM44HJ9AYY3zlWuy?si=aa0db15e616941fa"]

while True:
        for link in playlists:
                subprocess.run(["spotdl", "download", link, "--output", "/music"])
        time.sleep(4*60*60)
