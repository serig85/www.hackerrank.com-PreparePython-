def is_leap(year):
    leap = False
    
    # Write your logic here
    if year//400 == year/400:
        leap=True
    else:
        if year//4 == year/4 and year//100 != year/100:
            leap=True
            
         
    return leap

