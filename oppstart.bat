START py weather_station_UDP_server.py 
timeout /t 14
START py stationtry.py
timeout /t 2
venv\Scripts\activate && flask run
PAUSE