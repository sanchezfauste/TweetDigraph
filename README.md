# TweetDigraph
Representation of Twitter conversation on graph format

## Dependences
- Python 2.7.x.
- Python dependences are specified on `requirements.txt` file.

## How to prepare the environment on Linux (Debian)
The easiest way to prepare the environment is to create a virtualenv and install the Python dependences with pip.

You can install the necessary Debian packages with `# apt-get install python python-pip python-virtualenv`.

Now execute this commands to prepare the application:
```
git clone https://github.com/sanchezfauste/TweetDigraph.git
cd TweetDigraph
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python TwitterAPI/twitter_api.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
deactivate
```

Register a Twitter application:
1. Go to: https://apps.twitter.com/
2. Register a new app.
3. Go to `Keys and Access Tokens` tab.
4. Edit the file `TwitterAPI/config.ini` with the obtained `Consumer Key` and `Consumer Secret`.

The application is ready to run.

## How to run the application on Linux
Enter to root directory of the application (normally `TweetDigraph`) and run:
```
source env/bin/activate
python manage.py runserver 0.0.0.0:8080
```

To stop the application press `CTRL-C` and run the command `deactivate` to deactivate the Python virtual environment.

## API RESTful
| Method | Resource                  | Description                                                 |
|--------|---------------------------|-------------------------------------------------------------|
| GET    | /conversation             | Show the list of imported conversations                     |
| GET    | /conversation/{id}/import | Import the Twitter conversation with the specified id       |
| GET    | /conversation/{id}/show   | Show the conversation with the specified id                 |
| GET    | /conversation/{id}/graph  | Show the conversation with the specified id on graph format |
