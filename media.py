#!/usr/bin/env python
print("content-type:text/html \r")
import webbrowser
class Movie():
    VALID_RATINGS = ["EXCELLENT","GOOD","BAD","AVERAGE"]
    def __init__(self,cineMax,cineLine,cinePostImage,cineTube):
        self.title=cineMax
        self.storyline=cineLine
        self.poster_image_url = cinePostImage
        self.trailer_youtube_url = cineTube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
