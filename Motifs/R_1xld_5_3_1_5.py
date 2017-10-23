'''
FUNC:R_1xld_5_3_1_5
PDB:1xld
EC:5.3.1.5
RESI:mn,mn
LOCI:a-398,399;
'''
import motifFunctions as cmd
MN_MN = { 
	'distances':
		[6.68, 6.68],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 6.68), ('MN', 'MN', 'MN', 'MN', 6.68)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MN_MN, d, 'R_1xld_5_3_1_5')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MN_MN' :  match1}