'''
FUNC:M_1qh5_3_1_2_6
PDB:1qh5
EC:3.1.2.6
RESI:asp,zn,zn
LOCI:a-58,261,262;
'''
import motifFunctions as cmd
ASP_ZN = { 
	'distances':
		[[8.67], [7.19], [6.53], [6.92], [6.58], [5.29], [5.55], [4.28]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 8.67)], [('CG', 'ASP', 'ZN', 'ZN', 7.19)], [('OD1', 'ASP', 'ZN', 'ZN', 6.53)], [('OD2', 'ASP', 'ZN', 'ZN', 6.92)], [('CB', 'ASP', 'ZN', 'ZN', 6.58)], [('CG', 'ASP', 'ZN', 'ZN', 5.29)], [('OD1', 'ASP', 'ZN', 'ZN', 5.55)], [('OD2', 'ASP', 'ZN', 'ZN', 4.28)]]}
ZN_ZN = { 
	'distances':
		[5.46, 5.46],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 5.46), ('ZN', 'ZN', 'ZN', 'ZN', 5.46)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ZN, d, 'M_1qh5_3_1_2_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ZN_ZN, d, 'M_1qh5_3_1_2_6')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ZN' :  match1,
		'ZN_ZN' :  match2}