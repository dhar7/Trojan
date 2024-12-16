# encoder.py
def encode_script_to_whitespace(content):
    #with open(script_path, 'r') as file:
    #    content = file.read()
    
    # Convert each character to its 8-bit binary representation
    binary_content = ''.join(format(ord(char), '08b') for char in content)
    
    # Replace '0' with a space and '1' with a tab
    whitespace_encoded = binary_content.replace('0', ' ').replace('1', '\t')
    
    return whitespace_encoded,binary_content

def decode(encoded_content):
    intermediate = ''.join([chr(int(byte, 2)) for byte in [encoded_content.replace(' ', '0').replace('\t', '1')[i:i+8] for i in range(0, len(encoded_content.replace(' ', '0').replace('\t', '1')), 8)]])
    return intermediate

# Save the encoded script to a file
encoded_content, binary_content = encode_script_to_whitespace('argha')

with open('encoded_script.txt', 'w') as file:
    file.write(encoded_content)
    
original = decode(" 		    	 			  	  		  			 		 	    		    	")    
    
print ("Encoded: ",encoded_content)
print ("Binary: ",binary_content)
print ("Binary: ",original)