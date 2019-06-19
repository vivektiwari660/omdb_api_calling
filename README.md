# omdb_api_calling
Simple application for calling the OMDB rest api

1. Install omdb from internet using: pip install omdb
2. Generate api keys from the website: http://www.omdbapi.com/apikey.aspx
3. We also check the requets module, if not installed, we have to install it.
4. Run python file omdb_api_calling.py in CMD using: python omdb_api_calling.py
5. Program ask for the user input 
6. Give the information in the form of XML data.
7. Add docker to the module we Creating a Dockerfile without extension: The file content looks like this 

              FROM python:3
              ADD omdb_api_calling.py /
              RUN pip install pystrich
              CMD [ "python", "./omdb_api_calling.py","-OPTIONAL_FLAG"]
              
              
8. Ready to built docker with COMMAND:        "docker build -t python-barcode ."
9.Run Your Image :
                                               "docker run python-barcode"
                                               
10. Run docker with single line: 

          "docker run -it --rm --name first-python-script -v "$PWD":/usr/src/widget_app python:3 python omdb_api_calling.py"

*** Right Now I am facing issue on installing& configuring the docker in windows.

11. 11. Find the git close repository : 
                                        "https://github.com/vivektiwari660/omdb_api_calling.git"
