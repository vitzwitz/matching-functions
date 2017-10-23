'''
FUNC:M_1sml_3_5_2_6
PDB:1sml
EC:3.5.2.6
RESI:tyr,zn,zn
LOCI:a-191,270,271;
'''
import motifFunctions as cmd
TYR_ZN = { 
	'distances':
		[[14.95], [13.58], [12.75], [13.29], [11.54], [12.13], [11.2], [10.15], [12.61], [11.13], [10.37], [10.68], [9.03], [9.38], [8.46], [7.21]],
	'comparisons':
		[[('CB', 'TYR', 'ZN', 'ZN', 14.95)], [('CG', 'TYR', 'ZN', 'ZN', 13.58)], [('CD1', 'TYR', 'ZN', 'ZN', 12.75)], [('CD2', 'TYR', 'ZN', 'ZN', 13.29)], [('CE1', 'TYR', 'ZN', 'ZN', 11.54)], [('CE2', 'TYR', 'ZN', 'ZN', 12.13)], [('CZ', 'TYR', 'ZN', 'ZN', 11.2)], [('OH', 'TYR', 'ZN', 'ZN', 10.15)], [('CB', 'TYR', 'ZN', 'ZN', 12.61)], [('CG', 'TYR', 'ZN', 'ZN', 11.13)], [('CD1', 'TYR', 'ZN', 'ZN', 10.37)], [('CD2', 'TYR', 'ZN', 'ZN', 10.68)], [('CE1', 'TYR', 'ZN', 'ZN', 9.03)], [('CE2', 'TYR', 'ZN', 'ZN', 9.38)], [('CZ', 'TYR', 'ZN', 'ZN', 8.46)], [('OH', 'TYR', 'ZN', 'ZN', 7.21)]]}
ZN_ZN = { 
	'distances':
		[5.46, 5.46],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 5.46), ('ZN', 'ZN', 'ZN', 'ZN', 5.46)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ZN, d, 'M_1sml_3_5_2_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ZN_ZN, d, 'M_1sml_3_5_2_6')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ZN' :  match1,
		'ZN_ZN' :  match2}