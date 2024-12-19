def plant_decision(plant_id):

    # Get plant ID from user input 
    plant_id = int(plant_id) 

    binary_string = bin(plant_id)

    #return binary_string 
    last_bit = binary_string[-1] 

    if last_bit == '0':
        last_bit = "Skip"
        return last_bit
    elif last_bit == '1':
        last_bit = "Plant"
        return last_bit
     
# Get plant ID from user input
plant_id = input("Input plant ID in decimal: ") 

# Call the function and print the result
binary_result = plant_decision(plant_id)
Decision = plant_decision(plant_id)
print(f"Decision: {Decision}")
