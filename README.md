# andela_command_line_api_program

ANGA

ANGA is a command line app that uses the openweathermap api to get the current day's weather.

USAGE:

Command        Argument    Example



fetch_weather   city     fetch_weather Nairobi


INSTALLATION

Clone the repo into your computer : git clone https://github.com/zmwas/andela_command_line_api_program.git

Create a virtualenv  then run the following commands to download dependencies: pip install requests and pip install docopt

Go to the main folder of the repo you cloned and type python anga.py


You can change the api key and get your own by signing up at https://home.openweathermap.org/users/sign_up and copying the key.

Then change the key in the weather.py file by modifying this variable: api_key ="&APPID="YOUR_KEY_HERE" which is located

in the fetch weather method

