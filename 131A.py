s = input()

if s == s[0].lower()+s[1:].upper():
    print(s.capitalize())
elif s == s.upper():
    print(s.lower())
else:
    print(s)
    

    