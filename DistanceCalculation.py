from array import *
import math

class DistanceCalculation:
	def __init__(self, fieldWidth, fieldDepth, cellsRows, zonesCols):
	
	  # Constructor
		 # Creates a Distance Calculation Object with the given Values
		# @param double fieldWidth Width of the Field in Meters
		# @param double fieldDepth Depth of the Field in Meters
		# @param int cellsRows Number of Rows in the Field
		# @param int cellsCols Number of columns in the Field
		# Cells in the field are numbered from left to right starting at 1 (inclusive) 
		


		# EXAMPLE
		# Field:
		# ----Widht----   |
		# 1   2   3   4   |Depth
		# 5   6   7   8   |
		# 9   10  11  12  |

		# has 3 Rows and 4 Columns
		
		#Calculates all necessary Values
		self.zonesCount = cellsRows * zonesCols
		self.xDistance = fieldWidth / zonesCols
		self.yDistance = fieldDepth / cellsRows
		
		#initializes distance array. This is a 2D array based on the calculated zonesCount
		self.distances = [[[]*self.zonesCount]*self.zonesCount for x in range(self.zonesCount)]
		
		#initializes coordinates list of tuples
		self.coordinates = []
			
		
		
		#Fills a List with Coordinates, indexes are the number of the cells
		for i in range (0, cellsRows):
			
			for j in range (0, zonesCols):
				self.coordinates.append((j,i))
				
		#Fills the Distances Array with the actual Distances
		for i in range (0,self.zonesCount):
			
			for j in range (0, self.zonesCount):
				self.distances[j][i] = self.Calc(j,i)
			
		
				
				
	#Calculates the Euclidean Distance between two given Points				
	def Calc(self, start, goal):
		begin = self.coordinates[start]
		end = self.coordinates[goal]
		diff = pow(self.xDistance * abs(end[0] - begin[0]),2)
		diff += pow(self.yDistance * abs (end[1] - begin[1]),2)
		return math.sqrt(diff)
	
	#return the distance between two given Points
	def GetDistance (self, start, goal):
		return self.distances[start][goal]
		

		