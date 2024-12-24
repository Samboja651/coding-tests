"""
A: 65, Z: 90
a: 97, a: 122
0: 48, 9: 57
"""
if __name__ == '__main__':
    s = input()
    uppercase_char = set([chr(char) for char in range(65, 91)])
    lowercase_char = set([chr(char) for char in range(97, 123)])
    numbers = set([chr(char) for char in range(48, 58)])
    set_s = set(s)
    
    def _isalphanumeric()-> bool:
        status = False
        alphanumerics_chars = uppercase_char.union((lowercase_char.union(numbers)))
        set_difference = set_s.intersection(alphanumerics_chars)
        
        if len(set_difference) >= 1:
            status = True
        else:
            status = False
        return status 
    print(_isalphanumeric())
    
    def _isalphabetical()-> bool:
        status = False
        alphabetical_chars = uppercase_char.union(lowercase_char)
        set_intersection = set_s.intersection(alphabetical_chars)
        
        if len(set_intersection) >= 1:
            status = True
        else:
            status = False
        return status
    print(_isalphabetical())
    
    def _isdigit()-> bool:
        status =False
        set_intersection = set_s.intersection(numbers)
        if len(set_intersection) >= 1:
            status = True
        else:
            status = False         
        return status  
    print(_isdigit())
    
    def _islower()-> bool:
        status = False
        set_intersection = set_s.intersection(lowercase_char)
        if len(set_intersection) >= 1:
            status = True
        else:
            status = False
        return status
    print(_islower())
    
    def _isupper()-> bool:
        status = False
        set_intersection = set_s.intersection(uppercase_char)
        if len(set_intersection) >= 1:
            status = True
        else:
            status = False   
        return status
    print(_isupper())