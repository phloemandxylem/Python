#Numpy
#Import the numpy package as np, so that you can refer to numpy with np.
import numpy as np

#Create list baseball and convert to numpy array --------------------------

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

#Use np.array() to create a numpy array from baseball. Name this array np_baseball.
np_bas3ball = np.array(baseball)

#Print out the type of np_baseball to check that you got it right.
print(type(np_bas3ball))


#Converting numpy arrays -------------------------------------------------------

#Create a numpy array from height_in. Name this new array np_height_in.
height_in = [ 56, 48, 60, 52, 49 ]
np_height_in = np.array(height_in)

#Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
np_height_in_m = np_height_in * 0.0254
print(np_height_in_m)

#Subsetting numpy arrays------------------------------------------------------

#Print out the 50th row of np_baseball.
np_baseball = np.array(baseball)
print(np_baseball[49,:]

#Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
np_weight_lb = np_baseball[:,1]

#Select the height (first column) of the 124th baseball player in np_baseball and print it out.
print(np_baseball[123, 0])


