# Two libraries to be used
import fresh_tomatoes
import media

# List of movies
National_Treasure = media.Movie("National Treasure", "https://www.youtube.com/watch?v=mcf4tXYjaxo", "http://www.gstatic.com/tv/thumb/movieposters/35100/p35100_p_v8_aa.jpg")
Hitmans_bodyguard = media.Movie("The Hitman's Bodyguard", "https://www.youtube.com/watch?v=F4Afusxc2SM", "https://www.dvdsreleasedates.com/posters/800/T/The-Hitmans-Bodyguard-2017-movie-poster.jpg")
Fast_and_Furious = media.Movie("The Fast and the Furious", "https://www.youtube.com/watch?v=ZsJz2TJAPjw", "http://vignette1.wikia.nocookie.net/fastandfurious/images/0/04/The_Fast_and_the_Furious_%28DVD_Cover%29.jpeg/revision/latest?cb=20150501043627")
Fast_and_Furious_2 = media.Movie("2 Fast 2 Furious", "https://www.youtube.com/watch?v=F_VIM03DXWI", "https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/Two_fast_two_furious_ver5.jpg/220px-Two_fast_two_furious_ver5.jpg")
Fast_and_Furious_3 = media.Movie("The Fast and the Furious: Tokyo Drift", "https://www.youtube.com/watch?v=mgb-T6PvuvY", "https://i.ytimg.com/vi/9CZoR_1JZlI/movieposter.jpg")
Italian_Job = media.Movie("The Italian Job", "https://www.youtube.com/watch?v=5Eyw-Qiwpj0", "https://images-na.ssl-images-amazon.com/images/M/MV5BNDYyNzYxNjYtNmYzMC00MTE0LWIwMmYtNTAyZDBjYTIxMTRhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY1200_CR85,0,630,1200_AL_.jpg")

# Group them into a list
movie_list = [National_Treasure, Hitmans_bodyguard, Fast_and_Furious, Fast_and_Furious_2, Fast_and_Furious_3, Italian_Job]

# Run fresh tomatoes function to show the web page
fresh_tomatoes.open_movies_page(movie_list)

