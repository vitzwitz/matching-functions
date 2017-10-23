'''
FUNC:A_2dhn_4_1_2_25
PDB:2dhn
EC:4.1.2.25
RESI:glu,lys
LOCI:a-22,100;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[10.42, 9.53, 8.38, 7.86, 7.17, 12.41, 12.15, 11.54, 12.75], [10.31, 9.29, 8.03, 7.28, 6.35, 12.52, 12.28, 11.53, 12.62], [9.23, 8.29, 6.9, 6.27, 5.2, 11.42, 11.3, 10.56, 11.6], [8.03, 7.12, 5.76, 5.27, 4.41, 10.22, 10.06, 9.33, 10.41], [9.74, 8.86, 7.38, 6.77, 5.49, 11.89, 11.88, 11.16, 12.11], [11.68, 10.59, 9.8, 9.02, 8.69, 13.83, 13.28, 12.52, 13.7], [12.06, 10.98, 10.03, 9.23, 8.68, 14.21, 13.76, 13.01, 14.2], [11.75, 10.82, 9.77, 9.18, 8.55, 13.71, 13.38, 12.78, 14.02], [12.89, 12.01, 10.85, 10.27, 9.47, 14.8, 14.55, 13.99, 15.23]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 10.42), ('CB', 'GLU', 'CG', 'LYS', 9.53), ('CB', 'GLU', 'CD', 'LYS', 8.38), ('CB', 'GLU', 'CE', 'LYS', 7.86), ('CB', 'GLU', 'NZ', 'LYS', 7.17), ('CB', 'GLU', 'O', 'LYS', 12.41), ('CB', 'GLU', 'C', 'LYS', 12.15), ('CB', 'GLU', 'CA', 'LYS', 11.54), ('CB', 'GLU', 'N', 'LYS', 12.75)], [('CG', 'GLU', 'CB', 'LYS', 10.31), ('CG', 'GLU', 'CG', 'LYS', 9.29), ('CG', 'GLU', 'CD', 'LYS', 8.03), ('CG', 'GLU', 'CE', 'LYS', 7.28), ('CG', 'GLU', 'NZ', 'LYS', 6.35), ('CG', 'GLU', 'O', 'LYS', 12.52), ('CG', 'GLU', 'C', 'LYS', 12.28), ('CG', 'GLU', 'CA', 'LYS', 11.53), ('CG', 'GLU', 'N', 'LYS', 12.62)], [('CD', 'GLU', 'CB', 'LYS', 9.23), ('CD', 'GLU', 'CG', 'LYS', 8.29), ('CD', 'GLU', 'CD', 'LYS', 6.9), ('CD', 'GLU', 'CE', 'LYS', 6.27), ('CD', 'GLU', 'NZ', 'LYS', 5.2), ('CD', 'GLU', 'O', 'LYS', 11.42), ('CD', 'GLU', 'C', 'LYS', 11.3), ('CD', 'GLU', 'CA', 'LYS', 10.56), ('CD', 'GLU', 'N', 'LYS', 11.6)], [('OE1', 'GLU', 'CB', 'LYS', 8.03), ('OE1', 'GLU', 'CG', 'LYS', 7.12), ('OE1', 'GLU', 'CD', 'LYS', 5.76), ('OE1', 'GLU', 'CE', 'LYS', 5.27), ('OE1', 'GLU', 'NZ', 'LYS', 4.41), ('OE1', 'GLU', 'O', 'LYS', 10.22), ('OE1', 'GLU', 'C', 'LYS', 10.06), ('OE1', 'GLU', 'CA', 'LYS', 9.33), ('OE1', 'GLU', 'N', 'LYS', 10.41)], [('OE2', 'GLU', 'CB', 'LYS', 9.74), ('OE2', 'GLU', 'CG', 'LYS', 8.86), ('OE2', 'GLU', 'CD', 'LYS', 7.38), ('OE2', 'GLU', 'CE', 'LYS', 6.77), ('OE2', 'GLU', 'NZ', 'LYS', 5.49), ('OE2', 'GLU', 'O', 'LYS', 11.89), ('OE2', 'GLU', 'C', 'LYS', 11.88), ('OE2', 'GLU', 'CA', 'LYS', 11.16), ('OE2', 'GLU', 'N', 'LYS', 12.11)], [('O', 'GLU', 'CB', 'LYS', 11.68), ('O', 'GLU', 'CG', 'LYS', 10.59), ('O', 'GLU', 'CD', 'LYS', 9.8), ('O', 'GLU', 'CE', 'LYS', 9.02), ('O', 'GLU', 'NZ', 'LYS', 8.69), ('O', 'GLU', 'O', 'LYS', 13.83), ('O', 'GLU', 'C', 'LYS', 13.28), ('O', 'GLU', 'CA', 'LYS', 12.52), ('O', 'GLU', 'N', 'LYS', 13.7)], [('C', 'GLU', 'CB', 'LYS', 12.06), ('C', 'GLU', 'CG', 'LYS', 10.98), ('C', 'GLU', 'CD', 'LYS', 10.03), ('C', 'GLU', 'CE', 'LYS', 9.23), ('C', 'GLU', 'NZ', 'LYS', 8.68), ('C', 'GLU', 'O', 'LYS', 14.21), ('C', 'GLU', 'C', 'LYS', 13.76), ('C', 'GLU', 'CA', 'LYS', 13.01), ('C', 'GLU', 'N', 'LYS', 14.2)], [('CA', 'GLU', 'CB', 'LYS', 11.75), ('CA', 'GLU', 'CG', 'LYS', 10.82), ('CA', 'GLU', 'CD', 'LYS', 9.77), ('CA', 'GLU', 'CE', 'LYS', 9.18), ('CA', 'GLU', 'NZ', 'LYS', 8.55), ('CA', 'GLU', 'O', 'LYS', 13.71), ('CA', 'GLU', 'C', 'LYS', 13.38), ('CA', 'GLU', 'CA', 'LYS', 12.78), ('CA', 'GLU', 'N', 'LYS', 14.02)], [('N', 'GLU', 'CB', 'LYS', 12.89), ('N', 'GLU', 'CG', 'LYS', 12.01), ('N', 'GLU', 'CD', 'LYS', 10.85), ('N', 'GLU', 'CE', 'LYS', 10.27), ('N', 'GLU', 'NZ', 'LYS', 9.47), ('N', 'GLU', 'O', 'LYS', 14.8), ('N', 'GLU', 'C', 'LYS', 14.55), ('N', 'GLU', 'CA', 'LYS', 13.99), ('N', 'GLU', 'N', 'LYS', 15.23)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_2dhn_4_1_2_25')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1}