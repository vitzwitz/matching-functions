'''
FUNC:A_1cd5_3_5_99_6
PDB:1cd5
EC:3.5.99.6
RESI:asp,asp,his,glu
LOCI:a-72,141,143,148;
'''
import motifFunctions as cmd
ASP_ASP = { 
	'distances':
		[[18.72, 17.96, 18.64, 16.77], [17.26, 16.54, 17.25, 15.36], [16.33, 15.56, 16.23, 14.36], [17.1, 16.49, 17.25, 15.33], [18.72, 17.26, 16.33, 17.1], [17.96, 16.54, 15.56, 16.49], [18.64, 17.25, 16.23, 17.25], [16.77, 15.36, 14.36, 15.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 18.72), ('CB', 'ASP', 'CG', 'ASP', 17.96), ('CB', 'ASP', 'OD1', 'ASP', 18.64), ('CB', 'ASP', 'OD2', 'ASP', 16.77)], [('CG', 'ASP', 'CB', 'ASP', 17.26), ('CG', 'ASP', 'CG', 'ASP', 16.54), ('CG', 'ASP', 'OD1', 'ASP', 17.25), ('CG', 'ASP', 'OD2', 'ASP', 15.36)], [('OD1', 'ASP', 'CB', 'ASP', 16.33), ('OD1', 'ASP', 'CG', 'ASP', 15.56), ('OD1', 'ASP', 'OD1', 'ASP', 16.23), ('OD1', 'ASP', 'OD2', 'ASP', 14.36)], [('OD2', 'ASP', 'CB', 'ASP', 17.1), ('OD2', 'ASP', 'CG', 'ASP', 16.49), ('OD2', 'ASP', 'OD1', 'ASP', 17.25), ('OD2', 'ASP', 'OD2', 'ASP', 15.33)], [('CB', 'ASP', 'CB', 'ASP', 18.72), ('CB', 'ASP', 'CG', 'ASP', 17.26), ('CB', 'ASP', 'OD1', 'ASP', 16.33), ('CB', 'ASP', 'OD2', 'ASP', 17.1)], [('CG', 'ASP', 'CB', 'ASP', 17.96), ('CG', 'ASP', 'CG', 'ASP', 16.54), ('CG', 'ASP', 'OD1', 'ASP', 15.56), ('CG', 'ASP', 'OD2', 'ASP', 16.49)], [('OD1', 'ASP', 'CB', 'ASP', 18.64), ('OD1', 'ASP', 'CG', 'ASP', 17.25), ('OD1', 'ASP', 'OD1', 'ASP', 16.23), ('OD1', 'ASP', 'OD2', 'ASP', 17.25)], [('OD2', 'ASP', 'CB', 'ASP', 16.77), ('OD2', 'ASP', 'CG', 'ASP', 15.36), ('OD2', 'ASP', 'OD1', 'ASP', 14.36), ('OD2', 'ASP', 'OD2', 'ASP', 15.33)]]}
ASP_GLU = { 
	'distances':
		[[11.19, 11.01, 11.84, 11.55, 12.95], [10.04, 9.84, 10.55, 10.16, 11.7], [10.18, 10.1, 10.69, 10.14, 11.88], [9.16, 8.81, 9.53, 9.21, 10.63], [15.12, 15.32, 14.27, 13.18, 14.67], [15.23, 15.41, 14.44, 13.29, 14.97], [16.38, 16.52, 15.55, 14.37, 16.08], [14.27, 14.49, 13.59, 12.42, 14.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 11.19), ('CB', 'ASP', 'CG', 'GLU', 11.01), ('CB', 'ASP', 'CD', 'GLU', 11.84), ('CB', 'ASP', 'OE1', 'GLU', 11.55), ('CB', 'ASP', 'OE2', 'GLU', 12.95)], [('CG', 'ASP', 'CB', 'GLU', 10.04), ('CG', 'ASP', 'CG', 'GLU', 9.84), ('CG', 'ASP', 'CD', 'GLU', 10.55), ('CG', 'ASP', 'OE1', 'GLU', 10.16), ('CG', 'ASP', 'OE2', 'GLU', 11.7)], [('OD1', 'ASP', 'CB', 'GLU', 10.18), ('OD1', 'ASP', 'CG', 'GLU', 10.1), ('OD1', 'ASP', 'CD', 'GLU', 10.69), ('OD1', 'ASP', 'OE1', 'GLU', 10.14), ('OD1', 'ASP', 'OE2', 'GLU', 11.88)], [('OD2', 'ASP', 'CB', 'GLU', 9.16), ('OD2', 'ASP', 'CG', 'GLU', 8.81), ('OD2', 'ASP', 'CD', 'GLU', 9.53), ('OD2', 'ASP', 'OE1', 'GLU', 9.21), ('OD2', 'ASP', 'OE2', 'GLU', 10.63)], [('CB', 'ASP', 'CB', 'GLU', 15.12), ('CB', 'ASP', 'CG', 'GLU', 15.32), ('CB', 'ASP', 'CD', 'GLU', 14.27), ('CB', 'ASP', 'OE1', 'GLU', 13.18), ('CB', 'ASP', 'OE2', 'GLU', 14.67)], [('CG', 'ASP', 'CB', 'GLU', 15.23), ('CG', 'ASP', 'CG', 'GLU', 15.41), ('CG', 'ASP', 'CD', 'GLU', 14.44), ('CG', 'ASP', 'OE1', 'GLU', 13.29), ('CG', 'ASP', 'OE2', 'GLU', 14.97)], [('OD1', 'ASP', 'CB', 'GLU', 16.38), ('OD1', 'ASP', 'CG', 'GLU', 16.52), ('OD1', 'ASP', 'CD', 'GLU', 15.55), ('OD1', 'ASP', 'OE1', 'GLU', 14.37), ('OD1', 'ASP', 'OE2', 'GLU', 16.08)], [('OD2', 'ASP', 'CB', 'GLU', 14.27), ('OD2', 'ASP', 'CG', 'GLU', 14.49), ('OD2', 'ASP', 'CD', 'GLU', 13.59), ('OD2', 'ASP', 'OE1', 'GLU', 12.42), ('OD2', 'ASP', 'OE2', 'GLU', 14.21)]]}
HIS_ASP = { 
	'distances':
		[[7.52, 6.29, 5.51, 6.46], [7.76, 6.36, 5.45, 6.46], [6.99, 5.53, 4.65, 5.61], [9.0, 7.58, 6.62, 7.64], [7.94, 6.52, 5.66, 6.55], [9.07, 7.64, 6.7, 7.66], [14.03, 13.43, 14.28, 12.21], [13.13, 12.47, 13.27, 11.26], [13.73, 13.02, 13.75, 11.84], [11.81, 11.12, 11.92, 9.91], [12.92, 12.15, 12.82, 11.0], [11.69, 10.92, 11.62, 9.75]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.52), ('CB', 'HIS', 'CG', 'ASP', 6.29), ('CB', 'HIS', 'OD1', 'ASP', 5.51), ('CB', 'HIS', 'OD2', 'ASP', 6.46)], [('CG', 'HIS', 'CB', 'ASP', 7.76), ('CG', 'HIS', 'CG', 'ASP', 6.36), ('CG', 'HIS', 'OD1', 'ASP', 5.45), ('CG', 'HIS', 'OD2', 'ASP', 6.46)], [('ND1', 'HIS', 'CB', 'ASP', 6.99), ('ND1', 'HIS', 'CG', 'ASP', 5.53), ('ND1', 'HIS', 'OD1', 'ASP', 4.65), ('ND1', 'HIS', 'OD2', 'ASP', 5.61)], [('CD2', 'HIS', 'CB', 'ASP', 9.0), ('CD2', 'HIS', 'CG', 'ASP', 7.58), ('CD2', 'HIS', 'OD1', 'ASP', 6.62), ('CD2', 'HIS', 'OD2', 'ASP', 7.64)], [('CE1', 'HIS', 'CB', 'ASP', 7.94), ('CE1', 'HIS', 'CG', 'ASP', 6.52), ('CE1', 'HIS', 'OD1', 'ASP', 5.66), ('CE1', 'HIS', 'OD2', 'ASP', 6.55)], [('NE2', 'HIS', 'CB', 'ASP', 9.07), ('NE2', 'HIS', 'CG', 'ASP', 7.64), ('NE2', 'HIS', 'OD1', 'ASP', 6.7), ('NE2', 'HIS', 'OD2', 'ASP', 7.66)], [('CB', 'HIS', 'CB', 'ASP', 14.03), ('CB', 'HIS', 'CG', 'ASP', 13.43), ('CB', 'HIS', 'OD1', 'ASP', 14.28), ('CB', 'HIS', 'OD2', 'ASP', 12.21)], [('CG', 'HIS', 'CB', 'ASP', 13.13), ('CG', 'HIS', 'CG', 'ASP', 12.47), ('CG', 'HIS', 'OD1', 'ASP', 13.27), ('CG', 'HIS', 'OD2', 'ASP', 11.26)], [('ND1', 'HIS', 'CB', 'ASP', 13.73), ('ND1', 'HIS', 'CG', 'ASP', 13.02), ('ND1', 'HIS', 'OD1', 'ASP', 13.75), ('ND1', 'HIS', 'OD2', 'ASP', 11.84)], [('CD2', 'HIS', 'CB', 'ASP', 11.81), ('CD2', 'HIS', 'CG', 'ASP', 11.12), ('CD2', 'HIS', 'OD1', 'ASP', 11.92), ('CD2', 'HIS', 'OD2', 'ASP', 9.91)], [('CE1', 'HIS', 'CB', 'ASP', 12.92), ('CE1', 'HIS', 'CG', 'ASP', 12.15), ('CE1', 'HIS', 'OD1', 'ASP', 12.82), ('CE1', 'HIS', 'OD2', 'ASP', 11.0)], [('NE2', 'HIS', 'CB', 'ASP', 11.69), ('NE2', 'HIS', 'CG', 'ASP', 10.92), ('NE2', 'HIS', 'OD1', 'ASP', 11.62), ('NE2', 'HIS', 'OD2', 'ASP', 9.75)]]}
HIS_GLU = { 
	'distances':
		[[8.29, 8.76, 9.27, 8.63, 10.53], [8.65, 8.86, 9.09, 8.25, 10.32], [9.12, 9.04, 9.24, 8.4, 10.44], [9.07, 9.27, 9.24, 8.24, 10.41], [9.77, 9.56, 9.49, 8.51, 10.62], [9.74, 9.69, 9.48, 8.4, 10.6]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.29), ('CB', 'HIS', 'CG', 'GLU', 8.76), ('CB', 'HIS', 'CD', 'GLU', 9.27), ('CB', 'HIS', 'OE1', 'GLU', 8.63), ('CB', 'HIS', 'OE2', 'GLU', 10.53)], [('CG', 'HIS', 'CB', 'GLU', 8.65), ('CG', 'HIS', 'CG', 'GLU', 8.86), ('CG', 'HIS', 'CD', 'GLU', 9.09), ('CG', 'HIS', 'OE1', 'GLU', 8.25), ('CG', 'HIS', 'OE2', 'GLU', 10.32)], [('ND1', 'HIS', 'CB', 'GLU', 9.12), ('ND1', 'HIS', 'CG', 'GLU', 9.04), ('ND1', 'HIS', 'CD', 'GLU', 9.24), ('ND1', 'HIS', 'OE1', 'GLU', 8.4), ('ND1', 'HIS', 'OE2', 'GLU', 10.44)], [('CD2', 'HIS', 'CB', 'GLU', 9.07), ('CD2', 'HIS', 'CG', 'GLU', 9.27), ('CD2', 'HIS', 'CD', 'GLU', 9.24), ('CD2', 'HIS', 'OE1', 'GLU', 8.24), ('CD2', 'HIS', 'OE2', 'GLU', 10.41)], [('CE1', 'HIS', 'CB', 'GLU', 9.77), ('CE1', 'HIS', 'CG', 'GLU', 9.56), ('CE1', 'HIS', 'CD', 'GLU', 9.49), ('CE1', 'HIS', 'OE1', 'GLU', 8.51), ('CE1', 'HIS', 'OE2', 'GLU', 10.62)], [('NE2', 'HIS', 'CB', 'GLU', 9.74), ('NE2', 'HIS', 'CG', 'GLU', 9.69), ('NE2', 'HIS', 'CD', 'GLU', 9.48), ('NE2', 'HIS', 'OE1', 'GLU', 8.4), ('NE2', 'HIS', 'OE2', 'GLU', 10.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASP, d, 'A_1cd5_3_5_99_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLU, d, 'A_1cd5_3_5_99_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1cd5_3_5_99_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_1cd5_3_5_99_6')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASP' :  match1,
		'ASP_GLU' :  match2,
		'HIS_ASP' :  match3,
		'HIS_GLU' :  match4}