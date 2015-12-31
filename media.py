import webbrowser


class Movie():
	"""This class provides a way to store movie related information
	
	Attributes:
	title: The title of the movie
	storyline: A very brief summary of the storyline
	poster_image_url: A link to a poster image of the film
	trailer_youtube_url: A link to a youtube video of the trailer of the film
	"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline,
	             poster_image, trailer_youtube):

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
