chai_type = "Cardamom Chai "
customer_name = "Christian"

print(f"Order for {customer_name}: {chai_type} Please!")

chai_discription = "Aromatic & cardamom, ginger." 
print(f"First word: {chai_discription[::1]}")       #Full printing of the string
print(f"Second word: {chai_discription[::2]}")      #Every second character
print(f"Third word: {chai_discription[::3]}")       #Every third  character   

print(f"Last word: {chai_discription[::-1]}")    #Reversing the string

lable_txt = "Chai Special"
encoded_lable = lable_txt.encode("utf-8")       #Encoding the string into bytes using UTF-8 encoding scheme
print(f"Encoded label: {encoded_lable}")
decoded_lable = encoded_lable.decode("utf-8")   #Decoding the bytes back into a string using UTF-8 encoding scheme  
print(f"Decoded label: {decoded_lable}")

