val = [ x for x in input() if ( x == "H" ) or ( x == "Q" ) or ( x == "9" )]    
print(["NO", "YES"][len(val) >= 1])