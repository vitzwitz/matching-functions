'''
FUNC:A_3eca_3_5_1_1
PDB:3eca
EC:3.5.1.1
RESI:thr,tyr,thr,asp,lys
LOCI:a-12,25,89,90,162;
'''
import motifFunctions as cmd
THR_THR = { 
	'distances':
		[[8.37, 8.47, 9.26], [7.74, 7.61, 8.58], [7.94, 8.38, 8.71], [8.37, 7.74, 7.94], [8.47, 7.61, 8.38], [9.26, 8.58, 8.71]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'THR', 8.37), ('CB', 'THR', 'OG1', 'THR', 8.47), ('CB', 'THR', 'CG2', 'THR', 9.26)], [('OG1', 'THR', 'CB', 'THR', 7.74), ('OG1', 'THR', 'OG1', 'THR', 7.61), ('OG1', 'THR', 'CG2', 'THR', 8.58)], [('CG2', 'THR', 'CB', 'THR', 7.94), ('CG2', 'THR', 'OG1', 'THR', 8.38), ('CG2', 'THR', 'CG2', 'THR', 8.71)], [('CB', 'THR', 'CB', 'THR', 8.37), ('CB', 'THR', 'OG1', 'THR', 7.74), ('CB', 'THR', 'CG2', 'THR', 7.94)], [('OG1', 'THR', 'CB', 'THR', 8.47), ('OG1', 'THR', 'OG1', 'THR', 7.61), ('OG1', 'THR', 'CG2', 'THR', 8.38)], [('CG2', 'THR', 'CB', 'THR', 9.26), ('CG2', 'THR', 'OG1', 'THR', 8.58), ('CG2', 'THR', 'CG2', 'THR', 8.71)]]}
ASP_THR = { 
	'distances':
		[[7.58, 6.92, 8.99], [7.66, 6.65, 8.98], [6.94, 5.8, 8.23], [8.72, 7.65, 9.96], [10.49, 9.56, 11.61], [9.78, 8.75, 10.76], [9.34, 8.43, 10.19], [9.93, 8.73, 10.88]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 7.58), ('CB', 'ASP', 'OG1', 'THR', 6.92), ('CB', 'ASP', 'CG2', 'THR', 8.99)], [('CG', 'ASP', 'CB', 'THR', 7.66), ('CG', 'ASP', 'OG1', 'THR', 6.65), ('CG', 'ASP', 'CG2', 'THR', 8.98)], [('OD1', 'ASP', 'CB', 'THR', 6.94), ('OD1', 'ASP', 'OG1', 'THR', 5.8), ('OD1', 'ASP', 'CG2', 'THR', 8.23)], [('OD2', 'ASP', 'CB', 'THR', 8.72), ('OD2', 'ASP', 'OG1', 'THR', 7.65), ('OD2', 'ASP', 'CG2', 'THR', 9.96)], [('CB', 'ASP', 'CB', 'THR', 10.49), ('CB', 'ASP', 'OG1', 'THR', 9.56), ('CB', 'ASP', 'CG2', 'THR', 11.61)], [('CG', 'ASP', 'CB', 'THR', 9.78), ('CG', 'ASP', 'OG1', 'THR', 8.75), ('CG', 'ASP', 'CG2', 'THR', 10.76)], [('OD1', 'ASP', 'CB', 'THR', 9.34), ('OD1', 'ASP', 'OG1', 'THR', 8.43), ('OD1', 'ASP', 'CG2', 'THR', 10.19)], [('OD2', 'ASP', 'CB', 'THR', 9.93), ('OD2', 'ASP', 'OG1', 'THR', 8.73), ('OD2', 'ASP', 'CG2', 'THR', 10.88)]]}
ASP_TYR = { 
	'distances':
		[[15.16, 13.74, 13.45, 12.81, 12.21, 11.48, 11.15, 9.93], [13.99, 12.55, 12.16, 11.72, 10.9, 10.38, 9.92, 8.68], [13.71, 12.23, 11.73, 11.48, 10.41, 10.11, 9.5, 8.18], [13.49, 12.09, 11.73, 11.28, 10.53, 10.0, 9.58, 8.44]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 15.16), ('CB', 'ASP', 'CG', 'TYR', 13.74), ('CB', 'ASP', 'CD1', 'TYR', 13.45), ('CB', 'ASP', 'CD2', 'TYR', 12.81), ('CB', 'ASP', 'CE1', 'TYR', 12.21), ('CB', 'ASP', 'CE2', 'TYR', 11.48), ('CB', 'ASP', 'CZ', 'TYR', 11.15), ('CB', 'ASP', 'OH', 'TYR', 9.93)], [('CG', 'ASP', 'CB', 'TYR', 13.99), ('CG', 'ASP', 'CG', 'TYR', 12.55), ('CG', 'ASP', 'CD1', 'TYR', 12.16), ('CG', 'ASP', 'CD2', 'TYR', 11.72), ('CG', 'ASP', 'CE1', 'TYR', 10.9), ('CG', 'ASP', 'CE2', 'TYR', 10.38), ('CG', 'ASP', 'CZ', 'TYR', 9.92), ('CG', 'ASP', 'OH', 'TYR', 8.68)], [('OD1', 'ASP', 'CB', 'TYR', 13.71), ('OD1', 'ASP', 'CG', 'TYR', 12.23), ('OD1', 'ASP', 'CD1', 'TYR', 11.73), ('OD1', 'ASP', 'CD2', 'TYR', 11.48), ('OD1', 'ASP', 'CE1', 'TYR', 10.41), ('OD1', 'ASP', 'CE2', 'TYR', 10.11), ('OD1', 'ASP', 'CZ', 'TYR', 9.5), ('OD1', 'ASP', 'OH', 'TYR', 8.18)], [('OD2', 'ASP', 'CB', 'TYR', 13.49), ('OD2', 'ASP', 'CG', 'TYR', 12.09), ('OD2', 'ASP', 'CD1', 'TYR', 11.73), ('OD2', 'ASP', 'CD2', 'TYR', 11.28), ('OD2', 'ASP', 'CE1', 'TYR', 10.53), ('OD2', 'ASP', 'CE2', 'TYR', 10.0), ('OD2', 'ASP', 'CZ', 'TYR', 9.58), ('OD2', 'ASP', 'OH', 'TYR', 8.44)]]}
LYS_TYR = { 
	'distances':
		[[19.35, 17.85, 17.19, 17.21, 15.83, 15.84, 15.1, 13.75], [18.04, 16.54, 15.83, 15.96, 14.47, 14.61, 13.8, 12.46], [16.86, 15.35, 14.7, 14.72, 13.34, 13.35, 12.59, 11.23], [15.55, 14.04, 13.33, 13.5, 11.97, 12.15, 11.3, 9.97], [14.41, 12.9, 12.27, 12.26, 10.91, 10.89, 10.13, 8.77]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 19.35), ('CB', 'LYS', 'CG', 'TYR', 17.85), ('CB', 'LYS', 'CD1', 'TYR', 17.19), ('CB', 'LYS', 'CD2', 'TYR', 17.21), ('CB', 'LYS', 'CE1', 'TYR', 15.83), ('CB', 'LYS', 'CE2', 'TYR', 15.84), ('CB', 'LYS', 'CZ', 'TYR', 15.1), ('CB', 'LYS', 'OH', 'TYR', 13.75)], [('CG', 'LYS', 'CB', 'TYR', 18.04), ('CG', 'LYS', 'CG', 'TYR', 16.54), ('CG', 'LYS', 'CD1', 'TYR', 15.83), ('CG', 'LYS', 'CD2', 'TYR', 15.96), ('CG', 'LYS', 'CE1', 'TYR', 14.47), ('CG', 'LYS', 'CE2', 'TYR', 14.61), ('CG', 'LYS', 'CZ', 'TYR', 13.8), ('CG', 'LYS', 'OH', 'TYR', 12.46)], [('CD', 'LYS', 'CB', 'TYR', 16.86), ('CD', 'LYS', 'CG', 'TYR', 15.35), ('CD', 'LYS', 'CD1', 'TYR', 14.7), ('CD', 'LYS', 'CD2', 'TYR', 14.72), ('CD', 'LYS', 'CE1', 'TYR', 13.34), ('CD', 'LYS', 'CE2', 'TYR', 13.35), ('CD', 'LYS', 'CZ', 'TYR', 12.59), ('CD', 'LYS', 'OH', 'TYR', 11.23)], [('CE', 'LYS', 'CB', 'TYR', 15.55), ('CE', 'LYS', 'CG', 'TYR', 14.04), ('CE', 'LYS', 'CD1', 'TYR', 13.33), ('CE', 'LYS', 'CD2', 'TYR', 13.5), ('CE', 'LYS', 'CE1', 'TYR', 11.97), ('CE', 'LYS', 'CE2', 'TYR', 12.15), ('CE', 'LYS', 'CZ', 'TYR', 11.3), ('CE', 'LYS', 'OH', 'TYR', 9.97)], [('NZ', 'LYS', 'CB', 'TYR', 14.41), ('NZ', 'LYS', 'CG', 'TYR', 12.9), ('NZ', 'LYS', 'CD1', 'TYR', 12.27), ('NZ', 'LYS', 'CD2', 'TYR', 12.26), ('NZ', 'LYS', 'CE1', 'TYR', 10.91), ('NZ', 'LYS', 'CE2', 'TYR', 10.89), ('NZ', 'LYS', 'CZ', 'TYR', 10.13), ('NZ', 'LYS', 'OH', 'TYR', 8.77)]]}
THR_LYS = { 
	'distances':
		[[8.03, 7.3, 6.41, 6.18, 5.63], [8.2, 7.24, 6.1, 5.5, 4.58], [9.09, 8.32, 7.64, 7.24, 6.82], [13.9, 12.79, 11.65, 10.61, 9.45], [13.67, 12.57, 11.3, 10.28, 8.98], [14.56, 13.34, 12.29, 11.1, 10.07]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 8.03), ('CB', 'THR', 'CG', 'LYS', 7.3), ('CB', 'THR', 'CD', 'LYS', 6.41), ('CB', 'THR', 'CE', 'LYS', 6.18), ('CB', 'THR', 'NZ', 'LYS', 5.63)], [('OG1', 'THR', 'CB', 'LYS', 8.2), ('OG1', 'THR', 'CG', 'LYS', 7.24), ('OG1', 'THR', 'CD', 'LYS', 6.1), ('OG1', 'THR', 'CE', 'LYS', 5.5), ('OG1', 'THR', 'NZ', 'LYS', 4.58)], [('CG2', 'THR', 'CB', 'LYS', 9.09), ('CG2', 'THR', 'CG', 'LYS', 8.32), ('CG2', 'THR', 'CD', 'LYS', 7.64), ('CG2', 'THR', 'CE', 'LYS', 7.24), ('CG2', 'THR', 'NZ', 'LYS', 6.82)], [('CB', 'THR', 'CB', 'LYS', 13.9), ('CB', 'THR', 'CG', 'LYS', 12.79), ('CB', 'THR', 'CD', 'LYS', 11.65), ('CB', 'THR', 'CE', 'LYS', 10.61), ('CB', 'THR', 'NZ', 'LYS', 9.45)], [('OG1', 'THR', 'CB', 'LYS', 13.67), ('OG1', 'THR', 'CG', 'LYS', 12.57), ('OG1', 'THR', 'CD', 'LYS', 11.3), ('OG1', 'THR', 'CE', 'LYS', 10.28), ('OG1', 'THR', 'NZ', 'LYS', 8.98)], [('CG2', 'THR', 'CB', 'LYS', 14.56), ('CG2', 'THR', 'CG', 'LYS', 13.34), ('CG2', 'THR', 'CD', 'LYS', 12.29), ('CG2', 'THR', 'CE', 'LYS', 11.1), ('CG2', 'THR', 'NZ', 'LYS', 10.07)]]}
THR_TYR = { 
	'distances':
		[[14.8, 13.38, 13.12, 12.49, 11.92, 11.19, 10.87, 9.71], [13.77, 12.31, 11.96, 11.48, 10.71, 10.14, 9.7, 8.47], [14.59, 13.24, 13.04, 12.35, 11.93, 11.15, 10.91, 9.88], [8.94, 7.75, 8.02, 6.7, 7.34, 5.78, 6.18, 5.94], [8.61, 7.31, 7.52, 6.17, 6.7, 5.0, 5.37, 4.97], [8.14, 7.01, 7.19, 6.23, 6.64, 5.53, 5.77, 5.82]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'TYR', 14.8), ('CB', 'THR', 'CG', 'TYR', 13.38), ('CB', 'THR', 'CD1', 'TYR', 13.12), ('CB', 'THR', 'CD2', 'TYR', 12.49), ('CB', 'THR', 'CE1', 'TYR', 11.92), ('CB', 'THR', 'CE2', 'TYR', 11.19), ('CB', 'THR', 'CZ', 'TYR', 10.87), ('CB', 'THR', 'OH', 'TYR', 9.71)], [('OG1', 'THR', 'CB', 'TYR', 13.77), ('OG1', 'THR', 'CG', 'TYR', 12.31), ('OG1', 'THR', 'CD1', 'TYR', 11.96), ('OG1', 'THR', 'CD2', 'TYR', 11.48), ('OG1', 'THR', 'CE1', 'TYR', 10.71), ('OG1', 'THR', 'CE2', 'TYR', 10.14), ('OG1', 'THR', 'CZ', 'TYR', 9.7), ('OG1', 'THR', 'OH', 'TYR', 8.47)], [('CG2', 'THR', 'CB', 'TYR', 14.59), ('CG2', 'THR', 'CG', 'TYR', 13.24), ('CG2', 'THR', 'CD1', 'TYR', 13.04), ('CG2', 'THR', 'CD2', 'TYR', 12.35), ('CG2', 'THR', 'CE1', 'TYR', 11.93), ('CG2', 'THR', 'CE2', 'TYR', 11.15), ('CG2', 'THR', 'CZ', 'TYR', 10.91), ('CG2', 'THR', 'OH', 'TYR', 9.88)], [('CB', 'THR', 'CB', 'TYR', 8.94), ('CB', 'THR', 'CG', 'TYR', 7.75), ('CB', 'THR', 'CD1', 'TYR', 8.02), ('CB', 'THR', 'CD2', 'TYR', 6.7), ('CB', 'THR', 'CE1', 'TYR', 7.34), ('CB', 'THR', 'CE2', 'TYR', 5.78), ('CB', 'THR', 'CZ', 'TYR', 6.18), ('CB', 'THR', 'OH', 'TYR', 5.94)], [('OG1', 'THR', 'CB', 'TYR', 8.61), ('OG1', 'THR', 'CG', 'TYR', 7.31), ('OG1', 'THR', 'CD1', 'TYR', 7.52), ('OG1', 'THR', 'CD2', 'TYR', 6.17), ('OG1', 'THR', 'CE1', 'TYR', 6.7), ('OG1', 'THR', 'CE2', 'TYR', 5.0), ('OG1', 'THR', 'CZ', 'TYR', 5.37), ('OG1', 'THR', 'OH', 'TYR', 4.97)], [('CG2', 'THR', 'CB', 'TYR', 8.14), ('CG2', 'THR', 'CG', 'TYR', 7.01), ('CG2', 'THR', 'CD1', 'TYR', 7.19), ('CG2', 'THR', 'CD2', 'TYR', 6.23), ('CG2', 'THR', 'CE1', 'TYR', 6.64), ('CG2', 'THR', 'CE2', 'TYR', 5.53), ('CG2', 'THR', 'CZ', 'TYR', 5.77), ('CG2', 'THR', 'OH', 'TYR', 5.82)]]}
ASP_LYS = { 
	'distances':
		[[9.11, 8.73, 7.28, 7.52, 6.38], [9.42, 8.75, 7.24, 7.08, 5.79], [8.72, 7.87, 6.36, 5.96, 4.61], [10.58, 9.9, 8.4, 8.14, 6.82]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 9.11), ('CB', 'ASP', 'CG', 'LYS', 8.73), ('CB', 'ASP', 'CD', 'LYS', 7.28), ('CB', 'ASP', 'CE', 'LYS', 7.52), ('CB', 'ASP', 'NZ', 'LYS', 6.38)], [('CG', 'ASP', 'CB', 'LYS', 9.42), ('CG', 'ASP', 'CG', 'LYS', 8.75), ('CG', 'ASP', 'CD', 'LYS', 7.24), ('CG', 'ASP', 'CE', 'LYS', 7.08), ('CG', 'ASP', 'NZ', 'LYS', 5.79)], [('OD1', 'ASP', 'CB', 'LYS', 8.72), ('OD1', 'ASP', 'CG', 'LYS', 7.87), ('OD1', 'ASP', 'CD', 'LYS', 6.36), ('OD1', 'ASP', 'CE', 'LYS', 5.96), ('OD1', 'ASP', 'NZ', 'LYS', 4.61)], [('OD2', 'ASP', 'CB', 'LYS', 10.58), ('OD2', 'ASP', 'CG', 'LYS', 9.9), ('OD2', 'ASP', 'CD', 'LYS', 8.4), ('OD2', 'ASP', 'CE', 'LYS', 8.14), ('OD2', 'ASP', 'NZ', 'LYS', 6.82)]]}
TYR_THRI = { 
	'distances':
		[[8.94, 8.61, 8.14], [7.75, 7.31, 7.01], [8.02, 7.52, 7.19], [6.7, 6.17, 6.23], [7.34, 6.7, 6.64], [5.78, 5.0, 5.53], [6.18, 5.37, 5.77], [5.94, 4.97, 5.82]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'THRI', 8.94), ('CB', 'TYR', 'OG1', 'THRI', 8.61), ('CB', 'TYR', 'CG2', 'THRI', 8.14)], [('CG', 'TYR', 'CB', 'THRI', 7.75), ('CG', 'TYR', 'OG1', 'THRI', 7.31), ('CG', 'TYR', 'CG2', 'THRI', 7.01)], [('CD1', 'TYR', 'CB', 'THRI', 8.02), ('CD1', 'TYR', 'OG1', 'THRI', 7.52), ('CD1', 'TYR', 'CG2', 'THRI', 7.19)], [('CD2', 'TYR', 'CB', 'THRI', 6.7), ('CD2', 'TYR', 'OG1', 'THRI', 6.17), ('CD2', 'TYR', 'CG2', 'THRI', 6.23)], [('CE1', 'TYR', 'CB', 'THRI', 7.34), ('CE1', 'TYR', 'OG1', 'THRI', 6.7), ('CE1', 'TYR', 'CG2', 'THRI', 6.64)], [('CE2', 'TYR', 'CB', 'THRI', 5.78), ('CE2', 'TYR', 'OG1', 'THRI', 5.0), ('CE2', 'TYR', 'CG2', 'THRI', 5.53)], [('CZ', 'TYR', 'CB', 'THRI', 6.18), ('CZ', 'TYR', 'OG1', 'THRI', 5.37), ('CZ', 'TYR', 'CG2', 'THRI', 5.77)], [('OH', 'TYR', 'CB', 'THRI', 5.94), ('OH', 'TYR', 'OG1', 'THRI', 4.97), ('OH', 'TYR', 'CG2', 'THRI', 5.82)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_THR, d, 'A_3eca_3_5_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_THR, d, 'A_3eca_3_5_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TYR, d, 'A_3eca_3_5_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_TYR, d, 'A_3eca_3_5_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(THR_LYS, d, 'A_3eca_3_5_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_TYR, d, 'A_3eca_3_5_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASP_LYS, d, 'A_3eca_3_5_1_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(TYR_THRI, d, 'A_3eca_3_5_1_1')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_THR' :  match1,
		'ASP_THR' :  match2,
		'ASP_TYR' :  match3,
		'LYS_TYR' :  match4,
		'THR_LYS' :  match5,
		'THR_TYR' :  match6,
		'ASP_LYS' :  match7,
		'TYR_THRI' :  match8}