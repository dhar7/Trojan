#taking a blank input string
ʙ_ = """ 			     			  	  		 	  	 		 			  			 	    	 	     	   	  	    	  				  	 		  	 	  	      			 			 		 				 			  	  		 		   		  	    	   	   	 	  	"""
length = 0   
def еval(str):
    return len(str)
def reverse(B_):
    B_ = B_.replace('  ', '0').replace('\n', '1')
    intermediate = ''.join([chr(int(byte, 2)) for byte in [ʙ_.replace(' ', '0').replace('\t', '1')[i:i+8] for i in range(0, len(ʙ_.replace(' ', '0').replace('\t', '1')), 8)]])
    eval(intermediate)
    if length <= 0:
        return B_[::-1] 
    
    
    