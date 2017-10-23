'''
FUNC:M_1ti6_1_97_1_2
PDB:1ti6
EC:1.97.1.2
RESI:his,asp,tyr,4mo
LOCI:a-144,174,404,903;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[12.05, 11.07, 11.43, 9.8, 10.5, 9.41], [10.84, 9.84, 10.13, 8.64, 9.21, 8.2], [10.73, 9.6, 9.68, 8.44, 8.64, 7.76], [10.16, 9.33, 9.75, 8.18, 8.99, 7.95]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 12.05), ('CB', 'ASP', 'CG', 'HIS', 11.07), ('CB', 'ASP', 'ND1', 'HIS', 11.43), ('CB', 'ASP', 'CD2', 'HIS', 9.8), ('CB', 'ASP', 'CE1', 'HIS', 10.5), ('CB', 'ASP', 'NE2', 'HIS', 9.41)], [('CG', 'ASP', 'CB', 'HIS', 10.84), ('CG', 'ASP', 'CG', 'HIS', 9.84), ('CG', 'ASP', 'ND1', 'HIS', 10.13), ('CG', 'ASP', 'CD2', 'HIS', 8.64), ('CG', 'ASP', 'CE1', 'HIS', 9.21), ('CG', 'ASP', 'NE2', 'HIS', 8.2)], [('OD1', 'ASP', 'CB', 'HIS', 10.73), ('OD1', 'ASP', 'CG', 'HIS', 9.6), ('OD1', 'ASP', 'ND1', 'HIS', 9.68), ('OD1', 'ASP', 'CD2', 'HIS', 8.44), ('OD1', 'ASP', 'CE1', 'HIS', 8.64), ('OD1', 'ASP', 'NE2', 'HIS', 7.76)], [('OD2', 'ASP', 'CB', 'HIS', 10.16), ('OD2', 'ASP', 'CG', 'HIS', 9.33), ('OD2', 'ASP', 'ND1', 'HIS', 9.75), ('OD2', 'ASP', 'CD2', 'HIS', 8.18), ('OD2', 'ASP', 'CE1', 'HIS', 8.99), ('OD2', 'ASP', 'NE2', 'HIS', 7.95)]]}
HIS_4MO = { 
	'distances':
		[[9.27], [7.9], [7.91], [6.69], [6.78], [5.85]],
	'comparisons':
		[[('CB', 'HIS', 'MO', '4MO', 9.27)], [('CG', 'HIS', 'MO', '4MO', 7.9)], [('ND1', 'HIS', 'MO', '4MO', 7.91)], [('CD2', 'HIS', 'MO', '4MO', 6.69)], [('CE1', 'HIS', 'MO', '4MO', 6.78)], [('NE2', 'HIS', 'MO', '4MO', 5.85)]]}
TYR_ASP = { 
	'distances':
		[[18.64, 17.14, 16.4, 16.77], [17.25, 15.76, 14.99, 15.44], [16.2, 14.69, 13.93, 14.37], [17.1, 15.64, 14.84, 15.37], [14.92, 13.43, 12.63, 13.16], [15.91, 14.47, 13.64, 14.27], [14.77, 13.31, 12.48, 13.11], [13.6, 12.18, 11.3, 12.06]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 18.64), ('CB', 'TYR', 'CG', 'ASP', 17.14), ('CB', 'TYR', 'OD1', 'ASP', 16.4), ('CB', 'TYR', 'OD2', 'ASP', 16.77)], [('CG', 'TYR', 'CB', 'ASP', 17.25), ('CG', 'TYR', 'CG', 'ASP', 15.76), ('CG', 'TYR', 'OD1', 'ASP', 14.99), ('CG', 'TYR', 'OD2', 'ASP', 15.44)], [('CD1', 'TYR', 'CB', 'ASP', 16.2), ('CD1', 'TYR', 'CG', 'ASP', 14.69), ('CD1', 'TYR', 'OD1', 'ASP', 13.93), ('CD1', 'TYR', 'OD2', 'ASP', 14.37)], [('CD2', 'TYR', 'CB', 'ASP', 17.1), ('CD2', 'TYR', 'CG', 'ASP', 15.64), ('CD2', 'TYR', 'OD1', 'ASP', 14.84), ('CD2', 'TYR', 'OD2', 'ASP', 15.37)], [('CE1', 'TYR', 'CB', 'ASP', 14.92), ('CE1', 'TYR', 'CG', 'ASP', 13.43), ('CE1', 'TYR', 'OD1', 'ASP', 12.63), ('CE1', 'TYR', 'OD2', 'ASP', 13.16)], [('CE2', 'TYR', 'CB', 'ASP', 15.91), ('CE2', 'TYR', 'CG', 'ASP', 14.47), ('CE2', 'TYR', 'OD1', 'ASP', 13.64), ('CE2', 'TYR', 'OD2', 'ASP', 14.27)], [('CZ', 'TYR', 'CB', 'ASP', 14.77), ('CZ', 'TYR', 'CG', 'ASP', 13.31), ('CZ', 'TYR', 'OD1', 'ASP', 12.48), ('CZ', 'TYR', 'OD2', 'ASP', 13.11)], [('OH', 'TYR', 'CB', 'ASP', 13.6), ('OH', 'TYR', 'CG', 'ASP', 12.18), ('OH', 'TYR', 'OD1', 'ASP', 11.3), ('OH', 'TYR', 'OD2', 'ASP', 12.06)]]}
TYR_HIS = { 
	'distances':
		[[12.22, 12.22, 11.19, 13.2, 11.63, 12.84], [11.09, 10.95, 9.85, 11.86, 10.2, 11.42], [10.74, 10.52, 9.45, 11.32, 9.68, 10.82], [10.61, 10.4, 9.23, 11.34, 9.6, 10.88], [9.91, 9.5, 8.37, 10.19, 8.45, 9.58], [9.76, 9.36, 8.11, 10.22, 8.36, 9.65], [9.38, 8.87, 7.62, 9.58, 7.7, 8.93], [8.81, 8.06, 6.75, 8.61, 6.59, 7.8]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 12.22), ('CB', 'TYR', 'CG', 'HIS', 12.22), ('CB', 'TYR', 'ND1', 'HIS', 11.19), ('CB', 'TYR', 'CD2', 'HIS', 13.2), ('CB', 'TYR', 'CE1', 'HIS', 11.63), ('CB', 'TYR', 'NE2', 'HIS', 12.84)], [('CG', 'TYR', 'CB', 'HIS', 11.09), ('CG', 'TYR', 'CG', 'HIS', 10.95), ('CG', 'TYR', 'ND1', 'HIS', 9.85), ('CG', 'TYR', 'CD2', 'HIS', 11.86), ('CG', 'TYR', 'CE1', 'HIS', 10.2), ('CG', 'TYR', 'NE2', 'HIS', 11.42)], [('CD1', 'TYR', 'CB', 'HIS', 10.74), ('CD1', 'TYR', 'CG', 'HIS', 10.52), ('CD1', 'TYR', 'ND1', 'HIS', 9.45), ('CD1', 'TYR', 'CD2', 'HIS', 11.32), ('CD1', 'TYR', 'CE1', 'HIS', 9.68), ('CD1', 'TYR', 'NE2', 'HIS', 10.82)], [('CD2', 'TYR', 'CB', 'HIS', 10.61), ('CD2', 'TYR', 'CG', 'HIS', 10.4), ('CD2', 'TYR', 'ND1', 'HIS', 9.23), ('CD2', 'TYR', 'CD2', 'HIS', 11.34), ('CD2', 'TYR', 'CE1', 'HIS', 9.6), ('CD2', 'TYR', 'NE2', 'HIS', 10.88)], [('CE1', 'TYR', 'CB', 'HIS', 9.91), ('CE1', 'TYR', 'CG', 'HIS', 9.5), ('CE1', 'TYR', 'ND1', 'HIS', 8.37), ('CE1', 'TYR', 'CD2', 'HIS', 10.19), ('CE1', 'TYR', 'CE1', 'HIS', 8.45), ('CE1', 'TYR', 'NE2', 'HIS', 9.58)], [('CE2', 'TYR', 'CB', 'HIS', 9.76), ('CE2', 'TYR', 'CG', 'HIS', 9.36), ('CE2', 'TYR', 'ND1', 'HIS', 8.11), ('CE2', 'TYR', 'CD2', 'HIS', 10.22), ('CE2', 'TYR', 'CE1', 'HIS', 8.36), ('CE2', 'TYR', 'NE2', 'HIS', 9.65)], [('CZ', 'TYR', 'CB', 'HIS', 9.38), ('CZ', 'TYR', 'CG', 'HIS', 8.87), ('CZ', 'TYR', 'ND1', 'HIS', 7.62), ('CZ', 'TYR', 'CD2', 'HIS', 9.58), ('CZ', 'TYR', 'CE1', 'HIS', 7.7), ('CZ', 'TYR', 'NE2', 'HIS', 8.93)], [('OH', 'TYR', 'CB', 'HIS', 8.81), ('OH', 'TYR', 'CG', 'HIS', 8.06), ('OH', 'TYR', 'ND1', 'HIS', 6.75), ('OH', 'TYR', 'CD2', 'HIS', 8.61), ('OH', 'TYR', 'CE1', 'HIS', 6.59), ('OH', 'TYR', 'NE2', 'HIS', 7.8)]]}
TYR_4MO = { 
	'distances':
		[[15.91], [14.42], [13.69], [13.87], [12.32], [12.53], [11.69], [10.36]],
	'comparisons':
		[[('CB', 'TYR', 'MO', '4MO', 15.91)], [('CG', 'TYR', 'MO', '4MO', 14.42)], [('CD1', 'TYR', 'MO', '4MO', 13.69)], [('CD2', 'TYR', 'MO', '4MO', 13.87)], [('CE1', 'TYR', 'MO', '4MO', 12.32)], [('CE2', 'TYR', 'MO', '4MO', 12.53)], [('CZ', 'TYR', 'MO', '4MO', 11.69)], [('OH', 'TYR', 'MO', '4MO', 10.36)]]}
ASP_4MO = { 
	'distances':
		[[7.03], [6.38], [5.8], [6.9]],
	'comparisons':
		[[('CB', 'ASP', 'MO', '4MO', 7.03)], [('CG', 'ASP', 'MO', '4MO', 6.38)], [('OD1', 'ASP', 'MO', '4MO', 5.8)], [('OD2', 'ASP', 'MO', '4MO', 6.9)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'M_1ti6_1_97_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_4MO, d, 'M_1ti6_1_97_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ASP, d, 'M_1ti6_1_97_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_HIS, d, 'M_1ti6_1_97_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_4MO, d, 'M_1ti6_1_97_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_4MO, d, 'M_1ti6_1_97_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'HIS_4MO' :  match2,
		'TYR_ASP' :  match3,
		'TYR_HIS' :  match4,
		'TYR_4MO' :  match5,
		'ASP_4MO' :  match6}