#mycopi_instructions.py
from time import *
import mycopi_GPIO
import mycopi_convert
	
boards={0:['NOP','0'],1:['4 BIT INPUT','0'],4:['REGISTER A','0'],12:['DELAY','0'],2:['4 BIT OUTPUT','0'],10:['ANALOG IN 1','0'],5:['REGISTER B','0'],13:['ALU','0'],3:['PWM OUTPUT','0'],11:['ANALOG IN 2','0'],6:['REGISTER C','0'],14:['SKIP UNIT','0',],7:['REGISTER D','0'],8:['PAGE REGISTER','0'],9:['PROGRAM CNTR','0']}

def print_boards(boards):
	index=1
	while index<15:
		print("\n",boards[index])
		index+=1

def address_change(address,increment):
	address=int(mycopi_convert.hex_to_decimal(address))
	address+=increment
	if address>255:
		address=address%256
	address=mycopi_convert.hex_from_decimal(address)
	if len(address)<2:
		address='0'+address
	return address

def do(agenda,inst_now_inst,data,pulse):
	address=agenda[0]
	boards=agenda[1]
	
	if inst_now_inst=='0':#NOP
		address=address_change(address,1)
		print(boards[0],"new address: ",address,"\n")
	
	if inst_now_inst=='1':#OUT
		out=boards[2]
		out[1]=data
		mycopi_GPIO.out(data)		
		address=address_change(address,1)
		print(boards[2],"new address: ",address,"\n")
	
	if inst_now_inst=='2':#WAIT
		wait=boards[12]
		wait[1]=data
		boards[12]=wait
		address=address_change(address,1)
		print(boards[12],"new address: ",address,"\n")
		if data=='0':
			sleep(0)
		if data=='1':
			sleep(0.002)
		if data=='2':
			sleep(0.005)
		if data=='3':
			sleep(0.01)
		if data=='4':
			sleep(0.02)
		if data=='5':
			sleep(0.05)
		if data=='6':
			sleep(0.1)
		if data=='7':
			sleep(0.2)
		if data=='8':
			sleep(0.5)
		if data=='9':
			sleep(1)
		if data=='A':
			sleep(2)
		if data=='B':
			sleep(5)
		if data=='C':
			sleep(10)
		if data=='D':
			sleep(20)
		if data=='E':
			sleep(30)
		if data=='F':
			sleep(60)
#		print at start, so "wait" shows before waiting!
	
	if inst_now_inst=='3':#JUMP BACK n ADDRESSES
		value=mycopi_convert.hex_to_decimal(data)
		value=int(value)
		address=address_change(address,-value)
		print("jump back to: ",address,"\n")

	if inst_now_inst=='4':#LOAD REG_A WITH X
		reg_A=boards[4]
		reg_A_value=data
		reg_A[1]=reg_A_value
		boards[4]=reg_A
		address=address_change(address,1)
		print(boards[4],"new address: ",address,"\n")
		
	if inst_now_inst=='5':#COPY A TO...
		board_A_value=boards[4][1]
		if data=='0':#NOP
			display=boards[0]
		if data=='1':#B<-A
			boards[5][1]=board_A_value
			display=boards[5]
		if data=='2':#C<-A
			boards[6][1]=board_A_value
			display=boards[6]
		if data=='3':#D<-A
			boards[7][1]=board_A_value
			display=boards[7]
		if data=='4':#OUT<-A
			boards[2][1]=board_A_value
			mycopi_GPIO.out(board_A_value)
			display=boards[2]
		if data=='5':#D0<-A03
			binnum=mycopi_convert.bin_from_hex(board_A_value)
			digit=binnum[3]
			if digit=="1":
				mycopi_GPIO.out('i1')
			else:
				mycopi_GPIO.out('i0')
			display="D0="+digit
		if data=='6':#D1<-A0
			binnum=mycopi_convert.bin_from_hex(board_A_value)
			digit=binnum[3]
			if digit=="1":
				mycopi_GPIO.out('ii1')
			else:
				mycopi_GPIO.out('ii0')
			display="D1="+digit
		if data=='7':#D2<-A0
			binnum=mycopi_convert.bin_from_hex(board_A_value)
			digit=binnum[3]
			if digit=="1":
				mycopi_GPIO.out('iii1')
			else:
				mycopi_GPIO.out('iii0')
			display="D2="+digit
		if data=='8':#D3<-A0
			binnum=mycopi_convert.bin_from_hex(board_A_value)
			digit=binnum[3]
			if digit=="1":
				mycopi_GPIO.out('iv1')
			else:
				mycopi_GPIO.out('iv0')
			display="D3="+digit
		if data=='9':#PWM<-A
			boards[3][1]=board_A_value
			mycopi_GPIO.pwm(board_A_value)
			display=3
		address=address_change(address,1)
		print(display,"new address: ",address,"\n")

	if inst_now_inst=='6':#COPY X TO A
		if data=='1':
			value=boards[5][1]#A<-B
		if data=='2':
			value=boards[6][1]#A<-C
		if data=='3':
			value=boards[7][1]#A<-D
		if data=='4':
			value=mycopi_GPIO.DI()#A<-DI
		if data=='5':
			value=mycopi_GPIO.D0()#A<-D0
		if data=='6':
			value=mycopi_GPIO.D1()#A<-D1
		if data=='7':
			value=mycopi_GPIO.D2()#A<-D2
		if data=='8':
			value=mycopi_GPIO.D3()#A<-D3
		if data=='9':
			value=mycopi_GPIO.AD1()#A<-AD1
		if data=='A':
			value=mycopi_GPIO.AD2()#A<-AD2
		boards[4][1]=value
		address=address_change(address,1)
		print(boards[4],"new address: ",address,"\n")
			
	if inst_now_inst=='7':#ARITHMETIC/LOGIC
		reg_A_value=boards[4][1]
		reg_B_value=boards[5][1]
		if data=='1':#A+1
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_A_value+=1
			reg_A_value=reg_A_value%16
			reg_A_value=mycopi_convert.hex_from_decimal(reg_A_value)
		if data=='2':#A-1
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_A_value-=1
			reg_A_value=reg_A_value%16
			reg_A_value=mycopi_convert.hex_from_decimal(reg_A_value)	
		if data=='3':#A+B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			reg_A_value=reg_A_value+reg_B_value
			reg_A_value=reg_A_value%16
			reg_A_value=mycopi_convert.hex_from_decimal(reg_A_value)				
		if data=='4':#A-B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			reg_A_value=reg_A_value-reg_B_value
			reg_A_value=reg_A_value%16
			reg_A_value=mycopi_convert.hex_from_decimal(reg_A_value)		
		if data=='5':#A*B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			reg_A_value=reg_A_value*reg_B_value
			reg_A_value=reg_A_value%16
			reg_A_value=mycopi_convert.hex_from_decimal(reg_A_value)	
		if data=='6':#A/B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			reg_A_value=math.floor(reg_A_value/reg_B_value)
			reg_A_value=reg_A_value%16
			reg_A_value=mycopi_convert.hex_from_decimal(reg_A_value)	
		if data=='7':#AandB
			bin_A=mycopi_convert.bin_from_hex(reg_A_value)
			bin_B=mycopi_convert.bin_from_hex(reg_B_value)
			bin_out=''
			for i in range(0,4):
				if bin_A[i]=='1' and bin_B[i]=='1':
					bin_out+='1'
				else:
					bin_out+='0'
			reg_A_value=mycopi_convert.bin_to_hex(bin_out)
		if data=='8':#AorB
			bin_A=mycopi_convert.bin_from_hex(reg_A_value)
			bin_B=mycopi_convert.bin_from_hex(reg_B_value)
			bin_out=''
			for i in range(0,4):
				if bin_A[i]=='1' or bin_B[i]=='1':
					bin_out+='1'
				else:
					bin_out+='0'
			reg_A_value=mycopi_convert.bin_to_hex(bin_out)
		if data=='9':#AxorB
			bin_A=mycopi_convert.bin_from_hex(reg_A_value)
			bin_B=mycopi_convert.bin_from_hex(reg_B_value)
			bin_out=''
			for i in range(0,4):
				if bin_A[i]=='1' and bin_B[i]=='1':
					bin_out+='0'
				elif bin_A[i]=='1' or bin_B[i]=='1':
					bin_out+='1'
				else:
					bin_out+='0'
			reg_A_value=mycopi_convert.bin_to_hex(bin_out)		
		if data=='A':#AnotA
			bin_value=mycopi_convert.bin_from_hex(reg_A_value)
			inv_bin=''
			for i in bin_value:
				if i=='1':
					inv_bin+='0'
				else:
					inv_bin+='1'
			reg_A_value=mycopi_convert.bin_to_hex(inv_bin)
			
		boards[4][1]=reg_A_value
		address=address_change(address,1)
		print(boards[4],"new address: ",address,"\n")
		
	if inst_now_inst=='8':#PAGE REGISTER
		old_page=boards[8][1]
		boards[8][1]=data
		address=address_change(address,1)
		print(boards[8],"new address: ",address,"\n")
				
	if inst_now_inst=='9':#JUMP
		new_count=data
		boards[9][1]=new_count
		page=boards[8][1]
		address=page+new_count
		print(boards[8],boards[9],"jump to: ",address,"\n")
			
	if inst_now_inst=='A':#DECREMENT REG C (BOARD 6) BY 1, IF 0, GOTO NEXT, ELSE JUMP TO DATA
		reg_C_value=boards[6][1]
		reg_C_value=mycopi_convert.hex_to_decimal(reg_C_value)
		reg_C_value-=1
		reg_C_value=reg_C_value%16
		reg_C_value=mycopi_convert.hex_from_decimal(reg_C_value)
		boards[6][1]=reg_C_value
		if reg_C_value=='0':
			address=address_change(address,1)
			print(boards[6],"new address: ",address,"\n")	
		else:
			new_count=data
			boards[9][1]=new_count
			page=boards[8][1]
			address=page+new_count
			print(boards[6],boards[8],boards[9],"jump to: ",address,"\n")
			
	if inst_now_inst=='B':#DECREMENT REG D (BOARD 7), JUMP OR NEXT AS ABOVE
		reg_D_value=boards[7][1]
		reg_D_value=mycopi_convert.hex_to_decimal(reg_D_value)
		reg_D_value-=1
		reg_D_value=reg_D_value%16
		reg_D_value=mycopi_convert.hex_from_decimal(reg_D_value)
		boards[7][1]=reg_D_value
		count=boards[9][1]
		if reg_D_value=='0':
			address=address_change(address,1)
			print(boards[7],"new address: ",address,"\n")	
		else:
			new_count=data
			boards[9][1]=new_count
			page=boards[8][1]
			address=page+new_count
			print(boards[7],boards[8],boards[9],"jump to: ",address,"\n")

	if inst_now_inst=='C':#SKIP
		reg_A_value=boards[4][1]
		reg_B_value=boards[5][1]
		skip='0'
		if data=='O':
			data=data
		if data=='1':#A>B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			if reg_A_value>reg_B_value:
				skip='1'
		if data=='2':#A<B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			if reg_A_value<reg_B_value:
				skip='1'
		if data=='3':#A=B
			reg_A_value=mycopi_convert.hex_to_decimal(reg_A_value)
			reg_B_value=mycopi_convert.hex_to_decimal(reg_B_value)
			if reg_A_value==reg_B_value:
				skip='1'
		if data=='4':#D0=1
			value=mycopi_GPIO.D0()
			if value=='1':
				skip='1'
		if data=='5':#D1=1
			value=mycopi_GPIO.D1()
			if value=='1':
				skip='1'
		if data=='6':#D2=1
			value=mycopi_GPIO.D2()
			if value=='1':
				skip='1'		
		if data=='7':#D3='1'
			value=mycopi_GPIO.D3()
			if value=='1':
				skip='1'
		if data=='8':#D0=0
			value=mycopi_GPIO.D0()
			if value=='0':
				skip='1'
		if data=='9':#D1=0
			value=mycopi_GPIO.D1()
			if value=='0':
				skip='1'
		if data=='A':#D2=0
			value=mycopi_GPIO.D2()
			if value=='0':
				skip='1'
		if data=='B':#D3=0
			value=mycopi_GPIO.D3()
			if value=='0':
				skip='1'
		if data=='C':#S1=0
			value=mycopi_GPIO.S1()
			if value=='0':
				skip='1'	
		if data=='D':#S2=0
			value=mycopi_GPIO.S2()
			if value=='0':
				skip='1'
		if data=='E':#S1=1
			value=mycopi_GPIO.S1()
			if value=='1':
				skip='1'	
		if data=='F':#S2=1
			value=mycopi_GPIO.S2()
			if value=='1':
				skip='1'	
#		count=boards[9][1]
		if skip=='1':
			address=address_change(address,2)
		else:
			address=address_change(address,1)
		boards[14][1]=data
		print(boards[14],"skip?:",skip,"new address: ",address,"\n")

	if inst_now_inst=='D':#call subroutine
		global old_address
		old_address= address
		new_count=data
		boards[9][1]=new_count
		page=boards[8][1]
		address=page+new_count
		print(boards[8],boards[9],"jump to subroutine at: ",address,"\n")

	if inst_now_inst=='E':#return to old address+1 from subroutine
		address=address_change(old_address,1)
		print("return to: ",address,"\n")

	if inst_now_inst=='F':
		data=data	
	
	sleep(pulse)
	qef=[address,boards]
	return qef

