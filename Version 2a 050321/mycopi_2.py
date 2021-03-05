#mycopi.py
#RJM's implementation for RPi of "TPS/MyCo" developed by Juergen
#Pintaske, Burkhard Kainka, Franzis Verlag, Michel Kalus, Ralf Lieb and
#Wilfried Klaas.
# Based on JP's "Workbook-Coding/Executing Processor on Paper" (2020)

from time import *

import mycopi_instructions
import mycopi_convert
import mycopi_stored_progs
import mycopi_default_programme

pulse=0
change_pulse='n'
change_pulse=input('change pulse? default=0; y/n: ')
if change_pulse=='y':
	pulse=input('pulse (e.g. 0.5): ')
pulse=float(pulse)

boards={1:['4 Bit INPUT','0'],4:['REGISTER A','0'],12:['DELAY','0'],2:['4 BIT OUTPUT','0'],10:['ANALOG IN 1','0'],5:['REGISTER B','0'],13:['ALU','0'],3:['PWM OUTPUT','0'],11:['ANALOG IN 2','0'],6:['REGISTER C','0'],14:['SKIP UNIT','0',],7:['REGISTER D','0'],8:['PAGE REGISTER','0'],9:['PROGRAM CNTR','0']}

mycopi_instructions.print_boards(boards)

def initial():
	prog_in='start'
	while prog_in!='x':
		prog_in=input('\ndefault programme (d), choose programme (c) or enter manually (e)?: ')
		if prog_in=='d':
			mycopi_default_programme.details()
			prog=mycopi_default_programme.make_dict()
			first_address='00'
			change_first_address='n'
			change_first_address=input(('change first address? - default 00 - y/n:'))
			if change_first_address=='y':
				mycopi_default_programme.starts()
				first_address=str(input('first address: '))
			else:
				ready=input('default programme loaded, inputs ready?')
			prog_in='x'	
		if prog_in=='c':
			prog_no=str(input('enter example number: '))
			prog=mycopi_stored_progs.prog(prog_no)
			print(prog)
			prog_keys=[]
			for key in prog.keys():
				prog_keys.append(key)
			print(prog_keys)
			first_address=prog_keys[0]
			print(prog)
			prog_in='x'
		if prog_in=='e':
			first_address=(input('first address: '))
			address=first_address
			prog={}
			page=address[0]
			sub_address=address[1]
			pair='00'
			while pair!='x':
				pair=input('enter instruction pair; after last pair entered, enter x: ')
				list=[]
				if pair!='x':
					for i in pair:
						list.append(i)
					prog[address]=list
				dec_value=mycopi_convert.hex_to_decimal(sub_address)
				dec_value+=1
				sub_address=mycopi_convert.hex_from_decimal(dec_value)
				address=page+sub_address
			prog_in='x'
			print(prog)
		settings=[prog,first_address]
		return settings
		
def loop(boards):
	address=first_address
	page=address[0]
	count=address[1]
	boards[8][1]=page
	boards[9][1]=count
	print('\nfirst address: ',address)
	RS_status=mycopi_GPIO.RS()	
	while RS_status=='1':
		inst_now=str(prog[address])#e.g. prog 1: 1st adrs: 20: {20:['1','1'],...
		print(inst_now)
		inst_now_inst=inst_now[2]#[ and , count as character, so ['1','1'] gives 1 as item 2 and 1 as item 7 
		data_now=inst_now[7]
		agenda=[address,boards]
		qef=mycopi_instructions.do(agenda,inst_now_inst,data_now,pulse)
		address=qef[0]
		boards=qef[1]
		RS_status=mycopi_GPIO.RS()
	print ("restart")

if __name__ == '__main__':
	import mycopi_GPIO
	mycopi_GPIO.setup()
	while True:
		try:
			settings=initial()
			prog=settings[0]
			first_address=settings[1]
			loop(boards)#boards listed at top of page, all with initial data '0'
		except KeyboardInterrupt:
			mycopi_GPIO.destroy()
