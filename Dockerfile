FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE $PORT
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
