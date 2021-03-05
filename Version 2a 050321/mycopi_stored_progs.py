#mycopi_stored_progs.py

def prog(prog_no):
	if prog_no=='1':
		print("\n1: 2 flashing LEDs")
		prog={'20':['1','1'],'21':['2','8'],'22':['1','8'],'23':['2','8'],'24':['3','4']}
	if prog_no=='2':
		print("\n2: binary counter + PWM")
		prog={'25':['7','1'],'26':['5','4'],'27':['5','9'],'28':['2','A'],'29':['3','4']}
	if prog_no=='3':
		print("\n3: AD inut, PWM output")
		prog={'2A':['6','9'],'2B':['5','4'],'2C':['5','9'],'2D':['2','A'],'2E':['3','4']}
	if prog_no=='4':
		print("\n4: random numbers")
		prog={'30':['5','4'],'31':['C','E'],'32':['7','1'],'33':['3','3']}
	if prog_no=='5':
		print("\n5: measuring time")
		prog={'34':['2','2'],'35':['C','C'],'36':['3','2'],'37':['4','0'],'38':['2','2'],'39':['7','1'],'3A':['5','4'],'3B':['C','E'],'3C':['3','4'],'3D':['3','9']}
	if prog_no=='6':
		print("\n6: USE DEFAULT CODE")
		prog={'00':['2','F'],'01':['3','1']}
	if prog_no=='7':
		print("\n7: switch on LEDs")
		prog={'00':['1','7'],'01':['3','0']}
	if prog_no=='8':
		print("\n8: USE DEFAULT CODE")
		prog={'00':['2','F'],'01':['3','1']}
	if prog_no=='9':
		print("\n9: flashing LEDs")
		prog={'00':['1','1'],'01':['2','7'],'02':['1','4'],'03':['2','7'],'04':['3','4']}
	if prog_no=='10':
		print("\n10: running light 1")
		prog={'00':['1','1'],'01':['2','8'],'02':['1','2'],'03':['2','8'],'04':['1','4'],'05':['2','8'],'06':['1','8'],'07':['2','8'],'08':['3','8']}
	if prog_no=='11':
		print("\n11: running light 2")
		prog={'00':['1','1'],'01':['2','8'],'02':['1','2'],'03':['2','8'],'04':['1','4'],'05':['2','8'],'06':['1','8'],'07':['2','8'],'08':['1','4'],'09':['2','8'],'0A':['1','2'],'0B':['2','8'],'0C':['3','C']}
	if prog_no=='12':
		print("\n12: timer for one minute")
		prog={'00':['1','F'],'01':['2','F'],'02':['1','0'],'03':['3','0']}
	if prog_no=='13':
		print("\n13: counter programme")
		prog={'00':['4','0'],'01':['7','1'],'02':['5','4'],'03':['5','9'],'04':['2','6'],'05':['3','4']}
	if prog_no=='14':
		print("\n14: inverting data")
		prog={'00':['6','9'],'01':['5','4'],'02':['7','A'],'03':['5','9'],'04':['2','6'],'05':['3','5']}
	if prog_no=='15':
		print("\n15: reaction test on S1")
		prog={'00':['C','C'],'01':['3','1'],'02':['4','0'],'03':['7','1'],'04':['5','4'],'05':['C','E'],'06':['3','3'],'07':['3','7']}
	if prog_no=='16':
		print("\n16: USE DEFAULT CODE")
		prog={'00':['2','F'],'01':['3','1']}
	if prog_no=='17':
		print("\n17: a counter loop")
		prog={'00':['4','5'],'01':['5','2'],'02':['1','5'],'03':['2','8'],'04':['1','A'],'05':['2','8'],'06':['8','0'],'07':['A','2'],'08':['3','0']}
	if prog_no=='18':
		print("\n18: flash LED x5")
		prog={'00':['4','5'],'01':['5','2'],'02':['8','0'],'03':['A','5'],'04':['3','0'],'05':['1','5'],'06':['2','8'],'07':['1','A'],'08':['2','8'],'09':['3','6']}
	if prog_no=='19':
		print("\n19: twilight switch")
		prog={'00':['4','5'],'01':['5','1'],'02':['8','0'],'03':['6','9'],'04':['C','2'],'05':['9','8'],'06':['1','F'],'07':['3','4'],'08':['1','0'],'09':['3','6']}
	if prog_no=='20':
		print("\n20: single bit test")
		prog={'00':['6','7'],'01':['5','4'],'02':['2','1'],'03':['3','3']}
	if prog_no=='21':
		print("\n21: flashing bit A3")
		prog={'00':['7','1'],'01':['5','7'],'02':['2','8'],'03':['3','3']}
	if prog_no=='22':
		print("\n22: bit invert and to out")
		prog={'00':['6','7'],'01':['7','A'],'02':['5','8'],'03':['3','3']}
	if prog_no=='23':
		print("\n23: simple RS flip-flop")
		prog={'00':['C','E'],'01':['1','1'],'02':['C','F'],'03':['1','8'],'04':['3','4']}
	if prog_no=='24':
		print("\n24: logic AND function")
		prog={'00':['6','4'],'01':['5','1'],'02':['4','3'],'03':['7','7'],'04':['5','4'],'05':['3','5']}
	if prog_no=='25':
		print("\n25: main prog plus sub")
		prog={'00':['8','0'],'01':['D','8'],'02':['5','4'],'03':['2','9'],'04':['D','8'],'05':['5','4'],'06':['2','8'],'07':['3','7'],'08':['7','2'],'09':['E','0']}
	if prog_no=='26':
		print("\n26: sub for 25: RUN EG 25")
		prog={'00':['2','F'],'01':['3','1']}		
	if prog_no=='27':
		print("\n27: counter using S1")
		prog={'00':['4','0'],'01':['5','4'],'02':['7','1'],'03':['8','6'],'04':['D','0'],'05':['3','4'],'60':['2','3'],'61':['C','E'],'62':['3','2'],'63':['2','3'],'64':['C','C'],'65':['3','1'],'66':['E','0']}
	if prog_no=='28':
		print("\n28: twilight with hysteresis")
		prog={'00':['1','0'],'01':['4','5'],'02':['5','1'],'03':['6','9'],'04':['C','2'],'05':['1','0'],'06':['4','9'],'07':['5','1'],'08':['6','9'],'09':['C','1'],'0A':['1','F'],'0B':['3','A']}
	if prog_no=='29':
		print("\n29: volage folower loop")
		prog={'00':['6','9'],'01':['5','1'],'02':['8','0'],'03':['6','A'],'04':['C','1'],'05':['9','8'],'06':['1','0'],'07':['3','7'],'08':['1','8'],'09':['3','9']}
	if prog_no=='30':
		print("\n30: LED dimmer, S1/S2")
		prog={'00':['8','0'],'01':['5','9'],'02':['2','7'],'03':['5','2'],'04':['4','F'],'05':['5','1'],'06':['6','2'],'07':['C','2'],'08':['9','B'],'09':['C','F'],'0A':['7','1'],'0B':['5','2'],'0C':['4','0'],'0D':['5','1'],'0E':['6','2'],'0F':['C','1'],'10':['9','0'],'11':['C','E'],'12':['7','2'],'13':['9','0']}
	if prog_no=='31':
		print("\n31: sound output")
		prog={'00':['8','0'],'01':['4','F'],'02':['9','4'],'03':['4','5'],'04':['5','3'],'05':['1','1'],'06':['1','0'],'07':['2','1'],'08':['1','1'],'09':['1','0'],'0A':['2','1'],'0B':['1','1'],'0C':['1','0'],'0D':['2','0'],'0E':['B','5'],'0F':['3','0']}
	if prog_no=='32':
		print("\n32: output Morse code")
		prog={'00':['8','5'],'01':['D','0'],'02':['2','6'],'03':['D','2'],'04':['2','6'],'05':['D','2'],'06':['2','6'],'07':['D','2'],'08':['2','6'],'09':['2','7'],'0A':['D','0'],'0B':['2','6'],'0C':['D','2'],'0D':['2','6'],'0E':['D','0'],'0F':['3','0' ],'50':['4','F'],'51':['9','3'],'52':['4','5'],'53':['5','3'],'54':['1','1'],'55':['1','0'],'56':['2','1'],'57':['1','1'],'58':['1','0'],'59':['2','1'],'5A':['1','1'],'5B':['1','0'],'5C':['2','0'],'5D':['B','4'],'5E':['1','0'],'5F':['E','0']}
	if prog_no=='33':
		print("\n33: start stop timer +33a: sub")
		prog={'00':['8','6'],'01':['D','0'],'02':['4','0'],'03':['7','1'],'04':['5','4'],'05':['2','9'],'06':['C','D'],'07':['3','4'],'08':['D','8'],'09':['4','0'],'0A':['5','4'],'0B':['3','B'],'60':['2','3'],'61':['C','E'],'62':['3','2'],'63':['2','3'],'64':['C','C'],'65':['3','1'],'66':['E','0'],'67':['F','F'],'68':['2','3'],'69':['C','F'],'6A':['3','2'],'6B':['2','3'],'6C':['C','D'],'6D':['3','1'],'6E':['E','0'],'6F':['F','F']}
	if prog_no=='34':
		print("\n34: jump to pre-programmed stopwatch code - USE DEFAULT CODE")
		prog={'00':['2','F'],'01':['3','1']}
	if prog_no=='35':
		print("\n35: input a number")
		prog={'00':['C','C'],'01':['3','1'],'02':['4','0'],'03':['5','4'],'04':['2','3'],'05':['C','E'],'06':['3','2'],'07':['C','F'],'08':['3','0'],'09':['C','C'],'0A':['3','3'],'0B':['7','1'],'0C':['2','3'],'0D':['C','C'],'0E':['3','1'],'0F':['3','C']}
	if prog_no=='36':
		print("\n36: combination lock+36a:sub")
		prog={'00':['8','7'],'01':['4','3'],'02':['5','1'],'03':['D','0'],'04':['C','3'],'05':['3','0'],'06':['1','0'],'07':['4','5'],'08':['5','1'],'09':['D','0'],'0A':['C','3'],'0B':['3','0'],'0C':['1','0'],'0D':['4','2'],'0E':['5','1'],'0F':['D','0'],'10':['C','3'],'11':['3','0'],'12':['1','0'],'13':['4','F'],'14':['5','9'],'15':['3','0'],'70':['C','C'],'71':['3','1'],'72':['4','0'],'73':['5','4'],'74':['2','3'],'75':['C','E'],'76':['3','2'],'77':['C','F'],'78':['E','0'],'79':['C','C'],'7A':['3','3'],'7B':['7','1'],'7C':['2','3'],'7D':['C','C'],'7E':['3','1'],'7F':['3','C']}
	if prog_no=='37':
		print("\n37: throwing dice")
		prog={'00':['4','7'],'01':['5','1'],'02':['4','1'],'03':['C','2'],'04':['4','1'],'05':['5','4'],'06':['C','E'],'07':['7','1'],'08':['3','5']}
	if prog_no=='38':
		print("\n38: reaction test")
		prog={'00':['4','0'],'01':['5','4'],'02':['2','5'],'03':['7','1'],'04':['C','C'],'05':['3','4'],'06':['7','1'],'07':['C','E'],'08':['3','2'],'09':['5','2'],'0A':['1','0'],'0B':['2','6'],'0C':['A','B'],'0D':['2','9'],'0E':['3','E']}
	if prog_no=='39':
		print("\n39: ping pong")
		prog={'00':['1','1'],'01':['2','7'],'02':['C','D'],'03':['3','1'],'04':['1','2'],'05':['2','7'],'06':['1','4'],'07':['2','7'],'08':['C','E'],'09':['3','1'],'0A':['1','8'],'0B':['2','7'],'0C':['C','C'],'0D':['3','1'],'0E':['1','4'],'0F':['2','7'],'10':['1','2'],'11':['2','7'],'12':['C','F'],'13':['3','1'],'14':['8','0'],'15':['9','0']}
	if prog_no=='40':
		print("\n40: whack a mole")
		prog={'00':['4','1'],'01':['C','E'],'02':['9','D'],'03':['4','2'],'04':['C','E'],'05':['9','D'],'06':['4','4'],'07':['C','E'],'08':['9','D'],'09':['4','8'],'0A':['C','E'],'0B':['9','D'],'0C':['3','C'],'0D':['2','8'],'0E':['5','4'],'0F':['2','8'],'10':['2','7'],'11':['5','1'],'12':['6','4'],'13':['7','A'],'14':['C','3'],'15':['2','A'],'16':['1','0'],'17':['8','0'],'18':['9','0']}
	return prog