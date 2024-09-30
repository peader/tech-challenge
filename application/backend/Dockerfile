FROM python:3.7-slim


# install flask and flask_cors
RUN pip install flask flask_cors

# copy server.py to the container
COPY server.py /app/server.py

EXPOSE 5000

# start the server when the container starts
CMD ["python", "/app/server.py"]
