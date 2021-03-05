#mycopi_default_programme.py

import mycopi_convert

def address_plus_1(address):
	dec_address=int(address,16)
	dec_address+=1
	hex_address=hex(dec_address)
	address=hex_address[2:].upper()
	return address

def details():
	print("1110: ex.13: count")
	print("1101: ex.3: AD/PWM")
	print("1011: ex.4: random")
	print("0111: ex.16: stop on S1")
	print("0011: ex.33: start/stop")
	print("else: ex. 2 LED blink")
	
def starts():
	print("20: ex.1: 2 LED blink")
	print("25: ex.13: count")
	print("2A: ex.3: AD/PWM")
	print("30: ex.4: random")
	print("34: ex.16: stop on S1")
	print("40: ex.40: start/stop")
	print("80: ex.32: morse")
	print("A0: ex.36: combination lock(continues at B0)")
	 
	
def make_dict():
	short_code_0=['64','51','4E','80','C3','98','82','95','4D','80','C3','9E','82','9A','4B','81']
	short_code_1=['C3','94','83','90','47','81','C3','9A','83','94','43','82','C3','90','84','90']
	short_code_2=['11','28','18','28','34','71','54','59','26','34','69','54','59','26','34','FF']
	short_code_3=['54','CE','71','33','22','CC','32','40','22','71','54','CE','34','39','FF','FF']
	short_code_4=['86','D0','40','71','54','23','CD','34','D8','40','54','3B','FF','FF','FF','FF']
	short_code_5=['4F','93','45','53','19','11','21','19','11','21','19','11','20','B4','10','E0']
	short_code_6=['23','CE','32','23','CC','31','E0','FF','23','CF','32','23','CD','31','E0','FF']
	short_code_7=['CC','31','40','54','23','CE','32','CF','E0','CC','33','71','23','CC','31','3C']
	short_code_8=['8C','D2','26','D0','26','D0','26','D0','26','28','D2','26','D0','26','D0','26']#Morse: SR call changed from 85 to 8C, BK changed to JP
	short_code_9=['D2','30','FF','FF','FF','FF','FF','FF','FF','FF','FF','FF','FF','FF','FF','FF']#continuation of code_8
	short_code_A=['87','43','51','D0','C3','30','11','45','51','D0','C3','33','10','42','51','D0']#comb. lock
	short_code_B=['C3','30','17','4F','59','30','FF','FF','FF','FF','FF','FF','FF','FF','FF','FF']#continuation of code_A
	short_code_C=['4F','93','45','53','11','25','B4','10','E0','FF','FF','FF','FF','FF','FF','FF']#new version of Morse sub-routine
	code_list=[short_code_0,short_code_1,short_code_2,short_code_3,short_code_4,short_code_5,short_code_6,short_code_7,short_code_8,short_code_9,short_code_A,short_code_B,short_code_C]
		
	address='00'
	def_prog={}
	
	for i in code_list:
		code=i
		page=address[0]
		sub_address=address[1]
		for i in code:
			inst=i[0]
			data=i[1]
			def_prog[page+sub_address]=[inst,data]
			sub_address=address_plus_1(sub_address)	
		page=mycopi_convert.hex_to_decimal(page)
		page+=1
		page=mycopi_convert.hex_from_decimal(page)
		address=page+'0'
	return def_prog
