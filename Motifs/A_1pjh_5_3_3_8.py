'''
FUNC:A_1pjh_5_3_3_8
PDB:1pjh
EC:5.3.3.8
RESI:ala,leu,glu
LOCI:a-70,126,158;
'''
import motifFunctions as cmd
GLU_ALA = { 
	'distances':
		[[10.84, 13.39, 13.13, 11.81, 11.41], [10.52, 13.05, 12.86, 11.64, 11.38], [9.07, 11.6, 11.42, 10.25, 10.06], [8.18, 10.79, 10.53, 9.27, 9.04], [9.01, 11.42, 11.33, 10.3, 10.23]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ALA', 10.84), ('CB', 'GLU', 'O', 'ALA', 13.39), ('CB', 'GLU', 'C', 'ALA', 13.13), ('CB', 'GLU', 'CA', 'ALA', 11.81), ('CB', 'GLU', 'N', 'ALA', 11.41)], [('CG', 'GLU', 'CB', 'ALA', 10.52), ('CG', 'GLU', 'O', 'ALA', 13.05), ('CG', 'GLU', 'C', 'ALA', 12.86), ('CG', 'GLU', 'CA', 'ALA', 11.64), ('CG', 'GLU', 'N', 'ALA', 11.38)], [('CD', 'GLU', 'CB', 'ALA', 9.07), ('CD', 'GLU', 'O', 'ALA', 11.6), ('CD', 'GLU', 'C', 'ALA', 11.42), ('CD', 'GLU', 'CA', 'ALA', 10.25), ('CD', 'GLU', 'N', 'ALA', 10.06)], [('OE1', 'GLU', 'CB', 'ALA', 8.18), ('OE1', 'GLU', 'O', 'ALA', 10.79), ('OE1', 'GLU', 'C', 'ALA', 10.53), ('OE1', 'GLU', 'CA', 'ALA', 9.27), ('OE1', 'GLU', 'N', 'ALA', 9.04)], [('OE2', 'GLU', 'CB', 'ALA', 9.01), ('OE2', 'GLU', 'O', 'ALA', 11.42), ('OE2', 'GLU', 'C', 'ALA', 11.33), ('OE2', 'GLU', 'CA', 'ALA', 10.3), ('OE2', 'GLU', 'N', 'ALA', 10.23)]]}
GLU_LEU = { 
	'distances':
		[[7.03, 7.27, 6.3, 7.88, 8.41, 8.26, 6.97, 7.27], [7.65, 8.05, 7.32, 8.4, 9.55, 9.22, 7.79, 7.84], [6.95, 7.56, 7.21, 7.75, 9.36, 8.82, 7.3, 7.18], [5.73, 6.41, 6.25, 6.64, 8.31, 7.71, 6.2, 6.17], [7.87, 8.56, 8.35, 8.58, 10.46, 9.82, 8.29, 7.99]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LEU', 7.03), ('CB', 'GLU', 'CG', 'LEU', 7.27), ('CB', 'GLU', 'CD1', 'LEU', 6.3), ('CB', 'GLU', 'CD2', 'LEU', 7.88), ('CB', 'GLU', 'O', 'LEU', 8.41), ('CB', 'GLU', 'C', 'LEU', 8.26), ('CB', 'GLU', 'CA', 'LEU', 6.97), ('CB', 'GLU', 'N', 'LEU', 7.27)], [('CG', 'GLU', 'CB', 'LEU', 7.65), ('CG', 'GLU', 'CG', 'LEU', 8.05), ('CG', 'GLU', 'CD1', 'LEU', 7.32), ('CG', 'GLU', 'CD2', 'LEU', 8.4), ('CG', 'GLU', 'O', 'LEU', 9.55), ('CG', 'GLU', 'C', 'LEU', 9.22), ('CG', 'GLU', 'CA', 'LEU', 7.79), ('CG', 'GLU', 'N', 'LEU', 7.84)], [('CD', 'GLU', 'CB', 'LEU', 6.95), ('CD', 'GLU', 'CG', 'LEU', 7.56), ('CD', 'GLU', 'CD1', 'LEU', 7.21), ('CD', 'GLU', 'CD2', 'LEU', 7.75), ('CD', 'GLU', 'O', 'LEU', 9.36), ('CD', 'GLU', 'C', 'LEU', 8.82), ('CD', 'GLU', 'CA', 'LEU', 7.3), ('CD', 'GLU', 'N', 'LEU', 7.18)], [('OE1', 'GLU', 'CB', 'LEU', 5.73), ('OE1', 'GLU', 'CG', 'LEU', 6.41), ('OE1', 'GLU', 'CD1', 'LEU', 6.25), ('OE1', 'GLU', 'CD2', 'LEU', 6.64), ('OE1', 'GLU', 'O', 'LEU', 8.31), ('OE1', 'GLU', 'C', 'LEU', 7.71), ('OE1', 'GLU', 'CA', 'LEU', 6.2), ('OE1', 'GLU', 'N', 'LEU', 6.17)], [('OE2', 'GLU', 'CB', 'LEU', 7.87), ('OE2', 'GLU', 'CG', 'LEU', 8.56), ('OE2', 'GLU', 'CD1', 'LEU', 8.35), ('OE2', 'GLU', 'CD2', 'LEU', 8.58), ('OE2', 'GLU', 'O', 'LEU', 10.46), ('OE2', 'GLU', 'C', 'LEU', 9.82), ('OE2', 'GLU', 'CA', 'LEU', 8.29), ('OE2', 'GLU', 'N', 'LEU', 7.99)]]}
LEU_ALA = { 
	'distances':
		[[7.47, 9.92, 9.37, 7.87, 7.37], [8.4, 11.01, 10.32, 8.8, 8.49], [9.62, 12.29, 11.66, 10.15, 9.8], [7.94, 10.78, 9.96, 8.48, 8.5], [10.2, 12.09, 11.59, 10.16, 9.31], [9.12, 10.92, 10.48, 9.07, 8.16], [8.38, 10.44, 10.05, 8.62, 7.81], [7.93, 9.66, 9.48, 8.16, 7.19]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'ALA', 7.47), ('CB', 'LEU', 'O', 'ALA', 9.92), ('CB', 'LEU', 'C', 'ALA', 9.37), ('CB', 'LEU', 'CA', 'ALA', 7.87), ('CB', 'LEU', 'N', 'ALA', 7.37)], [('CG', 'LEU', 'CB', 'ALA', 8.4), ('CG', 'LEU', 'O', 'ALA', 11.01), ('CG', 'LEU', 'C', 'ALA', 10.32), ('CG', 'LEU', 'CA', 'ALA', 8.8), ('CG', 'LEU', 'N', 'ALA', 8.49)], [('CD1', 'LEU', 'CB', 'ALA', 9.62), ('CD1', 'LEU', 'O', 'ALA', 12.29), ('CD1', 'LEU', 'C', 'ALA', 11.66), ('CD1', 'LEU', 'CA', 'ALA', 10.15), ('CD1', 'LEU', 'N', 'ALA', 9.8)], [('CD2', 'LEU', 'CB', 'ALA', 7.94), ('CD2', 'LEU', 'O', 'ALA', 10.78), ('CD2', 'LEU', 'C', 'ALA', 9.96), ('CD2', 'LEU', 'CA', 'ALA', 8.48), ('CD2', 'LEU', 'N', 'ALA', 8.5)], [('O', 'LEU', 'CB', 'ALA', 10.2), ('O', 'LEU', 'O', 'ALA', 12.09), ('O', 'LEU', 'C', 'ALA', 11.59), ('O', 'LEU', 'CA', 'ALA', 10.16), ('O', 'LEU', 'N', 'ALA', 9.31)], [('C', 'LEU', 'CB', 'ALA', 9.12), ('C', 'LEU', 'O', 'ALA', 10.92), ('C', 'LEU', 'C', 'ALA', 10.48), ('C', 'LEU', 'CA', 'ALA', 9.07), ('C', 'LEU', 'N', 'ALA', 8.16)], [('CA', 'LEU', 'CB', 'ALA', 8.38), ('CA', 'LEU', 'O', 'ALA', 10.44), ('CA', 'LEU', 'C', 'ALA', 10.05), ('CA', 'LEU', 'CA', 'ALA', 8.62), ('CA', 'LEU', 'N', 'ALA', 7.81)], [('N', 'LEU', 'CB', 'ALA', 7.93), ('N', 'LEU', 'O', 'ALA', 9.66), ('N', 'LEU', 'C', 'ALA', 9.48), ('N', 'LEU', 'CA', 'ALA', 8.16), ('N', 'LEU', 'N', 'ALA', 7.19)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ALA, d, 'A_1pjh_5_3_3_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LEU, d, 'A_1pjh_5_3_3_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LEU_ALA, d, 'A_1pjh_5_3_3_8')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ALA' :  match1,
		'GLU_LEU' :  match2,
		'LEU_ALA' :  match3}