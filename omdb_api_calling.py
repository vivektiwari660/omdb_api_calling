
#To access the OMDb API, we can create an ``OMDBClient`` instance:

from omdb import OMDBClient

# must use OMDb API parameters

client = OMDBClient(apikey='8ce3c73f')

print("Success")

# Default for Rotten Tomato rating... 
client.set_default('tomatoes', True)

# User Input 
movie_name = str(input("Please enter movie name : "))
#movie_year = input("Enter year as well : ")
res1 = client.request(t= movie_name, plot='full', tomatoes='true', timeout=5,r='xml') # y = movie_year
#res = client.request(t='True Grit', y=1969, r='xml')
xml_content = res1.content
#xml_content = res.content
# Output in the XML format
print(xml_content)

#with open


# search movies by string
#client.search_movie('True Grit')
#client.search_movie('True Grit', timeout=5)
#client.search_movie('true', page=2)


# lower level API request
#client.request(t='True Grit', y=1969, plot='full', tomatoes='true', timeout=5)

#input("Wait")
