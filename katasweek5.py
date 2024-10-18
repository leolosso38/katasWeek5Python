#Number of People in the Bus
def number(bus_stops):

    return sum(sube - baja for sube, baja in bus_stops)

#Quarter of the year
def quarter_of(month):
    return (month + 2) // 3

#Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
     return "Yes" if boolean else "No"

#DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace('T', 'U')

#Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#Convert a String to An Array
def string_to_array(s):
    if s == "":
        return [""]
    return s.split()
#Multiply
def multiply(a, b):
    return a * b

#Double Char
def double_char(s):
  
    return ''.join([char * 2 for char in s])


#Remove First and Last Character
def remove_char(s):
    
    
    return s[1:-1]

#Vowel Count
def get_count(sentence):
   
    vocales = 'aeiou'
  
    return sum(1 for char in sentence if char in vocales )
#Sum of Odd Numbers
def row_sum_odd_numbers(n):
   
    return n ** 3 