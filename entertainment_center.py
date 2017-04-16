#import libraries
import media
import fresh_tomatoes

#create blank list
movies = []

#create movie object with title, box art and trailer url and add to list
movies.append(media.Movie("Finding Dory","""http://vignette4.wikia.nocookie.net/\
pixar/images/0/0e/FINDING_DORY_-_Key_Art.jpg/revision/latest?cb=20160515234044""",
"""https://www.youtube.com/watch?v=dLIy1K8kJPo"""))
movies.append(media.Movie("Inside Out","""https://images.alphacoders.com/603/603\
342.jpg""","""https://www.youtube.com/watch?v=seMwpP0yeu4"""))
movies.append(media.Movie("Zootopia","""https://lumiere-a.akamaihd.net/v1/images\
/movie_poster_zootopia_866a1bf2.jpeg?region=0%2C0%2C300%2C450""","""https://www.\
youtube.com/watch?v=yCOPJi0Urq4"""))

#create the web page
fresh_tomatoes.open_movies_page(movies)
