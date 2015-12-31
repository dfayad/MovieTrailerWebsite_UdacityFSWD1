import media
import fresh_tomatoes

goodfellas = media.Movie(
	"Goodfellas",
	"Burh, ray liotta becomes the coolest gangster nshit",
	"https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
	"https://www.youtube.com/watch?v=qo5jJpHtI1Y")

nebraksa = media.Movie(
	"Nebraska", 
	"Old dude wins some contest, and travels to claim prize",
	"https://upload.wikimedia.org/wikipedia/en/7/76/Nebraska_Poster.jpg",
	"https://www.youtube.com/watch?v=aA98dqgJBgQ")

in_bruges = media.Movie(
	"In Bruges", 
	"Two hitmen go to Bruges to complete a mission.",
	"https://upload.wikimedia.org/wikipedia/en/6/63/In_Bruges_Poster.jpg",
	"https://www.youtube.com/watch?v=p-gG2qo_l_A")

dog_day_afternoon = media.Movie(
	"Dog day afternoon", 
	"A bank robbery",
	"http://brockelpress.files.wordpress.com/2014/09/1-dog-day-afternoon-001.jpg?w=620", # noqa
	"https://www.youtube.com/watch?v=CF1rtd8_pxA")

nightcrawler = media.Movie(
	"Nightcrawler", 
	"Creppy dude films accidents",
	"http://images.cinefacts.de/Nightcrawler-Charakter-Poster-DE.jpg",
	"https://www.youtube.com/watch?v=UPawRAHG-0g")

birdman = media.Movie(
	"Birdman", 
	"An old actor goes crazy",
	"http://cinemadeviant.com/wp-content/uploads/2015/01/birdman-movie-poster-1.jpg", # noqa
	"https://www.youtube.com/watch?v=uJfLoE6hanc")

before_sunrise = media.Movie(
	"Before Sunrise", 
	"The most beautiful film about love in the history of film",
	"http://images.moviepostershop.com/before-sunrise-movie-poster-1995-1020190611.jpg", #noqa
	"https://www.youtube.com/watch?v=9v6X-Dytlko")

movies = [goodfellas, nebraksa, in_bruges, dog_day_afternoon, 
	  nightcrawler, birdman, before_sunrise]

fresh_tomatoes.open_movies_page(movies)
