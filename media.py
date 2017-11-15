# a class to define the movie contributes
class Movie():
    # take movie title, trailer url and poster url as input, do initialization
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title   # movie title
        self.trailer_youtube_url = trailer_youtube_url   # movie trailer url
        self.poster_image_url = poster_image_url   # movie poster url
