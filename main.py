from booking.booking import Booking



with Booking(teardown= True) as bot:
  bot.land_first_page()
  bot.get_movies()

#RATINGS
#release date and genre