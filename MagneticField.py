#Jordan Stakenas
#4-1-21
#Exam 3 Individual
#The base for this code was taken from Reading Assignment Week 10, HW7-Q5
#This program attempts to calculate the magnetic fields at various locations perpendicular to a wire
#Rubric-relevant comments are marked with #!!#
#I'm basing this off the "calculating what a magnetic field looks like" rubric since this info will be used to draw out a magnetic field
#perpendicular to the wire (crosssection)
#---------------------------------------------------------------------------------------------------------------------------#
#!!#The basis for the mathematical operations is through the Biot-Savart law
#Currently, the exact values do not appear to be calculating correctly.
#I'm unsure why, but i have reason to believe i'm incorrectly calculating something under the '#segment Calculations' section
#However! The direction of the fields should be accurate.
#---------------------------------------------------------------------------------------------------------------------------#

import numpy as np
from scipy import constants

def magnetic_Field(x, y, z):
# Given information
    L = 1.8                         #length of the wire
    segment_Amount = 8              #Amount of segments of the wire, this should stay an even number to simplify things below/prevent them from breaking

    A = np.array([x, y, z])                             #!!#Observation location
    I = 7.4                                             #!!#Current running through the wire
    dB_Array = []                                       #init an array to hold all the resulting B values for each segment in regards to a given observation location
                    
    #This for loop goes from i = negate(segmentAmount)/2 to i = segmentAmount/2
    #In other words, its looping 8 times with values -4 to 3, and results in calculations on 8 segments
    #Note that the final segment, segment 8, has an initial of segment_len * 3 and a final of segment_len*3+1
    for i in range(int(-1*(segment_Amount/2)), int(segment_Amount/2)):
        
# Segment Calculations
        segment_Len = L/segment_Amount                                  #First we get the length of individual segments
        #!!# I believe the below 2-3 lines classifies under "direction of a segment"
        #as the inital and final positions of the segment are calculated here
        segment_Vector_Init = np.array([segment_Len * i, 0,0])          #!!#the above can be used to find the start point of a given segment 
        segment_Vector_Fin = np.array([segment_Len * i+1, 0, 0])        #!!#it can also be used to find the end point of a given segment
        segment_Center = (segment_Vector_Init + segment_Vector_Fin)/2   #!!#we can essentially take an "average" of the two points to find the center of this segment
        dl_Segment = segment_Vector_Fin - segment_Vector_Init           #subtracting the inital point from the end point gives us the length of a segment
        segment_Vector_Mag = np.linalg.norm(dl_Segment)                 #and we then find the 

#r_vector and r_hat calculations
        # We now have all segments that will be used for the calculations!
        # With some further math, we calculate the r vector and r hat vector
        #!!# I believe that this line below classifies as the position vector
        rVec = A - segment_Center
        rHat = rVec / np.linalg.norm(rVec)

#cross dL and r_hat
        # next is calculating the cross of dl and r hat
        # This could be done below, but the final equation is already a bit of a textual mess. Better to split things up
        dlr = np.cross(dl_Segment, rHat)

#Calculate magnetic field from a single segment
        # and finally we bring it all together to get the final B value
        #!!# Calculate the magnetic field at observation location using the Biot-Savart law
        dB_Array.append((constants.mu_0/(4*np.pi))*((I * dlr) / np.linalg.norm(rVec)**2))
        #print("The Magnetic field at segment ", i+5, " is ", dB_Array[i+4], "m")
        
#Summation of magnetic fields from each segment
    dB_Sum = np.array([0,0,0])                                          #Initialize an empty array
    for i in range(8):                                                  #Sort through the array of magnetic fields felt from each segment
        dB_Sum = np.add(dB_Sum, dB_Array[i])                            #and sum all of them together into one vector

    print("total magnetic field felt at [",x,y,z,"] is", dB_Sum)

#calculate the magnetic field felt at multiple locations of interest
magnetic_Field(0.112, 0.247, 0)         #a
magnetic_Field(0.112, 0.1235, 0.1235)   #i
magnetic_Field(0.112, 0, 0.247)         #b
magnetic_Field(0.112, -0.1235, 0.1235)  #j
magnetic_Field(0.112, -0.247, 0)        #c
magnetic_Field(0.112, -0.1235, -0.1235) #k
magnetic_Field(0.112, 0, -0.247)        #d
magnetic_Field(0.112, 0.1235, -0.1235)  #l


    
