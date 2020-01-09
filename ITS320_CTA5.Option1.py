print ('')
print ('Reverse Those Strings:')
print ('This program can be used to accept 3 string values and output ', end='')
print ('the reversed order of them.\n')

def main():
    s = first_string
    n = second_string
    p = third_string
    print ('1st reversed string: ',s)
    print ('2nd reversed string: ',n)
    print ('3rd reversed string: ',p)

s = input("Enter 1st string: ")
first_string = (s[::-1])

n = input("Enter 2nd string: ")
second_string = (n[::-1])

p = input("Enter 3rd string: ")
third_string = (p[::-1])

print('')

main()
