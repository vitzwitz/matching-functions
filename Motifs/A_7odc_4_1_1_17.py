'''
FUNC:A_7odc_4_1_1_17
PDB:7odc
EC:4.1.1.17
RESI:lys,his,glu
LOCI:a-69,197,274;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[14.54, 13.09, 12.3, 11.28, 9.84], [13.57, 12.1, 11.33, 10.19, 8.78], [13.1, 11.6, 11.01, 9.84, 8.52], [13.09, 11.64, 10.75, 9.54, 8.14], [12.37, 10.87, 10.29, 9.0, 7.75], [12.35, 10.89, 10.1, 8.78, 7.48]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 14.54), ('CB', 'HIS', 'CG', 'LYS', 13.09), ('CB', 'HIS', 'CD', 'LYS', 12.3), ('CB', 'HIS', 'CE', 'LYS', 11.28), ('CB', 'HIS', 'NZ', 'LYS', 9.84)], [('CG', 'HIS', 'CB', 'LYS', 13.57), ('CG', 'HIS', 'CG', 'LYS', 12.1), ('CG', 'HIS', 'CD', 'LYS', 11.33), ('CG', 'HIS', 'CE', 'LYS', 10.19), ('CG', 'HIS', 'NZ', 'LYS', 8.78)], [('ND1', 'HIS', 'CB', 'LYS', 13.1), ('ND1', 'HIS', 'CG', 'LYS', 11.6), ('ND1', 'HIS', 'CD', 'LYS', 11.01), ('ND1', 'HIS', 'CE', 'LYS', 9.84), ('ND1', 'HIS', 'NZ', 'LYS', 8.52)], [('CD2', 'HIS', 'CB', 'LYS', 13.09), ('CD2', 'HIS', 'CG', 'LYS', 11.64), ('CD2', 'HIS', 'CD', 'LYS', 10.75), ('CD2', 'HIS', 'CE', 'LYS', 9.54), ('CD2', 'HIS', 'NZ', 'LYS', 8.14)], [('CE1', 'HIS', 'CB', 'LYS', 12.37), ('CE1', 'HIS', 'CG', 'LYS', 10.87), ('CE1', 'HIS', 'CD', 'LYS', 10.29), ('CE1', 'HIS', 'CE', 'LYS', 9.0), ('CE1', 'HIS', 'NZ', 'LYS', 7.75)], [('NE2', 'HIS', 'CB', 'LYS', 12.35), ('NE2', 'HIS', 'CG', 'LYS', 10.89), ('NE2', 'HIS', 'CD', 'LYS', 10.1), ('NE2', 'HIS', 'CE', 'LYS', 8.78), ('NE2', 'HIS', 'NZ', 'LYS', 7.48)]]}
GLU_LYS = { 
	'distances':
		[[12.09, 10.82, 11.06, 10.55, 9.8], [12.87, 11.67, 11.83, 11.45, 10.64], [12.88, 11.65, 11.58, 11.2, 10.24], [12.52, 11.21, 10.99, 10.47, 9.39], [13.52, 12.37, 12.25, 11.98, 11.02]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 12.09), ('CB', 'GLU', 'CG', 'LYS', 10.82), ('CB', 'GLU', 'CD', 'LYS', 11.06), ('CB', 'GLU', 'CE', 'LYS', 10.55), ('CB', 'GLU', 'NZ', 'LYS', 9.8)], [('CG', 'GLU', 'CB', 'LYS', 12.87), ('CG', 'GLU', 'CG', 'LYS', 11.67), ('CG', 'GLU', 'CD', 'LYS', 11.83), ('CG', 'GLU', 'CE', 'LYS', 11.45), ('CG', 'GLU', 'NZ', 'LYS', 10.64)], [('CD', 'GLU', 'CB', 'LYS', 12.88), ('CD', 'GLU', 'CG', 'LYS', 11.65), ('CD', 'GLU', 'CD', 'LYS', 11.58), ('CD', 'GLU', 'CE', 'LYS', 11.2), ('CD', 'GLU', 'NZ', 'LYS', 10.24)], [('OE1', 'GLU', 'CB', 'LYS', 12.52), ('OE1', 'GLU', 'CG', 'LYS', 11.21), ('OE1', 'GLU', 'CD', 'LYS', 10.99), ('OE1', 'GLU', 'CE', 'LYS', 10.47), ('OE1', 'GLU', 'NZ', 'LYS', 9.39)], [('OE2', 'GLU', 'CB', 'LYS', 13.52), ('OE2', 'GLU', 'CG', 'LYS', 12.37), ('OE2', 'GLU', 'CD', 'LYS', 12.25), ('OE2', 'GLU', 'CE', 'LYS', 11.98), ('OE2', 'GLU', 'NZ', 'LYS', 11.02)]]}
GLU_HIS = { 
	'distances':
		[[9.12, 8.88, 7.94, 9.74, 8.38, 9.47], [9.29, 9.35, 8.63, 10.32, 9.29, 10.29], [8.29, 8.53, 8.06, 9.51, 8.85, 9.7], [7.13, 7.32, 6.91, 8.28, 7.72, 8.5], [8.82, 9.27, 8.98, 10.27, 9.85, 10.6]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 9.12), ('CB', 'GLU', 'CG', 'HIS', 8.88), ('CB', 'GLU', 'ND1', 'HIS', 7.94), ('CB', 'GLU', 'CD2', 'HIS', 9.74), ('CB', 'GLU', 'CE1', 'HIS', 8.38), ('CB', 'GLU', 'NE2', 'HIS', 9.47)], [('CG', 'GLU', 'CB', 'HIS', 9.29), ('CG', 'GLU', 'CG', 'HIS', 9.35), ('CG', 'GLU', 'ND1', 'HIS', 8.63), ('CG', 'GLU', 'CD2', 'HIS', 10.32), ('CG', 'GLU', 'CE1', 'HIS', 9.29), ('CG', 'GLU', 'NE2', 'HIS', 10.29)], [('CD', 'GLU', 'CB', 'HIS', 8.29), ('CD', 'GLU', 'CG', 'HIS', 8.53), ('CD', 'GLU', 'ND1', 'HIS', 8.06), ('CD', 'GLU', 'CD2', 'HIS', 9.51), ('CD', 'GLU', 'CE1', 'HIS', 8.85), ('CD', 'GLU', 'NE2', 'HIS', 9.7)], [('OE1', 'GLU', 'CB', 'HIS', 7.13), ('OE1', 'GLU', 'CG', 'HIS', 7.32), ('OE1', 'GLU', 'ND1', 'HIS', 6.91), ('OE1', 'GLU', 'CD2', 'HIS', 8.28), ('OE1', 'GLU', 'CE1', 'HIS', 7.72), ('OE1', 'GLU', 'NE2', 'HIS', 8.5)], [('OE2', 'GLU', 'CB', 'HIS', 8.82), ('OE2', 'GLU', 'CG', 'HIS', 9.27), ('OE2', 'GLU', 'ND1', 'HIS', 8.98), ('OE2', 'GLU', 'CD2', 'HIS', 10.27), ('OE2', 'GLU', 'CE1', 'HIS', 9.85), ('OE2', 'GLU', 'NE2', 'HIS', 10.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'A_7odc_4_1_1_17')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LYS, d, 'A_7odc_4_1_1_17')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_7odc_4_1_1_17')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'GLU_LYS' :  match2,
		'GLU_HIS' :  match3}