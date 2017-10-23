'''
FUNC:A_1gq8_3_1_1_11
PDB:1gq8
EC:3.1.1.11
RESI:gln,gln,asp,asp
LOCI:a-113,135,136,157;
'''
import motifFunctions as cmd
ASP_GLNI = { 
	'distances':
		[[8.59, 7.47, 8.21, 9.32, 7.86], [9.12, 7.87, 8.27, 9.3, 7.74], [10.02, 8.84, 9.23, 10.18, 8.75], [8.93, 7.53, 7.66, 8.68, 6.92]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLNI', 8.59), ('CB', 'ASP', 'CG', 'GLNI', 7.47), ('CB', 'ASP', 'CD', 'GLNI', 8.21), ('CB', 'ASP', 'OE1', 'GLNI', 9.32), ('CB', 'ASP', 'NE2', 'GLNI', 7.86)], [('CG', 'ASP', 'CB', 'GLNI', 9.12), ('CG', 'ASP', 'CG', 'GLNI', 7.87), ('CG', 'ASP', 'CD', 'GLNI', 8.27), ('CG', 'ASP', 'OE1', 'GLNI', 9.3), ('CG', 'ASP', 'NE2', 'GLNI', 7.74)], [('OD1', 'ASP', 'CB', 'GLNI', 10.02), ('OD1', 'ASP', 'CG', 'GLNI', 8.84), ('OD1', 'ASP', 'CD', 'GLNI', 9.23), ('OD1', 'ASP', 'OE1', 'GLNI', 10.18), ('OD1', 'ASP', 'NE2', 'GLNI', 8.75)], [('OD2', 'ASP', 'CB', 'GLNI', 8.93), ('OD2', 'ASP', 'CG', 'GLNI', 7.53), ('OD2', 'ASP', 'CD', 'GLNI', 7.66), ('OD2', 'ASP', 'OE1', 'GLNI', 8.68), ('OD2', 'ASP', 'NE2', 'GLNI', 6.92)]]}
ASP_ASP = { 
	'distances':
		[[7.82, 8.98, 10.12, 8.94], [6.92, 7.9, 9.1, 7.69], [5.71, 6.68, 7.88, 6.55], [7.67, 8.47, 9.7, 8.07], [7.82, 6.92, 5.71, 7.67], [8.98, 7.9, 6.68, 8.47], [10.12, 9.1, 7.88, 9.7], [8.94, 7.69, 6.55, 8.07]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.82), ('CB', 'ASP', 'CG', 'ASP', 8.98), ('CB', 'ASP', 'OD1', 'ASP', 10.12), ('CB', 'ASP', 'OD2', 'ASP', 8.94)], [('CG', 'ASP', 'CB', 'ASP', 6.92), ('CG', 'ASP', 'CG', 'ASP', 7.9), ('CG', 'ASP', 'OD1', 'ASP', 9.1), ('CG', 'ASP', 'OD2', 'ASP', 7.69)], [('OD1', 'ASP', 'CB', 'ASP', 5.71), ('OD1', 'ASP', 'CG', 'ASP', 6.68), ('OD1', 'ASP', 'OD1', 'ASP', 7.88), ('OD1', 'ASP', 'OD2', 'ASP', 6.55)], [('OD2', 'ASP', 'CB', 'ASP', 7.67), ('OD2', 'ASP', 'CG', 'ASP', 8.47), ('OD2', 'ASP', 'OD1', 'ASP', 9.7), ('OD2', 'ASP', 'OD2', 'ASP', 8.07)], [('CB', 'ASP', 'CB', 'ASP', 7.82), ('CB', 'ASP', 'CG', 'ASP', 6.92), ('CB', 'ASP', 'OD1', 'ASP', 5.71), ('CB', 'ASP', 'OD2', 'ASP', 7.67)], [('CG', 'ASP', 'CB', 'ASP', 8.98), ('CG', 'ASP', 'CG', 'ASP', 7.9), ('CG', 'ASP', 'OD1', 'ASP', 6.68), ('CG', 'ASP', 'OD2', 'ASP', 8.47)], [('OD1', 'ASP', 'CB', 'ASP', 10.12), ('OD1', 'ASP', 'CG', 'ASP', 9.1), ('OD1', 'ASP', 'OD1', 'ASP', 7.88), ('OD1', 'ASP', 'OD2', 'ASP', 9.7)], [('OD2', 'ASP', 'CB', 'ASP', 8.94), ('OD2', 'ASP', 'CG', 'ASP', 7.69), ('OD2', 'ASP', 'OD1', 'ASP', 6.55), ('OD2', 'ASP', 'OD2', 'ASP', 8.07)]]}
ASP_GLN = { 
	'distances':
		[[6.6, 6.73, 8.24, 8.97, 8.89], [6.34, 5.98, 7.4, 8.29, 7.84], [7.16, 6.53, 7.78, 8.66, 8.13], [5.75, 5.31, 6.68, 7.7, 6.98], [6.81, 6.49, 7.56, 8.54, 7.68], [6.94, 6.14, 6.96, 8.08, 6.76], [6.71, 5.7, 6.58, 7.77, 6.32], [7.72, 6.82, 7.32, 8.41, 6.89], [10.6, 9.65, 10.52, 11.36, 10.56], [11.1, 9.96, 10.59, 11.39, 10.48], [12.32, 11.17, 11.75, 12.51, 11.61], [10.42, 9.17, 9.64, 10.44, 9.43]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 6.6), ('CB', 'ASP', 'CG', 'GLN', 6.73), ('CB', 'ASP', 'CD', 'GLN', 8.24), ('CB', 'ASP', 'OE1', 'GLN', 8.97), ('CB', 'ASP', 'NE2', 'GLN', 8.89)], [('CG', 'ASP', 'CB', 'GLN', 6.34), ('CG', 'ASP', 'CG', 'GLN', 5.98), ('CG', 'ASP', 'CD', 'GLN', 7.4), ('CG', 'ASP', 'OE1', 'GLN', 8.29), ('CG', 'ASP', 'NE2', 'GLN', 7.84)], [('OD1', 'ASP', 'CB', 'GLN', 7.16), ('OD1', 'ASP', 'CG', 'GLN', 6.53), ('OD1', 'ASP', 'CD', 'GLN', 7.78), ('OD1', 'ASP', 'OE1', 'GLN', 8.66), ('OD1', 'ASP', 'NE2', 'GLN', 8.13)], [('OD2', 'ASP', 'CB', 'GLN', 5.75), ('OD2', 'ASP', 'CG', 'GLN', 5.31), ('OD2', 'ASP', 'CD', 'GLN', 6.68), ('OD2', 'ASP', 'OE1', 'GLN', 7.7), ('OD2', 'ASP', 'NE2', 'GLN', 6.98)], [('CB', 'ASP', 'CB', 'GLN', 6.81), ('CB', 'ASP', 'CG', 'GLN', 6.49), ('CB', 'ASP', 'CD', 'GLN', 7.56), ('CB', 'ASP', 'OE1', 'GLN', 8.54), ('CB', 'ASP', 'NE2', 'GLN', 7.68)], [('CG', 'ASP', 'CB', 'GLN', 6.94), ('CG', 'ASP', 'CG', 'GLN', 6.14), ('CG', 'ASP', 'CD', 'GLN', 6.96), ('CG', 'ASP', 'OE1', 'GLN', 8.08), ('CG', 'ASP', 'NE2', 'GLN', 6.76)], [('OD1', 'ASP', 'CB', 'GLN', 6.71), ('OD1', 'ASP', 'CG', 'GLN', 5.7), ('OD1', 'ASP', 'CD', 'GLN', 6.58), ('OD1', 'ASP', 'OE1', 'GLN', 7.77), ('OD1', 'ASP', 'NE2', 'GLN', 6.32)], [('OD2', 'ASP', 'CB', 'GLN', 7.72), ('OD2', 'ASP', 'CG', 'GLN', 6.82), ('OD2', 'ASP', 'CD', 'GLN', 7.32), ('OD2', 'ASP', 'OE1', 'GLN', 8.41), ('OD2', 'ASP', 'NE2', 'GLN', 6.89)], [('CB', 'ASP', 'CB', 'GLN', 10.6), ('CB', 'ASP', 'CG', 'GLN', 9.65), ('CB', 'ASP', 'CD', 'GLN', 10.52), ('CB', 'ASP', 'OE1', 'GLN', 11.36), ('CB', 'ASP', 'NE2', 'GLN', 10.56)], [('CG', 'ASP', 'CB', 'GLN', 11.1), ('CG', 'ASP', 'CG', 'GLN', 9.96), ('CG', 'ASP', 'CD', 'GLN', 10.59), ('CG', 'ASP', 'OE1', 'GLN', 11.39), ('CG', 'ASP', 'NE2', 'GLN', 10.48)], [('OD1', 'ASP', 'CB', 'GLN', 12.32), ('OD1', 'ASP', 'CG', 'GLN', 11.17), ('OD1', 'ASP', 'CD', 'GLN', 11.75), ('OD1', 'ASP', 'OE1', 'GLN', 12.51), ('OD1', 'ASP', 'NE2', 'GLN', 11.61)], [('OD2', 'ASP', 'CB', 'GLN', 10.42), ('OD2', 'ASP', 'CG', 'GLN', 9.17), ('OD2', 'ASP', 'CD', 'GLN', 9.64), ('OD2', 'ASP', 'OE1', 'GLN', 10.44), ('OD2', 'ASP', 'NE2', 'GLN', 9.43)]]}
GLN_GLN = { 
	'distances':
		[[7.48, 7.05, 6.88, 7.35, 6.74], [7.38, 6.55, 6.15, 6.79, 5.65], [8.22, 7.35, 6.52, 6.92, 5.84], [8.25, 7.58, 6.58, 6.66, 6.14], [9.22, 8.16, 7.29, 7.77, 6.34], [7.48, 7.38, 8.22, 8.25, 9.22], [7.05, 6.55, 7.35, 7.58, 8.16], [6.88, 6.15, 6.52, 6.58, 7.29], [7.35, 6.79, 6.92, 6.66, 7.77], [6.74, 5.65, 5.84, 6.14, 6.34]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'GLN', 7.48), ('CB', 'GLN', 'CG', 'GLN', 7.05), ('CB', 'GLN', 'CD', 'GLN', 6.88), ('CB', 'GLN', 'OE1', 'GLN', 7.35), ('CB', 'GLN', 'NE2', 'GLN', 6.74)], [('CG', 'GLN', 'CB', 'GLN', 7.38), ('CG', 'GLN', 'CG', 'GLN', 6.55), ('CG', 'GLN', 'CD', 'GLN', 6.15), ('CG', 'GLN', 'OE1', 'GLN', 6.79), ('CG', 'GLN', 'NE2', 'GLN', 5.65)], [('CD', 'GLN', 'CB', 'GLN', 8.22), ('CD', 'GLN', 'CG', 'GLN', 7.35), ('CD', 'GLN', 'CD', 'GLN', 6.52), ('CD', 'GLN', 'OE1', 'GLN', 6.92), ('CD', 'GLN', 'NE2', 'GLN', 5.84)], [('OE1', 'GLN', 'CB', 'GLN', 8.25), ('OE1', 'GLN', 'CG', 'GLN', 7.58), ('OE1', 'GLN', 'CD', 'GLN', 6.58), ('OE1', 'GLN', 'OE1', 'GLN', 6.66), ('OE1', 'GLN', 'NE2', 'GLN', 6.14)], [('NE2', 'GLN', 'CB', 'GLN', 9.22), ('NE2', 'GLN', 'CG', 'GLN', 8.16), ('NE2', 'GLN', 'CD', 'GLN', 7.29), ('NE2', 'GLN', 'OE1', 'GLN', 7.77), ('NE2', 'GLN', 'NE2', 'GLN', 6.34)], [('CB', 'GLN', 'CB', 'GLN', 7.48), ('CB', 'GLN', 'CG', 'GLN', 7.38), ('CB', 'GLN', 'CD', 'GLN', 8.22), ('CB', 'GLN', 'OE1', 'GLN', 8.25), ('CB', 'GLN', 'NE2', 'GLN', 9.22)], [('CG', 'GLN', 'CB', 'GLN', 7.05), ('CG', 'GLN', 'CG', 'GLN', 6.55), ('CG', 'GLN', 'CD', 'GLN', 7.35), ('CG', 'GLN', 'OE1', 'GLN', 7.58), ('CG', 'GLN', 'NE2', 'GLN', 8.16)], [('CD', 'GLN', 'CB', 'GLN', 6.88), ('CD', 'GLN', 'CG', 'GLN', 6.15), ('CD', 'GLN', 'CD', 'GLN', 6.52), ('CD', 'GLN', 'OE1', 'GLN', 6.58), ('CD', 'GLN', 'NE2', 'GLN', 7.29)], [('OE1', 'GLN', 'CB', 'GLN', 7.35), ('OE1', 'GLN', 'CG', 'GLN', 6.79), ('OE1', 'GLN', 'CD', 'GLN', 6.92), ('OE1', 'GLN', 'OE1', 'GLN', 6.66), ('OE1', 'GLN', 'NE2', 'GLN', 7.77)], [('NE2', 'GLN', 'CB', 'GLN', 6.74), ('NE2', 'GLN', 'CG', 'GLN', 5.65), ('NE2', 'GLN', 'CD', 'GLN', 5.84), ('NE2', 'GLN', 'OE1', 'GLN', 6.14), ('NE2', 'GLN', 'NE2', 'GLN', 6.34)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLNI, d, 'A_1gq8_3_1_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'A_1gq8_3_1_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLN, d, 'A_1gq8_3_1_1_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_GLN, d, 'A_1gq8_3_1_1_11')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLNI' :  match1,
		'ASP_ASP' :  match2,
		'ASP_GLN' :  match3,
		'GLN_GLN' :  match4}