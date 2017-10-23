'''
FUNC:M_1afr_1_14_19_2
PDB:1afr
EC:1.14.19.2
RESI:trp,his,asp,fe2,fe2
LOCI:a-62,146,228;a-364,365;
'''
import motifFunctions as cmd
TRP_ASP = { 
	'distances':
		[[10.62, 9.16, 8.57, 8.78], [9.19, 7.75, 7.25, 7.36], [8.1, 6.66, 6.01, 6.46], [8.9, 7.57, 7.34, 7.01], [6.98, 5.59, 5.15, 5.36], [7.55, 6.28, 6.17, 5.78], [9.88, 8.64, 8.56, 7.95], [7.3, 6.3, 6.53, 5.68], [9.68, 8.62, 8.77, 7.87], [8.5, 7.58, 7.89, 6.86]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'ASP', 10.62), ('CB', 'TRP', 'CG', 'ASP', 9.16), ('CB', 'TRP', 'OD1', 'ASP', 8.57), ('CB', 'TRP', 'OD2', 'ASP', 8.78)], [('CG', 'TRP', 'CB', 'ASP', 9.19), ('CG', 'TRP', 'CG', 'ASP', 7.75), ('CG', 'TRP', 'OD1', 'ASP', 7.25), ('CG', 'TRP', 'OD2', 'ASP', 7.36)], [('CD1', 'TRP', 'CB', 'ASP', 8.1), ('CD1', 'TRP', 'CG', 'ASP', 6.66), ('CD1', 'TRP', 'OD1', 'ASP', 6.01), ('CD1', 'TRP', 'OD2', 'ASP', 6.46)], [('CD2', 'TRP', 'CB', 'ASP', 8.9), ('CD2', 'TRP', 'CG', 'ASP', 7.57), ('CD2', 'TRP', 'OD1', 'ASP', 7.34), ('CD2', 'TRP', 'OD2', 'ASP', 7.01)], [('NE1', 'TRP', 'CB', 'ASP', 6.98), ('NE1', 'TRP', 'CG', 'ASP', 5.59), ('NE1', 'TRP', 'OD1', 'ASP', 5.15), ('NE1', 'TRP', 'OD2', 'ASP', 5.36)], [('CE2', 'TRP', 'CB', 'ASP', 7.55), ('CE2', 'TRP', 'CG', 'ASP', 6.28), ('CE2', 'TRP', 'OD1', 'ASP', 6.17), ('CE2', 'TRP', 'OD2', 'ASP', 5.78)], [('CE3', 'TRP', 'CB', 'ASP', 9.88), ('CE3', 'TRP', 'CG', 'ASP', 8.64), ('CE3', 'TRP', 'OD1', 'ASP', 8.56), ('CE3', 'TRP', 'OD2', 'ASP', 7.95)], [('CZ2', 'TRP', 'CB', 'ASP', 7.3), ('CZ2', 'TRP', 'CG', 'ASP', 6.3), ('CZ2', 'TRP', 'OD1', 'ASP', 6.53), ('CZ2', 'TRP', 'OD2', 'ASP', 5.68)], [('CZ3', 'TRP', 'CB', 'ASP', 9.68), ('CZ3', 'TRP', 'CG', 'ASP', 8.62), ('CZ3', 'TRP', 'OD1', 'ASP', 8.77), ('CZ3', 'TRP', 'OD2', 'ASP', 7.87)], [('CH2', 'TRP', 'CB', 'ASP', 8.5), ('CH2', 'TRP', 'CG', 'ASP', 7.58), ('CH2', 'TRP', 'OD1', 'ASP', 7.89), ('CH2', 'TRP', 'OD2', 'ASP', 6.86)]]}
ASP_HIS = { 
	'distances':
		[[9.02, 7.52, 6.97, 6.76, 5.67, 5.44], [9.2, 7.75, 7.56, 6.7, 6.31, 5.6], [10.19, 8.78, 8.63, 7.71, 7.42, 6.7], [8.57, 7.18, 7.22, 5.99, 6.07, 5.07]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 9.02), ('CB', 'ASP', 'CG', 'HIS', 7.52), ('CB', 'ASP', 'ND1', 'HIS', 6.97), ('CB', 'ASP', 'CD2', 'HIS', 6.76), ('CB', 'ASP', 'CE1', 'HIS', 5.67), ('CB', 'ASP', 'NE2', 'HIS', 5.44)], [('CG', 'ASP', 'CB', 'HIS', 9.2), ('CG', 'ASP', 'CG', 'HIS', 7.75), ('CG', 'ASP', 'ND1', 'HIS', 7.56), ('CG', 'ASP', 'CD2', 'HIS', 6.7), ('CG', 'ASP', 'CE1', 'HIS', 6.31), ('CG', 'ASP', 'NE2', 'HIS', 5.6)], [('OD1', 'ASP', 'CB', 'HIS', 10.19), ('OD1', 'ASP', 'CG', 'HIS', 8.78), ('OD1', 'ASP', 'ND1', 'HIS', 8.63), ('OD1', 'ASP', 'CD2', 'HIS', 7.71), ('OD1', 'ASP', 'CE1', 'HIS', 7.42), ('OD1', 'ASP', 'NE2', 'HIS', 6.7)], [('OD2', 'ASP', 'CB', 'HIS', 8.57), ('OD2', 'ASP', 'CG', 'HIS', 7.18), ('OD2', 'ASP', 'ND1', 'HIS', 7.22), ('OD2', 'ASP', 'CD2', 'HIS', 5.99), ('OD2', 'ASP', 'CE1', 'HIS', 6.07), ('OD2', 'ASP', 'NE2', 'HIS', 5.07)]]}
ASP_FE2 = { 
	'distances':
		[[7.81], [9.14], [10.18], [9.31], [8.39], [9.31], [10.42], [9.12]],
	'comparisons':
		[[('CB', 'ASP', 'FE', 'FE2', 7.81)], [('CG', 'ASP', 'FE', 'FE2', 9.14)], [('OD1', 'ASP', 'FE', 'FE2', 10.18)], [('OD2', 'ASP', 'FE', 'FE2', 9.31)], [('CB', 'ASP', 'FE', 'FE2', 8.39)], [('CG', 'ASP', 'FE', 'FE2', 9.31)], [('OD1', 'ASP', 'FE', 'FE2', 10.42)], [('OD2', 'ASP', 'FE', 'FE2', 9.12)]]}
FE2_FE2 = { 
	'distances':
		[6.21, 6.21],
	'comparisons':
		[('FE', 'FE2', 'FE', 'FE2', 6.21), ('FE', 'FE2', 'FE', 'FE2', 6.21)]}
HIS_FE2 = { 
	'distances':
		[[9.48], [8.48], [7.23], [8.84], [6.85], [7.91], [5.77], [5.36], [4.27], [6.42], [5.1], [6.3]],
	'comparisons':
		[[('CB', 'HIS', 'FE', 'FE2', 9.48)], [('CG', 'HIS', 'FE', 'FE2', 8.48)], [('ND1', 'HIS', 'FE', 'FE2', 7.23)], [('CD2', 'HIS', 'FE', 'FE2', 8.84)], [('CE1', 'HIS', 'FE', 'FE2', 6.85)], [('NE2', 'HIS', 'FE', 'FE2', 7.91)], [('CB', 'HIS', 'FE', 'FE2', 5.77)], [('CG', 'HIS', 'FE', 'FE2', 5.36)], [('ND1', 'HIS', 'FE', 'FE2', 4.27)], [('CD2', 'HIS', 'FE', 'FE2', 6.42)], [('CE1', 'HIS', 'FE', 'FE2', 5.1)], [('NE2', 'HIS', 'FE', 'FE2', 6.3)]]}
TRP_FE2 = { 
	'distances':
		[[16.03], [14.55], [13.66], [13.92], [12.42], [12.57], [14.51], [11.77], [13.83], [12.48], [14.89], [13.4], [12.87], [12.36], [11.51], [11.13], [12.53], [9.92], [11.49], [10.16]],
	'comparisons':
		[[('CB', 'TRP', 'FE', 'FE2', 16.03)], [('CG', 'TRP', 'FE', 'FE2', 14.55)], [('CD1', 'TRP', 'FE', 'FE2', 13.66)], [('CD2', 'TRP', 'FE', 'FE2', 13.92)], [('NE1', 'TRP', 'FE', 'FE2', 12.42)], [('CE2', 'TRP', 'FE', 'FE2', 12.57)], [('CE3', 'TRP', 'FE', 'FE2', 14.51)], [('CZ2', 'TRP', 'FE', 'FE2', 11.77)], [('CZ3', 'TRP', 'FE', 'FE2', 13.83)], [('CH2', 'TRP', 'FE', 'FE2', 12.48)], [('CB', 'TRP', 'FE', 'FE2', 14.89)], [('CG', 'TRP', 'FE', 'FE2', 13.4)], [('CD1', 'TRP', 'FE', 'FE2', 12.87)], [('CD2', 'TRP', 'FE', 'FE2', 12.36)], [('NE1', 'TRP', 'FE', 'FE2', 11.51)], [('CE2', 'TRP', 'FE', 'FE2', 11.13)], [('CE3', 'TRP', 'FE', 'FE2', 12.53)], [('CZ2', 'TRP', 'FE', 'FE2', 9.92)], [('CZ3', 'TRP', 'FE', 'FE2', 11.49)], [('CH2', 'TRP', 'FE', 'FE2', 10.16)]]}
TRP_HIS = { 
	'distances':
		[[12.67, 11.91, 12.64, 10.66, 11.94, 10.69], [11.3, 10.47, 11.15, 9.22, 10.43, 9.2], [11.2, 10.19, 10.69, 8.92, 9.82, 8.65], [10.0, 9.29, 10.09, 8.09, 9.52, 8.28], [9.94, 8.88, 9.33, 7.63, 8.46, 7.32], [9.07, 8.2, 8.87, 6.98, 8.21, 7.0], [9.74, 9.28, 10.27, 8.19, 9.9, 8.67], [7.69, 6.89, 7.65, 5.74, 7.16, 5.98], [8.48, 8.19, 9.27, 7.22, 9.09, 7.92], [7.35, 6.9, 7.92, 5.92, 7.71, 6.58]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'HIS', 12.67), ('CB', 'TRP', 'CG', 'HIS', 11.91), ('CB', 'TRP', 'ND1', 'HIS', 12.64), ('CB', 'TRP', 'CD2', 'HIS', 10.66), ('CB', 'TRP', 'CE1', 'HIS', 11.94), ('CB', 'TRP', 'NE2', 'HIS', 10.69)], [('CG', 'TRP', 'CB', 'HIS', 11.3), ('CG', 'TRP', 'CG', 'HIS', 10.47), ('CG', 'TRP', 'ND1', 'HIS', 11.15), ('CG', 'TRP', 'CD2', 'HIS', 9.22), ('CG', 'TRP', 'CE1', 'HIS', 10.43), ('CG', 'TRP', 'NE2', 'HIS', 9.2)], [('CD1', 'TRP', 'CB', 'HIS', 11.2), ('CD1', 'TRP', 'CG', 'HIS', 10.19), ('CD1', 'TRP', 'ND1', 'HIS', 10.69), ('CD1', 'TRP', 'CD2', 'HIS', 8.92), ('CD1', 'TRP', 'CE1', 'HIS', 9.82), ('CD1', 'TRP', 'NE2', 'HIS', 8.65)], [('CD2', 'TRP', 'CB', 'HIS', 10.0), ('CD2', 'TRP', 'CG', 'HIS', 9.29), ('CD2', 'TRP', 'ND1', 'HIS', 10.09), ('CD2', 'TRP', 'CD2', 'HIS', 8.09), ('CD2', 'TRP', 'CE1', 'HIS', 9.52), ('CD2', 'TRP', 'NE2', 'HIS', 8.28)], [('NE1', 'TRP', 'CB', 'HIS', 9.94), ('NE1', 'TRP', 'CG', 'HIS', 8.88), ('NE1', 'TRP', 'ND1', 'HIS', 9.33), ('NE1', 'TRP', 'CD2', 'HIS', 7.63), ('NE1', 'TRP', 'CE1', 'HIS', 8.46), ('NE1', 'TRP', 'NE2', 'HIS', 7.32)], [('CE2', 'TRP', 'CB', 'HIS', 9.07), ('CE2', 'TRP', 'CG', 'HIS', 8.2), ('CE2', 'TRP', 'ND1', 'HIS', 8.87), ('CE2', 'TRP', 'CD2', 'HIS', 6.98), ('CE2', 'TRP', 'CE1', 'HIS', 8.21), ('CE2', 'TRP', 'NE2', 'HIS', 7.0)], [('CE3', 'TRP', 'CB', 'HIS', 9.74), ('CE3', 'TRP', 'CG', 'HIS', 9.28), ('CE3', 'TRP', 'ND1', 'HIS', 10.27), ('CE3', 'TRP', 'CD2', 'HIS', 8.19), ('CE3', 'TRP', 'CE1', 'HIS', 9.9), ('CE3', 'TRP', 'NE2', 'HIS', 8.67)], [('CZ2', 'TRP', 'CB', 'HIS', 7.69), ('CZ2', 'TRP', 'CG', 'HIS', 6.89), ('CZ2', 'TRP', 'ND1', 'HIS', 7.65), ('CZ2', 'TRP', 'CD2', 'HIS', 5.74), ('CZ2', 'TRP', 'CE1', 'HIS', 7.16), ('CZ2', 'TRP', 'NE2', 'HIS', 5.98)], [('CZ3', 'TRP', 'CB', 'HIS', 8.48), ('CZ3', 'TRP', 'CG', 'HIS', 8.19), ('CZ3', 'TRP', 'ND1', 'HIS', 9.27), ('CZ3', 'TRP', 'CD2', 'HIS', 7.22), ('CZ3', 'TRP', 'CE1', 'HIS', 9.09), ('CZ3', 'TRP', 'NE2', 'HIS', 7.92)], [('CH2', 'TRP', 'CB', 'HIS', 7.35), ('CH2', 'TRP', 'CG', 'HIS', 6.9), ('CH2', 'TRP', 'ND1', 'HIS', 7.92), ('CH2', 'TRP', 'CD2', 'HIS', 5.92), ('CH2', 'TRP', 'CE1', 'HIS', 7.71), ('CH2', 'TRP', 'NE2', 'HIS', 6.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_ASP, d, 'M_1afr_1_14_19_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'M_1afr_1_14_19_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_FE2, d, 'M_1afr_1_14_19_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(FE2_FE2, d, 'M_1afr_1_14_19_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_FE2, d, 'M_1afr_1_14_19_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TRP_FE2, d, 'M_1afr_1_14_19_2')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(TRP_HIS, d, 'M_1afr_1_14_19_2')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_ASP' :  match1,
		'ASP_HIS' :  match2,
		'ASP_FE2' :  match3,
		'FE2_FE2' :  match4,
		'HIS_FE2' :  match5,
		'TRP_FE2' :  match6,
		'TRP_HIS' :  match7}