# MyCoPi
This is an amateur's attempt to interpret on a Raspberry Pithe scheme in Juergen Pintaske's "Workbook - Coding/Executing Processor on Paper" (Oct 2020). It does not allow for programming input through buttons only. It does allow for bespoke programmes to be entered  numerically, and it displays changes to function blocks as they happen.

Version 2 (Mycopi2):
    • includes restart button;
    • all inputs (switches and buttons) pulled up;
    • more consistent terminal display.

HARDWARE SET-UP:

Allocation of GPIO pins is as per table below (and see programme module mycopi_GPIO.py). Apart from SDA/SCL, the choice of pins is not critical. They could be bunched up and will easily fit on a 26-pin Pi.

Board 1 (3.3V): 3.3V to input board //
Board 3 (SDA): to PCF8591 via pull-up //
Board 5 (SCL): ditto //
Board 9 (GND): to out board //
Board 11 (BCM 17): to out D0(1) //
Board 13 (BCM 27): to out D3(8) //
Board 21 (BCM 9): to in S1 //
Board 29 (BCM 5): to in D0(1) //
Board 31 (BCM 6): to in D1(2) //
Board 33 (BCM 13): to in D2(4) //
Board 35 (BCM 19):  to in D3(8) //

Board 2 (5V): to out buzzer //
Board 6 (GND): to input board //
Board 12 (BCM 18): to out D1(2) //
Board 16 (BCM 23): to out D2(4) //
Board 18 (BCM 24): to out PWM //
Board 22 (BCM 25): to in S2 //
Board 40 (BCM 21): to in RS (restart) //

Pi GPIO has internally programmed pull-up/pull-down resistors.

Input switches (x4) and input buttons (x2): JP specifies pull-up resistors on the inputs (e.g. p. 40, p.78); this means that switch "on" gives logic "0" which can be confusing. LED switch indicator is default off; if switched: LED is on but logic is "0".

In my set up, analogue input is through a version of the PCF8591 AD/DA converter which has onboard sensors including LDR (using channel 0, programmed as AD1); PCF8591 returns voltage across LDR whereas JP requires voltage across the  other resistor, so programme needs to reverse the reading ("reading=255-reading").  PCF8591 allows external input through channel 1, programmed as AD2; external reading can be taken across either part of circuit, so reversal not required. It may be better to use only external sensors - internal sensors on this board can be bypassed, allowing for 4 input channels (and these chips can be "daisy-chained" to allow further multiple inputs.)

Sound output (ex. 31) is "pseudo-piezo". I have used a simple active buzzer (operated through a transistor to allow 5V input to buzzer) which gives high frequency buzz for ex. 31 (but this would not work on a real passive piezo buzzer?). 

PYTHON

My programming could certainly be made more beautiful: I would welcome constructive criticism!

The Python programme can be viewed in a text editor but will not run without GPIOs (unless all the GPIO calls are commented out).

The programme is organised in modules. The functions stored in a module are made available to another module by importing it.

The modules are:
- mycopi.py: the "main" programme; it is the only module which needs to be explicitly run;
- mycopi_instructions.py: implements each instruction by reference to instruction+data, updates board variables and advances address;
- mycopi_GPIO.py: sets up the GPIO pins (in/out/PWM, up/down, clock/data for I2C), controls output on basis of board 2/3 output, manages input for AD1/2, D.in 1-4;
- mycopi_convert.py: converts hex to/from decimal, and binary to/from decimal for purposes of address change and arithmetic operations;
- mycopi_stored_progs.py: lists most of JP's examples as separate "dictionaries"; each instruction pair (instruction+data) is indexed by reference to a dictionary key which is the programme address;
- mycopi_default_programme.py: specifies default code as a collection of lists comprising instruction pairs, provides for those lists to be complied into a dictionary, and allows for access either through D.in1-4, or by specifying start address.

When mycopi.py is run:
- other modules are imported, including the built-in "time" module which is used for sleep instructions;
- there is an input request for "change pulse": set as default "0" but this can be increased to slow the programme down to see what is happening; (the pulse variable is used in mycopi_instructions.py);
- the boards are set up as a dictionary of variables; each board is indexed with a key which is the board number; the variable comprises the name of the board plus the current value, initially all set to "0"; (JP calls these "function blocks" - my naming could be changed, but "function" has a special meaning in Python);
- the programme then prints (displays in the terminal) the list of boards, each with its initial zero value;
- there is an input request to choose "d": default programme, "c": choose an example, or "e": enter a list of instructions in the form of successive instruction pairs (instruction+data) which are then compiled into a dictionary;
- for "c" and "e", the initial programme list is displayed in the terminal;
- as the programme runs, the terminal displays (see screenshot):
  - instruction;
  - status of amended boards plus new address;
- the programme continues until the reset button is pressed which returns to the "choose d/c/e" input request; (reset could be adjusted to return to a different place in the programme);
-"ctrl+C" terminates the whole programme, kills the GPIOs (important) and closes the terminal.

PROGRAMME COUNTER ("PC") & PAGE REGISTER ("PR")

JP explains these on pp. 16, 18-19.

I can understand that, for more than 16 lines of code, we need a 2-digit hexadecimal address. This might be achieved using the Programme Counter to record the right-hand digit and the Page Register to record the left-hand digit. But this would require a change to the PR on every page turn.

In fact, the PR  and PC are only used to record the address required for a jump or subroutine instruction. 

So the working address is recorded as a separate variable independently of the function blocks. (And a separate global variable is needed to record the old address for return from a subroutine.)

EXAMPLES

Ex. 23: "simple RS flip-flop": using input switches with default value "1" is extremely confusing. Also, input for a flip-flop is more commonly instantaneous (push-button) rather than continuous (switched). I have adapted the programme to use the buttons (S1 and S2) instead of the switches, so:
- no buttons pushed: output change instructions skipped, so no change;
- S1 pushed: gives "set": 0001;
- S2 pushed: gives "reset: "1000";
- both pushed: not allowed.

Ex. 29: "voltage follower": hardware set-up and/or GPIO processing needs some adjustment to make this work.

Ex. 30: "LED dimmer": S2 brightens; S1 dims.

Ex. 32: "morse": I have added the sound output routine to stored programme 32 which gives very fast pseudo-piezo output. (cf adapted version in default programme.)

Ex. 35: "input a number": first button push enters "0"; cf ex. 27.

Ex. 36: "combination lock": not sure how the LEDs can be used to record success when also used to show input number; utility of combination lock hugely reduced if you can get separate feedback for each digit!

Ex. 40: "whack a mole": needs some more hardware - would it be possible to make the mole squeak when hit??

PRE-PROGRAMMED SAMPLE CODE (JP 133ff)

See mycopi_default_programme.py.

The subroutines at address 50 (p. 138: sound output for morse) and address 70 (p. 140: input a number for combination lock) are not called in JP's default code.

I have added:
- at address 80: main code for morse (with output initials upgraded);
- at address C0: simplified subroutine for morse, using active buzzer (and longer dashes for clarity);
- at address A0: main code for combination lock.

We will soon need a 3-digit address!

RJM - Mar. 2021.
