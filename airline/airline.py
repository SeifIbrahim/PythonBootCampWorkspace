# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:55:59 2015

@author: home
"""
import operator

airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", "LHR": "London-Heathrow", \
            "SVO": "Moscow", "CDA": "Chicago-Midway", "SBA": "Santa Barbara", "LAX": "Los Angeles",\
            "JFK": "New York City", "MIA": "Miami", "AUM": "Austin, Minnesota"}
            
# airline, number, heading to, gate, time (decimal hours) 
flights = [("Southwest",145,"DCA",1,6.00),("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
           ("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60), ("United",46,"LAX",5,6.5),\
           ("Southwest",23,"SBA",6,12.5),("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
           ("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),("United",2032,"MIA",21,15.1),\
           ("SpamAir",1,"AUM",42,14.4)]

flights.sort(key=operator.itemgetter(4))
print ("Flight \t Destination \t \t Gate \t Time")
print ("-"*53)
for flight in flights:
    dest = airports[flight[2]]
    dest += " "*(20 - len(dest))
    print (flight[0] + " " + str(flight[1]) + "\t" + dest + "\t" + str(flight[3]) + "\t" + str(flight[4]))