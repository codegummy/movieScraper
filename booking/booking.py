from selenium import webdriver
import booking.constants as const
from selenium.webdriver.common.by import By



class Booking(webdriver.Chrome) :
  def __init__(self, driver_path =  "chromedriver.exe", teardown = False):
    self.driver_path = driver_path
    self.teardown = teardown
    super(Booking, self).__init__()
    self.implicitly_wait(15)
    """  self.maximize_window() """
  def __exit__(self, exc_type, exc_val, exc_tb):
    if self.teardown:
      self.quit()
  def land_first_page(self):
    self.get(const.BASE_URL)


  def get_movies(self):
      moviesList = []
      #main movie div
      movies = self.find_elements(By.CSS_SELECTOR, "div.cli-children")
      for movie in movies:
        #title
        movie_title = movie.find_element(By.CSS_SELECTOR, "div.cli-title").text

        #metadata which has date and duration
        movie_meta_data = movie.find_element(By.CSS_SELECTOR, "div.cli-title-metadata")

        #date
        date = movie_meta_data.find_element(By.CSS_SELECTOR, "span.cli-title-metadata-item:nth-child(1)").text

        #duration
        duration = movie_meta_data.find_element(By.CSS_SELECTOR, "span.cli-title-metadata-item:nth-child(2)").text

        #rating
        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text
        moviesList.append({
          "title": movie_title,
          "duration" : duration,
          "date" : date,
          "rating" : rating
          
        })
     
      with open("movies.txt", "w") as file:
          for movie in moviesList:
            file.write(f'''
{ movie["title"]} 
  Date: {movie["date"]} 
  Duration: {movie["duration"]} 
  Rating: {movie["rating"]} \n''')
      


