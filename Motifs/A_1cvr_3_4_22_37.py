'''
FUNC:A_1cvr_3_4_22_37
PDB:1cvr
EC:3.4.22.37
RESI:glu,his,gly,cys
LOCI:a-152,211,212,244;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[8.77, 8.74, 9.34, 9.8, 9.19, 8.28], [8.94, 8.52, 10.1, 10.37, 9.54, 8.72], [8.13, 7.49, 9.77, 9.86, 8.93, 8.32], [10.1, 9.48, 11.38, 11.6, 10.68, 9.82], [8.94, 7.99, 10.88, 10.86, 9.8, 9.23], [10.07, 9.18, 11.78, 11.85, 10.8, 10.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 8.77), ('CB', 'HIS', 'SG', 'CYS', 8.74), ('CB', 'HIS', 'O', 'CYS', 9.34), ('CB', 'HIS', 'C', 'CYS', 9.8), ('CB', 'HIS', 'CA', 'CYS', 9.19), ('CB', 'HIS', 'N', 'CYS', 8.28)], [('CG', 'HIS', 'CB', 'CYS', 8.94), ('CG', 'HIS', 'SG', 'CYS', 8.52), ('CG', 'HIS', 'O', 'CYS', 10.1), ('CG', 'HIS', 'C', 'CYS', 10.37), ('CG', 'HIS', 'CA', 'CYS', 9.54), ('CG', 'HIS', 'N', 'CYS', 8.72)], [('ND1', 'HIS', 'CB', 'CYS', 8.13), ('ND1', 'HIS', 'SG', 'CYS', 7.49), ('ND1', 'HIS', 'O', 'CYS', 9.77), ('ND1', 'HIS', 'C', 'CYS', 9.86), ('ND1', 'HIS', 'CA', 'CYS', 8.93), ('ND1', 'HIS', 'N', 'CYS', 8.32)], [('CD2', 'HIS', 'CB', 'CYS', 10.1), ('CD2', 'HIS', 'SG', 'CYS', 9.48), ('CD2', 'HIS', 'O', 'CYS', 11.38), ('CD2', 'HIS', 'C', 'CYS', 11.6), ('CD2', 'HIS', 'CA', 'CYS', 10.68), ('CD2', 'HIS', 'N', 'CYS', 9.82)], [('CE1', 'HIS', 'CB', 'CYS', 8.94), ('CE1', 'HIS', 'SG', 'CYS', 7.99), ('CE1', 'HIS', 'O', 'CYS', 10.88), ('CE1', 'HIS', 'C', 'CYS', 10.86), ('CE1', 'HIS', 'CA', 'CYS', 9.8), ('CE1', 'HIS', 'N', 'CYS', 9.23)], [('NE2', 'HIS', 'CB', 'CYS', 10.07), ('NE2', 'HIS', 'SG', 'CYS', 9.18), ('NE2', 'HIS', 'O', 'CYS', 11.78), ('NE2', 'HIS', 'C', 'CYS', 11.85), ('NE2', 'HIS', 'CA', 'CYS', 10.8), ('NE2', 'HIS', 'N', 'CYS', 10.08)]]}
GLY_GLU = { 
	'distances':
		[[14.78, 14.52, 13.45, 13.46, 12.79], [14.94, 14.66, 13.69, 13.81, 13.0], [14.0, 13.79, 12.95, 13.13, 12.31], [12.64, 12.47, 11.6, 11.74, 11.02]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 14.78), ('O', 'GLY', 'CG', 'GLU', 14.52), ('O', 'GLY', 'CD', 'GLU', 13.45), ('O', 'GLY', 'OE1', 'GLU', 13.46), ('O', 'GLY', 'OE2', 'GLU', 12.79)], [('C', 'GLY', 'CB', 'GLU', 14.94), ('C', 'GLY', 'CG', 'GLU', 14.66), ('C', 'GLY', 'CD', 'GLU', 13.69), ('C', 'GLY', 'OE1', 'GLU', 13.81), ('C', 'GLY', 'OE2', 'GLU', 13.0)], [('CA', 'GLY', 'CB', 'GLU', 14.0), ('CA', 'GLY', 'CG', 'GLU', 13.79), ('CA', 'GLY', 'CD', 'GLU', 12.95), ('CA', 'GLY', 'OE1', 'GLU', 13.13), ('CA', 'GLY', 'OE2', 'GLU', 12.31)], [('N', 'GLY', 'CB', 'GLU', 12.64), ('N', 'GLY', 'CG', 'GLU', 12.47), ('N', 'GLY', 'CD', 'GLU', 11.6), ('N', 'GLY', 'OE1', 'GLU', 11.74), ('N', 'GLY', 'OE2', 'GLU', 11.02)]]}
GLY_CYS = { 
	'distances':
		[[5.59, 6.78, 5.4, 5.94, 6.16, 6.22], [6.55, 7.84, 5.49, 6.36, 6.8, 6.62], [7.09, 8.22, 5.86, 6.81, 7.05, 6.43], [6.85, 7.59, 6.46, 7.15, 6.96, 6.14]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'CYS', 5.59), ('O', 'GLY', 'SG', 'CYS', 6.78), ('O', 'GLY', 'O', 'CYS', 5.4), ('O', 'GLY', 'C', 'CYS', 5.94), ('O', 'GLY', 'CA', 'CYS', 6.16), ('O', 'GLY', 'N', 'CYS', 6.22)], [('C', 'GLY', 'CB', 'CYS', 6.55), ('C', 'GLY', 'SG', 'CYS', 7.84), ('C', 'GLY', 'O', 'CYS', 5.49), ('C', 'GLY', 'C', 'CYS', 6.36), ('C', 'GLY', 'CA', 'CYS', 6.8), ('C', 'GLY', 'N', 'CYS', 6.62)], [('CA', 'GLY', 'CB', 'CYS', 7.09), ('CA', 'GLY', 'SG', 'CYS', 8.22), ('CA', 'GLY', 'O', 'CYS', 5.86), ('CA', 'GLY', 'C', 'CYS', 6.81), ('CA', 'GLY', 'CA', 'CYS', 7.05), ('CA', 'GLY', 'N', 'CYS', 6.43)], [('N', 'GLY', 'CB', 'CYS', 6.85), ('N', 'GLY', 'SG', 'CYS', 7.59), ('N', 'GLY', 'O', 'CYS', 6.46), ('N', 'GLY', 'C', 'CYS', 7.15), ('N', 'GLY', 'CA', 'CYS', 6.96), ('N', 'GLY', 'N', 'CYS', 6.14)]]}
HIS_GLU = { 
	'distances':
		[[9.87, 9.52, 8.62, 8.87, 7.98], [8.99, 8.66, 7.59, 7.67, 7.02], [9.66, 9.38, 8.17, 8.0, 7.67], [7.71, 7.33, 6.24, 6.34, 5.74], [8.99, 8.73, 7.42, 7.06, 7.05], [7.74, 7.42, 6.13, 5.87, 5.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 9.87), ('CB', 'HIS', 'CG', 'GLU', 9.52), ('CB', 'HIS', 'CD', 'GLU', 8.62), ('CB', 'HIS', 'OE1', 'GLU', 8.87), ('CB', 'HIS', 'OE2', 'GLU', 7.98)], [('CG', 'HIS', 'CB', 'GLU', 8.99), ('CG', 'HIS', 'CG', 'GLU', 8.66), ('CG', 'HIS', 'CD', 'GLU', 7.59), ('CG', 'HIS', 'OE1', 'GLU', 7.67), ('CG', 'HIS', 'OE2', 'GLU', 7.02)], [('ND1', 'HIS', 'CB', 'GLU', 9.66), ('ND1', 'HIS', 'CG', 'GLU', 9.38), ('ND1', 'HIS', 'CD', 'GLU', 8.17), ('ND1', 'HIS', 'OE1', 'GLU', 8.0), ('ND1', 'HIS', 'OE2', 'GLU', 7.67)], [('CD2', 'HIS', 'CB', 'GLU', 7.71), ('CD2', 'HIS', 'CG', 'GLU', 7.33), ('CD2', 'HIS', 'CD', 'GLU', 6.24), ('CD2', 'HIS', 'OE1', 'GLU', 6.34), ('CD2', 'HIS', 'OE2', 'GLU', 5.74)], [('CE1', 'HIS', 'CB', 'GLU', 8.99), ('CE1', 'HIS', 'CG', 'GLU', 8.73), ('CE1', 'HIS', 'CD', 'GLU', 7.42), ('CE1', 'HIS', 'OE1', 'GLU', 7.06), ('CE1', 'HIS', 'OE2', 'GLU', 7.05)], [('NE2', 'HIS', 'CB', 'GLU', 7.74), ('NE2', 'HIS', 'CG', 'GLU', 7.42), ('NE2', 'HIS', 'CD', 'GLU', 6.13), ('NE2', 'HIS', 'OE1', 'GLU', 5.87), ('NE2', 'HIS', 'OE2', 'GLU', 5.79)]]}
HIS_GLY = { 
	'distances':
		[[7.14, 7.15, 6.34, 5.05], [7.88, 8.15, 7.54, 6.17], [7.52, 8.06, 7.74, 6.4], [9.22, 9.49, 8.83, 7.46], [8.73, 9.34, 9.05, 7.7], [9.65, 10.11, 9.63, 8.24]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 7.14), ('CB', 'HIS', 'C', 'GLY', 7.15), ('CB', 'HIS', 'CA', 'GLY', 6.34), ('CB', 'HIS', 'N', 'GLY', 5.05)], [('CG', 'HIS', 'O', 'GLY', 7.88), ('CG', 'HIS', 'C', 'GLY', 8.15), ('CG', 'HIS', 'CA', 'GLY', 7.54), ('CG', 'HIS', 'N', 'GLY', 6.17)], [('ND1', 'HIS', 'O', 'GLY', 7.52), ('ND1', 'HIS', 'C', 'GLY', 8.06), ('ND1', 'HIS', 'CA', 'GLY', 7.74), ('ND1', 'HIS', 'N', 'GLY', 6.4)], [('CD2', 'HIS', 'O', 'GLY', 9.22), ('CD2', 'HIS', 'C', 'GLY', 9.49), ('CD2', 'HIS', 'CA', 'GLY', 8.83), ('CD2', 'HIS', 'N', 'GLY', 7.46)], [('CE1', 'HIS', 'O', 'GLY', 8.73), ('CE1', 'HIS', 'C', 'GLY', 9.34), ('CE1', 'HIS', 'CA', 'GLY', 9.05), ('CE1', 'HIS', 'N', 'GLY', 7.7)], [('NE2', 'HIS', 'O', 'GLY', 9.65), ('NE2', 'HIS', 'C', 'GLY', 10.11), ('NE2', 'HIS', 'CA', 'GLY', 9.63), ('NE2', 'HIS', 'N', 'GLY', 8.24)]]}
CYS_GLU = { 
	'distances':
		[[15.11, 15.19, 14.09, 13.75, 13.75], [14.19, 14.33, 13.19, 12.69, 12.95], [16.4, 16.45, 15.54, 15.43, 15.1], [16.54, 16.66, 15.7, 15.48, 15.34], [15.44, 15.63, 14.66, 14.35, 14.38], [14.37, 14.61, 13.75, 13.49, 13.51]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 15.11), ('CB', 'CYS', 'CG', 'GLU', 15.19), ('CB', 'CYS', 'CD', 'GLU', 14.09), ('CB', 'CYS', 'OE1', 'GLU', 13.75), ('CB', 'CYS', 'OE2', 'GLU', 13.75)], [('SG', 'CYS', 'CB', 'GLU', 14.19), ('SG', 'CYS', 'CG', 'GLU', 14.33), ('SG', 'CYS', 'CD', 'GLU', 13.19), ('SG', 'CYS', 'OE1', 'GLU', 12.69), ('SG', 'CYS', 'OE2', 'GLU', 12.95)], [('O', 'CYS', 'CB', 'GLU', 16.4), ('O', 'CYS', 'CG', 'GLU', 16.45), ('O', 'CYS', 'CD', 'GLU', 15.54), ('O', 'CYS', 'OE1', 'GLU', 15.43), ('O', 'CYS', 'OE2', 'GLU', 15.1)], [('C', 'CYS', 'CB', 'GLU', 16.54), ('C', 'CYS', 'CG', 'GLU', 16.66), ('C', 'CYS', 'CD', 'GLU', 15.7), ('C', 'CYS', 'OE1', 'GLU', 15.48), ('C', 'CYS', 'OE2', 'GLU', 15.34)], [('CA', 'CYS', 'CB', 'GLU', 15.44), ('CA', 'CYS', 'CG', 'GLU', 15.63), ('CA', 'CYS', 'CD', 'GLU', 14.66), ('CA', 'CYS', 'OE1', 'GLU', 14.35), ('CA', 'CYS', 'OE2', 'GLU', 14.38)], [('N', 'CYS', 'CB', 'GLU', 14.37), ('N', 'CYS', 'CG', 'GLU', 14.61), ('N', 'CYS', 'CD', 'GLU', 13.75), ('N', 'CYS', 'OE1', 'GLU', 13.49), ('N', 'CYS', 'OE2', 'GLU', 13.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1cvr_3_4_22_37')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_GLU, d, 'A_1cvr_3_4_22_37')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_CYS, d, 'A_1cvr_3_4_22_37')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_1cvr_3_4_22_37')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_GLY, d, 'A_1cvr_3_4_22_37')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_GLU, d, 'A_1cvr_3_4_22_37')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'GLY_GLU' :  match2,
		'GLY_CYS' :  match3,
		'HIS_GLU' :  match4,
		'HIS_GLY' :  match5,
		'CYS_GLU' :  match6}