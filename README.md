# Movie Website

This code can be used to demonstrate the use of classes within python. 
It does so by creating instances of your favourite movies using the same instance variables and classes. The different instances are then used to generate a movie website of your movie instances.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need python 2.7 to run this code.


### Installing

Python can be installed from the python default website. 


## Initializing a new movie instance

To run the code, provide the information to your favourite movie to a new instance.


toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        81)#movie instance made for Toy Story.

 Instance_name = media.Movie("Movie name", 
 							"Movie discription", 
 							"Poster image url", 
 							"movie youtube trailer url", 
 							movie duration)

The instances are created by using the classes from the media.py file. The Video class is used as parent class to the Movie class and thus provides the Movie class with basic attributes such as the video name, video description, video image url and the video youtube trailer url. The Movie class allows for the addition of an addition property: movie duration.  
 
## Running the tests

Once you have added your favorite movie instances to the entertainment_center.py file. You can exectute the progrom by running the entertainment_center.py module through the python IDLE or executing entertainment_center.py through the command prompt. The various movie instances will be provided as an array to the fresh_tomatoes.py file where the html code for your movie website will be built. The fresh_tomatoes.py dynamically generates addition html code for every movie instance provided. 

# Running from Python IDLE

Open executing entertainment_center.py in the Python Shell. To do this click open in the top left corner of the shell windown and navigate to the executing entertainment_center.py file. Once the file has been opened in a seperate window, it can be executed by clicking on the "Run" button and then selecting "Run Module". This will execute the file and build your movies website containing your favorite movies. 

# Running from command prompt. 

To execute the program using your command prompt, navigate to the entertainment_center.py file and enter the file name "executing entertainment_center.py" as input. This will execute your code and  build your movies website containing your favorite movies. 