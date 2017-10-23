'''
FUNC:A_2isd_3_1_4_11
PDB:2isd
EC:3.1.4.11
RESI:his,glu,his
LOCI:a-311,341,356;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[12.81, 12.09, 12.14, 11.59, 11.7, 11.34], [11.75, 10.9, 10.91, 10.33, 10.37, 9.98], [11.05, 10.16, 10.0, 9.72, 9.46, 9.26], [11.5, 10.56, 10.64, 9.81, 9.98, 9.42], [10.35, 9.32, 9.11, 8.76, 8.43, 8.17], [10.62, 9.56, 9.52, 8.79, 8.76, 8.26], [12.81, 11.75, 11.05, 11.5, 10.35, 10.62], [12.09, 10.9, 10.16, 10.56, 9.32, 9.56], [12.14, 10.91, 10.0, 10.64, 9.11, 9.52], [11.59, 10.33, 9.72, 9.81, 8.76, 8.79], [11.7, 10.37, 9.46, 9.98, 8.43, 8.76], [11.34, 9.98, 9.26, 9.42, 8.17, 8.26]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 12.81), ('CB', 'HIS', 'CG', 'HIS', 12.09), ('CB', 'HIS', 'ND1', 'HIS', 12.14), ('CB', 'HIS', 'CD2', 'HIS', 11.59), ('CB', 'HIS', 'CE1', 'HIS', 11.7), ('CB', 'HIS', 'NE2', 'HIS', 11.34)], [('CG', 'HIS', 'CB', 'HIS', 11.75), ('CG', 'HIS', 'CG', 'HIS', 10.9), ('CG', 'HIS', 'ND1', 'HIS', 10.91), ('CG', 'HIS', 'CD2', 'HIS', 10.33), ('CG', 'HIS', 'CE1', 'HIS', 10.37), ('CG', 'HIS', 'NE2', 'HIS', 9.98)], [('ND1', 'HIS', 'CB', 'HIS', 11.05), ('ND1', 'HIS', 'CG', 'HIS', 10.16), ('ND1', 'HIS', 'ND1', 'HIS', 10.0), ('ND1', 'HIS', 'CD2', 'HIS', 9.72), ('ND1', 'HIS', 'CE1', 'HIS', 9.46), ('ND1', 'HIS', 'NE2', 'HIS', 9.26)], [('CD2', 'HIS', 'CB', 'HIS', 11.5), ('CD2', 'HIS', 'CG', 'HIS', 10.56), ('CD2', 'HIS', 'ND1', 'HIS', 10.64), ('CD2', 'HIS', 'CD2', 'HIS', 9.81), ('CD2', 'HIS', 'CE1', 'HIS', 9.98), ('CD2', 'HIS', 'NE2', 'HIS', 9.42)], [('CE1', 'HIS', 'CB', 'HIS', 10.35), ('CE1', 'HIS', 'CG', 'HIS', 9.32), ('CE1', 'HIS', 'ND1', 'HIS', 9.11), ('CE1', 'HIS', 'CD2', 'HIS', 8.76), ('CE1', 'HIS', 'CE1', 'HIS', 8.43), ('CE1', 'HIS', 'NE2', 'HIS', 8.17)], [('NE2', 'HIS', 'CB', 'HIS', 10.62), ('NE2', 'HIS', 'CG', 'HIS', 9.56), ('NE2', 'HIS', 'ND1', 'HIS', 9.52), ('NE2', 'HIS', 'CD2', 'HIS', 8.79), ('NE2', 'HIS', 'CE1', 'HIS', 8.76), ('NE2', 'HIS', 'NE2', 'HIS', 8.26)], [('CB', 'HIS', 'CB', 'HIS', 12.81), ('CB', 'HIS', 'CG', 'HIS', 11.75), ('CB', 'HIS', 'ND1', 'HIS', 11.05), ('CB', 'HIS', 'CD2', 'HIS', 11.5), ('CB', 'HIS', 'CE1', 'HIS', 10.35), ('CB', 'HIS', 'NE2', 'HIS', 10.62)], [('CG', 'HIS', 'CB', 'HIS', 12.09), ('CG', 'HIS', 'CG', 'HIS', 10.9), ('CG', 'HIS', 'ND1', 'HIS', 10.16), ('CG', 'HIS', 'CD2', 'HIS', 10.56), ('CG', 'HIS', 'CE1', 'HIS', 9.32), ('CG', 'HIS', 'NE2', 'HIS', 9.56)], [('ND1', 'HIS', 'CB', 'HIS', 12.14), ('ND1', 'HIS', 'CG', 'HIS', 10.91), ('ND1', 'HIS', 'ND1', 'HIS', 10.0), ('ND1', 'HIS', 'CD2', 'HIS', 10.64), ('ND1', 'HIS', 'CE1', 'HIS', 9.11), ('ND1', 'HIS', 'NE2', 'HIS', 9.52)], [('CD2', 'HIS', 'CB', 'HIS', 11.59), ('CD2', 'HIS', 'CG', 'HIS', 10.33), ('CD2', 'HIS', 'ND1', 'HIS', 9.72), ('CD2', 'HIS', 'CD2', 'HIS', 9.81), ('CD2', 'HIS', 'CE1', 'HIS', 8.76), ('CD2', 'HIS', 'NE2', 'HIS', 8.79)], [('CE1', 'HIS', 'CB', 'HIS', 11.7), ('CE1', 'HIS', 'CG', 'HIS', 10.37), ('CE1', 'HIS', 'ND1', 'HIS', 9.46), ('CE1', 'HIS', 'CD2', 'HIS', 9.98), ('CE1', 'HIS', 'CE1', 'HIS', 8.43), ('CE1', 'HIS', 'NE2', 'HIS', 8.76)], [('NE2', 'HIS', 'CB', 'HIS', 11.34), ('NE2', 'HIS', 'CG', 'HIS', 9.98), ('NE2', 'HIS', 'ND1', 'HIS', 9.26), ('NE2', 'HIS', 'CD2', 'HIS', 9.42), ('NE2', 'HIS', 'CE1', 'HIS', 8.17), ('NE2', 'HIS', 'NE2', 'HIS', 8.26)]]}
HIS_GLU = { 
	'distances':
		[[8.21, 7.76, 6.51, 5.93, 6.47], [8.36, 8.0, 6.62, 5.76, 6.7], [9.3, 9.13, 7.81, 6.81, 8.01], [8.1, 7.64, 6.17, 5.29, 6.21], [9.59, 9.45, 8.1, 7.03, 8.34], [8.92, 8.64, 7.24, 6.22, 7.4], [12.17, 13.16, 12.78, 11.65, 13.79], [11.99, 12.81, 12.25, 11.08, 13.16], [12.83, 13.55, 12.84, 11.63, 13.66], [11.34, 12.05, 11.44, 10.31, 12.29], [12.74, 13.3, 12.46, 11.26, 13.18], [11.86, 12.39, 11.59, 10.44, 12.32]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.21), ('CB', 'HIS', 'CG', 'GLU', 7.76), ('CB', 'HIS', 'CD', 'GLU', 6.51), ('CB', 'HIS', 'OE1', 'GLU', 5.93), ('CB', 'HIS', 'OE2', 'GLU', 6.47)], [('CG', 'HIS', 'CB', 'GLU', 8.36), ('CG', 'HIS', 'CG', 'GLU', 8.0), ('CG', 'HIS', 'CD', 'GLU', 6.62), ('CG', 'HIS', 'OE1', 'GLU', 5.76), ('CG', 'HIS', 'OE2', 'GLU', 6.7)], [('ND1', 'HIS', 'CB', 'GLU', 9.3), ('ND1', 'HIS', 'CG', 'GLU', 9.13), ('ND1', 'HIS', 'CD', 'GLU', 7.81), ('ND1', 'HIS', 'OE1', 'GLU', 6.81), ('ND1', 'HIS', 'OE2', 'GLU', 8.01)], [('CD2', 'HIS', 'CB', 'GLU', 8.1), ('CD2', 'HIS', 'CG', 'GLU', 7.64), ('CD2', 'HIS', 'CD', 'GLU', 6.17), ('CD2', 'HIS', 'OE1', 'GLU', 5.29), ('CD2', 'HIS', 'OE2', 'GLU', 6.21)], [('CE1', 'HIS', 'CB', 'GLU', 9.59), ('CE1', 'HIS', 'CG', 'GLU', 9.45), ('CE1', 'HIS', 'CD', 'GLU', 8.1), ('CE1', 'HIS', 'OE1', 'GLU', 7.03), ('CE1', 'HIS', 'OE2', 'GLU', 8.34)], [('NE2', 'HIS', 'CB', 'GLU', 8.92), ('NE2', 'HIS', 'CG', 'GLU', 8.64), ('NE2', 'HIS', 'CD', 'GLU', 7.24), ('NE2', 'HIS', 'OE1', 'GLU', 6.22), ('NE2', 'HIS', 'OE2', 'GLU', 7.4)], [('CB', 'HIS', 'CB', 'GLU', 12.17), ('CB', 'HIS', 'CG', 'GLU', 13.16), ('CB', 'HIS', 'CD', 'GLU', 12.78), ('CB', 'HIS', 'OE1', 'GLU', 11.65), ('CB', 'HIS', 'OE2', 'GLU', 13.79)], [('CG', 'HIS', 'CB', 'GLU', 11.99), ('CG', 'HIS', 'CG', 'GLU', 12.81), ('CG', 'HIS', 'CD', 'GLU', 12.25), ('CG', 'HIS', 'OE1', 'GLU', 11.08), ('CG', 'HIS', 'OE2', 'GLU', 13.16)], [('ND1', 'HIS', 'CB', 'GLU', 12.83), ('ND1', 'HIS', 'CG', 'GLU', 13.55), ('ND1', 'HIS', 'CD', 'GLU', 12.84), ('ND1', 'HIS', 'OE1', 'GLU', 11.63), ('ND1', 'HIS', 'OE2', 'GLU', 13.66)], [('CD2', 'HIS', 'CB', 'GLU', 11.34), ('CD2', 'HIS', 'CG', 'GLU', 12.05), ('CD2', 'HIS', 'CD', 'GLU', 11.44), ('CD2', 'HIS', 'OE1', 'GLU', 10.31), ('CD2', 'HIS', 'OE2', 'GLU', 12.29)], [('CE1', 'HIS', 'CB', 'GLU', 12.74), ('CE1', 'HIS', 'CG', 'GLU', 13.3), ('CE1', 'HIS', 'CD', 'GLU', 12.46), ('CE1', 'HIS', 'OE1', 'GLU', 11.26), ('CE1', 'HIS', 'OE2', 'GLU', 13.18)], [('NE2', 'HIS', 'CB', 'GLU', 11.86), ('NE2', 'HIS', 'CG', 'GLU', 12.39), ('NE2', 'HIS', 'CD', 'GLU', 11.59), ('NE2', 'HIS', 'OE1', 'GLU', 10.44), ('NE2', 'HIS', 'OE2', 'GLU', 12.32)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'A_2isd_3_1_4_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLU, d, 'A_2isd_3_1_4_11')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'HIS_GLU' :  match2}