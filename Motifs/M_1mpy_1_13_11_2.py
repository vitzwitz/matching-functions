'''
FUNC:M_1mpy_1_13_11_2
PDB:1mpy
EC:1.13.11.2
RESI:his,his,tyr,fe2
LOCI:a-199,246,255,308;
'''
import motifFunctions as cmd
FE2_HISI = { 
	'distances':
		[9.36, 8.28, 8.62, 7.09, 7.78, 6.73],
	'comparisons':
		[('FE', 'FE2', 'CB', 'HISI', 9.36), ('FE', 'FE2', 'CG', 'HISI', 8.28), ('FE', 'FE2', 'ND1', 'HISI', 8.62), ('FE', 'FE2', 'CD2', 'HISI', 7.09), ('FE', 'FE2', 'CE1', 'HISI', 7.78), ('FE', 'FE2', 'NE2', 'HISI', 6.73)]}
HIS_HIS = { 
	'distances':
		[[12.68, 12.6, 13.36, 12.04, 13.29, 12.51], [11.64, 11.43, 12.16, 10.76, 12.0, 11.16], [10.3, 10.14, 10.92, 9.52, 10.84, 10.01], [11.94, 11.52, 12.15, 10.72, 11.81, 10.93], [9.75, 9.37, 10.09, 8.62, 9.86, 8.98], [10.83, 10.3, 10.9, 9.44, 10.51, 9.6], [12.68, 11.64, 10.3, 11.94, 9.75, 10.83], [12.6, 11.43, 10.14, 11.52, 9.37, 10.3], [13.36, 12.16, 10.92, 12.15, 10.09, 10.9], [12.04, 10.76, 9.52, 10.72, 8.62, 9.44], [13.29, 12.0, 10.84, 11.81, 9.86, 10.51], [12.51, 11.16, 10.01, 10.93, 8.98, 9.6]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 12.68), ('CB', 'HIS', 'CG', 'HIS', 12.6), ('CB', 'HIS', 'ND1', 'HIS', 13.36), ('CB', 'HIS', 'CD2', 'HIS', 12.04), ('CB', 'HIS', 'CE1', 'HIS', 13.29), ('CB', 'HIS', 'NE2', 'HIS', 12.51)], [('CG', 'HIS', 'CB', 'HIS', 11.64), ('CG', 'HIS', 'CG', 'HIS', 11.43), ('CG', 'HIS', 'ND1', 'HIS', 12.16), ('CG', 'HIS', 'CD2', 'HIS', 10.76), ('CG', 'HIS', 'CE1', 'HIS', 12.0), ('CG', 'HIS', 'NE2', 'HIS', 11.16)], [('ND1', 'HIS', 'CB', 'HIS', 10.3), ('ND1', 'HIS', 'CG', 'HIS', 10.14), ('ND1', 'HIS', 'ND1', 'HIS', 10.92), ('ND1', 'HIS', 'CD2', 'HIS', 9.52), ('ND1', 'HIS', 'CE1', 'HIS', 10.84), ('ND1', 'HIS', 'NE2', 'HIS', 10.01)], [('CD2', 'HIS', 'CB', 'HIS', 11.94), ('CD2', 'HIS', 'CG', 'HIS', 11.52), ('CD2', 'HIS', 'ND1', 'HIS', 12.15), ('CD2', 'HIS', 'CD2', 'HIS', 10.72), ('CD2', 'HIS', 'CE1', 'HIS', 11.81), ('CD2', 'HIS', 'NE2', 'HIS', 10.93)], [('CE1', 'HIS', 'CB', 'HIS', 9.75), ('CE1', 'HIS', 'CG', 'HIS', 9.37), ('CE1', 'HIS', 'ND1', 'HIS', 10.09), ('CE1', 'HIS', 'CD2', 'HIS', 8.62), ('CE1', 'HIS', 'CE1', 'HIS', 9.86), ('CE1', 'HIS', 'NE2', 'HIS', 8.98)], [('NE2', 'HIS', 'CB', 'HIS', 10.83), ('NE2', 'HIS', 'CG', 'HIS', 10.3), ('NE2', 'HIS', 'ND1', 'HIS', 10.9), ('NE2', 'HIS', 'CD2', 'HIS', 9.44), ('NE2', 'HIS', 'CE1', 'HIS', 10.51), ('NE2', 'HIS', 'NE2', 'HIS', 9.6)], [('CB', 'HIS', 'CB', 'HIS', 12.68), ('CB', 'HIS', 'CG', 'HIS', 11.64), ('CB', 'HIS', 'ND1', 'HIS', 10.3), ('CB', 'HIS', 'CD2', 'HIS', 11.94), ('CB', 'HIS', 'CE1', 'HIS', 9.75), ('CB', 'HIS', 'NE2', 'HIS', 10.83)], [('CG', 'HIS', 'CB', 'HIS', 12.6), ('CG', 'HIS', 'CG', 'HIS', 11.43), ('CG', 'HIS', 'ND1', 'HIS', 10.14), ('CG', 'HIS', 'CD2', 'HIS', 11.52), ('CG', 'HIS', 'CE1', 'HIS', 9.37), ('CG', 'HIS', 'NE2', 'HIS', 10.3)], [('ND1', 'HIS', 'CB', 'HIS', 13.36), ('ND1', 'HIS', 'CG', 'HIS', 12.16), ('ND1', 'HIS', 'ND1', 'HIS', 10.92), ('ND1', 'HIS', 'CD2', 'HIS', 12.15), ('ND1', 'HIS', 'CE1', 'HIS', 10.09), ('ND1', 'HIS', 'NE2', 'HIS', 10.9)], [('CD2', 'HIS', 'CB', 'HIS', 12.04), ('CD2', 'HIS', 'CG', 'HIS', 10.76), ('CD2', 'HIS', 'ND1', 'HIS', 9.52), ('CD2', 'HIS', 'CD2', 'HIS', 10.72), ('CD2', 'HIS', 'CE1', 'HIS', 8.62), ('CD2', 'HIS', 'NE2', 'HIS', 9.44)], [('CE1', 'HIS', 'CB', 'HIS', 13.29), ('CE1', 'HIS', 'CG', 'HIS', 12.0), ('CE1', 'HIS', 'ND1', 'HIS', 10.84), ('CE1', 'HIS', 'CD2', 'HIS', 11.81), ('CE1', 'HIS', 'CE1', 'HIS', 9.86), ('CE1', 'HIS', 'NE2', 'HIS', 10.51)], [('NE2', 'HIS', 'CB', 'HIS', 12.51), ('NE2', 'HIS', 'CG', 'HIS', 11.16), ('NE2', 'HIS', 'ND1', 'HIS', 10.01), ('NE2', 'HIS', 'CD2', 'HIS', 10.93), ('NE2', 'HIS', 'CE1', 'HIS', 8.98), ('NE2', 'HIS', 'NE2', 'HIS', 9.6)]]}
TYR_FE2 = { 
	'distances':
		[[10.51], [9.15], [8.04], [9.18], [6.77], [8.14], [6.81], [5.82]],
	'comparisons':
		[[('CB', 'TYR', 'FE', 'FE2', 10.51)], [('CG', 'TYR', 'FE', 'FE2', 9.15)], [('CD1', 'TYR', 'FE', 'FE2', 8.04)], [('CD2', 'TYR', 'FE', 'FE2', 9.18)], [('CE1', 'TYR', 'FE', 'FE2', 6.77)], [('CE2', 'TYR', 'FE', 'FE2', 8.14)], [('CZ', 'TYR', 'FE', 'FE2', 6.81)], [('OH', 'TYR', 'FE', 'FE2', 5.82)]]}
HIS_FE2 = { 
	'distances':
		[[9.61], [8.11], [7.47], [7.32], [6.17], [6.0], [9.36], [8.28], [8.62], [7.09], [7.78], [6.73]],
	'comparisons':
		[[('CB', 'HIS', 'FE', 'FE2', 9.61)], [('CG', 'HIS', 'FE', 'FE2', 8.11)], [('ND1', 'HIS', 'FE', 'FE2', 7.47)], [('CD2', 'HIS', 'FE', 'FE2', 7.32)], [('CE1', 'HIS', 'FE', 'FE2', 6.17)], [('NE2', 'HIS', 'FE', 'FE2', 6.0)], [('CB', 'HIS', 'FE', 'FE2', 9.36)], [('CG', 'HIS', 'FE', 'FE2', 8.28)], [('ND1', 'HIS', 'FE', 'FE2', 8.62)], [('CD2', 'HIS', 'FE', 'FE2', 7.09)], [('CE1', 'HIS', 'FE', 'FE2', 7.78)], [('NE2', 'HIS', 'FE', 'FE2', 6.73)]]}
HIS_TYR = { 
	'distances':
		[[18.04, 16.62, 15.6, 16.38, 14.26, 15.1, 13.98, 12.67], [16.55, 15.14, 14.1, 14.93, 12.77, 13.67, 12.52, 11.24], [15.78, 14.34, 13.32, 14.12, 11.98, 12.85, 11.7, 10.4], [15.77, 14.39, 13.34, 14.23, 12.04, 13.02, 11.85, 10.62], [14.5, 13.07, 12.04, 12.88, 10.7, 11.63, 10.45, 9.17], [14.47, 13.07, 12.02, 12.92, 10.71, 11.71, 10.52, 9.29], [12.41, 11.19, 10.68, 10.78, 9.72, 9.81, 9.24, 8.51], [11.0, 9.74, 9.23, 9.32, 8.25, 8.34, 7.74, 7.05], [10.3, 9.05, 8.76, 8.45, 7.85, 7.47, 7.14, 6.57], [10.33, 9.03, 8.33, 8.78, 7.28, 7.79, 6.95, 6.22], [9.15, 7.83, 7.52, 7.23, 6.58, 6.2, 5.82, 5.31], [9.14, 7.78, 7.17, 7.45, 6.09, 6.42, 5.62, 4.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 18.04), ('CB', 'HIS', 'CG', 'TYR', 16.62), ('CB', 'HIS', 'CD1', 'TYR', 15.6), ('CB', 'HIS', 'CD2', 'TYR', 16.38), ('CB', 'HIS', 'CE1', 'TYR', 14.26), ('CB', 'HIS', 'CE2', 'TYR', 15.1), ('CB', 'HIS', 'CZ', 'TYR', 13.98), ('CB', 'HIS', 'OH', 'TYR', 12.67)], [('CG', 'HIS', 'CB', 'TYR', 16.55), ('CG', 'HIS', 'CG', 'TYR', 15.14), ('CG', 'HIS', 'CD1', 'TYR', 14.1), ('CG', 'HIS', 'CD2', 'TYR', 14.93), ('CG', 'HIS', 'CE1', 'TYR', 12.77), ('CG', 'HIS', 'CE2', 'TYR', 13.67), ('CG', 'HIS', 'CZ', 'TYR', 12.52), ('CG', 'HIS', 'OH', 'TYR', 11.24)], [('ND1', 'HIS', 'CB', 'TYR', 15.78), ('ND1', 'HIS', 'CG', 'TYR', 14.34), ('ND1', 'HIS', 'CD1', 'TYR', 13.32), ('ND1', 'HIS', 'CD2', 'TYR', 14.12), ('ND1', 'HIS', 'CE1', 'TYR', 11.98), ('ND1', 'HIS', 'CE2', 'TYR', 12.85), ('ND1', 'HIS', 'CZ', 'TYR', 11.7), ('ND1', 'HIS', 'OH', 'TYR', 10.4)], [('CD2', 'HIS', 'CB', 'TYR', 15.77), ('CD2', 'HIS', 'CG', 'TYR', 14.39), ('CD2', 'HIS', 'CD1', 'TYR', 13.34), ('CD2', 'HIS', 'CD2', 'TYR', 14.23), ('CD2', 'HIS', 'CE1', 'TYR', 12.04), ('CD2', 'HIS', 'CE2', 'TYR', 13.02), ('CD2', 'HIS', 'CZ', 'TYR', 11.85), ('CD2', 'HIS', 'OH', 'TYR', 10.62)], [('CE1', 'HIS', 'CB', 'TYR', 14.5), ('CE1', 'HIS', 'CG', 'TYR', 13.07), ('CE1', 'HIS', 'CD1', 'TYR', 12.04), ('CE1', 'HIS', 'CD2', 'TYR', 12.88), ('CE1', 'HIS', 'CE1', 'TYR', 10.7), ('CE1', 'HIS', 'CE2', 'TYR', 11.63), ('CE1', 'HIS', 'CZ', 'TYR', 10.45), ('CE1', 'HIS', 'OH', 'TYR', 9.17)], [('NE2', 'HIS', 'CB', 'TYR', 14.47), ('NE2', 'HIS', 'CG', 'TYR', 13.07), ('NE2', 'HIS', 'CD1', 'TYR', 12.02), ('NE2', 'HIS', 'CD2', 'TYR', 12.92), ('NE2', 'HIS', 'CE1', 'TYR', 10.71), ('NE2', 'HIS', 'CE2', 'TYR', 11.71), ('NE2', 'HIS', 'CZ', 'TYR', 10.52), ('NE2', 'HIS', 'OH', 'TYR', 9.29)], [('CB', 'HIS', 'CB', 'TYR', 12.41), ('CB', 'HIS', 'CG', 'TYR', 11.19), ('CB', 'HIS', 'CD1', 'TYR', 10.68), ('CB', 'HIS', 'CD2', 'TYR', 10.78), ('CB', 'HIS', 'CE1', 'TYR', 9.72), ('CB', 'HIS', 'CE2', 'TYR', 9.81), ('CB', 'HIS', 'CZ', 'TYR', 9.24), ('CB', 'HIS', 'OH', 'TYR', 8.51)], [('CG', 'HIS', 'CB', 'TYR', 11.0), ('CG', 'HIS', 'CG', 'TYR', 9.74), ('CG', 'HIS', 'CD1', 'TYR', 9.23), ('CG', 'HIS', 'CD2', 'TYR', 9.32), ('CG', 'HIS', 'CE1', 'TYR', 8.25), ('CG', 'HIS', 'CE2', 'TYR', 8.34), ('CG', 'HIS', 'CZ', 'TYR', 7.74), ('CG', 'HIS', 'OH', 'TYR', 7.05)], [('ND1', 'HIS', 'CB', 'TYR', 10.3), ('ND1', 'HIS', 'CG', 'TYR', 9.05), ('ND1', 'HIS', 'CD1', 'TYR', 8.76), ('ND1', 'HIS', 'CD2', 'TYR', 8.45), ('ND1', 'HIS', 'CE1', 'TYR', 7.85), ('ND1', 'HIS', 'CE2', 'TYR', 7.47), ('ND1', 'HIS', 'CZ', 'TYR', 7.14), ('ND1', 'HIS', 'OH', 'TYR', 6.57)], [('CD2', 'HIS', 'CB', 'TYR', 10.33), ('CD2', 'HIS', 'CG', 'TYR', 9.03), ('CD2', 'HIS', 'CD1', 'TYR', 8.33), ('CD2', 'HIS', 'CD2', 'TYR', 8.78), ('CD2', 'HIS', 'CE1', 'TYR', 7.28), ('CD2', 'HIS', 'CE2', 'TYR', 7.79), ('CD2', 'HIS', 'CZ', 'TYR', 6.95), ('CD2', 'HIS', 'OH', 'TYR', 6.22)], [('CE1', 'HIS', 'CB', 'TYR', 9.15), ('CE1', 'HIS', 'CG', 'TYR', 7.83), ('CE1', 'HIS', 'CD1', 'TYR', 7.52), ('CE1', 'HIS', 'CD2', 'TYR', 7.23), ('CE1', 'HIS', 'CE1', 'TYR', 6.58), ('CE1', 'HIS', 'CE2', 'TYR', 6.2), ('CE1', 'HIS', 'CZ', 'TYR', 5.82), ('CE1', 'HIS', 'OH', 'TYR', 5.31)], [('NE2', 'HIS', 'CB', 'TYR', 9.14), ('NE2', 'HIS', 'CG', 'TYR', 7.78), ('NE2', 'HIS', 'CD1', 'TYR', 7.17), ('NE2', 'HIS', 'CD2', 'TYR', 7.45), ('NE2', 'HIS', 'CE1', 'TYR', 6.09), ('NE2', 'HIS', 'CE2', 'TYR', 6.42), ('NE2', 'HIS', 'CZ', 'TYR', 5.62), ('NE2', 'HIS', 'OH', 'TYR', 4.97)]]}
TYR_HISI = { 
	'distances':
		[[12.41, 11.0, 10.3, 10.33, 9.15, 9.14], [11.19, 9.74, 9.05, 9.03, 7.83, 7.78], [10.68, 9.23, 8.76, 8.33, 7.52, 7.17], [10.78, 9.32, 8.45, 8.78, 7.23, 7.45], [9.72, 8.25, 7.85, 7.28, 6.58, 6.09], [9.81, 8.34, 7.47, 7.79, 6.2, 6.42], [9.24, 7.74, 7.14, 6.95, 5.82, 5.62], [8.51, 7.05, 6.57, 6.22, 5.31, 4.97]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HISI', 12.41), ('CB', 'TYR', 'CG', 'HISI', 11.0), ('CB', 'TYR', 'ND1', 'HISI', 10.3), ('CB', 'TYR', 'CD2', 'HISI', 10.33), ('CB', 'TYR', 'CE1', 'HISI', 9.15), ('CB', 'TYR', 'NE2', 'HISI', 9.14)], [('CG', 'TYR', 'CB', 'HISI', 11.19), ('CG', 'TYR', 'CG', 'HISI', 9.74), ('CG', 'TYR', 'ND1', 'HISI', 9.05), ('CG', 'TYR', 'CD2', 'HISI', 9.03), ('CG', 'TYR', 'CE1', 'HISI', 7.83), ('CG', 'TYR', 'NE2', 'HISI', 7.78)], [('CD1', 'TYR', 'CB', 'HISI', 10.68), ('CD1', 'TYR', 'CG', 'HISI', 9.23), ('CD1', 'TYR', 'ND1', 'HISI', 8.76), ('CD1', 'TYR', 'CD2', 'HISI', 8.33), ('CD1', 'TYR', 'CE1', 'HISI', 7.52), ('CD1', 'TYR', 'NE2', 'HISI', 7.17)], [('CD2', 'TYR', 'CB', 'HISI', 10.78), ('CD2', 'TYR', 'CG', 'HISI', 9.32), ('CD2', 'TYR', 'ND1', 'HISI', 8.45), ('CD2', 'TYR', 'CD2', 'HISI', 8.78), ('CD2', 'TYR', 'CE1', 'HISI', 7.23), ('CD2', 'TYR', 'NE2', 'HISI', 7.45)], [('CE1', 'TYR', 'CB', 'HISI', 9.72), ('CE1', 'TYR', 'CG', 'HISI', 8.25), ('CE1', 'TYR', 'ND1', 'HISI', 7.85), ('CE1', 'TYR', 'CD2', 'HISI', 7.28), ('CE1', 'TYR', 'CE1', 'HISI', 6.58), ('CE1', 'TYR', 'NE2', 'HISI', 6.09)], [('CE2', 'TYR', 'CB', 'HISI', 9.81), ('CE2', 'TYR', 'CG', 'HISI', 8.34), ('CE2', 'TYR', 'ND1', 'HISI', 7.47), ('CE2', 'TYR', 'CD2', 'HISI', 7.79), ('CE2', 'TYR', 'CE1', 'HISI', 6.2), ('CE2', 'TYR', 'NE2', 'HISI', 6.42)], [('CZ', 'TYR', 'CB', 'HISI', 9.24), ('CZ', 'TYR', 'CG', 'HISI', 7.74), ('CZ', 'TYR', 'ND1', 'HISI', 7.14), ('CZ', 'TYR', 'CD2', 'HISI', 6.95), ('CZ', 'TYR', 'CE1', 'HISI', 5.82), ('CZ', 'TYR', 'NE2', 'HISI', 5.62)], [('OH', 'TYR', 'CB', 'HISI', 8.51), ('OH', 'TYR', 'CG', 'HISI', 7.05), ('OH', 'TYR', 'ND1', 'HISI', 6.57), ('OH', 'TYR', 'CD2', 'HISI', 6.22), ('OH', 'TYR', 'CE1', 'HISI', 5.31), ('OH', 'TYR', 'NE2', 'HISI', 4.97)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(FE2_HISI, d, 'M_1mpy_1_13_11_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'M_1mpy_1_13_11_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_FE2, d, 'M_1mpy_1_13_11_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_FE2, d, 'M_1mpy_1_13_11_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_TYR, d, 'M_1mpy_1_13_11_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_HISI, d, 'M_1mpy_1_13_11_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'FE2_HISI' :  match1,
		'HIS_HIS' :  match2,
		'TYR_FE2' :  match3,
		'HIS_FE2' :  match4,
		'HIS_TYR' :  match5,
		'TYR_HISI' :  match6}