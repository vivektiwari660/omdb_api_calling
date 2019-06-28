import sys
import json
# To access the OMDb API, we can create an ``OMDBClient`` instance:
from omdb import OMDBClient

# must use OMDb API parameters
client = OMDBClient(apikey='8ce3c73f')
print("Success, API is connected")

# Default for Rotten Tomato rating...
client.set_default('tomatoes', True)

cmd_Argument = sys.argv[1:]

try:
    # print(cmd_Argument)
    if cmd_Argument:
        print("The command line argument is : %s" % (cmd_Argument))
    # User Input
    # movie_name = str(input("Please enter movie name : "))
    # movie_year = input("Enter year as well : ")

        res1 = client.request(t=cmd_Argument, plot='full', tomatoes='true', timeout=50)  # year = movie_year
        xml_content = res1.content

        my_json = xml_content.decode('utf8')  # .replace("'", '"')
        print('* ' * 20)

    # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        #print(data)
        # for i in data["Ratings"]:
        #     if i['Source'] == "Rotten Tomatoes":
        #         tomato_rat =i["Value"]

        tomato_rat =[i["Value"] for i in data["Ratings"] if i['Source'] == "Rotten Tomatoes"]
        if tomato_rat:
            print("Rotten Tomato rating is : ", *tomato_rat)
        else:
            print("Rotten Tomato rating is not found")

        #tomato_rat = data["Ratings"][1]["Value"]
except:
    print("please enter valid movies name")

# else:
#     print("please enter valid movies name")
