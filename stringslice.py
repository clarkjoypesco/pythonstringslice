# Insert the proper slicing indices for the substring variable 
# so that the slice is a string that contains everything after "A NOUN". 
# For example, if we wanted to store everything after "went", the returned 
# string would be equal to sentence[11:].

sentence = "A NOUN went on a walk."

first_location = sentence.find('N')
second_location = sentence.find('N', first_location + 1)
substring = sentence[second_location + 1:]
print substring
