Simple OMDB api calling application in python

1. Install omdb from internet using: pip install omdb
2. Generate api keys from the website: http://www.omdbapi.com/apikey.aspx
3. We also check the requets module, if not installed, we have to install it.
4. Run python file omdb_api_calling.py in CMD using: python omdb_api.py movie_name  (Only one argument to be passed)
5. Gives the information in the form of Json data.


		     (Linux Machine)
_________________________________________________________________________________

Note: Create a docker container in the server, and installed python3-pip. After installing all the dependies

6. Now run python script inside docker container and input movie whose ratings we need.
   
   # python /tmp/OMDB_API.py <Movie-Name>
   
   example:-
   python /tmp/OMDB_API.py The Avengers
7. For updated code, we want to push code to the /tmp directory...

docker pull vivekk1/omdb_repo:Python-Container
Copy the file in the folder. 
docker cp file-name <container-name>:/path


7. Find the git close repository : "https://github.com/vivektiwari660/omdb_api_calling.git"
