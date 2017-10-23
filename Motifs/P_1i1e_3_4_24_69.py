'''
FUNC:P_1i1e_3_4_24_69
PDB:1i1e
EC:3.4.24.69
RESI:glu,arg,tyr
LOCI:a-267,369,372;
'''
import motifFunctions as cmd
GLU_TYR = { 
	'distances':
		[[9.09, 8.23, 7.6, 8.45, 7.19, 8.11, 7.48, 7.62, 11.28, 11.14, 10.42, 11.41], [7.96, 7.01, 6.2, 7.37, 5.77, 7.05, 6.26, 6.54, 9.93, 9.87, 9.18, 10.27], [8.42, 7.57, 6.49, 8.2, 6.12, 7.94, 6.96, 7.22, 10.2, 10.24, 9.44, 10.52], [9.63, 8.71, 7.57, 9.27, 7.01, 8.86, 7.76, 7.76, 11.2, 11.33, 10.59, 11.71], [7.81, 7.17, 6.05, 8.05, 6.01, 8.03, 7.1, 7.62, 9.63, 9.63, 8.69, 9.71]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 9.09), ('CB', 'GLU', 'CG', 'TYR', 8.23), ('CB', 'GLU', 'CD1', 'TYR', 7.6), ('CB', 'GLU', 'CD2', 'TYR', 8.45), ('CB', 'GLU', 'CE1', 'TYR', 7.19), ('CB', 'GLU', 'CE2', 'TYR', 8.11), ('CB', 'GLU', 'CZ', 'TYR', 7.48), ('CB', 'GLU', 'OH', 'TYR', 7.62), ('CB', 'GLU', 'O', 'TYR', 11.28), ('CB', 'GLU', 'C', 'TYR', 11.14), ('CB', 'GLU', 'CA', 'TYR', 10.42), ('CB', 'GLU', 'N', 'TYR', 11.41)], [('CG', 'GLU', 'CB', 'TYR', 7.96), ('CG', 'GLU', 'CG', 'TYR', 7.01), ('CG', 'GLU', 'CD1', 'TYR', 6.2), ('CG', 'GLU', 'CD2', 'TYR', 7.37), ('CG', 'GLU', 'CE1', 'TYR', 5.77), ('CG', 'GLU', 'CE2', 'TYR', 7.05), ('CG', 'GLU', 'CZ', 'TYR', 6.26), ('CG', 'GLU', 'OH', 'TYR', 6.54), ('CG', 'GLU', 'O', 'TYR', 9.93), ('CG', 'GLU', 'C', 'TYR', 9.87), ('CG', 'GLU', 'CA', 'TYR', 9.18), ('CG', 'GLU', 'N', 'TYR', 10.27)], [('CD', 'GLU', 'CB', 'TYR', 8.42), ('CD', 'GLU', 'CG', 'TYR', 7.57), ('CD', 'GLU', 'CD1', 'TYR', 6.49), ('CD', 'GLU', 'CD2', 'TYR', 8.2), ('CD', 'GLU', 'CE1', 'TYR', 6.12), ('CD', 'GLU', 'CE2', 'TYR', 7.94), ('CD', 'GLU', 'CZ', 'TYR', 6.96), ('CD', 'GLU', 'OH', 'TYR', 7.22), ('CD', 'GLU', 'O', 'TYR', 10.2), ('CD', 'GLU', 'C', 'TYR', 10.24), ('CD', 'GLU', 'CA', 'TYR', 9.44), ('CD', 'GLU', 'N', 'TYR', 10.52)], [('OE1', 'GLU', 'CB', 'TYR', 9.63), ('OE1', 'GLU', 'CG', 'TYR', 8.71), ('OE1', 'GLU', 'CD1', 'TYR', 7.57), ('OE1', 'GLU', 'CD2', 'TYR', 9.27), ('OE1', 'GLU', 'CE1', 'TYR', 7.01), ('OE1', 'GLU', 'CE2', 'TYR', 8.86), ('OE1', 'GLU', 'CZ', 'TYR', 7.76), ('OE1', 'GLU', 'OH', 'TYR', 7.76), ('OE1', 'GLU', 'O', 'TYR', 11.2), ('OE1', 'GLU', 'C', 'TYR', 11.33), ('OE1', 'GLU', 'CA', 'TYR', 10.59), ('OE1', 'GLU', 'N', 'TYR', 11.71)], [('OE2', 'GLU', 'CB', 'TYR', 7.81), ('OE2', 'GLU', 'CG', 'TYR', 7.17), ('OE2', 'GLU', 'CD1', 'TYR', 6.05), ('OE2', 'GLU', 'CD2', 'TYR', 8.05), ('OE2', 'GLU', 'CE1', 'TYR', 6.01), ('OE2', 'GLU', 'CE2', 'TYR', 8.03), ('OE2', 'GLU', 'CZ', 'TYR', 7.1), ('OE2', 'GLU', 'OH', 'TYR', 7.62), ('OE2', 'GLU', 'O', 'TYR', 9.63), ('OE2', 'GLU', 'C', 'TYR', 9.63), ('OE2', 'GLU', 'CA', 'TYR', 8.69), ('OE2', 'GLU', 'N', 'TYR', 9.71)]]}
ARG_TYR = { 
	'distances':
		[[9.6, 10.44, 10.49, 11.44, 11.5, 12.36, 12.39, 13.46, 8.5, 8.51, 8.2, 7.81], [8.6, 9.42, 9.35, 10.54, 10.4, 11.46, 11.39, 12.49, 7.96, 7.91, 7.32, 7.08], [8.33, 8.86, 8.57, 9.97, 9.45, 10.71, 10.47, 11.46, 7.36, 7.59, 7.12, 7.3], [7.59, 7.99, 7.81, 8.95, 8.63, 9.65, 9.5, 10.47, 6.05, 6.44, 6.29, 6.67], [7.55, 7.6, 7.24, 8.47, 7.82, 8.95, 8.66, 9.5, 5.68, 6.38, 6.42, 7.17], [8.18, 8.06, 7.39, 8.99, 7.8, 9.31, 8.76, 9.47, 6.67, 7.4, 7.27, 8.13], [7.32, 7.2, 6.99, 7.81, 7.44, 8.2, 8.02, 8.81, 4.8, 5.75, 6.23, 7.12]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 9.6), ('CB', 'ARG', 'CG', 'TYR', 10.44), ('CB', 'ARG', 'CD1', 'TYR', 10.49), ('CB', 'ARG', 'CD2', 'TYR', 11.44), ('CB', 'ARG', 'CE1', 'TYR', 11.5), ('CB', 'ARG', 'CE2', 'TYR', 12.36), ('CB', 'ARG', 'CZ', 'TYR', 12.39), ('CB', 'ARG', 'OH', 'TYR', 13.46), ('CB', 'ARG', 'O', 'TYR', 8.5), ('CB', 'ARG', 'C', 'TYR', 8.51), ('CB', 'ARG', 'CA', 'TYR', 8.2), ('CB', 'ARG', 'N', 'TYR', 7.81)], [('CG', 'ARG', 'CB', 'TYR', 8.6), ('CG', 'ARG', 'CG', 'TYR', 9.42), ('CG', 'ARG', 'CD1', 'TYR', 9.35), ('CG', 'ARG', 'CD2', 'TYR', 10.54), ('CG', 'ARG', 'CE1', 'TYR', 10.4), ('CG', 'ARG', 'CE2', 'TYR', 11.46), ('CG', 'ARG', 'CZ', 'TYR', 11.39), ('CG', 'ARG', 'OH', 'TYR', 12.49), ('CG', 'ARG', 'O', 'TYR', 7.96), ('CG', 'ARG', 'C', 'TYR', 7.91), ('CG', 'ARG', 'CA', 'TYR', 7.32), ('CG', 'ARG', 'N', 'TYR', 7.08)], [('CD', 'ARG', 'CB', 'TYR', 8.33), ('CD', 'ARG', 'CG', 'TYR', 8.86), ('CD', 'ARG', 'CD1', 'TYR', 8.57), ('CD', 'ARG', 'CD2', 'TYR', 9.97), ('CD', 'ARG', 'CE1', 'TYR', 9.45), ('CD', 'ARG', 'CE2', 'TYR', 10.71), ('CD', 'ARG', 'CZ', 'TYR', 10.47), ('CD', 'ARG', 'OH', 'TYR', 11.46), ('CD', 'ARG', 'O', 'TYR', 7.36), ('CD', 'ARG', 'C', 'TYR', 7.59), ('CD', 'ARG', 'CA', 'TYR', 7.12), ('CD', 'ARG', 'N', 'TYR', 7.3)], [('NE', 'ARG', 'CB', 'TYR', 7.59), ('NE', 'ARG', 'CG', 'TYR', 7.99), ('NE', 'ARG', 'CD1', 'TYR', 7.81), ('NE', 'ARG', 'CD2', 'TYR', 8.95), ('NE', 'ARG', 'CE1', 'TYR', 8.63), ('NE', 'ARG', 'CE2', 'TYR', 9.65), ('NE', 'ARG', 'CZ', 'TYR', 9.5), ('NE', 'ARG', 'OH', 'TYR', 10.47), ('NE', 'ARG', 'O', 'TYR', 6.05), ('NE', 'ARG', 'C', 'TYR', 6.44), ('NE', 'ARG', 'CA', 'TYR', 6.29), ('NE', 'ARG', 'N', 'TYR', 6.67)], [('CZ', 'ARG', 'CB', 'TYR', 7.55), ('CZ', 'ARG', 'CG', 'TYR', 7.6), ('CZ', 'ARG', 'CD1', 'TYR', 7.24), ('CZ', 'ARG', 'CD2', 'TYR', 8.47), ('CZ', 'ARG', 'CE1', 'TYR', 7.82), ('CZ', 'ARG', 'CE2', 'TYR', 8.95), ('CZ', 'ARG', 'CZ', 'TYR', 8.66), ('CZ', 'ARG', 'OH', 'TYR', 9.5), ('CZ', 'ARG', 'O', 'TYR', 5.68), ('CZ', 'ARG', 'C', 'TYR', 6.38), ('CZ', 'ARG', 'CA', 'TYR', 6.42), ('CZ', 'ARG', 'N', 'TYR', 7.17)], [('NH1', 'ARG', 'CB', 'TYR', 8.18), ('NH1', 'ARG', 'CG', 'TYR', 8.06), ('NH1', 'ARG', 'CD1', 'TYR', 7.39), ('NH1', 'ARG', 'CD2', 'TYR', 8.99), ('NH1', 'ARG', 'CE1', 'TYR', 7.8), ('NH1', 'ARG', 'CE2', 'TYR', 9.31), ('NH1', 'ARG', 'CZ', 'TYR', 8.76), ('NH1', 'ARG', 'OH', 'TYR', 9.47), ('NH1', 'ARG', 'O', 'TYR', 6.67), ('NH1', 'ARG', 'C', 'TYR', 7.4), ('NH1', 'ARG', 'CA', 'TYR', 7.27), ('NH1', 'ARG', 'N', 'TYR', 8.13)], [('NH2', 'ARG', 'CB', 'TYR', 7.32), ('NH2', 'ARG', 'CG', 'TYR', 7.2), ('NH2', 'ARG', 'CD1', 'TYR', 6.99), ('NH2', 'ARG', 'CD2', 'TYR', 7.81), ('NH2', 'ARG', 'CE1', 'TYR', 7.44), ('NH2', 'ARG', 'CE2', 'TYR', 8.2), ('NH2', 'ARG', 'CZ', 'TYR', 8.02), ('NH2', 'ARG', 'OH', 'TYR', 8.81), ('NH2', 'ARG', 'O', 'TYR', 4.8), ('NH2', 'ARG', 'C', 'TYR', 5.75), ('NH2', 'ARG', 'CA', 'TYR', 6.23), ('NH2', 'ARG', 'N', 'TYR', 7.12)]]}
ARG_GLU = { 
	'distances':
		[[15.51, 14.13, 13.72, 14.61, 12.62], [14.14, 12.79, 12.32, 13.21, 11.19], [13.42, 11.99, 11.45, 12.25, 10.37], [13.04, 11.57, 11.2, 12.04, 10.23], [12.46, 10.96, 10.57, 11.34, 9.71], [12.18, 10.67, 10.08, 10.71, 9.22], [12.4, 10.9, 10.71, 11.49, 9.98]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 15.51), ('CB', 'ARG', 'CG', 'GLU', 14.13), ('CB', 'ARG', 'CD', 'GLU', 13.72), ('CB', 'ARG', 'OE1', 'GLU', 14.61), ('CB', 'ARG', 'OE2', 'GLU', 12.62)], [('CG', 'ARG', 'CB', 'GLU', 14.14), ('CG', 'ARG', 'CG', 'GLU', 12.79), ('CG', 'ARG', 'CD', 'GLU', 12.32), ('CG', 'ARG', 'OE1', 'GLU', 13.21), ('CG', 'ARG', 'OE2', 'GLU', 11.19)], [('CD', 'ARG', 'CB', 'GLU', 13.42), ('CD', 'ARG', 'CG', 'GLU', 11.99), ('CD', 'ARG', 'CD', 'GLU', 11.45), ('CD', 'ARG', 'OE1', 'GLU', 12.25), ('CD', 'ARG', 'OE2', 'GLU', 10.37)], [('NE', 'ARG', 'CB', 'GLU', 13.04), ('NE', 'ARG', 'CG', 'GLU', 11.57), ('NE', 'ARG', 'CD', 'GLU', 11.2), ('NE', 'ARG', 'OE1', 'GLU', 12.04), ('NE', 'ARG', 'OE2', 'GLU', 10.23)], [('CZ', 'ARG', 'CB', 'GLU', 12.46), ('CZ', 'ARG', 'CG', 'GLU', 10.96), ('CZ', 'ARG', 'CD', 'GLU', 10.57), ('CZ', 'ARG', 'OE1', 'GLU', 11.34), ('CZ', 'ARG', 'OE2', 'GLU', 9.71)], [('NH1', 'ARG', 'CB', 'GLU', 12.18), ('NH1', 'ARG', 'CG', 'GLU', 10.67), ('NH1', 'ARG', 'CD', 'GLU', 10.08), ('NH1', 'ARG', 'OE1', 'GLU', 10.71), ('NH1', 'ARG', 'OE2', 'GLU', 9.22)], [('NH2', 'ARG', 'CB', 'GLU', 12.4), ('NH2', 'ARG', 'CG', 'GLU', 10.9), ('NH2', 'ARG', 'CD', 'GLU', 10.71), ('NH2', 'ARG', 'OE1', 'GLU', 11.49), ('NH2', 'ARG', 'OE2', 'GLU', 9.98)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_TYR, d, 'P_1i1e_3_4_24_69')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_TYR, d, 'P_1i1e_3_4_24_69')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_GLU, d, 'P_1i1e_3_4_24_69')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_TYR' :  match1,
		'ARG_TYR' :  match2,
		'ARG_GLU' :  match3}