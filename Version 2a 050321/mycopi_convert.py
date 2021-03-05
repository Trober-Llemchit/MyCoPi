#mycopi_convert.py
import math

def hex_to_decimal(value):
	value=str(value)
	value=int(value,16)
	return value
		
def hex_from_decimal(value):
	value=hex(int(value))
	hex_value=value[2:].upper()
	return hex_value
	
def bin_to_decimal(value):
	value=str(value)
	value=int(value,2)
	return value
	
def bin_from_decimal(value):
	value=bin(int(value))
	bin_value=value[2:].upper()
	binnumlist=['0','0','0','0']
	for i in bin_value:
		binnumlist.append(i)
	while len(binnumlist)>4:
		binnumlist.remove(binnumlist[0])
	binnum=''
	for i in binnumlist:
		binnum+=i
	return binnum
	
def bin_from_hex(value):
	decnum=hex_to_decimal(value)
	binnum=bin_from_decimal(decnum)
	return binnum
	
def bin_to_hex(value):
	decnum=bin_to_decimal(value)
	hexnum=hex_from_decimal(decnum)
	return hexnum	

#decnum=input("dec_num: ")
#num=input("hex number: ")
#hexnum=hex_from_decimal(num)
#print("hexnum: ",hexnum)
#decnum=hex_to_decimal(hexnum)
#print(decnum)
#binnum=bin_from_decimal(decnum)
#print(binnum)
#decnum=bin_to_decimal(binnum)
#print(decnum)
#binnum=bin_from_hex(num)
#print(binnum)
