'''
FUNC:P_1ndw_3_5_4_4
PDB:1ndw
EC:3.5.4.4
RESI:glu,his,tyr,asp
LOCI:a-217,238,240,295;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[10.56, 9.82, 9.15, 10.18], [9.12, 8.33, 7.63, 8.71], [8.16, 7.54, 6.81, 8.13], [8.68, 7.67, 7.01, 7.87], [7.03, 6.29, 5.53, 6.9], [7.37, 6.32, 5.62, 6.62]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 10.56), ('CB', 'HIS', 'CG', 'ASP', 9.82), ('CB', 'HIS', 'OD1', 'ASP', 9.15), ('CB', 'HIS', 'OD2', 'ASP', 10.18)], [('CG', 'HIS', 'CB', 'ASP', 9.12), ('CG', 'HIS', 'CG', 'ASP', 8.33), ('CG', 'HIS', 'OD1', 'ASP', 7.63), ('CG', 'HIS', 'OD2', 'ASP', 8.71)], [('ND1', 'HIS', 'CB', 'ASP', 8.16), ('ND1', 'HIS', 'CG', 'ASP', 7.54), ('ND1', 'HIS', 'OD1', 'ASP', 6.81), ('ND1', 'HIS', 'OD2', 'ASP', 8.13)], [('CD2', 'HIS', 'CB', 'ASP', 8.68), ('CD2', 'HIS', 'CG', 'ASP', 7.67), ('CD2', 'HIS', 'OD1', 'ASP', 7.01), ('CD2', 'HIS', 'OD2', 'ASP', 7.87)], [('CE1', 'HIS', 'CB', 'ASP', 7.03), ('CE1', 'HIS', 'CG', 'ASP', 6.29), ('CE1', 'HIS', 'OD1', 'ASP', 5.53), ('CE1', 'HIS', 'OD2', 'ASP', 6.9)], [('NE2', 'HIS', 'CB', 'ASP', 7.37), ('NE2', 'HIS', 'CG', 'ASP', 6.32), ('NE2', 'HIS', 'OD1', 'ASP', 5.62), ('NE2', 'HIS', 'OD2', 'ASP', 6.62)]]}
GLU_TYR = { 
	'distances':
		[[8.39, 7.83, 8.64, 6.8, 8.5, 6.68, 7.63, 8.06], [8.84, 8.07, 8.87, 6.82, 8.56, 6.4, 7.44, 7.66], [10.3, 9.43, 10.09, 8.18, 9.58, 7.54, 8.38, 8.3], [10.94, 10.13, 10.75, 8.97, 10.24, 8.39, 9.13, 9.03], [11.0, 10.01, 10.6, 8.71, 9.96, 7.89, 8.66, 8.38]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 8.39), ('CB', 'GLU', 'CG', 'TYR', 7.83), ('CB', 'GLU', 'CD1', 'TYR', 8.64), ('CB', 'GLU', 'CD2', 'TYR', 6.8), ('CB', 'GLU', 'CE1', 'TYR', 8.5), ('CB', 'GLU', 'CE2', 'TYR', 6.68), ('CB', 'GLU', 'CZ', 'TYR', 7.63), ('CB', 'GLU', 'OH', 'TYR', 8.06)], [('CG', 'GLU', 'CB', 'TYR', 8.84), ('CG', 'GLU', 'CG', 'TYR', 8.07), ('CG', 'GLU', 'CD1', 'TYR', 8.87), ('CG', 'GLU', 'CD2', 'TYR', 6.82), ('CG', 'GLU', 'CE1', 'TYR', 8.56), ('CG', 'GLU', 'CE2', 'TYR', 6.4), ('CG', 'GLU', 'CZ', 'TYR', 7.44), ('CG', 'GLU', 'OH', 'TYR', 7.66)], [('CD', 'GLU', 'CB', 'TYR', 10.3), ('CD', 'GLU', 'CG', 'TYR', 9.43), ('CD', 'GLU', 'CD1', 'TYR', 10.09), ('CD', 'GLU', 'CD2', 'TYR', 8.18), ('CD', 'GLU', 'CE1', 'TYR', 9.58), ('CD', 'GLU', 'CE2', 'TYR', 7.54), ('CD', 'GLU', 'CZ', 'TYR', 8.38), ('CD', 'GLU', 'OH', 'TYR', 8.3)], [('OE1', 'GLU', 'CB', 'TYR', 10.94), ('OE1', 'GLU', 'CG', 'TYR', 10.13), ('OE1', 'GLU', 'CD1', 'TYR', 10.75), ('OE1', 'GLU', 'CD2', 'TYR', 8.97), ('OE1', 'GLU', 'CE1', 'TYR', 10.24), ('OE1', 'GLU', 'CE2', 'TYR', 8.39), ('OE1', 'GLU', 'CZ', 'TYR', 9.13), ('OE1', 'GLU', 'OH', 'TYR', 9.03)], [('OE2', 'GLU', 'CB', 'TYR', 11.0), ('OE2', 'GLU', 'CG', 'TYR', 10.01), ('OE2', 'GLU', 'CD1', 'TYR', 10.6), ('OE2', 'GLU', 'CD2', 'TYR', 8.71), ('OE2', 'GLU', 'CE1', 'TYR', 9.96), ('OE2', 'GLU', 'CE2', 'TYR', 7.89), ('OE2', 'GLU', 'CZ', 'TYR', 8.66), ('OE2', 'GLU', 'OH', 'TYR', 8.38)]]}
GLU_HIS = { 
	'distances':
		[[5.7, 5.6, 6.31, 5.57, 6.7, 6.3], [6.31, 5.78, 5.96, 5.75, 6.12, 5.97], [7.07, 6.15, 6.2, 5.65, 5.87, 5.47], [7.28, 6.37, 6.69, 5.56, 6.28, 5.5], [7.82, 6.71, 6.41, 6.22, 5.82, 5.62]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 5.7), ('CB', 'GLU', 'CG', 'HIS', 5.6), ('CB', 'GLU', 'ND1', 'HIS', 6.31), ('CB', 'GLU', 'CD2', 'HIS', 5.57), ('CB', 'GLU', 'CE1', 'HIS', 6.7), ('CB', 'GLU', 'NE2', 'HIS', 6.3)], [('CG', 'GLU', 'CB', 'HIS', 6.31), ('CG', 'GLU', 'CG', 'HIS', 5.78), ('CG', 'GLU', 'ND1', 'HIS', 5.96), ('CG', 'GLU', 'CD2', 'HIS', 5.75), ('CG', 'GLU', 'CE1', 'HIS', 6.12), ('CG', 'GLU', 'NE2', 'HIS', 5.97)], [('CD', 'GLU', 'CB', 'HIS', 7.07), ('CD', 'GLU', 'CG', 'HIS', 6.15), ('CD', 'GLU', 'ND1', 'HIS', 6.2), ('CD', 'GLU', 'CD2', 'HIS', 5.65), ('CD', 'GLU', 'CE1', 'HIS', 5.87), ('CD', 'GLU', 'NE2', 'HIS', 5.47)], [('OE1', 'GLU', 'CB', 'HIS', 7.28), ('OE1', 'GLU', 'CG', 'HIS', 6.37), ('OE1', 'GLU', 'ND1', 'HIS', 6.69), ('OE1', 'GLU', 'CD2', 'HIS', 5.56), ('OE1', 'GLU', 'CE1', 'HIS', 6.28), ('OE1', 'GLU', 'NE2', 'HIS', 5.5)], [('OE2', 'GLU', 'CB', 'HIS', 7.82), ('OE2', 'GLU', 'CG', 'HIS', 6.71), ('OE2', 'GLU', 'ND1', 'HIS', 6.41), ('OE2', 'GLU', 'CD2', 'HIS', 6.22), ('OE2', 'GLU', 'CE1', 'HIS', 5.82), ('OE2', 'GLU', 'NE2', 'HIS', 5.62)]]}
HIS_TYR = { 
	'distances':
		[[7.3, 6.27, 6.29, 5.87, 5.76, 5.43, 5.34, 5.7], [8.46, 7.27, 7.28, 6.58, 6.46, 5.73, 5.65, 5.48], [8.78, 7.4, 7.33, 6.59, 6.29, 5.42, 5.21, 4.62], [9.64, 8.53, 8.62, 7.76, 7.81, 6.93, 6.95, 6.64], [10.0, 8.64, 8.6, 7.73, 7.51, 6.51, 6.38, 5.57], [10.52, 9.28, 9.33, 8.38, 8.36, 7.34, 7.33, 6.7]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 7.3), ('CB', 'HIS', 'CG', 'TYR', 6.27), ('CB', 'HIS', 'CD1', 'TYR', 6.29), ('CB', 'HIS', 'CD2', 'TYR', 5.87), ('CB', 'HIS', 'CE1', 'TYR', 5.76), ('CB', 'HIS', 'CE2', 'TYR', 5.43), ('CB', 'HIS', 'CZ', 'TYR', 5.34), ('CB', 'HIS', 'OH', 'TYR', 5.7)], [('CG', 'HIS', 'CB', 'TYR', 8.46), ('CG', 'HIS', 'CG', 'TYR', 7.27), ('CG', 'HIS', 'CD1', 'TYR', 7.28), ('CG', 'HIS', 'CD2', 'TYR', 6.58), ('CG', 'HIS', 'CE1', 'TYR', 6.46), ('CG', 'HIS', 'CE2', 'TYR', 5.73), ('CG', 'HIS', 'CZ', 'TYR', 5.65), ('CG', 'HIS', 'OH', 'TYR', 5.48)], [('ND1', 'HIS', 'CB', 'TYR', 8.78), ('ND1', 'HIS', 'CG', 'TYR', 7.4), ('ND1', 'HIS', 'CD1', 'TYR', 7.33), ('ND1', 'HIS', 'CD2', 'TYR', 6.59), ('ND1', 'HIS', 'CE1', 'TYR', 6.29), ('ND1', 'HIS', 'CE2', 'TYR', 5.42), ('ND1', 'HIS', 'CZ', 'TYR', 5.21), ('ND1', 'HIS', 'OH', 'TYR', 4.62)], [('CD2', 'HIS', 'CB', 'TYR', 9.64), ('CD2', 'HIS', 'CG', 'TYR', 8.53), ('CD2', 'HIS', 'CD1', 'TYR', 8.62), ('CD2', 'HIS', 'CD2', 'TYR', 7.76), ('CD2', 'HIS', 'CE1', 'TYR', 7.81), ('CD2', 'HIS', 'CE2', 'TYR', 6.93), ('CD2', 'HIS', 'CZ', 'TYR', 6.95), ('CD2', 'HIS', 'OH', 'TYR', 6.64)], [('CE1', 'HIS', 'CB', 'TYR', 10.0), ('CE1', 'HIS', 'CG', 'TYR', 8.64), ('CE1', 'HIS', 'CD1', 'TYR', 8.6), ('CE1', 'HIS', 'CD2', 'TYR', 7.73), ('CE1', 'HIS', 'CE1', 'TYR', 7.51), ('CE1', 'HIS', 'CE2', 'TYR', 6.51), ('CE1', 'HIS', 'CZ', 'TYR', 6.38), ('CE1', 'HIS', 'OH', 'TYR', 5.57)], [('NE2', 'HIS', 'CB', 'TYR', 10.52), ('NE2', 'HIS', 'CG', 'TYR', 9.28), ('NE2', 'HIS', 'CD1', 'TYR', 9.33), ('NE2', 'HIS', 'CD2', 'TYR', 8.38), ('NE2', 'HIS', 'CE1', 'TYR', 8.36), ('NE2', 'HIS', 'CE2', 'TYR', 7.34), ('NE2', 'HIS', 'CZ', 'TYR', 7.33), ('NE2', 'HIS', 'OH', 'TYR', 6.7)]]}
TYR_ASP = { 
	'distances':
		[[14.72, 14.24, 13.36, 14.9], [13.23, 12.83, 11.98, 13.52], [12.94, 12.67, 11.96, 13.35], [12.36, 11.88, 10.95, 12.61], [11.62, 11.43, 10.8, 12.12], [10.98, 10.57, 9.66, 11.35], [10.57, 10.33, 9.59, 11.08], [9.27, 9.16, 8.53, 9.95]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 14.72), ('CB', 'TYR', 'CG', 'ASP', 14.24), ('CB', 'TYR', 'OD1', 'ASP', 13.36), ('CB', 'TYR', 'OD2', 'ASP', 14.9)], [('CG', 'TYR', 'CB', 'ASP', 13.23), ('CG', 'TYR', 'CG', 'ASP', 12.83), ('CG', 'TYR', 'OD1', 'ASP', 11.98), ('CG', 'TYR', 'OD2', 'ASP', 13.52)], [('CD1', 'TYR', 'CB', 'ASP', 12.94), ('CD1', 'TYR', 'CG', 'ASP', 12.67), ('CD1', 'TYR', 'OD1', 'ASP', 11.96), ('CD1', 'TYR', 'OD2', 'ASP', 13.35)], [('CD2', 'TYR', 'CB', 'ASP', 12.36), ('CD2', 'TYR', 'CG', 'ASP', 11.88), ('CD2', 'TYR', 'OD1', 'ASP', 10.95), ('CD2', 'TYR', 'OD2', 'ASP', 12.61)], [('CE1', 'TYR', 'CB', 'ASP', 11.62), ('CE1', 'TYR', 'CG', 'ASP', 11.43), ('CE1', 'TYR', 'OD1', 'ASP', 10.8), ('CE1', 'TYR', 'OD2', 'ASP', 12.12)], [('CE2', 'TYR', 'CB', 'ASP', 10.98), ('CE2', 'TYR', 'CG', 'ASP', 10.57), ('CE2', 'TYR', 'OD1', 'ASP', 9.66), ('CE2', 'TYR', 'OD2', 'ASP', 11.35)], [('CZ', 'TYR', 'CB', 'ASP', 10.57), ('CZ', 'TYR', 'CG', 'ASP', 10.33), ('CZ', 'TYR', 'OD1', 'ASP', 9.59), ('CZ', 'TYR', 'OD2', 'ASP', 11.08)], [('OH', 'TYR', 'CB', 'ASP', 9.27), ('OH', 'TYR', 'CG', 'ASP', 9.16), ('OH', 'TYR', 'OD1', 'ASP', 8.53), ('OH', 'TYR', 'OD2', 'ASP', 9.95)]]}
GLU_ASP = { 
	'distances':
		[[11.36, 10.25, 9.22, 10.61], [10.44, 9.39, 8.25, 9.92], [9.54, 8.35, 7.2, 8.79], [9.77, 8.44, 7.42, 8.67], [8.76, 7.63, 6.41, 8.2]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 11.36), ('CB', 'GLU', 'CG', 'ASP', 10.25), ('CB', 'GLU', 'OD1', 'ASP', 9.22), ('CB', 'GLU', 'OD2', 'ASP', 10.61)], [('CG', 'GLU', 'CB', 'ASP', 10.44), ('CG', 'GLU', 'CG', 'ASP', 9.39), ('CG', 'GLU', 'OD1', 'ASP', 8.25), ('CG', 'GLU', 'OD2', 'ASP', 9.92)], [('CD', 'GLU', 'CB', 'ASP', 9.54), ('CD', 'GLU', 'CG', 'ASP', 8.35), ('CD', 'GLU', 'OD1', 'ASP', 7.2), ('CD', 'GLU', 'OD2', 'ASP', 8.79)], [('OE1', 'GLU', 'CB', 'ASP', 9.77), ('OE1', 'GLU', 'CG', 'ASP', 8.44), ('OE1', 'GLU', 'OD1', 'ASP', 7.42), ('OE1', 'GLU', 'OD2', 'ASP', 8.67)], [('OE2', 'GLU', 'CB', 'ASP', 8.76), ('OE2', 'GLU', 'CG', 'ASP', 7.63), ('OE2', 'GLU', 'OD1', 'ASP', 6.41), ('OE2', 'GLU', 'OD2', 'ASP', 8.2)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'P_1ndw_3_5_4_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_TYR, d, 'P_1ndw_3_5_4_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'P_1ndw_3_5_4_4')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_TYR, d, 'P_1ndw_3_5_4_4')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_ASP, d, 'P_1ndw_3_5_4_4')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_ASP, d, 'P_1ndw_3_5_4_4')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'GLU_TYR' :  match2,
		'GLU_HIS' :  match3,
		'HIS_TYR' :  match4,
		'TYR_ASP' :  match5,
		'GLU_ASP' :  match6}