'''
FUNC:Pab_1edd_3_8_1_5
PDB:1edd
EC:3.8.1.5
RESI:asp,asp,his
LOCI:a-124,260,289;
'''
import motifFunctions as cmd
HIS_ASPI = { 
	'distances':
		[[6.43, 5.53, 5.34, 5.61], [7.09, 5.91, 5.76, 5.56], [6.72, 5.38, 5.41, 4.72], [8.42, 7.2, 6.97, 6.78], [7.94, 6.57, 6.55, 5.77], [8.82, 7.48, 7.33, 6.83]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 6.43), ('CB', 'HIS', 'CG', 'ASPI', 5.53), ('CB', 'HIS', 'OD1', 'ASPI', 5.34), ('CB', 'HIS', 'OD2', 'ASPI', 5.61)], [('CG', 'HIS', 'CB', 'ASPI', 7.09), ('CG', 'HIS', 'CG', 'ASPI', 5.91), ('CG', 'HIS', 'OD1', 'ASPI', 5.76), ('CG', 'HIS', 'OD2', 'ASPI', 5.56)], [('ND1', 'HIS', 'CB', 'ASPI', 6.72), ('ND1', 'HIS', 'CG', 'ASPI', 5.38), ('ND1', 'HIS', 'OD1', 'ASPI', 5.41), ('ND1', 'HIS', 'OD2', 'ASPI', 4.72)], [('CD2', 'HIS', 'CB', 'ASPI', 8.42), ('CD2', 'HIS', 'CG', 'ASPI', 7.2), ('CD2', 'HIS', 'OD1', 'ASPI', 6.97), ('CD2', 'HIS', 'OD2', 'ASPI', 6.78)], [('CE1', 'HIS', 'CB', 'ASPI', 7.94), ('CE1', 'HIS', 'CG', 'ASPI', 6.57), ('CE1', 'HIS', 'OD1', 'ASPI', 6.55), ('CE1', 'HIS', 'OD2', 'ASPI', 5.77)], [('NE2', 'HIS', 'CB', 'ASPI', 8.82), ('NE2', 'HIS', 'CG', 'ASPI', 7.48), ('NE2', 'HIS', 'OD1', 'ASPI', 7.33), ('NE2', 'HIS', 'OD2', 'ASPI', 6.83)]]}
ASP_ASP = { 
	'distances':
		[[11.62, 10.42, 10.58, 9.41], [11.74, 10.4, 10.35, 9.51], [10.88, 9.48, 9.32, 8.67], [12.95, 11.6, 11.5, 10.75], [11.62, 11.74, 10.88, 12.95], [10.42, 10.4, 9.48, 11.6], [10.58, 10.35, 9.32, 11.5], [9.41, 9.51, 8.67, 10.75]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.62), ('CB', 'ASP', 'CG', 'ASP', 10.42), ('CB', 'ASP', 'OD1', 'ASP', 10.58), ('CB', 'ASP', 'OD2', 'ASP', 9.41)], [('CG', 'ASP', 'CB', 'ASP', 11.74), ('CG', 'ASP', 'CG', 'ASP', 10.4), ('CG', 'ASP', 'OD1', 'ASP', 10.35), ('CG', 'ASP', 'OD2', 'ASP', 9.51)], [('OD1', 'ASP', 'CB', 'ASP', 10.88), ('OD1', 'ASP', 'CG', 'ASP', 9.48), ('OD1', 'ASP', 'OD1', 'ASP', 9.32), ('OD1', 'ASP', 'OD2', 'ASP', 8.67)], [('OD2', 'ASP', 'CB', 'ASP', 12.95), ('OD2', 'ASP', 'CG', 'ASP', 11.6), ('OD2', 'ASP', 'OD1', 'ASP', 11.5), ('OD2', 'ASP', 'OD2', 'ASP', 10.75)], [('CB', 'ASP', 'CB', 'ASP', 11.62), ('CB', 'ASP', 'CG', 'ASP', 11.74), ('CB', 'ASP', 'OD1', 'ASP', 10.88), ('CB', 'ASP', 'OD2', 'ASP', 12.95)], [('CG', 'ASP', 'CB', 'ASP', 10.42), ('CG', 'ASP', 'CG', 'ASP', 10.4), ('CG', 'ASP', 'OD1', 'ASP', 9.48), ('CG', 'ASP', 'OD2', 'ASP', 11.6)], [('OD1', 'ASP', 'CB', 'ASP', 10.58), ('OD1', 'ASP', 'CG', 'ASP', 10.35), ('OD1', 'ASP', 'OD1', 'ASP', 9.32), ('OD1', 'ASP', 'OD2', 'ASP', 11.5)], [('OD2', 'ASP', 'CB', 'ASP', 9.41), ('OD2', 'ASP', 'CG', 'ASP', 9.51), ('OD2', 'ASP', 'OD1', 'ASP', 8.67), ('OD2', 'ASP', 'OD2', 'ASP', 10.75)]]}
ASP_HIS = { 
	'distances':
		[[8.87, 7.49, 7.2, 6.66, 6.07, 5.63], [8.77, 7.34, 7.09, 6.36, 5.84, 5.23], [8.04, 6.58, 6.24, 5.7, 4.95, 4.46], [9.8, 8.4, 8.27, 7.31, 7.04, 6.31], [6.43, 7.09, 6.72, 8.42, 7.94, 8.82], [5.53, 5.91, 5.38, 7.2, 6.57, 7.48], [5.34, 5.76, 5.41, 6.97, 6.55, 7.33], [5.61, 5.56, 4.72, 6.78, 5.77, 6.83]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.87), ('CB', 'ASP', 'CG', 'HIS', 7.49), ('CB', 'ASP', 'ND1', 'HIS', 7.2), ('CB', 'ASP', 'CD2', 'HIS', 6.66), ('CB', 'ASP', 'CE1', 'HIS', 6.07), ('CB', 'ASP', 'NE2', 'HIS', 5.63)], [('CG', 'ASP', 'CB', 'HIS', 8.77), ('CG', 'ASP', 'CG', 'HIS', 7.34), ('CG', 'ASP', 'ND1', 'HIS', 7.09), ('CG', 'ASP', 'CD2', 'HIS', 6.36), ('CG', 'ASP', 'CE1', 'HIS', 5.84), ('CG', 'ASP', 'NE2', 'HIS', 5.23)], [('OD1', 'ASP', 'CB', 'HIS', 8.04), ('OD1', 'ASP', 'CG', 'HIS', 6.58), ('OD1', 'ASP', 'ND1', 'HIS', 6.24), ('OD1', 'ASP', 'CD2', 'HIS', 5.7), ('OD1', 'ASP', 'CE1', 'HIS', 4.95), ('OD1', 'ASP', 'NE2', 'HIS', 4.46)], [('OD2', 'ASP', 'CB', 'HIS', 9.8), ('OD2', 'ASP', 'CG', 'HIS', 8.4), ('OD2', 'ASP', 'ND1', 'HIS', 8.27), ('OD2', 'ASP', 'CD2', 'HIS', 7.31), ('OD2', 'ASP', 'CE1', 'HIS', 7.04), ('OD2', 'ASP', 'NE2', 'HIS', 6.31)], [('CB', 'ASP', 'CB', 'HIS', 6.43), ('CB', 'ASP', 'CG', 'HIS', 7.09), ('CB', 'ASP', 'ND1', 'HIS', 6.72), ('CB', 'ASP', 'CD2', 'HIS', 8.42), ('CB', 'ASP', 'CE1', 'HIS', 7.94), ('CB', 'ASP', 'NE2', 'HIS', 8.82)], [('CG', 'ASP', 'CB', 'HIS', 5.53), ('CG', 'ASP', 'CG', 'HIS', 5.91), ('CG', 'ASP', 'ND1', 'HIS', 5.38), ('CG', 'ASP', 'CD2', 'HIS', 7.2), ('CG', 'ASP', 'CE1', 'HIS', 6.57), ('CG', 'ASP', 'NE2', 'HIS', 7.48)], [('OD1', 'ASP', 'CB', 'HIS', 5.34), ('OD1', 'ASP', 'CG', 'HIS', 5.76), ('OD1', 'ASP', 'ND1', 'HIS', 5.41), ('OD1', 'ASP', 'CD2', 'HIS', 6.97), ('OD1', 'ASP', 'CE1', 'HIS', 6.55), ('OD1', 'ASP', 'NE2', 'HIS', 7.33)], [('OD2', 'ASP', 'CB', 'HIS', 5.61), ('OD2', 'ASP', 'CG', 'HIS', 5.56), ('OD2', 'ASP', 'ND1', 'HIS', 4.72), ('OD2', 'ASP', 'CD2', 'HIS', 6.78), ('OD2', 'ASP', 'CE1', 'HIS', 5.77), ('OD2', 'ASP', 'NE2', 'HIS', 6.83)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASPI, d, 'Pab_1edd_3_8_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'Pab_1edd_3_8_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'Pab_1edd_3_8_1_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASPI' :  match1,
		'ASP_ASP' :  match2,
		'ASP_HIS' :  match3}