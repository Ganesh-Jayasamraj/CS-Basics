# String, List, tuple ...

# String
Str = 'Hello World '

print (Str)             # Print sting
print (Str[0])          # Print First character
print (Str[2:5])        # Slicing (Format)
print (Str[2:])         # Slicing (Format)
print (Str * 2)         # Print Twice "or Multiple TImes"
print (Str + "Alpha")   # Concatenation


# List
list = [ 'abcd', 666, 0.666, "Hello", "World"]

list_01 = [123, "abcd"]

print(list)
print(list[0])
print(list[1:3])
print(list + list_01)

# Tuples

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples