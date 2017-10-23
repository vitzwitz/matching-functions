'''
FUNC:P_1cg4_6_3_4_4
PDB:1cg4
EC:6.3.4.4
RESI:asp,his,gln
LOCI:a-13,41,224;
'''
import motifFunctions as cmd
HIS_GLN = { 
	'distances':
		[[12.12, 12.08, 11.4, 11.88, 10.46], [10.77, 10.77, 10.04, 10.47, 9.17], [10.07, 10.26, 9.65, 10.07, 8.94], [10.21, 10.07, 9.19, 9.54, 8.28], [9.0, 9.2, 8.52, 8.85, 7.9], [9.08, 9.07, 8.19, 8.47, 7.42]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 12.12), ('CB', 'HIS', 'CG', 'GLN', 12.08), ('CB', 'HIS', 'CD', 'GLN', 11.4), ('CB', 'HIS', 'OE1', 'GLN', 11.88), ('CB', 'HIS', 'NE2', 'GLN', 10.46)], [('CG', 'HIS', 'CB', 'GLN', 10.77), ('CG', 'HIS', 'CG', 'GLN', 10.77), ('CG', 'HIS', 'CD', 'GLN', 10.04), ('CG', 'HIS', 'OE1', 'GLN', 10.47), ('CG', 'HIS', 'NE2', 'GLN', 9.17)], [('ND1', 'HIS', 'CB', 'GLN', 10.07), ('ND1', 'HIS', 'CG', 'GLN', 10.26), ('ND1', 'HIS', 'CD', 'GLN', 9.65), ('ND1', 'HIS', 'OE1', 'GLN', 10.07), ('ND1', 'HIS', 'NE2', 'GLN', 8.94)], [('CD2', 'HIS', 'CB', 'GLN', 10.21), ('CD2', 'HIS', 'CG', 'GLN', 10.07), ('CD2', 'HIS', 'CD', 'GLN', 9.19), ('CD2', 'HIS', 'OE1', 'GLN', 9.54), ('CD2', 'HIS', 'NE2', 'GLN', 8.28)], [('CE1', 'HIS', 'CB', 'GLN', 9.0), ('CE1', 'HIS', 'CG', 'GLN', 9.2), ('CE1', 'HIS', 'CD', 'GLN', 8.52), ('CE1', 'HIS', 'OE1', 'GLN', 8.85), ('CE1', 'HIS', 'NE2', 'GLN', 7.9)], [('NE2', 'HIS', 'CB', 'GLN', 9.08), ('NE2', 'HIS', 'CG', 'GLN', 9.07), ('NE2', 'HIS', 'CD', 'GLN', 8.19), ('NE2', 'HIS', 'OE1', 'GLN', 8.47), ('NE2', 'HIS', 'NE2', 'GLN', 7.42)]]}
ASP_HIS = { 
	'distances':
		[[10.06, 9.79, 9.31, 10.27, 9.53, 10.11], [9.97, 9.63, 9.3, 9.92, 9.41, 9.78], [9.06, 8.61, 8.33, 8.8, 8.36, 8.65], [10.95, 10.64, 10.4, 10.87, 10.49, 10.77]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 10.06), ('CB', 'ASP', 'CG', 'HIS', 9.79), ('CB', 'ASP', 'ND1', 'HIS', 9.31), ('CB', 'ASP', 'CD2', 'HIS', 10.27), ('CB', 'ASP', 'CE1', 'HIS', 9.53), ('CB', 'ASP', 'NE2', 'HIS', 10.11)], [('CG', 'ASP', 'CB', 'HIS', 9.97), ('CG', 'ASP', 'CG', 'HIS', 9.63), ('CG', 'ASP', 'ND1', 'HIS', 9.3), ('CG', 'ASP', 'CD2', 'HIS', 9.92), ('CG', 'ASP', 'CE1', 'HIS', 9.41), ('CG', 'ASP', 'NE2', 'HIS', 9.78)], [('OD1', 'ASP', 'CB', 'HIS', 9.06), ('OD1', 'ASP', 'CG', 'HIS', 8.61), ('OD1', 'ASP', 'ND1', 'HIS', 8.33), ('OD1', 'ASP', 'CD2', 'HIS', 8.8), ('OD1', 'ASP', 'CE1', 'HIS', 8.36), ('OD1', 'ASP', 'NE2', 'HIS', 8.65)], [('OD2', 'ASP', 'CB', 'HIS', 10.95), ('OD2', 'ASP', 'CG', 'HIS', 10.64), ('OD2', 'ASP', 'ND1', 'HIS', 10.4), ('OD2', 'ASP', 'CD2', 'HIS', 10.87), ('OD2', 'ASP', 'CE1', 'HIS', 10.49), ('OD2', 'ASP', 'NE2', 'HIS', 10.77)]]}
ASP_GLN = { 
	'distances':
		[[9.84, 9.97, 10.62, 11.73, 10.11], [9.27, 9.17, 9.76, 10.92, 9.15], [8.53, 8.35, 8.79, 9.93, 8.09], [9.79, 9.56, 10.22, 11.42, 9.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 9.84), ('CB', 'ASP', 'CG', 'GLN', 9.97), ('CB', 'ASP', 'CD', 'GLN', 10.62), ('CB', 'ASP', 'OE1', 'GLN', 11.73), ('CB', 'ASP', 'NE2', 'GLN', 10.11)], [('CG', 'ASP', 'CB', 'GLN', 9.27), ('CG', 'ASP', 'CG', 'GLN', 9.17), ('CG', 'ASP', 'CD', 'GLN', 9.76), ('CG', 'ASP', 'OE1', 'GLN', 10.92), ('CG', 'ASP', 'NE2', 'GLN', 9.15)], [('OD1', 'ASP', 'CB', 'GLN', 8.53), ('OD1', 'ASP', 'CG', 'GLN', 8.35), ('OD1', 'ASP', 'CD', 'GLN', 8.79), ('OD1', 'ASP', 'OE1', 'GLN', 9.93), ('OD1', 'ASP', 'NE2', 'GLN', 8.09)], [('OD2', 'ASP', 'CB', 'GLN', 9.79), ('OD2', 'ASP', 'CG', 'GLN', 9.56), ('OD2', 'ASP', 'CD', 'GLN', 10.22), ('OD2', 'ASP', 'OE1', 'GLN', 11.42), ('OD2', 'ASP', 'NE2', 'GLN', 9.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLN, d, 'P_1cg4_6_3_4_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_1cg4_6_3_4_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLN, d, 'P_1cg4_6_3_4_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLN' :  match1,
		'ASP_HIS' :  match2,
		'ASP_GLN' :  match3}