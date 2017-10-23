'''
FUNC:A_1uch_3_4_19_12
PDB:1uch
EC:3.4.19.12
RESI:gln,cys,his,asp
LOCI:a-89,95,169,184;
'''
import motifFunctions as cmd
HIS_GLN = { 
	'distances':
		[[11.13, 10.57, 9.07, 8.49, 8.63, 13.35, 13.3, 12.64, 13.25], [9.77, 9.34, 7.86, 7.22, 7.55, 12.04, 12.0, 11.28, 11.82], [8.63, 8.08, 6.59, 5.96, 6.33, 10.96, 10.83, 10.14, 10.79], [9.55, 9.38, 8.0, 7.27, 7.84, 11.83, 11.84, 11.04, 11.38], [7.61, 7.3, 5.88, 5.11, 5.88, 10.04, 9.91, 9.11, 9.65], [8.25, 8.19, 6.88, 6.1, 6.91, 10.61, 10.58, 9.71, 10.03]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 11.13), ('CB', 'HIS', 'CG', 'GLN', 10.57), ('CB', 'HIS', 'CD', 'GLN', 9.07), ('CB', 'HIS', 'OE1', 'GLN', 8.49), ('CB', 'HIS', 'NE2', 'GLN', 8.63), ('CB', 'HIS', 'O', 'GLN', 13.35), ('CB', 'HIS', 'C', 'GLN', 13.3), ('CB', 'HIS', 'CA', 'GLN', 12.64), ('CB', 'HIS', 'N', 'GLN', 13.25)], [('CG', 'HIS', 'CB', 'GLN', 9.77), ('CG', 'HIS', 'CG', 'GLN', 9.34), ('CG', 'HIS', 'CD', 'GLN', 7.86), ('CG', 'HIS', 'OE1', 'GLN', 7.22), ('CG', 'HIS', 'NE2', 'GLN', 7.55), ('CG', 'HIS', 'O', 'GLN', 12.04), ('CG', 'HIS', 'C', 'GLN', 12.0), ('CG', 'HIS', 'CA', 'GLN', 11.28), ('CG', 'HIS', 'N', 'GLN', 11.82)], [('ND1', 'HIS', 'CB', 'GLN', 8.63), ('ND1', 'HIS', 'CG', 'GLN', 8.08), ('ND1', 'HIS', 'CD', 'GLN', 6.59), ('ND1', 'HIS', 'OE1', 'GLN', 5.96), ('ND1', 'HIS', 'NE2', 'GLN', 6.33), ('ND1', 'HIS', 'O', 'GLN', 10.96), ('ND1', 'HIS', 'C', 'GLN', 10.83), ('ND1', 'HIS', 'CA', 'GLN', 10.14), ('ND1', 'HIS', 'N', 'GLN', 10.79)], [('CD2', 'HIS', 'CB', 'GLN', 9.55), ('CD2', 'HIS', 'CG', 'GLN', 9.38), ('CD2', 'HIS', 'CD', 'GLN', 8.0), ('CD2', 'HIS', 'OE1', 'GLN', 7.27), ('CD2', 'HIS', 'NE2', 'GLN', 7.84), ('CD2', 'HIS', 'O', 'GLN', 11.83), ('CD2', 'HIS', 'C', 'GLN', 11.84), ('CD2', 'HIS', 'CA', 'GLN', 11.04), ('CD2', 'HIS', 'N', 'GLN', 11.38)], [('CE1', 'HIS', 'CB', 'GLN', 7.61), ('CE1', 'HIS', 'CG', 'GLN', 7.3), ('CE1', 'HIS', 'CD', 'GLN', 5.88), ('CE1', 'HIS', 'OE1', 'GLN', 5.11), ('CE1', 'HIS', 'NE2', 'GLN', 5.88), ('CE1', 'HIS', 'O', 'GLN', 10.04), ('CE1', 'HIS', 'C', 'GLN', 9.91), ('CE1', 'HIS', 'CA', 'GLN', 9.11), ('CE1', 'HIS', 'N', 'GLN', 9.65)], [('NE2', 'HIS', 'CB', 'GLN', 8.25), ('NE2', 'HIS', 'CG', 'GLN', 8.19), ('NE2', 'HIS', 'CD', 'GLN', 6.88), ('NE2', 'HIS', 'OE1', 'GLN', 6.1), ('NE2', 'HIS', 'NE2', 'GLN', 6.91), ('NE2', 'HIS', 'O', 'GLN', 10.61), ('NE2', 'HIS', 'C', 'GLN', 10.58), ('NE2', 'HIS', 'CA', 'GLN', 9.71), ('NE2', 'HIS', 'N', 'GLN', 10.03)]]}
CYS_GLN = { 
	'distances':
		[[7.93, 7.23, 6.1, 5.25, 6.53, 10.62, 10.02, 9.15, 10.04], [9.58, 8.71, 7.5, 6.82, 7.58, 12.11, 11.57, 10.82, 11.77]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 7.93), ('CB', 'CYS', 'CG', 'GLN', 7.23), ('CB', 'CYS', 'CD', 'GLN', 6.1), ('CB', 'CYS', 'OE1', 'GLN', 5.25), ('CB', 'CYS', 'NE2', 'GLN', 6.53), ('CB', 'CYS', 'O', 'GLN', 10.62), ('CB', 'CYS', 'C', 'GLN', 10.02), ('CB', 'CYS', 'CA', 'GLN', 9.15), ('CB', 'CYS', 'N', 'GLN', 10.04)], [('SG', 'CYS', 'CB', 'GLN', 9.58), ('SG', 'CYS', 'CG', 'GLN', 8.71), ('SG', 'CYS', 'CD', 'GLN', 7.5), ('SG', 'CYS', 'OE1', 'GLN', 6.82), ('SG', 'CYS', 'NE2', 'GLN', 7.58), ('SG', 'CYS', 'O', 'GLN', 12.11), ('SG', 'CYS', 'C', 'GLN', 11.57), ('SG', 'CYS', 'CA', 'GLN', 10.82), ('SG', 'CYS', 'N', 'GLN', 11.77)]]}
ASP_GLN = { 
	'distances':
		[[9.71, 10.5, 9.78, 8.97, 10.24, 11.76, 11.84, 10.73, 10.25], [9.07, 9.67, 8.8, 8.09, 9.09, 11.08, 11.23, 10.25, 9.97], [7.85, 8.42, 7.59, 6.92, 7.92, 9.91, 10.03, 9.08, 8.89], [9.98, 10.43, 9.44, 8.78, 9.53, 11.88, 12.11, 11.23, 11.03]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 9.71), ('CB', 'ASP', 'CG', 'GLN', 10.5), ('CB', 'ASP', 'CD', 'GLN', 9.78), ('CB', 'ASP', 'OE1', 'GLN', 8.97), ('CB', 'ASP', 'NE2', 'GLN', 10.24), ('CB', 'ASP', 'O', 'GLN', 11.76), ('CB', 'ASP', 'C', 'GLN', 11.84), ('CB', 'ASP', 'CA', 'GLN', 10.73), ('CB', 'ASP', 'N', 'GLN', 10.25)], [('CG', 'ASP', 'CB', 'GLN', 9.07), ('CG', 'ASP', 'CG', 'GLN', 9.67), ('CG', 'ASP', 'CD', 'GLN', 8.8), ('CG', 'ASP', 'OE1', 'GLN', 8.09), ('CG', 'ASP', 'NE2', 'GLN', 9.09), ('CG', 'ASP', 'O', 'GLN', 11.08), ('CG', 'ASP', 'C', 'GLN', 11.23), ('CG', 'ASP', 'CA', 'GLN', 10.25), ('CG', 'ASP', 'N', 'GLN', 9.97)], [('OD1', 'ASP', 'CB', 'GLN', 7.85), ('OD1', 'ASP', 'CG', 'GLN', 8.42), ('OD1', 'ASP', 'CD', 'GLN', 7.59), ('OD1', 'ASP', 'OE1', 'GLN', 6.92), ('OD1', 'ASP', 'NE2', 'GLN', 7.92), ('OD1', 'ASP', 'O', 'GLN', 9.91), ('OD1', 'ASP', 'C', 'GLN', 10.03), ('OD1', 'ASP', 'CA', 'GLN', 9.08), ('OD1', 'ASP', 'N', 'GLN', 8.89)], [('OD2', 'ASP', 'CB', 'GLN', 9.98), ('OD2', 'ASP', 'CG', 'GLN', 10.43), ('OD2', 'ASP', 'CD', 'GLN', 9.44), ('OD2', 'ASP', 'OE1', 'GLN', 8.78), ('OD2', 'ASP', 'NE2', 'GLN', 9.53), ('OD2', 'ASP', 'O', 'GLN', 11.88), ('OD2', 'ASP', 'C', 'GLN', 12.11), ('OD2', 'ASP', 'CA', 'GLN', 11.23), ('OD2', 'ASP', 'N', 'GLN', 11.03)]]}
CYS_HIS = { 
	'distances':
		[[7.44, 6.69, 5.53, 7.28, 5.55, 6.67], [6.9, 6.66, 5.76, 7.6, 6.35, 7.42]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.44), ('CB', 'CYS', 'CG', 'HIS', 6.69), ('CB', 'CYS', 'ND1', 'HIS', 5.53), ('CB', 'CYS', 'CD2', 'HIS', 7.28), ('CB', 'CYS', 'CE1', 'HIS', 5.55), ('CB', 'CYS', 'NE2', 'HIS', 6.67)], [('SG', 'CYS', 'CB', 'HIS', 6.9), ('SG', 'CYS', 'CG', 'HIS', 6.66), ('SG', 'CYS', 'ND1', 'HIS', 5.76), ('SG', 'CYS', 'CD2', 'HIS', 7.6), ('SG', 'CYS', 'CE1', 'HIS', 6.35), ('SG', 'CYS', 'NE2', 'HIS', 7.42)]]}
CYS_ASP = { 
	'distances':
		[[10.23, 9.45, 8.61, 9.93], [11.35, 10.49, 9.78, 10.74]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 10.23), ('CB', 'CYS', 'CG', 'ASP', 9.45), ('CB', 'CYS', 'OD1', 'ASP', 8.61), ('CB', 'CYS', 'OD2', 'ASP', 9.93)], [('SG', 'CYS', 'CB', 'ASP', 11.35), ('SG', 'CYS', 'CG', 'ASP', 10.49), ('SG', 'CYS', 'OD1', 'ASP', 9.78), ('SG', 'CYS', 'OD2', 'ASP', 10.74)]]}
HIS_ASP = { 
	'distances':
		[[9.65, 8.47, 8.27, 8.0], [8.42, 7.19, 6.86, 6.89], [8.65, 7.43, 6.8, 7.42], [7.12, 5.89, 5.71, 5.56], [7.63, 6.45, 5.66, 6.68], [6.53, 5.3, 4.74, 5.4]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.65), ('CB', 'HIS', 'CG', 'ASP', 8.47), ('CB', 'HIS', 'OD1', 'ASP', 8.27), ('CB', 'HIS', 'OD2', 'ASP', 8.0)], [('CG', 'HIS', 'CB', 'ASP', 8.42), ('CG', 'HIS', 'CG', 'ASP', 7.19), ('CG', 'HIS', 'OD1', 'ASP', 6.86), ('CG', 'HIS', 'OD2', 'ASP', 6.89)], [('ND1', 'HIS', 'CB', 'ASP', 8.65), ('ND1', 'HIS', 'CG', 'ASP', 7.43), ('ND1', 'HIS', 'OD1', 'ASP', 6.8), ('ND1', 'HIS', 'OD2', 'ASP', 7.42)], [('CD2', 'HIS', 'CB', 'ASP', 7.12), ('CD2', 'HIS', 'CG', 'ASP', 5.89), ('CD2', 'HIS', 'OD1', 'ASP', 5.71), ('CD2', 'HIS', 'OD2', 'ASP', 5.56)], [('CE1', 'HIS', 'CB', 'ASP', 7.63), ('CE1', 'HIS', 'CG', 'ASP', 6.45), ('CE1', 'HIS', 'OD1', 'ASP', 5.66), ('CE1', 'HIS', 'OD2', 'ASP', 6.68)], [('NE2', 'HIS', 'CB', 'ASP', 6.53), ('NE2', 'HIS', 'CG', 'ASP', 5.3), ('NE2', 'HIS', 'OD1', 'ASP', 4.74), ('NE2', 'HIS', 'OD2', 'ASP', 5.4)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLN, d, 'A_1uch_3_4_19_12')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_GLN, d, 'A_1uch_3_4_19_12')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLN, d, 'A_1uch_3_4_19_12')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_HIS, d, 'A_1uch_3_4_19_12')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_ASP, d, 'A_1uch_3_4_19_12')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_ASP, d, 'A_1uch_3_4_19_12')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLN' :  match1,
		'CYS_GLN' :  match2,
		'ASP_GLN' :  match3,
		'CYS_HIS' :  match4,
		'CYS_ASP' :  match5,
		'HIS_ASP' :  match6}