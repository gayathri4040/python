import requests
import pandas
from bs4 import BeautifulSoup

base_url = "https://www.oyorooms.com/hotels-in-hyderabad/?page="

# Added this as we cannot access the site, without headers
headers = {
    'User-Agent': 'My User Agent 1.0', 
    'From': 'youremail@domain.com'
}

#gets the content from the website
req = requests.get(base_url, headers=headers)
content = req.content

#parses the html content received
soup = BeautifulSoup(content, "html.parser")

#To store all the info of the hotels
scraped_info_list = []

#To get the number of pages
pages = soup.find("div", {"class": "ListingPagination__pageContainer"})
for page_num in pages.findAll("a", {"class": "ListingPagination__pageContainer--page"}):
    url = base_url + page_num.text
    
    req = requests.get(url, headers=headers)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    hotel_cards_list = soup.find_all("div", {"class": "hotelCardListing"})   

    for hotel_card in hotel_cards_list:
        hotel_dict = {}
        hotel_dict["Name"] = hotel_card.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["Address"] = hotel_card.find("span", {"itemprop": "streetAddress"}).text
        try:
            hotel_dict["Price"] = hotel_card.find("span", {"class": "listingPrice__finalPrice"}).text
            hotel_dict["Rating"] = hotel_card.find("span", {"class": "hotelRating__rating"}).text
        except AttributeError:
            pass

        amenities =  hotel_card.find("div", {"class": "amenityWrapper"})

        amenities_list = []
        for amenity in amenities.findAll("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

        hotel_dict["Amenities"] = ', '.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)

dataframe = pandas.DataFrame(scraped_info_list)
dataframe.to_csv("hotels_csv")
