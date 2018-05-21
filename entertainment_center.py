#!/usr/bin/env python
import media
import fresh_tomatoes
adm = media.Movie("ae dil hai mushkil", "Breakup", "https://bit.ly/2s09AH9",
                  "https://www.youtube.com/embed/Z_PODraXg4E")
mal = media.Movie("1983", "cricket", "https://bit.ly/2KERUbM",
                  "https://www.youtube.com/embed/bROIs4zMgjo")
etd = media.Movie("Enter the Dragon", "Martial Art", "https://bit.ly/2Iz3jsV",
                  "https://www.youtube.com/embed/tB-QGOChuQc")
lor = media.Movie("lord of rings", "adventure", "https://bit.ly/2BmwxHN",
                  "https://www.youtube.com/embed/Pki6jbSbXIY")
aiw = media.Movie("Avengers infinity war", "frictional",
                  "https://bit.ly/2rWEksF",
                  "https://www.youtube.com/embed/6ZfuNTqbHE8")
mtk = media.Movie("Monkey The king 3", "kingdom", "https://bit.ly/2IyEku8",
                  "https://www.youtube.com/embed/jTxAUX_hbJA")

movies = [adm, mal, etd, lor, aiw, mtk]
fresh_tomatoes.open_movies_page(movies)
