# find if a degree sequence represents a valid graph

def havel_hakimi(degrees):
    degrees.sort(reverse=True)
    while degrees:
        largest = degrees.pop(0)
        if largest == 0:
            return True
        
        if largest > len(degrees):
            return False
        
        for i in range(largest):
            degrees[i] -= 1
            
            if degrees[i] < 0:
                return False
    
    return True

# examples from practice midterm 2
print(havel_hakimi([2, 2, 2, 2]))  # True
print(havel_hakimi([4, 4, 4, 2, 2]))    # False
print(havel_hakimi([4, 3, 2, 1]))    # False
