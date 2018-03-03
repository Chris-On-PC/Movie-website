import media
# import the self written media library
import fresh_tomatoes
# import the provided fresh_tomatoes lib that generates the html/css code for
# the provided movie classes


toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous"
                        "when a new spaceman figure supplants him as top toy"
                        "in a boy's room",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        81)  # movie instance made for Toy Story.

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a"
                     "unique mission becomes torn between following his orders"
                     "and protecting the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     162)  # movie instance made for Avatar.

interstellar = media.Movie("Interstellar ",
                           "A team of explorers travel through a wormhole in"
                           "space in an attempt to ensure humanity's survival",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                           168)  # movie instance made for Interstellar.

black_panther = media.Movie("Black Panther",
                            "T'Challa, the King of Wakanda, rises to the"
                            "throne in the isolated, technologically advanced"
                            "African nation, but his claim is challenged by a"
                            "vengeful outsider who was a childhood victim of"
                            "T'Challa's father's mistake.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU",
                            134)  # movie instance made for Black Panther.

walter_mitty = media.Movie("The Secret Life of Walter Mitty",
                           "When his job along with that of his co-worker are"
                           "threatened, Walter takes action in the real world"
                           "embarking on a global journey that turns into an "
                           "adventure more extraordinary than anything he"
                           "could have ever imagined.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BODYwNDYxNDk1Nl5BMl5BanBnXkFtZTgwOTAwMTk2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=HddkucqSzSM",
                           114)
# movie instance made for The Secret Life of Walter Mitty.

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting, a janitor at M.I.T., has a gift"
                                "for mathematics, but needs help from a "
                                "psychologist to find direction in his life.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=ReIJ1lbL-Q8",
                                126)
# movie instance made for Good Will Hunting.

movies = [toy_story, avatar, interstellar, black_panther, walter_mitty,
          good_will_hunting]
#  Array of movie instances/objects

fresh_tomatoes.open_movies_page(movies)
# Call the open_movies_page function from the fresh_tomatoes lib.
# It is then provided with the movies array.
