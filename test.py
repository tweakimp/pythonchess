a
# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

print (u' \u2654')
print (u' \u2655')
print (u' \u2656')
print (u' \u2657')
print (u' \u2658')
print (u' \u2659')
print (u' \u265A')
print (u' \u265B')
print (u' \u265C')
print (u' \u265D')
print (u' \u265E')
print (u' \u265F')
print (" ")
#print('\x1b[1;30;43m' + " " + u'\u265F'+ " " + '\x1b[0m')
#print('\x1b[0;30;47m' + " " + u'\u265F'+ " " + '\x1b[0m')
# print ('\x1b[1;32;40m' +"test" + u'\u265F'+"test"+'\x1b[0m')

print(u"\u001b[30;47m\u265F\u001b[0m")
print(u"\u001b[37;107m\u265F\u001b[0m")

print(u"\u001b[30;47m\u265F\u001b[37;40m\u265F\u001b[30;47m\u265F\u001b[37;40m\u265F\u001b[30;47m\u265F\u001b[37;40m\u265F\u001b[30;47m\u265F\u001b[37;40m\u265F\u001b[0m")
