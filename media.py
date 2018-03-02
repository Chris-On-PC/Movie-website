import webbrowser # import the webbrowser module to be used to open the trailers for the various movies.

class Video(): # The parent video class containing the basic information to the various videos.
    """This class provides a way to store information about a video """
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, video_title, video_story, video_poster, video_trailer): #The init method 
        
        self.title = video_title # provide the video title property to the instance
        self.storyline = video_story # provide the video storyline property to the instance
        self.poster_image_url = video_poster # provide the video image property to the instance
        self.trailer_youtube_url = video_trailer # provide the video trailer property to the instance
        
    def show_trailer(self): # function to play the video trailer
        webbrowser.open(self.trailer_youtube)
        
class Movie(Video):
    """This class is a child class to the video parent class and
        provides a way to add additional information about a movie """
    def __init__(self, video_title, video_story, video_poster, video_trailer, video_duration):
        Video.__init__(self, video_title, video_story, video_poster, video_trailer)
        
        self.movie_duration = video_duration # provide the movie duration property to the instance

    def show_trailer(self): # function to play the movie trailer. Although it is the same as the parent class show_trailer function, it will overwrite it.
        webbrowser.open(self.trailer_youtube)

class Series(Video):
    """This class is a child class to the video parent class and
        provides a way to add additional information about a Series """
    def __init__(self, video_title, video_story, video_poster, video_trailer, video_duration, episode_number):
        Video.__init__(self, video_title, video_story, video_poster, video_trailer)
        
        self.episode_duration = video_duration # provide the episode duartion property to the instance
        self.episode_number = episode_number # provide the episode number property to the instance

    def show_trailer(self):  # function to play the movie trailer. Although it is the same as the parent class show_trailer function, it will overwrite it.
        webbrowser.open(self.trailer_youtube)
    
