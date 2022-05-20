# Spotify app
This app is able to fetch data from spotify api, and display data about users most listened songs. It is able to sort these data in different ways, for example by songs popularity.
It requires user authorization, to be able to access data on spotify api.

## Usage
To run this app python(django) is needed. Server is launched by command python3 manage.py runserver. App runs localy by default on adress http://localhost:8000 . After succsseful start, on this adress should apear button, that
asks for user authorization, if this wasnt already done before user should be redirected to spotify and will be asked to login and confirm sharing of information.
After authorization is completed user will be redirected back to app and will be able to see desired data. App was tested in Chrome and Firefox environment.

## Account
Because of user authorization i have created new spotify account (i dindt want to share my personal), this account can serve for testing purposes, if you would like to
try this app whitout the need of logging in whit your own account feel free to use this one.\n
login email: testspotifyapi@gmail.com\n
password: Test123@4
