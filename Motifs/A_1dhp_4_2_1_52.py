'''
FUNC:A_1dhp_4_2_1_52
PDB:1dhp
EC:4.2.1.52
RESI:tyr,arg,lys
LOCI:a-133,138,161;
'''
import motifFunctions as cmd
LYS_TYR = { 
	'distances':
		[[6.43, 6.54, 6.21, 7.52, 6.95, 8.1, 7.84, 8.81], [7.0, 6.65, 6.04, 7.43, 6.36, 7.67, 7.18, 7.92], [6.66, 6.04, 5.66, 6.48, 5.77, 6.57, 6.23, 6.92], [7.73, 6.79, 6.16, 6.98, 5.74, 6.64, 6.01, 6.27], [7.92, 6.79, 6.4, 6.56, 5.74, 5.94, 5.48, 5.49]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 6.43), ('CB', 'LYS', 'CG', 'TYR', 6.54), ('CB', 'LYS', 'CD1', 'TYR', 6.21), ('CB', 'LYS', 'CD2', 'TYR', 7.52), ('CB', 'LYS', 'CE1', 'TYR', 6.95), ('CB', 'LYS', 'CE2', 'TYR', 8.1), ('CB', 'LYS', 'CZ', 'TYR', 7.84), ('CB', 'LYS', 'OH', 'TYR', 8.81)], [('CG', 'LYS', 'CB', 'TYR', 7.0), ('CG', 'LYS', 'CG', 'TYR', 6.65), ('CG', 'LYS', 'CD1', 'TYR', 6.04), ('CG', 'LYS', 'CD2', 'TYR', 7.43), ('CG', 'LYS', 'CE1', 'TYR', 6.36), ('CG', 'LYS', 'CE2', 'TYR', 7.67), ('CG', 'LYS', 'CZ', 'TYR', 7.18), ('CG', 'LYS', 'OH', 'TYR', 7.92)], [('CD', 'LYS', 'CB', 'TYR', 6.66), ('CD', 'LYS', 'CG', 'TYR', 6.04), ('CD', 'LYS', 'CD1', 'TYR', 5.66), ('CD', 'LYS', 'CD2', 'TYR', 6.48), ('CD', 'LYS', 'CE1', 'TYR', 5.77), ('CD', 'LYS', 'CE2', 'TYR', 6.57), ('CD', 'LYS', 'CZ', 'TYR', 6.23), ('CD', 'LYS', 'OH', 'TYR', 6.92)], [('CE', 'LYS', 'CB', 'TYR', 7.73), ('CE', 'LYS', 'CG', 'TYR', 6.79), ('CE', 'LYS', 'CD1', 'TYR', 6.16), ('CE', 'LYS', 'CD2', 'TYR', 6.98), ('CE', 'LYS', 'CE1', 'TYR', 5.74), ('CE', 'LYS', 'CE2', 'TYR', 6.64), ('CE', 'LYS', 'CZ', 'TYR', 6.01), ('CE', 'LYS', 'OH', 'TYR', 6.27)], [('NZ', 'LYS', 'CB', 'TYR', 7.92), ('NZ', 'LYS', 'CG', 'TYR', 6.79), ('NZ', 'LYS', 'CD1', 'TYR', 6.4), ('NZ', 'LYS', 'CD2', 'TYR', 6.56), ('NZ', 'LYS', 'CE1', 'TYR', 5.74), ('NZ', 'LYS', 'CE2', 'TYR', 5.94), ('NZ', 'LYS', 'CZ', 'TYR', 5.48), ('NZ', 'LYS', 'OH', 'TYR', 5.49)]]}
TYR_ARG = { 
	'distances':
		[[11.98, 12.36, 11.55, 12.24, 13.28, 13.75, 14.03], [10.77, 11.02, 10.13, 10.81, 11.8, 12.25, 12.57], [10.38, 10.48, 9.61, 10.44, 11.38, 11.67, 12.28], [10.29, 10.55, 9.54, 10.03, 11.01, 11.59, 11.66], [9.5, 9.41, 8.44, 9.26, 10.13, 10.35, 11.05], [9.41, 9.5, 8.38, 8.79, 9.71, 10.28, 10.35], [8.99, 8.89, 7.76, 8.35, 9.21, 9.59, 10.01], [8.43, 8.08, 6.79, 7.29, 8.02, 8.33, 8.82]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 11.98), ('CB', 'TYR', 'CG', 'ARG', 12.36), ('CB', 'TYR', 'CD', 'ARG', 11.55), ('CB', 'TYR', 'NE', 'ARG', 12.24), ('CB', 'TYR', 'CZ', 'ARG', 13.28), ('CB', 'TYR', 'NH1', 'ARG', 13.75), ('CB', 'TYR', 'NH2', 'ARG', 14.03)], [('CG', 'TYR', 'CB', 'ARG', 10.77), ('CG', 'TYR', 'CG', 'ARG', 11.02), ('CG', 'TYR', 'CD', 'ARG', 10.13), ('CG', 'TYR', 'NE', 'ARG', 10.81), ('CG', 'TYR', 'CZ', 'ARG', 11.8), ('CG', 'TYR', 'NH1', 'ARG', 12.25), ('CG', 'TYR', 'NH2', 'ARG', 12.57)], [('CD1', 'TYR', 'CB', 'ARG', 10.38), ('CD1', 'TYR', 'CG', 'ARG', 10.48), ('CD1', 'TYR', 'CD', 'ARG', 9.61), ('CD1', 'TYR', 'NE', 'ARG', 10.44), ('CD1', 'TYR', 'CZ', 'ARG', 11.38), ('CD1', 'TYR', 'NH1', 'ARG', 11.67), ('CD1', 'TYR', 'NH2', 'ARG', 12.28)], [('CD2', 'TYR', 'CB', 'ARG', 10.29), ('CD2', 'TYR', 'CG', 'ARG', 10.55), ('CD2', 'TYR', 'CD', 'ARG', 9.54), ('CD2', 'TYR', 'NE', 'ARG', 10.03), ('CD2', 'TYR', 'CZ', 'ARG', 11.01), ('CD2', 'TYR', 'NH1', 'ARG', 11.59), ('CD2', 'TYR', 'NH2', 'ARG', 11.66)], [('CE1', 'TYR', 'CB', 'ARG', 9.5), ('CE1', 'TYR', 'CG', 'ARG', 9.41), ('CE1', 'TYR', 'CD', 'ARG', 8.44), ('CE1', 'TYR', 'NE', 'ARG', 9.26), ('CE1', 'TYR', 'CZ', 'ARG', 10.13), ('CE1', 'TYR', 'NH1', 'ARG', 10.35), ('CE1', 'TYR', 'NH2', 'ARG', 11.05)], [('CE2', 'TYR', 'CB', 'ARG', 9.41), ('CE2', 'TYR', 'CG', 'ARG', 9.5), ('CE2', 'TYR', 'CD', 'ARG', 8.38), ('CE2', 'TYR', 'NE', 'ARG', 8.79), ('CE2', 'TYR', 'CZ', 'ARG', 9.71), ('CE2', 'TYR', 'NH1', 'ARG', 10.28), ('CE2', 'TYR', 'NH2', 'ARG', 10.35)], [('CZ', 'TYR', 'CB', 'ARG', 8.99), ('CZ', 'TYR', 'CG', 'ARG', 8.89), ('CZ', 'TYR', 'CD', 'ARG', 7.76), ('CZ', 'TYR', 'NE', 'ARG', 8.35), ('CZ', 'TYR', 'CZ', 'ARG', 9.21), ('CZ', 'TYR', 'NH1', 'ARG', 9.59), ('CZ', 'TYR', 'NH2', 'ARG', 10.01)], [('OH', 'TYR', 'CB', 'ARG', 8.43), ('OH', 'TYR', 'CG', 'ARG', 8.08), ('OH', 'TYR', 'CD', 'ARG', 6.79), ('OH', 'TYR', 'NE', 'ARG', 7.29), ('OH', 'TYR', 'CZ', 'ARG', 8.02), ('OH', 'TYR', 'NH1', 'ARG', 8.33), ('OH', 'TYR', 'NH2', 'ARG', 8.82)]]}
LYS_ARG = { 
	'distances':
		[[14.42, 14.3, 13.3, 14.04, 14.76, 14.85, 15.59], [13.77, 13.49, 12.42, 13.12, 13.73, 13.74, 14.55], [13.09, 12.81, 11.62, 12.17, 12.76, 12.87, 13.49], [12.53, 12.06, 10.81, 11.31, 11.75, 11.76, 12.48], [11.89, 11.41, 10.05, 10.36, 10.76, 10.89, 11.37]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 14.42), ('CB', 'LYS', 'CG', 'ARG', 14.3), ('CB', 'LYS', 'CD', 'ARG', 13.3), ('CB', 'LYS', 'NE', 'ARG', 14.04), ('CB', 'LYS', 'CZ', 'ARG', 14.76), ('CB', 'LYS', 'NH1', 'ARG', 14.85), ('CB', 'LYS', 'NH2', 'ARG', 15.59)], [('CG', 'LYS', 'CB', 'ARG', 13.77), ('CG', 'LYS', 'CG', 'ARG', 13.49), ('CG', 'LYS', 'CD', 'ARG', 12.42), ('CG', 'LYS', 'NE', 'ARG', 13.12), ('CG', 'LYS', 'CZ', 'ARG', 13.73), ('CG', 'LYS', 'NH1', 'ARG', 13.74), ('CG', 'LYS', 'NH2', 'ARG', 14.55)], [('CD', 'LYS', 'CB', 'ARG', 13.09), ('CD', 'LYS', 'CG', 'ARG', 12.81), ('CD', 'LYS', 'CD', 'ARG', 11.62), ('CD', 'LYS', 'NE', 'ARG', 12.17), ('CD', 'LYS', 'CZ', 'ARG', 12.76), ('CD', 'LYS', 'NH1', 'ARG', 12.87), ('CD', 'LYS', 'NH2', 'ARG', 13.49)], [('CE', 'LYS', 'CB', 'ARG', 12.53), ('CE', 'LYS', 'CG', 'ARG', 12.06), ('CE', 'LYS', 'CD', 'ARG', 10.81), ('CE', 'LYS', 'NE', 'ARG', 11.31), ('CE', 'LYS', 'CZ', 'ARG', 11.75), ('CE', 'LYS', 'NH1', 'ARG', 11.76), ('CE', 'LYS', 'NH2', 'ARG', 12.48)], [('NZ', 'LYS', 'CB', 'ARG', 11.89), ('NZ', 'LYS', 'CG', 'ARG', 11.41), ('NZ', 'LYS', 'CD', 'ARG', 10.05), ('NZ', 'LYS', 'NE', 'ARG', 10.36), ('NZ', 'LYS', 'CZ', 'ARG', 10.76), ('NZ', 'LYS', 'NH1', 'ARG', 10.89), ('NZ', 'LYS', 'NH2', 'ARG', 11.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_TYR, d, 'A_1dhp_4_2_1_52')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ARG, d, 'A_1dhp_4_2_1_52')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_ARG, d, 'A_1dhp_4_2_1_52')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_TYR' :  match1,
		'TYR_ARG' :  match2,
		'LYS_ARG' :  match3}