'''
FUNC:P_2had_3_8_1_5
PDB:2had
EC:3.8.1.5
RESI:asp,asp,his
LOCI:a-124,260,289;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[6.32, 5.47, 5.32, 5.61], [7.07, 5.91, 5.76, 5.64], [6.76, 5.45, 5.45, 4.82], [8.43, 7.24, 7.01, 6.88], [8.01, 6.66, 6.6, 5.9], [8.88, 7.57, 7.39, 6.97], [8.98, 9.0, 8.34, 10.02], [7.58, 7.53, 6.84, 8.58], [7.22, 7.2, 6.4, 8.38], [6.74, 6.57, 6.01, 7.49], [6.06, 5.91, 5.08, 7.11], [5.68, 5.39, 4.71, 6.43]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.32), ('CB', 'HIS', 'CG', 'ASP', 5.47), ('CB', 'HIS', 'OD1', 'ASP', 5.32), ('CB', 'HIS', 'OD2', 'ASP', 5.61)], [('CG', 'HIS', 'CB', 'ASP', 7.07), ('CG', 'HIS', 'CG', 'ASP', 5.91), ('CG', 'HIS', 'OD1', 'ASP', 5.76), ('CG', 'HIS', 'OD2', 'ASP', 5.64)], [('ND1', 'HIS', 'CB', 'ASP', 6.76), ('ND1', 'HIS', 'CG', 'ASP', 5.45), ('ND1', 'HIS', 'OD1', 'ASP', 5.45), ('ND1', 'HIS', 'OD2', 'ASP', 4.82)], [('CD2', 'HIS', 'CB', 'ASP', 8.43), ('CD2', 'HIS', 'CG', 'ASP', 7.24), ('CD2', 'HIS', 'OD1', 'ASP', 7.01), ('CD2', 'HIS', 'OD2', 'ASP', 6.88)], [('CE1', 'HIS', 'CB', 'ASP', 8.01), ('CE1', 'HIS', 'CG', 'ASP', 6.66), ('CE1', 'HIS', 'OD1', 'ASP', 6.6), ('CE1', 'HIS', 'OD2', 'ASP', 5.9)], [('NE2', 'HIS', 'CB', 'ASP', 8.88), ('NE2', 'HIS', 'CG', 'ASP', 7.57), ('NE2', 'HIS', 'OD1', 'ASP', 7.39), ('NE2', 'HIS', 'OD2', 'ASP', 6.97)], [('CB', 'HIS', 'CB', 'ASP', 8.98), ('CB', 'HIS', 'CG', 'ASP', 9.0), ('CB', 'HIS', 'OD1', 'ASP', 8.34), ('CB', 'HIS', 'OD2', 'ASP', 10.02)], [('CG', 'HIS', 'CB', 'ASP', 7.58), ('CG', 'HIS', 'CG', 'ASP', 7.53), ('CG', 'HIS', 'OD1', 'ASP', 6.84), ('CG', 'HIS', 'OD2', 'ASP', 8.58)], [('ND1', 'HIS', 'CB', 'ASP', 7.22), ('ND1', 'HIS', 'CG', 'ASP', 7.2), ('ND1', 'HIS', 'OD1', 'ASP', 6.4), ('ND1', 'HIS', 'OD2', 'ASP', 8.38)], [('CD2', 'HIS', 'CB', 'ASP', 6.74), ('CD2', 'HIS', 'CG', 'ASP', 6.57), ('CD2', 'HIS', 'OD1', 'ASP', 6.01), ('CD2', 'HIS', 'OD2', 'ASP', 7.49)], [('CE1', 'HIS', 'CB', 'ASP', 6.06), ('CE1', 'HIS', 'CG', 'ASP', 5.91), ('CE1', 'HIS', 'OD1', 'ASP', 5.08), ('CE1', 'HIS', 'OD2', 'ASP', 7.11)], [('NE2', 'HIS', 'CB', 'ASP', 5.68), ('NE2', 'HIS', 'CG', 'ASP', 5.39), ('NE2', 'HIS', 'OD1', 'ASP', 4.71), ('NE2', 'HIS', 'OD2', 'ASP', 6.43)]]}
ASP_ASP = { 
	'distances':
		[[11.7, 11.88, 11.06, 13.1], [10.51, 10.56, 9.68, 11.76], [10.63, 10.47, 9.5, 11.61], [9.52, 9.69, 8.88, 10.95], [11.7, 10.51, 10.63, 9.52], [11.88, 10.56, 10.47, 9.69], [11.06, 9.68, 9.5, 8.88], [13.1, 11.76, 11.61, 10.95]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.7), ('CB', 'ASP', 'CG', 'ASP', 11.88), ('CB', 'ASP', 'OD1', 'ASP', 11.06), ('CB', 'ASP', 'OD2', 'ASP', 13.1)], [('CG', 'ASP', 'CB', 'ASP', 10.51), ('CG', 'ASP', 'CG', 'ASP', 10.56), ('CG', 'ASP', 'OD1', 'ASP', 9.68), ('CG', 'ASP', 'OD2', 'ASP', 11.76)], [('OD1', 'ASP', 'CB', 'ASP', 10.63), ('OD1', 'ASP', 'CG', 'ASP', 10.47), ('OD1', 'ASP', 'OD1', 'ASP', 9.5), ('OD1', 'ASP', 'OD2', 'ASP', 11.61)], [('OD2', 'ASP', 'CB', 'ASP', 9.52), ('OD2', 'ASP', 'CG', 'ASP', 9.69), ('OD2', 'ASP', 'OD1', 'ASP', 8.88), ('OD2', 'ASP', 'OD2', 'ASP', 10.95)], [('CB', 'ASP', 'CB', 'ASP', 11.7), ('CB', 'ASP', 'CG', 'ASP', 10.51), ('CB', 'ASP', 'OD1', 'ASP', 10.63), ('CB', 'ASP', 'OD2', 'ASP', 9.52)], [('CG', 'ASP', 'CB', 'ASP', 11.88), ('CG', 'ASP', 'CG', 'ASP', 10.56), ('CG', 'ASP', 'OD1', 'ASP', 10.47), ('CG', 'ASP', 'OD2', 'ASP', 9.69)], [('OD1', 'ASP', 'CB', 'ASP', 11.06), ('OD1', 'ASP', 'CG', 'ASP', 9.68), ('OD1', 'ASP', 'OD1', 'ASP', 9.5), ('OD1', 'ASP', 'OD2', 'ASP', 8.88)], [('OD2', 'ASP', 'CB', 'ASP', 13.1), ('OD2', 'ASP', 'CG', 'ASP', 11.76), ('OD2', 'ASP', 'OD1', 'ASP', 11.61), ('OD2', 'ASP', 'OD2', 'ASP', 10.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'P_2had_3_8_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'P_2had_3_8_1_5')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'ASP_ASP' :  match2}