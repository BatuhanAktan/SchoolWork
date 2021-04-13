"""
This application uses the data to keep track of the information and process bike rentals and returns.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Nov 2020
"""


def initializeBikeInfo():
    """
    This function defines the dictionary that will hold all the information.
    The dictionary is of the format:
        stationID (key): value is a dictionary
        So, for example an entry for station ID = 70 might look like:
            70: {"location": "Jarvis", "cap": 50, "numBikes": 4, "docks":2}
    A dictionary containing all the stations' info is returned.
    Parameters:  None
    Return:  A dictionary
    """
    
    # creates bikeInfo dictionary
    
    bikeInfo = {
        
        7000:{"location": "York", "cap": 31, "numBikes": 20, "docks": 11},
        
        7001:{"location": "Esplanade", "cap": 15, "numBikes": 5, "docks": 10},
        
        7002:{"location": "George", "cap": 19, "numBikes": 1, "docks": 18},
        
        7003:{"location": "Madison", "cap": 15, "numBikes": 2, "docks": 13},
        
        7004:{"location": "Elm", "cap": 11, "numBikes": 0, "docks": 11},
        
        7005:{"location": "University", "cap": 19, "numBikes": 0, "docks": 18},
        
        7006:{"location": "Bay", "cap": 11, "numBikes": 0, "docks": 11},
        
        7007:{"location": "College", "cap": 11, "numBikes": 1, "docks": 10}
        }
    

    return bikeInfo
   


def addNewStation(bikeInfo, id, location, cap, numBikes, docks):
    """
    This function adds a new entry into the dictionary containing the
    information passed as parameters.
    Parameters:  bikeInfo - a dictionary
                 id - integer indicating the location id
                 location - string indicating the location of the rental station
                 cap - integer - number of bikes that the station accommodates
                 numBikes - how many bikes are currently available for rent
                 docks - how many docs are currently free
    Returns:  Nothing returned, but bikeInfo is updated.
    """
    
    #updates bikeInfo dictionary using the parameters
    
    bikeInfo.update({id:{"location": location, "cap": cap, "numBikes": numBikes, "docks": docks}}) #updates bike info with the information from the parameters


def bikeRental(bikeInfo, stationID):
    """
    Checks to ensure that stationID is a valid station in bikeInfo.
    If so, checks to see if there are bikes available at this station.
    If so, decrements the number of bikes available for rent at this station.
    Parameters: bikeInfo - a dictionary
                stationID -- integer representing the ID of the station from which to rent
    Returns:  True (bike was rented successfully), False (something went wrong)
              bikeInfo may be updated.
    """
    
    # if station Id is in bikeinfo and number of bikes is greater than 0 decreases the number of bikes by one and returns true.

    if stationID in bikeInfo and bikeInfo[stationID]["numBikes"]>0:
        bikeInfo[stationID]["numBikes"] -= 1
        return True
    else:   
        return False
        

def returnBike(bikeInfo, stationID):
    """
    Indicates whether or not a bike can be returned to the given station ID.
    Need to check if stationID is valid.  If not, return False (bike can't be returned here).
    A bike can be returned if there are available docks, otherwise it cannot be returned
    to that location.
    Parameters:  bikeInfo - a dictionary
                 stationID - an integer
    Returns: True (bike can be returned), False (something went wrong) #Added my own returns because otherwise it did not return anything.
              bikeInfo may be updated.
    """

    # if station id is in bikeinfo and the number of docks is greater than 0 it returns true.
    
    if stationID in bikeInfo and bikeInfo[stationID]["docks"]>0:
        return True
    else:   
        return False


def getInfo(bikeInfo, stationID):
    """
    This function looks up the information found at stationID in bikeInfo
    and returns the location, capacity, bikes available and docks in a list.
    If stationID does not exist in bikeInfo, return an empty list []
    Parameters:  bikeInfo - a dictionary of the format {stationID: {values}}
                 stationId - integer
    Return: a list [location, capacity, bikesAvailable, docks] or []
    """
    
    emptyList = [] #creates empty list to return if station is not in bikeinfo
    
    if stationID in bikeInfo:
        return list(bikeInfo[stationID].values()) #gets all the values for the station id and makes it a list
    return emptyList


def bikesAvailable(bikeInfo):
    """
    This function returns the total number of bikes available to rent across all
    locations.
    Parameters:  bikeInfo - a dictionary of the format {stationID: {values}}
    Return: integer
    """
    
    total = 0
    
    for stationID in bikeInfo: # iterates through the dictionary and adds the number of bikes to total.
        total +=  bikeInfo[stationID]["numBikes"] # adds the value of numbikes to total
        
    return total
