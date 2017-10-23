'''
FUNC:A_1p7m_3_2_2_20
PDB:1p7m
EC:3.2.2.20
RESI:tyr,glu,trp
LOCI:a-16,38,46;
'''
import motifFunctions as cmd
TRP_GLU = { 
	'distances':
		[[10.47, 10.11, 8.92, 8.98, 8.18], [10.42, 10.22, 8.94, 8.74, 8.41], [11.59, 11.45, 10.15, 9.84, 9.67], [9.42, 9.33, 8.04, 7.65, 7.72], [11.51, 11.49, 10.18, 9.67, 9.88], [10.26, 10.3, 9.0, 8.41, 8.83], [8.03, 7.96, 6.68, 6.27, 6.48], [9.95, 10.13, 8.88, 8.09, 8.94], [7.6, 7.72, 6.49, 5.76, 6.64], [8.68, 8.92, 7.73, 6.85, 7.97]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'GLU', 10.47), ('CB', 'TRP', 'CG', 'GLU', 10.11), ('CB', 'TRP', 'CD', 'GLU', 8.92), ('CB', 'TRP', 'OE1', 'GLU', 8.98), ('CB', 'TRP', 'OE2', 'GLU', 8.18)], [('CG', 'TRP', 'CB', 'GLU', 10.42), ('CG', 'TRP', 'CG', 'GLU', 10.22), ('CG', 'TRP', 'CD', 'GLU', 8.94), ('CG', 'TRP', 'OE1', 'GLU', 8.74), ('CG', 'TRP', 'OE2', 'GLU', 8.41)], [('CD1', 'TRP', 'CB', 'GLU', 11.59), ('CD1', 'TRP', 'CG', 'GLU', 11.45), ('CD1', 'TRP', 'CD', 'GLU', 10.15), ('CD1', 'TRP', 'OE1', 'GLU', 9.84), ('CD1', 'TRP', 'OE2', 'GLU', 9.67)], [('CD2', 'TRP', 'CB', 'GLU', 9.42), ('CD2', 'TRP', 'CG', 'GLU', 9.33), ('CD2', 'TRP', 'CD', 'GLU', 8.04), ('CD2', 'TRP', 'OE1', 'GLU', 7.65), ('CD2', 'TRP', 'OE2', 'GLU', 7.72)], [('NE1', 'TRP', 'CB', 'GLU', 11.51), ('NE1', 'TRP', 'CG', 'GLU', 11.49), ('NE1', 'TRP', 'CD', 'GLU', 10.18), ('NE1', 'TRP', 'OE1', 'GLU', 9.67), ('NE1', 'TRP', 'OE2', 'GLU', 9.88)], [('CE2', 'TRP', 'CB', 'GLU', 10.26), ('CE2', 'TRP', 'CG', 'GLU', 10.3), ('CE2', 'TRP', 'CD', 'GLU', 9.0), ('CE2', 'TRP', 'OE1', 'GLU', 8.41), ('CE2', 'TRP', 'OE2', 'GLU', 8.83)], [('CE3', 'TRP', 'CB', 'GLU', 8.03), ('CE3', 'TRP', 'CG', 'GLU', 7.96), ('CE3', 'TRP', 'CD', 'GLU', 6.68), ('CE3', 'TRP', 'OE1', 'GLU', 6.27), ('CE3', 'TRP', 'OE2', 'GLU', 6.48)], [('CZ2', 'TRP', 'CB', 'GLU', 9.95), ('CZ2', 'TRP', 'CG', 'GLU', 10.13), ('CZ2', 'TRP', 'CD', 'GLU', 8.88), ('CZ2', 'TRP', 'OE1', 'GLU', 8.09), ('CZ2', 'TRP', 'OE2', 'GLU', 8.94)], [('CZ3', 'TRP', 'CB', 'GLU', 7.6), ('CZ3', 'TRP', 'CG', 'GLU', 7.72), ('CZ3', 'TRP', 'CD', 'GLU', 6.49), ('CZ3', 'TRP', 'OE1', 'GLU', 5.76), ('CZ3', 'TRP', 'OE2', 'GLU', 6.64)], [('CH2', 'TRP', 'CB', 'GLU', 8.68), ('CH2', 'TRP', 'CG', 'GLU', 8.92), ('CH2', 'TRP', 'CD', 'GLU', 7.73), ('CH2', 'TRP', 'OE1', 'GLU', 6.85), ('CH2', 'TRP', 'OE2', 'GLU', 7.97)]]}
TYR_TRP = { 
	'distances':
		[[10.44, 8.99, 8.08, 8.49, 6.83, 7.1, 9.32, 6.67, 9.01, 7.78], [9.79, 8.34, 7.66, 7.61, 6.37, 6.28, 8.25, 5.61, 7.8, 6.56], [10.33, 8.86, 8.39, 7.88, 7.04, 6.6, 8.24, 5.56, 7.51, 6.15], [8.94, 7.57, 6.97, 6.93, 5.82, 5.76, 7.61, 5.37, 7.34, 6.31], [10.09, 8.69, 8.49, 7.53, 7.23, 6.46, 7.6, 5.25, 6.68, 5.4], [8.65, 7.36, 7.1, 6.51, 6.06, 5.59, 6.88, 5.04, 6.49, 5.59], [9.27, 7.97, 7.89, 6.84, 6.78, 5.97, 6.88, 4.97, 6.1, 5.06], [9.39, 8.25, 8.45, 7.02, 7.51, 6.49, 6.69, 5.53, 5.76, 5.07]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TRP', 10.44), ('CB', 'TYR', 'CG', 'TRP', 8.99), ('CB', 'TYR', 'CD1', 'TRP', 8.08), ('CB', 'TYR', 'CD2', 'TRP', 8.49), ('CB', 'TYR', 'NE1', 'TRP', 6.83), ('CB', 'TYR', 'CE2', 'TRP', 7.1), ('CB', 'TYR', 'CE3', 'TRP', 9.32), ('CB', 'TYR', 'CZ2', 'TRP', 6.67), ('CB', 'TYR', 'CZ3', 'TRP', 9.01), ('CB', 'TYR', 'CH2', 'TRP', 7.78)], [('CG', 'TYR', 'CB', 'TRP', 9.79), ('CG', 'TYR', 'CG', 'TRP', 8.34), ('CG', 'TYR', 'CD1', 'TRP', 7.66), ('CG', 'TYR', 'CD2', 'TRP', 7.61), ('CG', 'TYR', 'NE1', 'TRP', 6.37), ('CG', 'TYR', 'CE2', 'TRP', 6.28), ('CG', 'TYR', 'CE3', 'TRP', 8.25), ('CG', 'TYR', 'CZ2', 'TRP', 5.61), ('CG', 'TYR', 'CZ3', 'TRP', 7.8), ('CG', 'TYR', 'CH2', 'TRP', 6.56)], [('CD1', 'TYR', 'CB', 'TRP', 10.33), ('CD1', 'TYR', 'CG', 'TRP', 8.86), ('CD1', 'TYR', 'CD1', 'TRP', 8.39), ('CD1', 'TYR', 'CD2', 'TRP', 7.88), ('CD1', 'TYR', 'NE1', 'TRP', 7.04), ('CD1', 'TYR', 'CE2', 'TRP', 6.6), ('CD1', 'TYR', 'CE3', 'TRP', 8.24), ('CD1', 'TYR', 'CZ2', 'TRP', 5.56), ('CD1', 'TYR', 'CZ3', 'TRP', 7.51), ('CD1', 'TYR', 'CH2', 'TRP', 6.15)], [('CD2', 'TYR', 'CB', 'TRP', 8.94), ('CD2', 'TYR', 'CG', 'TRP', 7.57), ('CD2', 'TYR', 'CD1', 'TRP', 6.97), ('CD2', 'TYR', 'CD2', 'TRP', 6.93), ('CD2', 'TYR', 'NE1', 'TRP', 5.82), ('CD2', 'TYR', 'CE2', 'TRP', 5.76), ('CD2', 'TYR', 'CE3', 'TRP', 7.61), ('CD2', 'TYR', 'CZ2', 'TRP', 5.37), ('CD2', 'TYR', 'CZ3', 'TRP', 7.34), ('CD2', 'TYR', 'CH2', 'TRP', 6.31)], [('CE1', 'TYR', 'CB', 'TRP', 10.09), ('CE1', 'TYR', 'CG', 'TRP', 8.69), ('CE1', 'TYR', 'CD1', 'TRP', 8.49), ('CE1', 'TYR', 'CD2', 'TRP', 7.53), ('CE1', 'TYR', 'NE1', 'TRP', 7.23), ('CE1', 'TYR', 'CE2', 'TRP', 6.46), ('CE1', 'TYR', 'CE3', 'TRP', 7.6), ('CE1', 'TYR', 'CZ2', 'TRP', 5.25), ('CE1', 'TYR', 'CZ3', 'TRP', 6.68), ('CE1', 'TYR', 'CH2', 'TRP', 5.4)], [('CE2', 'TYR', 'CB', 'TRP', 8.65), ('CE2', 'TYR', 'CG', 'TRP', 7.36), ('CE2', 'TYR', 'CD1', 'TRP', 7.1), ('CE2', 'TYR', 'CD2', 'TRP', 6.51), ('CE2', 'TYR', 'NE1', 'TRP', 6.06), ('CE2', 'TYR', 'CE2', 'TRP', 5.59), ('CE2', 'TYR', 'CE3', 'TRP', 6.88), ('CE2', 'TYR', 'CZ2', 'TRP', 5.04), ('CE2', 'TYR', 'CZ3', 'TRP', 6.49), ('CE2', 'TYR', 'CH2', 'TRP', 5.59)], [('CZ', 'TYR', 'CB', 'TRP', 9.27), ('CZ', 'TYR', 'CG', 'TRP', 7.97), ('CZ', 'TYR', 'CD1', 'TRP', 7.89), ('CZ', 'TYR', 'CD2', 'TRP', 6.84), ('CZ', 'TYR', 'NE1', 'TRP', 6.78), ('CZ', 'TYR', 'CE2', 'TRP', 5.97), ('CZ', 'TYR', 'CE3', 'TRP', 6.88), ('CZ', 'TYR', 'CZ2', 'TRP', 4.97), ('CZ', 'TYR', 'CZ3', 'TRP', 6.1), ('CZ', 'TYR', 'CH2', 'TRP', 5.06)], [('OH', 'TYR', 'CB', 'TRP', 9.39), ('OH', 'TYR', 'CG', 'TRP', 8.25), ('OH', 'TYR', 'CD1', 'TRP', 8.45), ('OH', 'TYR', 'CD2', 'TRP', 7.02), ('OH', 'TYR', 'NE1', 'TRP', 7.51), ('OH', 'TYR', 'CE2', 'TRP', 6.49), ('OH', 'TYR', 'CE3', 'TRP', 6.69), ('OH', 'TYR', 'CZ2', 'TRP', 5.53), ('OH', 'TYR', 'CZ3', 'TRP', 5.76), ('OH', 'TYR', 'CH2', 'TRP', 5.07)]]}
TYR_GLU = { 
	'distances':
		[[14.44, 14.61, 13.31, 12.4, 13.35], [13.15, 13.27, 11.96, 11.01, 12.04], [12.52, 12.78, 11.56, 10.53, 11.82], [12.74, 12.69, 11.29, 10.41, 11.24], [11.4, 11.62, 10.42, 9.33, 10.74], [11.64, 11.51, 10.1, 9.2, 10.09], [10.91, 10.92, 9.61, 8.58, 9.81], [9.94, 9.87, 8.58, 7.51, 8.85]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 14.44), ('CB', 'TYR', 'CG', 'GLU', 14.61), ('CB', 'TYR', 'CD', 'GLU', 13.31), ('CB', 'TYR', 'OE1', 'GLU', 12.4), ('CB', 'TYR', 'OE2', 'GLU', 13.35)], [('CG', 'TYR', 'CB', 'GLU', 13.15), ('CG', 'TYR', 'CG', 'GLU', 13.27), ('CG', 'TYR', 'CD', 'GLU', 11.96), ('CG', 'TYR', 'OE1', 'GLU', 11.01), ('CG', 'TYR', 'OE2', 'GLU', 12.04)], [('CD1', 'TYR', 'CB', 'GLU', 12.52), ('CD1', 'TYR', 'CG', 'GLU', 12.78), ('CD1', 'TYR', 'CD', 'GLU', 11.56), ('CD1', 'TYR', 'OE1', 'GLU', 10.53), ('CD1', 'TYR', 'OE2', 'GLU', 11.82)], [('CD2', 'TYR', 'CB', 'GLU', 12.74), ('CD2', 'TYR', 'CG', 'GLU', 12.69), ('CD2', 'TYR', 'CD', 'GLU', 11.29), ('CD2', 'TYR', 'OE1', 'GLU', 10.41), ('CD2', 'TYR', 'OE2', 'GLU', 11.24)], [('CE1', 'TYR', 'CB', 'GLU', 11.4), ('CE1', 'TYR', 'CG', 'GLU', 11.62), ('CE1', 'TYR', 'CD', 'GLU', 10.42), ('CE1', 'TYR', 'OE1', 'GLU', 9.33), ('CE1', 'TYR', 'OE2', 'GLU', 10.74)], [('CE2', 'TYR', 'CB', 'GLU', 11.64), ('CE2', 'TYR', 'CG', 'GLU', 11.51), ('CE2', 'TYR', 'CD', 'GLU', 10.1), ('CE2', 'TYR', 'OE1', 'GLU', 9.2), ('CE2', 'TYR', 'OE2', 'GLU', 10.09)], [('CZ', 'TYR', 'CB', 'GLU', 10.91), ('CZ', 'TYR', 'CG', 'GLU', 10.92), ('CZ', 'TYR', 'CD', 'GLU', 9.61), ('CZ', 'TYR', 'OE1', 'GLU', 8.58), ('CZ', 'TYR', 'OE2', 'GLU', 9.81)], [('OH', 'TYR', 'CB', 'GLU', 9.94), ('OH', 'TYR', 'CG', 'GLU', 9.87), ('OH', 'TYR', 'CD', 'GLU', 8.58), ('OH', 'TYR', 'OE1', 'GLU', 7.51), ('OH', 'TYR', 'OE2', 'GLU', 8.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_GLU, d, 'A_1p7m_3_2_2_20')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_TRP, d, 'A_1p7m_3_2_2_20')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_GLU, d, 'A_1p7m_3_2_2_20')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_GLU' :  match1,
		'TYR_TRP' :  match2,
		'TYR_GLU' :  match3}