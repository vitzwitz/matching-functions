'''
FUNC:P_1afr_1_14_19_2
PDB:1afr
EC:1.14.19.2
RESI:trp,his,thr,asp
LOCI:a-62,146,199,228;
'''
import motifFunctions as cmd
TRP_ASP = { 
	'distances':
		[[10.62, 9.16, 8.57, 8.78], [9.19, 7.75, 7.25, 7.36], [8.1, 6.66, 6.01, 6.46], [8.9, 7.57, 7.34, 7.01], [6.98, 5.59, 5.15, 5.36], [7.55, 6.28, 6.17, 5.78], [9.88, 8.64, 8.56, 7.95], [7.3, 6.3, 6.53, 5.68], [9.68, 8.62, 8.77, 7.87], [8.5, 7.58, 7.89, 6.86]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'ASP', 10.62), ('CB', 'TRP', 'CG', 'ASP', 9.16), ('CB', 'TRP', 'OD1', 'ASP', 8.57), ('CB', 'TRP', 'OD2', 'ASP', 8.78)], [('CG', 'TRP', 'CB', 'ASP', 9.19), ('CG', 'TRP', 'CG', 'ASP', 7.75), ('CG', 'TRP', 'OD1', 'ASP', 7.25), ('CG', 'TRP', 'OD2', 'ASP', 7.36)], [('CD1', 'TRP', 'CB', 'ASP', 8.1), ('CD1', 'TRP', 'CG', 'ASP', 6.66), ('CD1', 'TRP', 'OD1', 'ASP', 6.01), ('CD1', 'TRP', 'OD2', 'ASP', 6.46)], [('CD2', 'TRP', 'CB', 'ASP', 8.9), ('CD2', 'TRP', 'CG', 'ASP', 7.57), ('CD2', 'TRP', 'OD1', 'ASP', 7.34), ('CD2', 'TRP', 'OD2', 'ASP', 7.01)], [('NE1', 'TRP', 'CB', 'ASP', 6.98), ('NE1', 'TRP', 'CG', 'ASP', 5.59), ('NE1', 'TRP', 'OD1', 'ASP', 5.15), ('NE1', 'TRP', 'OD2', 'ASP', 5.36)], [('CE2', 'TRP', 'CB', 'ASP', 7.55), ('CE2', 'TRP', 'CG', 'ASP', 6.28), ('CE2', 'TRP', 'OD1', 'ASP', 6.17), ('CE2', 'TRP', 'OD2', 'ASP', 5.78)], [('CE3', 'TRP', 'CB', 'ASP', 9.88), ('CE3', 'TRP', 'CG', 'ASP', 8.64), ('CE3', 'TRP', 'OD1', 'ASP', 8.56), ('CE3', 'TRP', 'OD2', 'ASP', 7.95)], [('CZ2', 'TRP', 'CB', 'ASP', 7.3), ('CZ2', 'TRP', 'CG', 'ASP', 6.3), ('CZ2', 'TRP', 'OD1', 'ASP', 6.53), ('CZ2', 'TRP', 'OD2', 'ASP', 5.68)], [('CZ3', 'TRP', 'CB', 'ASP', 9.68), ('CZ3', 'TRP', 'CG', 'ASP', 8.62), ('CZ3', 'TRP', 'OD1', 'ASP', 8.77), ('CZ3', 'TRP', 'OD2', 'ASP', 7.87)], [('CH2', 'TRP', 'CB', 'ASP', 8.5), ('CH2', 'TRP', 'CG', 'ASP', 7.58), ('CH2', 'TRP', 'OD1', 'ASP', 7.89), ('CH2', 'TRP', 'OD2', 'ASP', 6.86)]]}
HIS_ASP = { 
	'distances':
		[[9.02, 9.2, 10.19, 8.57], [7.52, 7.75, 8.78, 7.18], [6.97, 7.56, 8.63, 7.22], [6.76, 6.7, 7.71, 5.99], [5.67, 6.31, 7.42, 6.07], [5.44, 5.6, 6.7, 5.07]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.02), ('CB', 'HIS', 'CG', 'ASP', 9.2), ('CB', 'HIS', 'OD1', 'ASP', 10.19), ('CB', 'HIS', 'OD2', 'ASP', 8.57)], [('CG', 'HIS', 'CB', 'ASP', 7.52), ('CG', 'HIS', 'CG', 'ASP', 7.75), ('CG', 'HIS', 'OD1', 'ASP', 8.78), ('CG', 'HIS', 'OD2', 'ASP', 7.18)], [('ND1', 'HIS', 'CB', 'ASP', 6.97), ('ND1', 'HIS', 'CG', 'ASP', 7.56), ('ND1', 'HIS', 'OD1', 'ASP', 8.63), ('ND1', 'HIS', 'OD2', 'ASP', 7.22)], [('CD2', 'HIS', 'CB', 'ASP', 6.76), ('CD2', 'HIS', 'CG', 'ASP', 6.7), ('CD2', 'HIS', 'OD1', 'ASP', 7.71), ('CD2', 'HIS', 'OD2', 'ASP', 5.99)], [('CE1', 'HIS', 'CB', 'ASP', 5.67), ('CE1', 'HIS', 'CG', 'ASP', 6.31), ('CE1', 'HIS', 'OD1', 'ASP', 7.42), ('CE1', 'HIS', 'OD2', 'ASP', 6.07)], [('NE2', 'HIS', 'CB', 'ASP', 5.44), ('NE2', 'HIS', 'CG', 'ASP', 5.6), ('NE2', 'HIS', 'OD1', 'ASP', 6.7), ('NE2', 'HIS', 'OD2', 'ASP', 5.07)]]}
THR_ASP = { 
	'distances':
		[[11.09, 12.42, 13.2, 12.82], [10.27, 11.68, 12.44, 12.14], [12.05, 13.37, 14.24, 13.65]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 11.09), ('CB', 'THR', 'CG', 'ASP', 12.42), ('CB', 'THR', 'OD1', 'ASP', 13.2), ('CB', 'THR', 'OD2', 'ASP', 12.82)], [('OG1', 'THR', 'CB', 'ASP', 10.27), ('OG1', 'THR', 'CG', 'ASP', 11.68), ('OG1', 'THR', 'OD1', 'ASP', 12.44), ('OG1', 'THR', 'OD2', 'ASP', 12.14)], [('CG2', 'THR', 'CB', 'ASP', 12.05), ('CG2', 'THR', 'CG', 'ASP', 13.37), ('CG2', 'THR', 'OD1', 'ASP', 14.24), ('CG2', 'THR', 'OD2', 'ASP', 13.65)]]}
HIS_THR = { 
	'distances':
		[[10.59, 10.75, 10.85], [10.21, 10.15, 10.64], [8.99, 8.82, 9.46], [11.15, 10.93, 11.69], [9.34, 8.94, 9.97], [10.65, 10.25, 11.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'THR', 10.59), ('CB', 'HIS', 'OG1', 'THR', 10.75), ('CB', 'HIS', 'CG2', 'THR', 10.85)], [('CG', 'HIS', 'CB', 'THR', 10.21), ('CG', 'HIS', 'OG1', 'THR', 10.15), ('CG', 'HIS', 'CG2', 'THR', 10.64)], [('ND1', 'HIS', 'CB', 'THR', 8.99), ('ND1', 'HIS', 'OG1', 'THR', 8.82), ('ND1', 'HIS', 'CG2', 'THR', 9.46)], [('CD2', 'HIS', 'CB', 'THR', 11.15), ('CD2', 'HIS', 'OG1', 'THR', 10.93), ('CD2', 'HIS', 'CG2', 'THR', 11.69)], [('CE1', 'HIS', 'CB', 'THR', 9.34), ('CE1', 'HIS', 'OG1', 'THR', 8.94), ('CE1', 'HIS', 'CG2', 'THR', 9.97)], [('NE2', 'HIS', 'CB', 'THR', 10.65), ('NE2', 'HIS', 'OG1', 'THR', 10.25), ('NE2', 'HIS', 'CG2', 'THR', 11.3)]]}
TRP_THR = { 
	'distances':
		[[18.56, 18.15, 19.52], [17.05, 16.64, 18.01], [16.3, 15.79, 17.3], [16.21, 15.89, 17.1], [14.96, 14.48, 15.94], [14.88, 14.52, 15.78], [16.58, 16.38, 17.39], [13.84, 13.58, 14.68], [15.66, 15.56, 16.4], [14.29, 14.16, 15.04]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'THR', 18.56), ('CB', 'TRP', 'OG1', 'THR', 18.15), ('CB', 'TRP', 'CG2', 'THR', 19.52)], [('CG', 'TRP', 'CB', 'THR', 17.05), ('CG', 'TRP', 'OG1', 'THR', 16.64), ('CG', 'TRP', 'CG2', 'THR', 18.01)], [('CD1', 'TRP', 'CB', 'THR', 16.3), ('CD1', 'TRP', 'OG1', 'THR', 15.79), ('CD1', 'TRP', 'CG2', 'THR', 17.3)], [('CD2', 'TRP', 'CB', 'THR', 16.21), ('CD2', 'TRP', 'OG1', 'THR', 15.89), ('CD2', 'TRP', 'CG2', 'THR', 17.1)], [('NE1', 'TRP', 'CB', 'THR', 14.96), ('NE1', 'TRP', 'OG1', 'THR', 14.48), ('NE1', 'TRP', 'CG2', 'THR', 15.94)], [('CE2', 'TRP', 'CB', 'THR', 14.88), ('CE2', 'TRP', 'OG1', 'THR', 14.52), ('CE2', 'TRP', 'CG2', 'THR', 15.78)], [('CE3', 'TRP', 'CB', 'THR', 16.58), ('CE3', 'TRP', 'OG1', 'THR', 16.38), ('CE3', 'TRP', 'CG2', 'THR', 17.39)], [('CZ2', 'TRP', 'CB', 'THR', 13.84), ('CZ2', 'TRP', 'OG1', 'THR', 13.58), ('CZ2', 'TRP', 'CG2', 'THR', 14.68)], [('CZ3', 'TRP', 'CB', 'THR', 15.66), ('CZ3', 'TRP', 'OG1', 'THR', 15.56), ('CZ3', 'TRP', 'CG2', 'THR', 16.4)], [('CH2', 'TRP', 'CB', 'THR', 14.29), ('CH2', 'TRP', 'OG1', 'THR', 14.16), ('CH2', 'TRP', 'CG2', 'THR', 15.04)]]}
TRP_HIS = { 
	'distances':
		[[12.67, 11.91, 12.64, 10.66, 11.94, 10.69], [11.3, 10.47, 11.15, 9.22, 10.43, 9.2], [11.2, 10.19, 10.69, 8.92, 9.82, 8.65], [10.0, 9.29, 10.09, 8.09, 9.52, 8.28], [9.94, 8.88, 9.33, 7.63, 8.46, 7.32], [9.07, 8.2, 8.87, 6.98, 8.21, 7.0], [9.74, 9.28, 10.27, 8.19, 9.9, 8.67], [7.69, 6.89, 7.65, 5.74, 7.16, 5.98], [8.48, 8.19, 9.27, 7.22, 9.09, 7.92], [7.35, 6.9, 7.92, 5.92, 7.71, 6.58]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'HIS', 12.67), ('CB', 'TRP', 'CG', 'HIS', 11.91), ('CB', 'TRP', 'ND1', 'HIS', 12.64), ('CB', 'TRP', 'CD2', 'HIS', 10.66), ('CB', 'TRP', 'CE1', 'HIS', 11.94), ('CB', 'TRP', 'NE2', 'HIS', 10.69)], [('CG', 'TRP', 'CB', 'HIS', 11.3), ('CG', 'TRP', 'CG', 'HIS', 10.47), ('CG', 'TRP', 'ND1', 'HIS', 11.15), ('CG', 'TRP', 'CD2', 'HIS', 9.22), ('CG', 'TRP', 'CE1', 'HIS', 10.43), ('CG', 'TRP', 'NE2', 'HIS', 9.2)], [('CD1', 'TRP', 'CB', 'HIS', 11.2), ('CD1', 'TRP', 'CG', 'HIS', 10.19), ('CD1', 'TRP', 'ND1', 'HIS', 10.69), ('CD1', 'TRP', 'CD2', 'HIS', 8.92), ('CD1', 'TRP', 'CE1', 'HIS', 9.82), ('CD1', 'TRP', 'NE2', 'HIS', 8.65)], [('CD2', 'TRP', 'CB', 'HIS', 10.0), ('CD2', 'TRP', 'CG', 'HIS', 9.29), ('CD2', 'TRP', 'ND1', 'HIS', 10.09), ('CD2', 'TRP', 'CD2', 'HIS', 8.09), ('CD2', 'TRP', 'CE1', 'HIS', 9.52), ('CD2', 'TRP', 'NE2', 'HIS', 8.28)], [('NE1', 'TRP', 'CB', 'HIS', 9.94), ('NE1', 'TRP', 'CG', 'HIS', 8.88), ('NE1', 'TRP', 'ND1', 'HIS', 9.33), ('NE1', 'TRP', 'CD2', 'HIS', 7.63), ('NE1', 'TRP', 'CE1', 'HIS', 8.46), ('NE1', 'TRP', 'NE2', 'HIS', 7.32)], [('CE2', 'TRP', 'CB', 'HIS', 9.07), ('CE2', 'TRP', 'CG', 'HIS', 8.2), ('CE2', 'TRP', 'ND1', 'HIS', 8.87), ('CE2', 'TRP', 'CD2', 'HIS', 6.98), ('CE2', 'TRP', 'CE1', 'HIS', 8.21), ('CE2', 'TRP', 'NE2', 'HIS', 7.0)], [('CE3', 'TRP', 'CB', 'HIS', 9.74), ('CE3', 'TRP', 'CG', 'HIS', 9.28), ('CE3', 'TRP', 'ND1', 'HIS', 10.27), ('CE3', 'TRP', 'CD2', 'HIS', 8.19), ('CE3', 'TRP', 'CE1', 'HIS', 9.9), ('CE3', 'TRP', 'NE2', 'HIS', 8.67)], [('CZ2', 'TRP', 'CB', 'HIS', 7.69), ('CZ2', 'TRP', 'CG', 'HIS', 6.89), ('CZ2', 'TRP', 'ND1', 'HIS', 7.65), ('CZ2', 'TRP', 'CD2', 'HIS', 5.74), ('CZ2', 'TRP', 'CE1', 'HIS', 7.16), ('CZ2', 'TRP', 'NE2', 'HIS', 5.98)], [('CZ3', 'TRP', 'CB', 'HIS', 8.48), ('CZ3', 'TRP', 'CG', 'HIS', 8.19), ('CZ3', 'TRP', 'ND1', 'HIS', 9.27), ('CZ3', 'TRP', 'CD2', 'HIS', 7.22), ('CZ3', 'TRP', 'CE1', 'HIS', 9.09), ('CZ3', 'TRP', 'NE2', 'HIS', 7.92)], [('CH2', 'TRP', 'CB', 'HIS', 7.35), ('CH2', 'TRP', 'CG', 'HIS', 6.9), ('CH2', 'TRP', 'ND1', 'HIS', 7.92), ('CH2', 'TRP', 'CD2', 'HIS', 5.92), ('CH2', 'TRP', 'CE1', 'HIS', 7.71), ('CH2', 'TRP', 'NE2', 'HIS', 6.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_ASP, d, 'P_1afr_1_14_19_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1afr_1_14_19_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_ASP, d, 'P_1afr_1_14_19_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_THR, d, 'P_1afr_1_14_19_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TRP_THR, d, 'P_1afr_1_14_19_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TRP_HIS, d, 'P_1afr_1_14_19_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_ASP' :  match1,
		'HIS_ASP' :  match2,
		'THR_ASP' :  match3,
		'HIS_THR' :  match4,
		'TRP_THR' :  match5,
		'TRP_HIS' :  match6}