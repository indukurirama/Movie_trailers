#!/usr/bin/env python
import webbrowser
import os
import re


# styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang = "en">
<head>
   <meta name = "viewport" varma = " width = device-width, initial-scale=1.0">
   <title>Movie trailers</title>
   <style>
    .modal {
    display: none;
    position: fixed;
    z-index: 2;
    padding-top:35px:
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.4);
    }
    .modal-varma {
    position:relative;
    margin: 5% auto;
    padding: 20px;
    width: 60%;
    min-height:500px;
    }
    .close {
    color: white;
    float: right;
    font-size: 28px;
    font-weight: bold;
    position: absolute;
    background-color: red;
    padding:5px;
    }
    .close:hover,
      .close:focus {
    text-decoration: none;
    cursor: pointer;
     }
      .container{
        display: flex;
        flex-wrap: wrap;
       }
     .box{
          width: 100%;
          min-height: 150px;
        }
      @media screen and (min-width : 450px)  {
      div.a:hover{
             border: 1px;
             background-color: Aquamarine;
             border-radius: 100px;
             }
       div.b:hover{
             border: 1px;
             background-color: green;
             border-radius: 100px;
             }
       div.c:hover{
             border: 1px;
             background-color: tomato;
             border-radius: 100px;
             }
       div.d:hover{
             border: 0px;
             background-color: MediumSeaGreen;
             border-radius: 100px;
             }
       div.e:hover{
             border: 0px;
             background-color: orange;
             background-radius: 30%;
             border-radius: 100px;
             }
        div.f:hover{
             border: 0px;
             background-color: orange;
             background-radius: 30%;
             border-radius: 100px;
             }
       .a{width: 33%;}
       .b{width: 33%;}
       .c{width: 34%;}
       .d{width: 33%;}
       .e{width: 33%;}
       .f{width: 34%;}
       .i{border-radius: 100px;}
      }
      </style>
      <div>
         <div id = "myModal" class = "modal">
            <div class = "modal-varma">
                <span class = "close">&times;</span>
                 <iframe id = "s" width = 60% height = "315"
                  src = "" frameborder = "0"
                  allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
        </div>
</div>
<script>
var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];
   onc = function(c) {
   modal.style.display = "block";
   c='https://www.youtube.com/embed/'+c;
   console.log(c);
   document.getElementById("s").setAttribute("src",c);
  }
    span.onclick = function() {
        document.getElementById("s").src = document.getElementById("s").src;
        modal.style.display = "none";
   }
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>
</head>
'''
main_page_content = '''
<body style = "text-align: center">
   <h1 style = "color: white"><mark style="color: red" >MOVIE TRAILERS</h1>
   <div class = "container">
        <div class = "box a" onclick = "onc('Z_PODraXg4E')"><img vspace = "30"
             src = "https://bit.ly/2s09AH9"style= "width: 60%"height = "300"
              hspace = "30" class = "i">
              <h2 style = "color: white;">AE DILL HI MUSKHILL</h2>
        </div>
        <div class = "box b" onclick = "onc('bROIs4zMgjo')"><img vspace = "30"
              src = "https://bit.ly/2KERUbM" style="width:60%"height="300"
               hspace = "30" class = "i">
               <h2 style = "color:white;">1983 </h2>
        </div>
        <div class = "box c"onclick = "onc('tB-QGOChuQc')"><img vspace = "30"
             src = "https://bit.ly/2Iz3jsV" style = "width:60%" height = "300"
             hspace = "30" class = "i">
             <h2 style = "color:white;">ENTER THE DRAGON</h2>
        </div>
        <div class = "box d"onclick = "onc('Pki6jbSbXIY')"><img vspace = "30"
             src = "https://bit.ly/2BmwxHN" style = "width:60%"height = "300"
             hspace = "30" class = "i">
             <h2 style="color:white;">LORD OF THE RINGS </h2>
             </div>
        <div class = "box e"onclick = "onc('6ZfuNTqbHE8')"><img vspace = "30"
              src = "https://bit.ly/2rWEksF" style = "width:60%"height = "300"
              hspace = "30"class = "i">
              <h2 style = "color:white;">AVENGERS INFINITY WAR</h2>
        </div>
        <div class = "box f"onclick = "onc('jTxAUX_hbJA')"><img vspace = "30"
              src = "https://bit.ly/2IyEku8" style = "width: 60%"height = 300"
              hspace = "30"class = "i">
              <h2 style = "color: white;">The MOnkey king 3</h2>
        </div>
</body>
</html>
'''
cineTiles = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
            data-trailer-youtube-id="{trailer_youtube_id}" data-toogle="modal"
            data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):

    varma = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        varma += cineTiles.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return varma


def open_movies_page(movies):
    # Create or overwrite the output file

    output_file = open('trailer3.htm', 'w')
    # Replace create_movie_tiles_content with produced content.
    rendered_content = main_page_content.format(
                       movie_tile=create_movie_tiles_content(movies))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    # Open the output file in new browser.
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
