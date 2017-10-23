'''
FUNC:A_1odt_3_1_1_41
PDB:1odt
EC:3.1.1.41
RESI:ala,gln,asp,his
LOCI:c-181,182,269,298;
'''
import motifFunctions as cmd
HIS_ALA = { 
	'distances':
		[[8.7], [7.27], [6.68], [6.57], [5.48], [5.36]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ALA', 8.7)], [('CG', 'HIS', 'CB', 'ALA', 7.27)], [('ND1', 'HIS', 'CB', 'ALA', 6.68)], [('CD2', 'HIS', 'CB', 'ALA', 6.57)], [('CE1', 'HIS', 'CB', 'ALA', 5.48)], [('NE2', 'HIS', 'CB', 'ALA', 5.36)]]}
HIS_ASP = { 
	'distances':
		[[6.69, 5.65, 5.44, 5.54], [7.26, 5.93, 5.61, 5.52], [6.79, 5.32, 5.09, 4.71], [8.59, 7.21, 6.81, 6.74], [7.94, 6.44, 6.15, 5.76], [8.92, 7.44, 7.04, 6.83]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.69), ('CB', 'HIS', 'CG', 'ASP', 5.65), ('CB', 'HIS', 'OD1', 'ASP', 5.44), ('CB', 'HIS', 'OD2', 'ASP', 5.54)], [('CG', 'HIS', 'CB', 'ASP', 7.26), ('CG', 'HIS', 'CG', 'ASP', 5.93), ('CG', 'HIS', 'OD1', 'ASP', 5.61), ('CG', 'HIS', 'OD2', 'ASP', 5.52)], [('ND1', 'HIS', 'CB', 'ASP', 6.79), ('ND1', 'HIS', 'CG', 'ASP', 5.32), ('ND1', 'HIS', 'OD1', 'ASP', 5.09), ('ND1', 'HIS', 'OD2', 'ASP', 4.71)], [('CD2', 'HIS', 'CB', 'ASP', 8.59), ('CD2', 'HIS', 'CG', 'ASP', 7.21), ('CD2', 'HIS', 'OD1', 'ASP', 6.81), ('CD2', 'HIS', 'OD2', 'ASP', 6.74)], [('CE1', 'HIS', 'CB', 'ASP', 7.94), ('CE1', 'HIS', 'CG', 'ASP', 6.44), ('CE1', 'HIS', 'OD1', 'ASP', 6.15), ('CE1', 'HIS', 'OD2', 'ASP', 5.76)], [('NE2', 'HIS', 'CB', 'ASP', 8.92), ('NE2', 'HIS', 'CG', 'ASP', 7.44), ('NE2', 'HIS', 'OD1', 'ASP', 7.04), ('NE2', 'HIS', 'OD2', 'ASP', 6.83)]]}
ASP_ALA = { 
	'distances':
		[[11.04], [9.61], [9.51], [8.66]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ALA', 11.04)], [('CG', 'ASP', 'CB', 'ALA', 9.61)], [('OD1', 'ASP', 'CB', 'ALA', 9.51)], [('OD2', 'ASP', 'CB', 'ALA', 8.66)]]}
ALA_GLN = { 
	'distances':
		[7.02, 8.5, 9.33, 9.5, 10.09, 8.12, 7.06, 6.32, 4.85],
	'comparisons':
		[('CB', 'ALA', 'CB', 'GLN', 7.02), ('CB', 'ALA', 'CG', 'GLN', 8.5), ('CB', 'ALA', 'CD', 'GLN', 9.33), ('CB', 'ALA', 'OE1', 'GLN', 9.5), ('CB', 'ALA', 'NE2', 'GLN', 10.09), ('CB', 'ALA', 'O', 'GLN', 8.12), ('CB', 'ALA', 'C', 'GLN', 7.06), ('CB', 'ALA', 'CA', 'GLN', 6.32), ('CB', 'ALA', 'N', 'GLN', 4.85)]}
HIS_GLN = { 
	'distances':
		[[13.3, 14.82, 15.3, 15.33, 15.82, 14.79, 13.76, 12.87, 11.43], [11.82, 13.34, 13.85, 13.92, 14.37, 13.35, 12.31, 11.39, 9.96], [11.32, 12.85, 13.5, 13.69, 14.01, 12.6, 11.63, 10.72, 9.29], [10.85, 12.35, 12.75, 12.76, 13.28, 12.63, 11.53, 10.58, 9.19], [10.0, 11.53, 12.19, 12.41, 12.7, 11.36, 10.39, 9.43, 8.01], [9.64, 11.16, 11.65, 11.75, 12.18, 11.35, 10.29, 9.29, 7.9]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 13.3), ('CB', 'HIS', 'CG', 'GLN', 14.82), ('CB', 'HIS', 'CD', 'GLN', 15.3), ('CB', 'HIS', 'OE1', 'GLN', 15.33), ('CB', 'HIS', 'NE2', 'GLN', 15.82), ('CB', 'HIS', 'O', 'GLN', 14.79), ('CB', 'HIS', 'C', 'GLN', 13.76), ('CB', 'HIS', 'CA', 'GLN', 12.87), ('CB', 'HIS', 'N', 'GLN', 11.43)], [('CG', 'HIS', 'CB', 'GLN', 11.82), ('CG', 'HIS', 'CG', 'GLN', 13.34), ('CG', 'HIS', 'CD', 'GLN', 13.85), ('CG', 'HIS', 'OE1', 'GLN', 13.92), ('CG', 'HIS', 'NE2', 'GLN', 14.37), ('CG', 'HIS', 'O', 'GLN', 13.35), ('CG', 'HIS', 'C', 'GLN', 12.31), ('CG', 'HIS', 'CA', 'GLN', 11.39), ('CG', 'HIS', 'N', 'GLN', 9.96)], [('ND1', 'HIS', 'CB', 'GLN', 11.32), ('ND1', 'HIS', 'CG', 'GLN', 12.85), ('ND1', 'HIS', 'CD', 'GLN', 13.5), ('ND1', 'HIS', 'OE1', 'GLN', 13.69), ('ND1', 'HIS', 'NE2', 'GLN', 14.01), ('ND1', 'HIS', 'O', 'GLN', 12.6), ('ND1', 'HIS', 'C', 'GLN', 11.63), ('ND1', 'HIS', 'CA', 'GLN', 10.72), ('ND1', 'HIS', 'N', 'GLN', 9.29)], [('CD2', 'HIS', 'CB', 'GLN', 10.85), ('CD2', 'HIS', 'CG', 'GLN', 12.35), ('CD2', 'HIS', 'CD', 'GLN', 12.75), ('CD2', 'HIS', 'OE1', 'GLN', 12.76), ('CD2', 'HIS', 'NE2', 'GLN', 13.28), ('CD2', 'HIS', 'O', 'GLN', 12.63), ('CD2', 'HIS', 'C', 'GLN', 11.53), ('CD2', 'HIS', 'CA', 'GLN', 10.58), ('CD2', 'HIS', 'N', 'GLN', 9.19)], [('CE1', 'HIS', 'CB', 'GLN', 10.0), ('CE1', 'HIS', 'CG', 'GLN', 11.53), ('CE1', 'HIS', 'CD', 'GLN', 12.19), ('CE1', 'HIS', 'OE1', 'GLN', 12.41), ('CE1', 'HIS', 'NE2', 'GLN', 12.7), ('CE1', 'HIS', 'O', 'GLN', 11.36), ('CE1', 'HIS', 'C', 'GLN', 10.39), ('CE1', 'HIS', 'CA', 'GLN', 9.43), ('CE1', 'HIS', 'N', 'GLN', 8.01)], [('NE2', 'HIS', 'CB', 'GLN', 9.64), ('NE2', 'HIS', 'CG', 'GLN', 11.16), ('NE2', 'HIS', 'CD', 'GLN', 11.65), ('NE2', 'HIS', 'OE1', 'GLN', 11.75), ('NE2', 'HIS', 'NE2', 'GLN', 12.18), ('NE2', 'HIS', 'O', 'GLN', 11.35), ('NE2', 'HIS', 'C', 'GLN', 10.29), ('NE2', 'HIS', 'CA', 'GLN', 9.29), ('NE2', 'HIS', 'N', 'GLN', 7.9)]]}
ASP_GLN = { 
	'distances':
		[[15.66, 17.17, 17.97, 18.29, 18.42, 16.41, 15.64, 14.83, 13.46], [14.2, 15.71, 16.49, 16.8, 16.93, 15.09, 14.27, 13.42, 12.04], [13.87, 15.38, 16.07, 16.4, 16.42, 15.02, 14.19, 13.2, 11.86], [13.39, 14.9, 15.72, 16.01, 16.25, 14.12, 13.3, 12.54, 11.14]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 15.66), ('CB', 'ASP', 'CG', 'GLN', 17.17), ('CB', 'ASP', 'CD', 'GLN', 17.97), ('CB', 'ASP', 'OE1', 'GLN', 18.29), ('CB', 'ASP', 'NE2', 'GLN', 18.42), ('CB', 'ASP', 'O', 'GLN', 16.41), ('CB', 'ASP', 'C', 'GLN', 15.64), ('CB', 'ASP', 'CA', 'GLN', 14.83), ('CB', 'ASP', 'N', 'GLN', 13.46)], [('CG', 'ASP', 'CB', 'GLN', 14.2), ('CG', 'ASP', 'CG', 'GLN', 15.71), ('CG', 'ASP', 'CD', 'GLN', 16.49), ('CG', 'ASP', 'OE1', 'GLN', 16.8), ('CG', 'ASP', 'NE2', 'GLN', 16.93), ('CG', 'ASP', 'O', 'GLN', 15.09), ('CG', 'ASP', 'C', 'GLN', 14.27), ('CG', 'ASP', 'CA', 'GLN', 13.42), ('CG', 'ASP', 'N', 'GLN', 12.04)], [('OD1', 'ASP', 'CB', 'GLN', 13.87), ('OD1', 'ASP', 'CG', 'GLN', 15.38), ('OD1', 'ASP', 'CD', 'GLN', 16.07), ('OD1', 'ASP', 'OE1', 'GLN', 16.4), ('OD1', 'ASP', 'NE2', 'GLN', 16.42), ('OD1', 'ASP', 'O', 'GLN', 15.02), ('OD1', 'ASP', 'C', 'GLN', 14.19), ('OD1', 'ASP', 'CA', 'GLN', 13.2), ('OD1', 'ASP', 'N', 'GLN', 11.86)], [('OD2', 'ASP', 'CB', 'GLN', 13.39), ('OD2', 'ASP', 'CG', 'GLN', 14.9), ('OD2', 'ASP', 'CD', 'GLN', 15.72), ('OD2', 'ASP', 'OE1', 'GLN', 16.01), ('OD2', 'ASP', 'NE2', 'GLN', 16.25), ('OD2', 'ASP', 'O', 'GLN', 14.12), ('OD2', 'ASP', 'C', 'GLN', 13.3), ('OD2', 'ASP', 'CA', 'GLN', 12.54), ('OD2', 'ASP', 'N', 'GLN', 11.14)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ALA, d, 'A_1odt_3_1_1_41')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1odt_3_1_1_41')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ALA, d, 'A_1odt_3_1_1_41')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ALA_GLN, d, 'A_1odt_3_1_1_41')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_GLN, d, 'A_1odt_3_1_1_41')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_GLN, d, 'A_1odt_3_1_1_41')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ALA' :  match1,
		'HIS_ASP' :  match2,
		'ASP_ALA' :  match3,
		'ALA_GLN' :  match4,
		'HIS_GLN' :  match5,
		'ASP_GLN' :  match6}