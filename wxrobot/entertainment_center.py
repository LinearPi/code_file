import media
import fresh_tomatoes

avater = media.Movie('nod','oneoneoneone','https://zh.wikipedia.org/wiki/Wikipedia:首页#/media/File:Tropical_storm_alberto_2006.jpg','https://www.youtube.com/watch?v=ozPAs9DNEbw')

# avater.show_trailer()
movie = [avater,]

fresh_tomatoes.open_movies_page(movie)