print ('')
print ('Value of Ferrari 250 GTO\n')
print ('This program was designed with the intention of giving')
print ('the aproximate value of a Ferrari 250 GTO depending on the')
print ('year that it was produced.\n')

no_price = 0
sixtwo_to_64 = 18500
sixfive_to_68 = 6000
sixnine_to_71 = 12000
seventwo_to_75 = 48000
sevensix_to_80 = 200000
eightone_to_85 = 650000
eightsix_to_2012 = 35000000
thirteen_to_2014 = 52000000

fer_value = 0
fer_year = int(input('Enter year of Ferrari 250 GTO (e.g. 1977): '))

if fer_year <= 1961:
    print ('Ferrari 250 GTO not yet created, no value available')
    fer_value = no_price 
elif fer_year <= 1964:
    fer_value = sixtwo_to_64 
elif fer_year <= 1968:
    fer_value = sixfive_to_68
elif fer_year <= 1971:
    fer_value = sixnine_to_71 
elif fer_year <= 1975:
    fer_value = seventwo_to_75 
elif fer_year <= 1980:
    fer_value = sevensix_to_80 
elif fer_year <= 1985:
    fer_value = eightone_to_85 
elif fer_year <= 2012:
    fer_value = eightsix_to_2012 
elif fer_year == 2013:
    fer_value = thirteen_to_2014 
elif fer_year == 2014:
    fer_value = thirteen_to_2014 
elif fer_year > 2014:
    print ('We will have to wait and see')
    fer_value = no_price 

print ('Ferrari 250 GTO value: $',fer_value)

