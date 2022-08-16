from socket import *
from time import sleep

from station import StationSimulator

bergen_station = StationSimulator(simulation_interval=1)
oslo_station = StationSimulator(simulation_interval=1)
# Turn on the simulator
bergen_station.turn_on()
oslo_station.turn_on()

# Two lists for temperature and precipitation
bergentemperature = []
bergenprecipitation = []

oslotemperature = []
osloprecipitation = []
# Capture data for 72 hours
# Note that the simulation interval is 1 second
for _ in range(10):
    # Sleep for 1 second to wait for new weather data
    # to be simulated
    sleep(1)
    # Read new weather data and append it to the
    # corresponding list
    bergentemperature.append(bergen_station.temperature)
    bergenprecipitation.append(bergen_station.rain)

    oslotemperature.append(oslo_station.temperature)
    osloprecipitation.append(oslo_station.rain)

# Shut down the simulation
bergen_station.shut_down()
oslo_station.shut_down()

print("b"+ str(bergentemperature))
print("o" + str(oslotemperature))
print("bregn"+ str(bergenprecipitation))
print("oregn"+ str(osloprecipitation))

serverName = "localhost"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
open("bergenTemp.txt", "w").close()
open("osloTemp.txt", "w").close()
open("bergenPrecipitation.txt", "w").close()
open("osloPrecipitation.txt", "w").close()
    



while True:
    message, clientAdress = serverSocket.recvfrom(2084)
    serverSocket.sendto(("b" + str(bergentemperature)).encode(), clientAdress)
    serverSocket.sendto(("o" + str(oslotemperature)).encode(), clientAdress)
    serverSocket.sendto(("p" + str(osloprecipitation)).encode(), clientAdress)
    serverSocket.sendto(("r" + str(bergenprecipitation)).encode(), clientAdress)


