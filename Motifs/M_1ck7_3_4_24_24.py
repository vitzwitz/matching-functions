'''
FUNC:M_1ck7_3_4_24_24
PDB:1ck7
EC:3.4.24.24
RESI:ala,zn
LOCI:a-404,990;
'''
import motifFunctions as cmd
ALA_ZN = { 
	'distances':
		[8.69],
	'comparisons':
		[('CB', 'ALA', 'ZN', 'ZN', 8.69)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ALA_ZN, d, 'M_1ck7_3_4_24_24')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ALA_ZN' :  match1}