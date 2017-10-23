'''
FUNC:M_1ah7_3_1_4_3
PDB:1ah7
EC:3.1.4.3
RESI:asp,zn,zn,zn
LOCI:a-55,246,247,248;
'''
import motifFunctions as cmd
ASP_ZN = { 
	'distances':
		[[6.65], [5.3], [4.29], [5.57], [10.33], [9.03], [8.83], [8.37], [8.45], [7.02], [6.83], [6.25]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 6.65)], [('CG', 'ASP', 'ZN', 'ZN', 5.3)], [('OD1', 'ASP', 'ZN', 'ZN', 4.29)], [('OD2', 'ASP', 'ZN', 'ZN', 5.57)], [('CB', 'ASP', 'ZN', 'ZN', 10.33)], [('CG', 'ASP', 'ZN', 'ZN', 9.03)], [('OD1', 'ASP', 'ZN', 'ZN', 8.83)], [('OD2', 'ASP', 'ZN', 'ZN', 8.37)], [('CB', 'ASP', 'ZN', 'ZN', 8.45)], [('CG', 'ASP', 'ZN', 'ZN', 7.02)], [('OD1', 'ASP', 'ZN', 'ZN', 6.83)], [('OD2', 'ASP', 'ZN', 'ZN', 6.25)]]}
ZN_ZNI = { 
	'distances':
		[6.58],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZNI', 6.58)]}
ZN_ZN = { 
	'distances':
		[8.12, 5.59, 8.12, 6.58, 5.59],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 8.12), ('ZN', 'ZN', 'ZN', 'ZN', 5.59), ('ZN', 'ZN', 'ZN', 'ZN', 8.12), ('ZN', 'ZN', 'ZN', 'ZN', 6.58), ('ZN', 'ZN', 'ZN', 'ZN', 5.59)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ZN, d, 'M_1ah7_3_1_4_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ZN_ZNI, d, 'M_1ah7_3_1_4_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ZN_ZN, d, 'M_1ah7_3_1_4_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ZN' :  match1,
		'ZN_ZNI' :  match2,
		'ZN_ZN' :  match3}