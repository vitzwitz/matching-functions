'''
FUNC:A_1afr_1_14_19_2
PDB:1afr
EC:1.14.19.2
RESI:trp,his,thr,asp
LOCI:a-62,146,199,228;
'''
import motifFunctions as cmd
ASP_TRP = { 
	'distances':
		[[10.62, 9.19, 8.1, 8.9, 6.98, 7.55, 9.88, 7.3, 9.68, 8.5], [9.16, 7.75, 6.66, 7.57, 5.59, 6.28, 8.64, 6.3, 8.62, 7.58], [8.57, 7.25, 6.01, 7.34, 5.15, 6.17, 8.56, 6.53, 8.77, 7.89], [8.78, 7.36, 6.46, 7.01, 5.36, 5.78, 7.95, 5.68, 7.87, 6.86]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TRP', 10.62), ('CB', 'ASP', 'CG', 'TRP', 9.19), ('CB', 'ASP', 'CD1', 'TRP', 8.1), ('CB', 'ASP', 'CD2', 'TRP', 8.9), ('CB', 'ASP', 'NE1', 'TRP', 6.98), ('CB', 'ASP', 'CE2', 'TRP', 7.55), ('CB', 'ASP', 'CE3', 'TRP', 9.88), ('CB', 'ASP', 'CZ2', 'TRP', 7.3), ('CB', 'ASP', 'CZ3', 'TRP', 9.68), ('CB', 'ASP', 'CH2', 'TRP', 8.5)], [('CG', 'ASP', 'CB', 'TRP', 9.16), ('CG', 'ASP', 'CG', 'TRP', 7.75), ('CG', 'ASP', 'CD1', 'TRP', 6.66), ('CG', 'ASP', 'CD2', 'TRP', 7.57), ('CG', 'ASP', 'NE1', 'TRP', 5.59), ('CG', 'ASP', 'CE2', 'TRP', 6.28), ('CG', 'ASP', 'CE3', 'TRP', 8.64), ('CG', 'ASP', 'CZ2', 'TRP', 6.3), ('CG', 'ASP', 'CZ3', 'TRP', 8.62), ('CG', 'ASP', 'CH2', 'TRP', 7.58)], [('OD1', 'ASP', 'CB', 'TRP', 8.57), ('OD1', 'ASP', 'CG', 'TRP', 7.25), ('OD1', 'ASP', 'CD1', 'TRP', 6.01), ('OD1', 'ASP', 'CD2', 'TRP', 7.34), ('OD1', 'ASP', 'NE1', 'TRP', 5.15), ('OD1', 'ASP', 'CE2', 'TRP', 6.17), ('OD1', 'ASP', 'CE3', 'TRP', 8.56), ('OD1', 'ASP', 'CZ2', 'TRP', 6.53), ('OD1', 'ASP', 'CZ3', 'TRP', 8.77), ('OD1', 'ASP', 'CH2', 'TRP', 7.89)], [('OD2', 'ASP', 'CB', 'TRP', 8.78), ('OD2', 'ASP', 'CG', 'TRP', 7.36), ('OD2', 'ASP', 'CD1', 'TRP', 6.46), ('OD2', 'ASP', 'CD2', 'TRP', 7.01), ('OD2', 'ASP', 'NE1', 'TRP', 5.36), ('OD2', 'ASP', 'CE2', 'TRP', 5.78), ('OD2', 'ASP', 'CE3', 'TRP', 7.95), ('OD2', 'ASP', 'CZ2', 'TRP', 5.68), ('OD2', 'ASP', 'CZ3', 'TRP', 7.87), ('OD2', 'ASP', 'CH2', 'TRP', 6.86)]]}
ASP_HIS = { 
	'distances':
		[[9.02, 7.52, 6.97, 6.76, 5.67, 5.44], [9.2, 7.75, 7.56, 6.7, 6.31, 5.6], [10.19, 8.78, 8.63, 7.71, 7.42, 6.7], [8.57, 7.18, 7.22, 5.99, 6.07, 5.07]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 9.02), ('CB', 'ASP', 'CG', 'HIS', 7.52), ('CB', 'ASP', 'ND1', 'HIS', 6.97), ('CB', 'ASP', 'CD2', 'HIS', 6.76), ('CB', 'ASP', 'CE1', 'HIS', 5.67), ('CB', 'ASP', 'NE2', 'HIS', 5.44)], [('CG', 'ASP', 'CB', 'HIS', 9.2), ('CG', 'ASP', 'CG', 'HIS', 7.75), ('CG', 'ASP', 'ND1', 'HIS', 7.56), ('CG', 'ASP', 'CD2', 'HIS', 6.7), ('CG', 'ASP', 'CE1', 'HIS', 6.31), ('CG', 'ASP', 'NE2', 'HIS', 5.6)], [('OD1', 'ASP', 'CB', 'HIS', 10.19), ('OD1', 'ASP', 'CG', 'HIS', 8.78), ('OD1', 'ASP', 'ND1', 'HIS', 8.63), ('OD1', 'ASP', 'CD2', 'HIS', 7.71), ('OD1', 'ASP', 'CE1', 'HIS', 7.42), ('OD1', 'ASP', 'NE2', 'HIS', 6.7)], [('OD2', 'ASP', 'CB', 'HIS', 8.57), ('OD2', 'ASP', 'CG', 'HIS', 7.18), ('OD2', 'ASP', 'ND1', 'HIS', 7.22), ('OD2', 'ASP', 'CD2', 'HIS', 5.99), ('OD2', 'ASP', 'CE1', 'HIS', 6.07), ('OD2', 'ASP', 'NE2', 'HIS', 5.07)]]}
HIS_THR = { 
	'distances':
		[[10.59, 10.75, 10.85], [10.21, 10.15, 10.64], [8.99, 8.82, 9.46], [11.15, 10.93, 11.69], [9.34, 8.94, 9.97], [10.65, 10.25, 11.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'THR', 10.59), ('CB', 'HIS', 'OG1', 'THR', 10.75), ('CB', 'HIS', 'CG2', 'THR', 10.85)], [('CG', 'HIS', 'CB', 'THR', 10.21), ('CG', 'HIS', 'OG1', 'THR', 10.15), ('CG', 'HIS', 'CG2', 'THR', 10.64)], [('ND1', 'HIS', 'CB', 'THR', 8.99), ('ND1', 'HIS', 'OG1', 'THR', 8.82), ('ND1', 'HIS', 'CG2', 'THR', 9.46)], [('CD2', 'HIS', 'CB', 'THR', 11.15), ('CD2', 'HIS', 'OG1', 'THR', 10.93), ('CD2', 'HIS', 'CG2', 'THR', 11.69)], [('CE1', 'HIS', 'CB', 'THR', 9.34), ('CE1', 'HIS', 'OG1', 'THR', 8.94), ('CE1', 'HIS', 'CG2', 'THR', 9.97)], [('NE2', 'HIS', 'CB', 'THR', 10.65), ('NE2', 'HIS', 'OG1', 'THR', 10.25), ('NE2', 'HIS', 'CG2', 'THR', 11.3)]]}
THR_TRP = { 
	'distances':
		[[18.56, 17.05, 16.3, 16.21, 14.96, 14.88, 16.58, 13.84, 15.66, 14.29], [18.15, 16.64, 15.79, 15.89, 14.48, 14.52, 16.38, 13.58, 15.56, 14.16], [19.52, 18.01, 17.3, 17.1, 15.94, 15.78, 17.39, 14.68, 16.4, 15.04]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'TRP', 18.56), ('CB', 'THR', 'CG', 'TRP', 17.05), ('CB', 'THR', 'CD1', 'TRP', 16.3), ('CB', 'THR', 'CD2', 'TRP', 16.21), ('CB', 'THR', 'NE1', 'TRP', 14.96), ('CB', 'THR', 'CE2', 'TRP', 14.88), ('CB', 'THR', 'CE3', 'TRP', 16.58), ('CB', 'THR', 'CZ2', 'TRP', 13.84), ('CB', 'THR', 'CZ3', 'TRP', 15.66), ('CB', 'THR', 'CH2', 'TRP', 14.29)], [('OG1', 'THR', 'CB', 'TRP', 18.15), ('OG1', 'THR', 'CG', 'TRP', 16.64), ('OG1', 'THR', 'CD1', 'TRP', 15.79), ('OG1', 'THR', 'CD2', 'TRP', 15.89), ('OG1', 'THR', 'NE1', 'TRP', 14.48), ('OG1', 'THR', 'CE2', 'TRP', 14.52), ('OG1', 'THR', 'CE3', 'TRP', 16.38), ('OG1', 'THR', 'CZ2', 'TRP', 13.58), ('OG1', 'THR', 'CZ3', 'TRP', 15.56), ('OG1', 'THR', 'CH2', 'TRP', 14.16)], [('CG2', 'THR', 'CB', 'TRP', 19.52), ('CG2', 'THR', 'CG', 'TRP', 18.01), ('CG2', 'THR', 'CD1', 'TRP', 17.3), ('CG2', 'THR', 'CD2', 'TRP', 17.1), ('CG2', 'THR', 'NE1', 'TRP', 15.94), ('CG2', 'THR', 'CE2', 'TRP', 15.78), ('CG2', 'THR', 'CE3', 'TRP', 17.39), ('CG2', 'THR', 'CZ2', 'TRP', 14.68), ('CG2', 'THR', 'CZ3', 'TRP', 16.4), ('CG2', 'THR', 'CH2', 'TRP', 15.04)]]}
ASP_THR = { 
	'distances':
		[[11.09, 10.27, 12.05], [12.42, 11.68, 13.37], [13.2, 12.44, 14.24], [12.82, 12.14, 13.65]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 11.09), ('CB', 'ASP', 'OG1', 'THR', 10.27), ('CB', 'ASP', 'CG2', 'THR', 12.05)], [('CG', 'ASP', 'CB', 'THR', 12.42), ('CG', 'ASP', 'OG1', 'THR', 11.68), ('CG', 'ASP', 'CG2', 'THR', 13.37)], [('OD1', 'ASP', 'CB', 'THR', 13.2), ('OD1', 'ASP', 'OG1', 'THR', 12.44), ('OD1', 'ASP', 'CG2', 'THR', 14.24)], [('OD2', 'ASP', 'CB', 'THR', 12.82), ('OD2', 'ASP', 'OG1', 'THR', 12.14), ('OD2', 'ASP', 'CG2', 'THR', 13.65)]]}
HIS_TRP = { 
	'distances':
		[[12.67, 11.3, 11.2, 10.0, 9.94, 9.07, 9.74, 7.69, 8.48, 7.35], [11.91, 10.47, 10.19, 9.29, 8.88, 8.2, 9.28, 6.89, 8.19, 6.9], [12.64, 11.15, 10.69, 10.09, 9.33, 8.87, 10.27, 7.65, 9.27, 7.92], [10.66, 9.22, 8.92, 8.09, 7.63, 6.98, 8.19, 5.74, 7.22, 5.92], [11.94, 10.43, 9.82, 9.52, 8.46, 8.21, 9.9, 7.16, 9.09, 7.71], [10.69, 9.2, 8.65, 8.28, 7.32, 7.0, 8.67, 5.98, 7.92, 6.58]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TRP', 12.67), ('CB', 'HIS', 'CG', 'TRP', 11.3), ('CB', 'HIS', 'CD1', 'TRP', 11.2), ('CB', 'HIS', 'CD2', 'TRP', 10.0), ('CB', 'HIS', 'NE1', 'TRP', 9.94), ('CB', 'HIS', 'CE2', 'TRP', 9.07), ('CB', 'HIS', 'CE3', 'TRP', 9.74), ('CB', 'HIS', 'CZ2', 'TRP', 7.69), ('CB', 'HIS', 'CZ3', 'TRP', 8.48), ('CB', 'HIS', 'CH2', 'TRP', 7.35)], [('CG', 'HIS', 'CB', 'TRP', 11.91), ('CG', 'HIS', 'CG', 'TRP', 10.47), ('CG', 'HIS', 'CD1', 'TRP', 10.19), ('CG', 'HIS', 'CD2', 'TRP', 9.29), ('CG', 'HIS', 'NE1', 'TRP', 8.88), ('CG', 'HIS', 'CE2', 'TRP', 8.2), ('CG', 'HIS', 'CE3', 'TRP', 9.28), ('CG', 'HIS', 'CZ2', 'TRP', 6.89), ('CG', 'HIS', 'CZ3', 'TRP', 8.19), ('CG', 'HIS', 'CH2', 'TRP', 6.9)], [('ND1', 'HIS', 'CB', 'TRP', 12.64), ('ND1', 'HIS', 'CG', 'TRP', 11.15), ('ND1', 'HIS', 'CD1', 'TRP', 10.69), ('ND1', 'HIS', 'CD2', 'TRP', 10.09), ('ND1', 'HIS', 'NE1', 'TRP', 9.33), ('ND1', 'HIS', 'CE2', 'TRP', 8.87), ('ND1', 'HIS', 'CE3', 'TRP', 10.27), ('ND1', 'HIS', 'CZ2', 'TRP', 7.65), ('ND1', 'HIS', 'CZ3', 'TRP', 9.27), ('ND1', 'HIS', 'CH2', 'TRP', 7.92)], [('CD2', 'HIS', 'CB', 'TRP', 10.66), ('CD2', 'HIS', 'CG', 'TRP', 9.22), ('CD2', 'HIS', 'CD1', 'TRP', 8.92), ('CD2', 'HIS', 'CD2', 'TRP', 8.09), ('CD2', 'HIS', 'NE1', 'TRP', 7.63), ('CD2', 'HIS', 'CE2', 'TRP', 6.98), ('CD2', 'HIS', 'CE3', 'TRP', 8.19), ('CD2', 'HIS', 'CZ2', 'TRP', 5.74), ('CD2', 'HIS', 'CZ3', 'TRP', 7.22), ('CD2', 'HIS', 'CH2', 'TRP', 5.92)], [('CE1', 'HIS', 'CB', 'TRP', 11.94), ('CE1', 'HIS', 'CG', 'TRP', 10.43), ('CE1', 'HIS', 'CD1', 'TRP', 9.82), ('CE1', 'HIS', 'CD2', 'TRP', 9.52), ('CE1', 'HIS', 'NE1', 'TRP', 8.46), ('CE1', 'HIS', 'CE2', 'TRP', 8.21), ('CE1', 'HIS', 'CE3', 'TRP', 9.9), ('CE1', 'HIS', 'CZ2', 'TRP', 7.16), ('CE1', 'HIS', 'CZ3', 'TRP', 9.09), ('CE1', 'HIS', 'CH2', 'TRP', 7.71)], [('NE2', 'HIS', 'CB', 'TRP', 10.69), ('NE2', 'HIS', 'CG', 'TRP', 9.2), ('NE2', 'HIS', 'CD1', 'TRP', 8.65), ('NE2', 'HIS', 'CD2', 'TRP', 8.28), ('NE2', 'HIS', 'NE1', 'TRP', 7.32), ('NE2', 'HIS', 'CE2', 'TRP', 7.0), ('NE2', 'HIS', 'CE3', 'TRP', 8.67), ('NE2', 'HIS', 'CZ2', 'TRP', 5.98), ('NE2', 'HIS', 'CZ3', 'TRP', 7.92), ('NE2', 'HIS', 'CH2', 'TRP', 6.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_TRP, d, 'A_1afr_1_14_19_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1afr_1_14_19_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_THR, d, 'A_1afr_1_14_19_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_TRP, d, 'A_1afr_1_14_19_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_THR, d, 'A_1afr_1_14_19_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_TRP, d, 'A_1afr_1_14_19_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_TRP' :  match1,
		'ASP_HIS' :  match2,
		'HIS_THR' :  match3,
		'THR_TRP' :  match4,
		'ASP_THR' :  match5,
		'HIS_TRP' :  match6}