# A00258304

from datetime import datetime
from datetime import timedelta

# filename = input("Enter the filename: ")
filename = "flight_times1.csv"

flights = {}

with open(filename) as file:       
    _ = file.readline() # FLIGHT#,Year,Month,Day,Origin,Destination,Distance,Departure,Arrival

    for line in file:
        flight_number, year, month, day, origin, destination, distance, deparature, arrival = line.strip().split(",")

        # departure_time = datetime(int(year), int(month), int(day))
        # arrival_time = datetime(int(year), int(month), int(day))
        depart_time = datetime.strptime(deparature, "%H:%M")
        arrive_time = datetime.strptime(arrival, "%H:%M")

        if depart_time > arrive_time:
            arrive_time += timedelta(days=1)
        
        duration = arrive_time - depart_time

        flights[(flight_number, origin, destination)] = str(duration)
        # print(str(duration))

        

# print(len(flights))
longest_flight = max(flights, key=flights.get)
print(f"Longest flight: {longest_flight[0]} Duration: {flights[longest_flight]} From: {longest_flight[1]} To: {longest_flight[2]}")
shortest_flight = min(flights, key=flights.get)
print(f"Shortest flight: {shortest_flight[0]} Duration: {flights[shortest_flight]} From: {shortest_flight[1]} To: {shortest_flight[2]}")