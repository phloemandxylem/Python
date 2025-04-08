#Numpy
#Import the numpy package as np, so that you can refer to numpy with np.
import numpy as np

#Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

#Use np.array() to create a numpy array from baseball. Name this array np_baseball.
np_bas3ball = np.array(baseball)

#Print out the type of np_baseball to check that you got it right.
print(type(np_bas3ball))

#Converting lists
#Create a numpy array from height_in. Name this new array np_height_in.
height_in = [ 56, 48, 60, 52, 49 ]
np_height_in = np.array(height_in)

#Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
np_height_in_m = np_height_in * 0.0254

