#!/usr/bin/env python
print("Content-type:text/html \r")
import media
import fresh_tomatoes
adm = media.Movie("ae dil hai mushkil","Breakup","https://spiderimg.amarujala.com/assets/images/2016/09/28/ae-dil-hai-mushkil_1475055893.jpeg","https://www.youtube.com/embed/Z_PODraXg4E")
mal = media.Movie("1983","cricket","https://d1k89quaw9hlgo.cloudfront.net/raagaimg/r_img/250/m/m0002913.jpg","https://www.youtube.com/embed/bROIs4zMgjo")
etd = media.Movie("Enter the Dragon","Martial Arts","https://illustractiongallery.com/15436-large/enter-the-dragon-japanese-style-b.jpg","https://www.youtube.com/embed/tB-QGOChuQc")
lor = media.Movie("lord of rings","adventure","https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg","https://www.youtube.com/embed/Pki6jbSbXIY")
aiw = media.Movie("Avengers infinity war","frictional","https://cdn.flickeringmyth.com/wp-content/uploads/2018/03/avengers-infinity-war-2.jpg","https://www.youtube.com/embed/6ZfuNTqbHE8")
movies=[adm,mal,etd,lor,aiw]
fresh_tomatoes.open_movies_page(movies)
