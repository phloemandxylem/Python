# Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print list areas
print(areas)

# Provide keys of a list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath] 
print(areas) 

# Create a list of lists 
house = [["hallway", hall], 
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed], 
         ["bathroom", bath]]
print(house)

# Subsetting lists
# Print out the second element from the list
print(areas[1])

# Print out the last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Slicing and dicing lists - selecting multiple elements
# Create a list called downstairs that contains just the first 6 elements of the areas list (the 6th will not be included) 

downstairs=areas[0:6]

# Subsetting lists of lists
# Subset the house list to get the float 9.5

house[4][1]

# Manipulating Lists
# Update the area of the bathroom to be 10.50 square meters instead of 9.50 using negative indexing and update the living room string to parlour

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath] 
areas[-1] = 10.50
areas[4] = "parlour"

# Extend a list 
# Use the + operator to paste the list ["outhouse", 22.1] to the end of the areas list. Store the resulting list as areas_2.

outhouse = 22.1
areas_2 = areas + ["outhouse", outhouse]

# Delete list elements
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
poolhouse = 22.1

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath, "poolhouse", poolhouse] 
del areas[10:12] # deletes element 10 and 11 

# Prevent changes in lists
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas) # create a copy of the list that can be manipulated
areas_copy[0] = 5.0

print(areas)











