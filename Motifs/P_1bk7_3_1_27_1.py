'''
FUNC:P_1bk7_3_1_27_1
PDB:1bk7
EC:3.1.27.1
RESI:his,glu,his
LOCI:a-34,84,88;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[11.98, 11.29, 11.61, 10.54, 11.13, 10.44], [11.48, 10.62, 10.9, 9.73, 10.26, 9.49], [12.08, 11.07, 11.18, 10.15, 10.38, 9.69], [10.67, 9.8, 10.19, 8.79, 9.54, 8.62], [11.73, 10.61, 10.7, 9.57, 9.78, 9.01], [10.87, 9.81, 10.07, 8.7, 9.23, 8.3], [11.98, 11.48, 12.08, 10.67, 11.73, 10.87], [11.29, 10.62, 11.07, 9.8, 10.61, 9.81], [11.61, 10.9, 11.18, 10.19, 10.7, 10.07], [10.54, 9.73, 10.15, 8.79, 9.57, 8.7], [11.13, 10.26, 10.38, 9.54, 9.78, 9.23], [10.44, 9.49, 9.69, 8.62, 9.01, 8.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 11.98), ('CB', 'HIS', 'CG', 'HIS', 11.29), ('CB', 'HIS', 'ND1', 'HIS', 11.61), ('CB', 'HIS', 'CD2', 'HIS', 10.54), ('CB', 'HIS', 'CE1', 'HIS', 11.13), ('CB', 'HIS', 'NE2', 'HIS', 10.44)], [('CG', 'HIS', 'CB', 'HIS', 11.48), ('CG', 'HIS', 'CG', 'HIS', 10.62), ('CG', 'HIS', 'ND1', 'HIS', 10.9), ('CG', 'HIS', 'CD2', 'HIS', 9.73), ('CG', 'HIS', 'CE1', 'HIS', 10.26), ('CG', 'HIS', 'NE2', 'HIS', 9.49)], [('ND1', 'HIS', 'CB', 'HIS', 12.08), ('ND1', 'HIS', 'CG', 'HIS', 11.07), ('ND1', 'HIS', 'ND1', 'HIS', 11.18), ('ND1', 'HIS', 'CD2', 'HIS', 10.15), ('ND1', 'HIS', 'CE1', 'HIS', 10.38), ('ND1', 'HIS', 'NE2', 'HIS', 9.69)], [('CD2', 'HIS', 'CB', 'HIS', 10.67), ('CD2', 'HIS', 'CG', 'HIS', 9.8), ('CD2', 'HIS', 'ND1', 'HIS', 10.19), ('CD2', 'HIS', 'CD2', 'HIS', 8.79), ('CD2', 'HIS', 'CE1', 'HIS', 9.54), ('CD2', 'HIS', 'NE2', 'HIS', 8.62)], [('CE1', 'HIS', 'CB', 'HIS', 11.73), ('CE1', 'HIS', 'CG', 'HIS', 10.61), ('CE1', 'HIS', 'ND1', 'HIS', 10.7), ('CE1', 'HIS', 'CD2', 'HIS', 9.57), ('CE1', 'HIS', 'CE1', 'HIS', 9.78), ('CE1', 'HIS', 'NE2', 'HIS', 9.01)], [('NE2', 'HIS', 'CB', 'HIS', 10.87), ('NE2', 'HIS', 'CG', 'HIS', 9.81), ('NE2', 'HIS', 'ND1', 'HIS', 10.07), ('NE2', 'HIS', 'CD2', 'HIS', 8.7), ('NE2', 'HIS', 'CE1', 'HIS', 9.23), ('NE2', 'HIS', 'NE2', 'HIS', 8.3)], [('CB', 'HIS', 'CB', 'HIS', 11.98), ('CB', 'HIS', 'CG', 'HIS', 11.48), ('CB', 'HIS', 'ND1', 'HIS', 12.08), ('CB', 'HIS', 'CD2', 'HIS', 10.67), ('CB', 'HIS', 'CE1', 'HIS', 11.73), ('CB', 'HIS', 'NE2', 'HIS', 10.87)], [('CG', 'HIS', 'CB', 'HIS', 11.29), ('CG', 'HIS', 'CG', 'HIS', 10.62), ('CG', 'HIS', 'ND1', 'HIS', 11.07), ('CG', 'HIS', 'CD2', 'HIS', 9.8), ('CG', 'HIS', 'CE1', 'HIS', 10.61), ('CG', 'HIS', 'NE2', 'HIS', 9.81)], [('ND1', 'HIS', 'CB', 'HIS', 11.61), ('ND1', 'HIS', 'CG', 'HIS', 10.9), ('ND1', 'HIS', 'ND1', 'HIS', 11.18), ('ND1', 'HIS', 'CD2', 'HIS', 10.19), ('ND1', 'HIS', 'CE1', 'HIS', 10.7), ('ND1', 'HIS', 'NE2', 'HIS', 10.07)], [('CD2', 'HIS', 'CB', 'HIS', 10.54), ('CD2', 'HIS', 'CG', 'HIS', 9.73), ('CD2', 'HIS', 'ND1', 'HIS', 10.15), ('CD2', 'HIS', 'CD2', 'HIS', 8.79), ('CD2', 'HIS', 'CE1', 'HIS', 9.57), ('CD2', 'HIS', 'NE2', 'HIS', 8.7)], [('CE1', 'HIS', 'CB', 'HIS', 11.13), ('CE1', 'HIS', 'CG', 'HIS', 10.26), ('CE1', 'HIS', 'ND1', 'HIS', 10.38), ('CE1', 'HIS', 'CD2', 'HIS', 9.54), ('CE1', 'HIS', 'CE1', 'HIS', 9.78), ('CE1', 'HIS', 'NE2', 'HIS', 9.23)], [('NE2', 'HIS', 'CB', 'HIS', 10.44), ('NE2', 'HIS', 'CG', 'HIS', 9.49), ('NE2', 'HIS', 'ND1', 'HIS', 9.69), ('NE2', 'HIS', 'CD2', 'HIS', 8.62), ('NE2', 'HIS', 'CE1', 'HIS', 9.01), ('NE2', 'HIS', 'NE2', 'HIS', 8.3)]]}
HIS_GLU = { 
	'distances':
		[[10.03, 8.75, 8.24, 8.14, 8.31], [9.65, 8.28, 7.54, 7.53, 7.36], [10.69, 9.32, 8.4, 8.37, 8.03], [8.57, 7.16, 6.34, 6.49, 6.05], [10.42, 9.03, 7.98, 8.06, 7.39], [9.16, 7.76, 6.73, 6.92, 6.11], [7.63, 8.27, 7.58, 6.62, 8.27], [7.79, 8.1, 7.09, 6.13, 7.55], [9.08, 9.24, 8.09, 7.1, 8.4], [7.16, 7.23, 6.06, 5.25, 6.33], [9.29, 9.21, 7.89, 7.01, 7.96], [8.25, 8.06, 6.7, 5.97, 6.68]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 10.03), ('CB', 'HIS', 'CG', 'GLU', 8.75), ('CB', 'HIS', 'CD', 'GLU', 8.24), ('CB', 'HIS', 'OE1', 'GLU', 8.14), ('CB', 'HIS', 'OE2', 'GLU', 8.31)], [('CG', 'HIS', 'CB', 'GLU', 9.65), ('CG', 'HIS', 'CG', 'GLU', 8.28), ('CG', 'HIS', 'CD', 'GLU', 7.54), ('CG', 'HIS', 'OE1', 'GLU', 7.53), ('CG', 'HIS', 'OE2', 'GLU', 7.36)], [('ND1', 'HIS', 'CB', 'GLU', 10.69), ('ND1', 'HIS', 'CG', 'GLU', 9.32), ('ND1', 'HIS', 'CD', 'GLU', 8.4), ('ND1', 'HIS', 'OE1', 'GLU', 8.37), ('ND1', 'HIS', 'OE2', 'GLU', 8.03)], [('CD2', 'HIS', 'CB', 'GLU', 8.57), ('CD2', 'HIS', 'CG', 'GLU', 7.16), ('CD2', 'HIS', 'CD', 'GLU', 6.34), ('CD2', 'HIS', 'OE1', 'GLU', 6.49), ('CD2', 'HIS', 'OE2', 'GLU', 6.05)], [('CE1', 'HIS', 'CB', 'GLU', 10.42), ('CE1', 'HIS', 'CG', 'GLU', 9.03), ('CE1', 'HIS', 'CD', 'GLU', 7.98), ('CE1', 'HIS', 'OE1', 'GLU', 8.06), ('CE1', 'HIS', 'OE2', 'GLU', 7.39)], [('NE2', 'HIS', 'CB', 'GLU', 9.16), ('NE2', 'HIS', 'CG', 'GLU', 7.76), ('NE2', 'HIS', 'CD', 'GLU', 6.73), ('NE2', 'HIS', 'OE1', 'GLU', 6.92), ('NE2', 'HIS', 'OE2', 'GLU', 6.11)], [('CB', 'HIS', 'CB', 'GLU', 7.63), ('CB', 'HIS', 'CG', 'GLU', 8.27), ('CB', 'HIS', 'CD', 'GLU', 7.58), ('CB', 'HIS', 'OE1', 'GLU', 6.62), ('CB', 'HIS', 'OE2', 'GLU', 8.27)], [('CG', 'HIS', 'CB', 'GLU', 7.79), ('CG', 'HIS', 'CG', 'GLU', 8.1), ('CG', 'HIS', 'CD', 'GLU', 7.09), ('CG', 'HIS', 'OE1', 'GLU', 6.13), ('CG', 'HIS', 'OE2', 'GLU', 7.55)], [('ND1', 'HIS', 'CB', 'GLU', 9.08), ('ND1', 'HIS', 'CG', 'GLU', 9.24), ('ND1', 'HIS', 'CD', 'GLU', 8.09), ('ND1', 'HIS', 'OE1', 'GLU', 7.1), ('ND1', 'HIS', 'OE2', 'GLU', 8.4)], [('CD2', 'HIS', 'CB', 'GLU', 7.16), ('CD2', 'HIS', 'CG', 'GLU', 7.23), ('CD2', 'HIS', 'CD', 'GLU', 6.06), ('CD2', 'HIS', 'OE1', 'GLU', 5.25), ('CD2', 'HIS', 'OE2', 'GLU', 6.33)], [('CE1', 'HIS', 'CB', 'GLU', 9.29), ('CE1', 'HIS', 'CG', 'GLU', 9.21), ('CE1', 'HIS', 'CD', 'GLU', 7.89), ('CE1', 'HIS', 'OE1', 'GLU', 7.01), ('CE1', 'HIS', 'OE2', 'GLU', 7.96)], [('NE2', 'HIS', 'CB', 'GLU', 8.25), ('NE2', 'HIS', 'CG', 'GLU', 8.06), ('NE2', 'HIS', 'CD', 'GLU', 6.7), ('NE2', 'HIS', 'OE1', 'GLU', 5.97), ('NE2', 'HIS', 'OE2', 'GLU', 6.68)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'P_1bk7_3_1_27_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLU, d, 'P_1bk7_3_1_27_1')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'HIS_GLU' :  match2}