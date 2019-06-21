import sys
import json
#To access the OMDb API, we can create an ``OMDBClient`` instance:
from omdb import OMDBClient
# must use OMDb API parameters
client = OMDBClient(apikey='8ce3c73f')
print("Success, API is connected")

# Default for Rotten Tomato rating... 
client.set_default('tomatoes', True)

cmd_Argument = sys.argv[1:]

#print(cmd_Argument)
print ("The command line argument is : %s" %(cmd_Argument))
# User Input 
#movie_name = str(input("Please enter movie name : "))
#movie_year = input("Enter year as well : ")

res1 = client.request(t= cmd_Argument, plot='full', tomatoes='true', timeout=50) # year = movie_year
xml_content = res1.content

my_json = xml_content.decode('utf8')          #.replace("'", '"')
print('* ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
#movie_title = data["Title"]
#print("The Title of the Movie : ", movie_title)
tomato_rat = data["Ratings"][1]["Value"]
print("Rotten Tomato rating is : ", tomato_rat)
print('& ' * 20)
print('& ' * 20)

# All the information about particular movie name
s = json.dumps(data, indent=4, sort_keys=True)
print(s)
