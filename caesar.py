############## rotate_character ##############
#Returns ==> character string (alpha position of character)

def rotate_character(char, rot):

    if char.isupper():              
        position = ord('A')
    elif char.islower():
        position = ord('a')
    else:
        return char         

    order = ord(char) - position          
    table = (order + rot) % 26 + position  
    return chr(table)

################## caesar ###################
#################### encrypt ##################
#Returns ==> letter string (new letter reposition of string)

def rotate_string(text, rot):

     new_text = ''
     for rotation in text:
         new_letters = rotate_character(rotation, rot)
         new_text += new_letters
     return new_text
