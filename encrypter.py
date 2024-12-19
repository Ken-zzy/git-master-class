'''def sprang_encryption(message, enemies):
    # Write code here 
    message = input("Input message here: ")
    enemies = input("Input enemy names here: ")
    enemy_names = []
    #for x in enemy_names:
    if len(enemy_names) < 5: 
        #enemies = input("")
        enemy_names.append(enemies)
    #This is to join the list and the message which is a string together    
    crypted_message = "".join(enemy_names) + message 
    return crypted_message

crypted_message = sprang_encryption("Hello","dragon")
print (crypted_message)'''


def sprang_encryption(message, enemies):
    """
    Encrypts a message by concatenating a list of enemies before the message.

    Args:
        message: The message to be encrypted.
        enemies: A list of enemy names.

    Returns:
        The encrypted message.
    """

    encrypted_message = "".join(enemies) + message
    return encrypted_message

# Example usage:
message = "Secret Message"
enemies = ["Dragon", "Witch", "Orc"]

encrypted_message = sprang_encryption("", "")
print(encrypted_message)