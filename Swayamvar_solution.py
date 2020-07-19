def bridegroom(n,bride,groom):

    if bride.count("r") == groom.count("r"):  #IF NUMBER OF RUM DRINKERS AND MOJITO DRINKERS ARE EQUAL THEN NO PAIRS LEFT
        return 0
        
    else:
        while 1:
            if bride[0] in groom:  #CHECK IF FIRST ELEMENT OF BRIDE LIST PRESENT IN GROOM LIST
                groom.remove(bride[0])  #IF PRESENT REMOVE ONE OF SUCH ELEMENT
                bride.pop(0)  #AND DELETE THE FIRST ELEMNT OF BRIDE AND SEARCH A GROOM FOR THAT ELEMENT
            
            else:  #IF BRIDE ELEMENT NOT IN GROOM LIST BREAK THE LOOP
                break
                
        return(len(bride))  # RETURNING UNMATCHED PAIRS
    
    
n = int(input())  #NUMBER OF BRIDE AND GROOM
b = list(input().lower().rstrip())  #BRIDE STRING TO LIST
g = list(input().lower().rstrip())  #GROOM STRING TO LIST
print(bridegroom(n,b,g))  #PRINTING THE RESULT OF FUNCTION CALL

        
        
