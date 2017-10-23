'''
FUNC:A_1snz_5_1_3_3
PDB:1snz
EC:5.1.3.3
RESI:his,glu
LOCI:a-176,307;
'''
import motifFunctions as cmd
HIS_GLU = { 
	'distances':
		[[7.91, 6.98, 6.8, 6.75, 7.24, 10.88, 10.15, 8.82, 9.18], [7.94, 6.79, 6.25, 6.22, 6.4, 10.92, 10.35, 8.99, 9.19], [8.57, 7.22, 6.69, 6.94, 6.48, 11.49, 10.93, 9.5, 9.44], [7.87, 6.81, 5.89, 5.6, 6.03, 10.77, 10.37, 9.12, 9.39], [8.82, 7.44, 6.6, 6.8, 6.14, 11.65, 11.25, 9.87, 9.74], [8.45, 7.23, 6.15, 6.04, 5.85, 11.25, 10.95, 9.68, 9.73], [9.21, 8.0, 8.08, 8.49, 8.1, 12.05, 11.22, 9.75, 9.67], [8.41, 7.35, 7.67, 8.09, 7.9, 11.19, 10.28, 8.84, 8.87], [7.29, 6.38, 6.65, 6.89, 7.15, 10.16, 9.29, 7.91, 8.19], [7.32, 6.79, 7.28, 7.38, 8.04, 10.0, 9.04, 7.8, 8.34]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 7.91), ('CB', 'HIS', 'CG', 'GLU', 6.98), ('CB', 'HIS', 'CD', 'GLU', 6.8), ('CB', 'HIS', 'OE1', 'GLU', 6.75), ('CB', 'HIS', 'OE2', 'GLU', 7.24), ('CB', 'HIS', 'O', 'GLU', 10.88), ('CB', 'HIS', 'C', 'GLU', 10.15), ('CB', 'HIS', 'CA', 'GLU', 8.82), ('CB', 'HIS', 'N', 'GLU', 9.18)], [('CG', 'HIS', 'CB', 'GLU', 7.94), ('CG', 'HIS', 'CG', 'GLU', 6.79), ('CG', 'HIS', 'CD', 'GLU', 6.25), ('CG', 'HIS', 'OE1', 'GLU', 6.22), ('CG', 'HIS', 'OE2', 'GLU', 6.4), ('CG', 'HIS', 'O', 'GLU', 10.92), ('CG', 'HIS', 'C', 'GLU', 10.35), ('CG', 'HIS', 'CA', 'GLU', 8.99), ('CG', 'HIS', 'N', 'GLU', 9.19)], [('ND1', 'HIS', 'CB', 'GLU', 8.57), ('ND1', 'HIS', 'CG', 'GLU', 7.22), ('ND1', 'HIS', 'CD', 'GLU', 6.69), ('ND1', 'HIS', 'OE1', 'GLU', 6.94), ('ND1', 'HIS', 'OE2', 'GLU', 6.48), ('ND1', 'HIS', 'O', 'GLU', 11.49), ('ND1', 'HIS', 'C', 'GLU', 10.93), ('ND1', 'HIS', 'CA', 'GLU', 9.5), ('ND1', 'HIS', 'N', 'GLU', 9.44)], [('CD2', 'HIS', 'CB', 'GLU', 7.87), ('CD2', 'HIS', 'CG', 'GLU', 6.81), ('CD2', 'HIS', 'CD', 'GLU', 5.89), ('CD2', 'HIS', 'OE1', 'GLU', 5.6), ('CD2', 'HIS', 'OE2', 'GLU', 6.03), ('CD2', 'HIS', 'O', 'GLU', 10.77), ('CD2', 'HIS', 'C', 'GLU', 10.37), ('CD2', 'HIS', 'CA', 'GLU', 9.12), ('CD2', 'HIS', 'N', 'GLU', 9.39)], [('CE1', 'HIS', 'CB', 'GLU', 8.82), ('CE1', 'HIS', 'CG', 'GLU', 7.44), ('CE1', 'HIS', 'CD', 'GLU', 6.6), ('CE1', 'HIS', 'OE1', 'GLU', 6.8), ('CE1', 'HIS', 'OE2', 'GLU', 6.14), ('CE1', 'HIS', 'O', 'GLU', 11.65), ('CE1', 'HIS', 'C', 'GLU', 11.25), ('CE1', 'HIS', 'CA', 'GLU', 9.87), ('CE1', 'HIS', 'N', 'GLU', 9.74)], [('NE2', 'HIS', 'CB', 'GLU', 8.45), ('NE2', 'HIS', 'CG', 'GLU', 7.23), ('NE2', 'HIS', 'CD', 'GLU', 6.15), ('NE2', 'HIS', 'OE1', 'GLU', 6.04), ('NE2', 'HIS', 'OE2', 'GLU', 5.85), ('NE2', 'HIS', 'O', 'GLU', 11.25), ('NE2', 'HIS', 'C', 'GLU', 10.95), ('NE2', 'HIS', 'CA', 'GLU', 9.68), ('NE2', 'HIS', 'N', 'GLU', 9.73)], [('O', 'HIS', 'CB', 'GLU', 9.21), ('O', 'HIS', 'CG', 'GLU', 8.0), ('O', 'HIS', 'CD', 'GLU', 8.08), ('O', 'HIS', 'OE1', 'GLU', 8.49), ('O', 'HIS', 'OE2', 'GLU', 8.1), ('O', 'HIS', 'O', 'GLU', 12.05), ('O', 'HIS', 'C', 'GLU', 11.22), ('O', 'HIS', 'CA', 'GLU', 9.75), ('O', 'HIS', 'N', 'GLU', 9.67)], [('C', 'HIS', 'CB', 'GLU', 8.41), ('C', 'HIS', 'CG', 'GLU', 7.35), ('C', 'HIS', 'CD', 'GLU', 7.67), ('C', 'HIS', 'OE1', 'GLU', 8.09), ('C', 'HIS', 'OE2', 'GLU', 7.9), ('C', 'HIS', 'O', 'GLU', 11.19), ('C', 'HIS', 'C', 'GLU', 10.28), ('C', 'HIS', 'CA', 'GLU', 8.84), ('C', 'HIS', 'N', 'GLU', 8.87)], [('CA', 'HIS', 'CB', 'GLU', 7.29), ('CA', 'HIS', 'CG', 'GLU', 6.38), ('CA', 'HIS', 'CD', 'GLU', 6.65), ('CA', 'HIS', 'OE1', 'GLU', 6.89), ('CA', 'HIS', 'OE2', 'GLU', 7.15), ('CA', 'HIS', 'O', 'GLU', 10.16), ('CA', 'HIS', 'C', 'GLU', 9.29), ('CA', 'HIS', 'CA', 'GLU', 7.91), ('CA', 'HIS', 'N', 'GLU', 8.19)], [('N', 'HIS', 'CB', 'GLU', 7.32), ('N', 'HIS', 'CG', 'GLU', 6.79), ('N', 'HIS', 'CD', 'GLU', 7.28), ('N', 'HIS', 'OE1', 'GLU', 7.38), ('N', 'HIS', 'OE2', 'GLU', 8.04), ('N', 'HIS', 'O', 'GLU', 10.0), ('N', 'HIS', 'C', 'GLU', 9.04), ('N', 'HIS', 'CA', 'GLU', 7.8), ('N', 'HIS', 'N', 'GLU', 8.34)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLU, d, 'A_1snz_5_1_3_3')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLU' :  match1}