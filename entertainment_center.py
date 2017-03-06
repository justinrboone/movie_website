# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

# Create movie objects
the_phantom_menace = media.Movies("Star Wars: Episode I – The Phantom Menace",
                                  "Star Wars: Episode I – The Phantom Menace is a 1999 American epic space opera film written and directed by George Lucas, produced by Lucasfilm and distributed by 20th Century Fox.",
                                  "http://t0.gstatic.com/images?q=tbn:ANd9GcSb2JIB-OTEmF4VxKWNaXzWi8QwxhMTIG4YsqgnyTrfl1WfEqvy",
                                  "https://www.youtube.com/watch?v=0MTp807E7_k")

attack_of_the_clones = media.Movies("Star Wars: Episode II – Attack of the Clones",
                                    "Star Wars: Episode II – Attack of the Clones is a 2002 American epic space opera film directed by George Lucas and written by Lucas and Jonathan Hales.",
                                    "http://t3.gstatic.com/images?q=tbn:ANd9GcS_urKXRdNkSND8mvflceI4Lxbn5uUd7xJyydZFXitXstRe03h7",
                                    "https://www.youtube.com/watch?v=5NWacXGA4nY")

revenge_of_the_sith = media.Movies("Star Wars: Episode III – Revenge of the Sith",
                                   "Star Wars: Episode III – Revenge of the Sith is a 2005 American epic space opera film written and directed by George Lucas. It is the third installment of the Star Wars prequel trilogy.",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcT7TlfhiJ93841oYulGpyJZ3YULcgzah1CGumaVQuZ3-zXarfai",
                                   "https://www.youtube.com/watch?v=-lnegsUlzjM")

star_wars = media.Movies("Star Wars",
                         "Star Wars is a 1977 American epic space opera film written and directed by George Lucas. The first installment in the Star Wars film series, it stars Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing, and Alec Guinness.",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX",
                         "https://www.youtube.com/watch?v=H38MpZtujJc")

empire_strikes_back = media.Movies("The Empire Strikes Back",
                                   "The Empire Strikes Back is a 1980 American epic space opera film directed by Irvin Kershner. Leigh Brackett and Lawrence Kasdan wrote the screenplay, with George Lucas writing the film's story and serving as executive producer.",
                                   "http://t1.gstatic.com/images?q=tbn:ANd9GcTtXwQAEDxEY3E9Nn78H96VZCjlV6hZWPlDd5IpVNyeuzO2vT17",
                                   "https://www.youtube.com/watch?v=Ft9a-CfdZi8")

reture_of_the_jedi = media.Movies("Return of the Jedi",
                                  "In the epic conclusion of the saga, the Empire prepares to crush the Rebellion with a more powerful Death Star while the Rebel fleet mounts a massive attack on the space station. Luke Skywalker confronts his father Darth Vader in a final climactic duel before the evil Emperor. In the last second, Vader makes a momentous choice: he destroys the Emperor and saves his son. The Empire is finally defeated, the Sith are destroyed, and Anakin Skywalker is thus redeemed. At long last, freedom is restored to the galaxy.",
                                  "http://t0.gstatic.com/images?q=tbn:ANd9GcRnTSmH4ckpqTGuLeBlI6DEnAagQq1Oha9c8fDlm2SRbcpEKZK0",
                                  "https://www.youtube.com/watch?v=sG5r-XRfI0I")

force_awakens = media.Movies("Star Wars: The Force Awakens",
                             "Star Wars: The Force Awakens is a 2015 American epic space opera film directed, co-produced, and co-written by J. J. Abrams.",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",
                             "https://www.youtube.com/watch?v=UitsQDWSlUg")

# Add all movie obects to a list
movies = [the_phantom_menace, attack_of_the_clones, revenge_of_the_sith, 
          star_wars, empire_strikes_back, reture_of_the_jedi, force_awakens]

# Create and open movie web site using objects from the movies array
fresh_tomatoes.open_movies_page(movies)
