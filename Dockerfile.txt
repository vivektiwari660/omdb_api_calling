#FROM python:3
#publicly available docker image "python" on docker hub will be pulled
FROM python
#creating directory docker_build in container (linux machine)
RUN mkdir c:\home\docker_build
#copying .py from local directory to container's docker_build folder
COPY omdb_api_calling.py /home/docker_build/omdb_api_calling.py
#running omdb_api_calling.py in container
CMD python /home/docker_build/omdb_api_calling.py
