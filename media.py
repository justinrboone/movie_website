import webbrowser

class Movies():

    #Create movie obejcts with title, storyline, poster image url and trailer url
    def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url

    # Open the trailer url in the web browser
    def show_movie_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
