def search(arr, x):
    """ Given an array 'arr' and an element 'x', this is a linear
        search of the array's elements to find a match and the return
        the position of the observed match in the array, or the return 
        of -1 as an indication of no match found.
        """
    # Store the lenght of the array as "N"
    N = len(arr)
    
    # Loop through a range of values from "0" to "N"
    for i in range(0, N):
        # Compare the given element "x" with the array's elements.
        if (arr[i] == x):
            # Print the position of the element if found
            print(i)
            # Return the position of the element if found
            return i   
    print(-1) # Print "-1" if not found
    return -1
        
        
search([1,2,3,4],3)