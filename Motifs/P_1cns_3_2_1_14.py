'''
FUNC:P_1cns_3_2_1_14
PDB:1cns
EC:3.2.1.14
RESI:glu,glu,ser
LOCI:a-67,89,120;
'''
import motifFunctions as cmd
SER_GLU = { 
	'distances':
		[[11.52, 11.56, 11.29, 10.48, 12.04], [11.14, 11.01, 10.58, 9.77, 11.22], [8.33, 8.71, 7.7, 6.46, 8.31], [8.97, 9.19, 8.11, 6.93, 8.61]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 11.52), ('CB', 'SER', 'CG', 'GLU', 11.56), ('CB', 'SER', 'CD', 'GLU', 11.29), ('CB', 'SER', 'OE1', 'GLU', 10.48), ('CB', 'SER', 'OE2', 'GLU', 12.04)], [('OG', 'SER', 'CB', 'GLU', 11.14), ('OG', 'SER', 'CG', 'GLU', 11.01), ('OG', 'SER', 'CD', 'GLU', 10.58), ('OG', 'SER', 'OE1', 'GLU', 9.77), ('OG', 'SER', 'OE2', 'GLU', 11.22)], [('CB', 'SER', 'CB', 'GLU', 8.33), ('CB', 'SER', 'CG', 'GLU', 8.71), ('CB', 'SER', 'CD', 'GLU', 7.7), ('CB', 'SER', 'OE1', 'GLU', 6.46), ('CB', 'SER', 'OE2', 'GLU', 8.31)], [('OG', 'SER', 'CB', 'GLU', 8.97), ('OG', 'SER', 'CG', 'GLU', 9.19), ('OG', 'SER', 'CD', 'GLU', 8.11), ('OG', 'SER', 'OE1', 'GLU', 6.93), ('OG', 'SER', 'OE2', 'GLU', 8.61)]]}
GLU_GLU = { 
	'distances':
		[[11.29, 11.88, 12.15, 11.64, 13.03], [12.23, 12.74, 12.83, 12.25, 13.65], [12.11, 12.44, 12.41, 11.87, 13.11], [11.07, 11.31, 11.25, 10.74, 11.91], [13.21, 13.47, 13.36, 12.82, 13.99], [11.29, 12.23, 12.11, 11.07, 13.21], [11.88, 12.74, 12.44, 11.31, 13.47], [12.15, 12.83, 12.41, 11.25, 13.36], [11.64, 12.25, 11.87, 10.74, 12.82], [13.03, 13.65, 13.11, 11.91, 13.99]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 11.29), ('CB', 'GLU', 'CG', 'GLU', 11.88), ('CB', 'GLU', 'CD', 'GLU', 12.15), ('CB', 'GLU', 'OE1', 'GLU', 11.64), ('CB', 'GLU', 'OE2', 'GLU', 13.03)], [('CG', 'GLU', 'CB', 'GLU', 12.23), ('CG', 'GLU', 'CG', 'GLU', 12.74), ('CG', 'GLU', 'CD', 'GLU', 12.83), ('CG', 'GLU', 'OE1', 'GLU', 12.25), ('CG', 'GLU', 'OE2', 'GLU', 13.65)], [('CD', 'GLU', 'CB', 'GLU', 12.11), ('CD', 'GLU', 'CG', 'GLU', 12.44), ('CD', 'GLU', 'CD', 'GLU', 12.41), ('CD', 'GLU', 'OE1', 'GLU', 11.87), ('CD', 'GLU', 'OE2', 'GLU', 13.11)], [('OE1', 'GLU', 'CB', 'GLU', 11.07), ('OE1', 'GLU', 'CG', 'GLU', 11.31), ('OE1', 'GLU', 'CD', 'GLU', 11.25), ('OE1', 'GLU', 'OE1', 'GLU', 10.74), ('OE1', 'GLU', 'OE2', 'GLU', 11.91)], [('OE2', 'GLU', 'CB', 'GLU', 13.21), ('OE2', 'GLU', 'CG', 'GLU', 13.47), ('OE2', 'GLU', 'CD', 'GLU', 13.36), ('OE2', 'GLU', 'OE1', 'GLU', 12.82), ('OE2', 'GLU', 'OE2', 'GLU', 13.99)], [('CB', 'GLU', 'CB', 'GLU', 11.29), ('CB', 'GLU', 'CG', 'GLU', 12.23), ('CB', 'GLU', 'CD', 'GLU', 12.11), ('CB', 'GLU', 'OE1', 'GLU', 11.07), ('CB', 'GLU', 'OE2', 'GLU', 13.21)], [('CG', 'GLU', 'CB', 'GLU', 11.88), ('CG', 'GLU', 'CG', 'GLU', 12.74), ('CG', 'GLU', 'CD', 'GLU', 12.44), ('CG', 'GLU', 'OE1', 'GLU', 11.31), ('CG', 'GLU', 'OE2', 'GLU', 13.47)], [('CD', 'GLU', 'CB', 'GLU', 12.15), ('CD', 'GLU', 'CG', 'GLU', 12.83), ('CD', 'GLU', 'CD', 'GLU', 12.41), ('CD', 'GLU', 'OE1', 'GLU', 11.25), ('CD', 'GLU', 'OE2', 'GLU', 13.36)], [('OE1', 'GLU', 'CB', 'GLU', 11.64), ('OE1', 'GLU', 'CG', 'GLU', 12.25), ('OE1', 'GLU', 'CD', 'GLU', 11.87), ('OE1', 'GLU', 'OE1', 'GLU', 10.74), ('OE1', 'GLU', 'OE2', 'GLU', 12.82)], [('OE2', 'GLU', 'CB', 'GLU', 13.03), ('OE2', 'GLU', 'CG', 'GLU', 13.65), ('OE2', 'GLU', 'CD', 'GLU', 13.11), ('OE2', 'GLU', 'OE1', 'GLU', 11.91), ('OE2', 'GLU', 'OE2', 'GLU', 13.99)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_GLU, d, 'P_1cns_3_2_1_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'P_1cns_3_2_1_14')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_GLU' :  match1,
		'GLU_GLU' :  match2}