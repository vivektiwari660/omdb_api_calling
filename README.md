Simple OMDB api calling application in python

1. Install omdb from internet using: pip install omdb
2. Generate api keys from the website: http://www.omdbapi.com/apikey.aspx
3. We also check the requets module, if not installed, we have to install it.
4. Run python file omdb_api_calling.py in CMD using: python omdb_api.py movie_name  (Only one argument to be passed)
5. Give the information in the form of Json data.
6. Add docker to the module we Creating a Dockerfile without extension :In windows Machine

		#publicly available docker image "python" on docker hub will be pulled
		FROM python:3
		#creating directory docker_build in container (linux machine)
		RUN mkdir c:\home\docker_build
		#copying .py from local directory to container's docker_build folder
		COPY omdb_api.py /home/docker_build/omdb_api.py
		#running omdb_api.py in container
		CMD python /home/docker_build/omdb_api.py



			OR   (Linux Machine)
_________________________________________________________________________________

Note: Create a docker container in the server, and installed python3-pip. After installing all the dependies, Create a docker tar file.

7. Find the OMDB.tar file in the git repo and run > docker load -i OMDB.tar
8. After it is done, we could see the file is loaded as Docker images by running CMD:  > docker images
9. Run the container using python command: > python omdb_api.py movie_name
10. Find the git close repository : "https://github.com/vivektiwari660/omdb_api_calling.git"
