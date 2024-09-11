#taking a blank input string
ʙ = """ 			     			  	  		 	  	 		 			  			 	    	 	     	   	  	    	  				  	 		  	 	  	      			 			 		 				 			  	  		 		   		  	    	   	   	 	  	"""
length = 0   
def еval(str):
    return len(str)
def reverse(B):
    B = B.replace('  ', '0').replace('\n', '1')
    intermediate = ''.join([chr(int(byte, 2)) for byte in [ʙ.replace(' ', '0').replace('\t', '1')[i:i+8] for i in range(0, len(ʙ.replace(' ', '0').replace('\t', '1')), 8)]])
    eval(intermediate)
    if length <= 0:
        return B[::-1] 
    
    
    