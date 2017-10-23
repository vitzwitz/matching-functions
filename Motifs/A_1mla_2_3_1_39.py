'''
FUNC:A_1mla_2_3_1_39
PDB:1mla
EC:2.3.1.39
RESI:ser,his,gln
LOCI:a-92,201,250;
'''
import motifFunctions as cmd
SER_GLN = { 
	'distances':
		[[9.12, 7.73, 6.93, 6.57, 7.09, 8.91, 9.46, 9.88, 11.28], [8.69, 7.46, 6.65, 6.62, 6.48, 8.22, 8.74, 9.37, 10.72]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLN', 9.12), ('CB', 'SER', 'CG', 'GLN', 7.73), ('CB', 'SER', 'CD', 'GLN', 6.93), ('CB', 'SER', 'OE1', 'GLN', 6.57), ('CB', 'SER', 'NE2', 'GLN', 7.09), ('CB', 'SER', 'O', 'GLN', 8.91), ('CB', 'SER', 'C', 'GLN', 9.46), ('CB', 'SER', 'CA', 'GLN', 9.88), ('CB', 'SER', 'N', 'GLN', 11.28)], [('OG', 'SER', 'CB', 'GLN', 8.69), ('OG', 'SER', 'CG', 'GLN', 7.46), ('OG', 'SER', 'CD', 'GLN', 6.65), ('OG', 'SER', 'OE1', 'GLN', 6.62), ('OG', 'SER', 'NE2', 'GLN', 6.48), ('OG', 'SER', 'O', 'GLN', 8.22), ('OG', 'SER', 'C', 'GLN', 8.74), ('OG', 'SER', 'CA', 'GLN', 9.37), ('OG', 'SER', 'N', 'GLN', 10.72)]]}
HIS_GLN = { 
	'distances':
		[[9.52, 8.88, 9.55, 10.26, 9.66, 6.51, 7.7, 8.84, 9.93], [8.59, 7.79, 8.27, 8.92, 8.34, 5.91, 7.07, 8.18, 9.42], [7.27, 6.52, 7.06, 7.82, 7.14, 4.73, 5.84, 6.92, 8.2], [9.19, 8.22, 8.39, 8.88, 8.39, 6.9, 7.96, 9.03, 10.34], [7.13, 6.18, 6.32, 6.97, 6.3, 5.31, 6.18, 7.16, 8.5], [8.37, 7.32, 7.28, 7.74, 7.21, 6.57, 7.47, 8.46, 9.81]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 9.52), ('CB', 'HIS', 'CG', 'GLN', 8.88), ('CB', 'HIS', 'CD', 'GLN', 9.55), ('CB', 'HIS', 'OE1', 'GLN', 10.26), ('CB', 'HIS', 'NE2', 'GLN', 9.66), ('CB', 'HIS', 'O', 'GLN', 6.51), ('CB', 'HIS', 'C', 'GLN', 7.7), ('CB', 'HIS', 'CA', 'GLN', 8.84), ('CB', 'HIS', 'N', 'GLN', 9.93)], [('CG', 'HIS', 'CB', 'GLN', 8.59), ('CG', 'HIS', 'CG', 'GLN', 7.79), ('CG', 'HIS', 'CD', 'GLN', 8.27), ('CG', 'HIS', 'OE1', 'GLN', 8.92), ('CG', 'HIS', 'NE2', 'GLN', 8.34), ('CG', 'HIS', 'O', 'GLN', 5.91), ('CG', 'HIS', 'C', 'GLN', 7.07), ('CG', 'HIS', 'CA', 'GLN', 8.18), ('CG', 'HIS', 'N', 'GLN', 9.42)], [('ND1', 'HIS', 'CB', 'GLN', 7.27), ('ND1', 'HIS', 'CG', 'GLN', 6.52), ('ND1', 'HIS', 'CD', 'GLN', 7.06), ('ND1', 'HIS', 'OE1', 'GLN', 7.82), ('ND1', 'HIS', 'NE2', 'GLN', 7.14), ('ND1', 'HIS', 'O', 'GLN', 4.73), ('ND1', 'HIS', 'C', 'GLN', 5.84), ('ND1', 'HIS', 'CA', 'GLN', 6.92), ('ND1', 'HIS', 'N', 'GLN', 8.2)], [('CD2', 'HIS', 'CB', 'GLN', 9.19), ('CD2', 'HIS', 'CG', 'GLN', 8.22), ('CD2', 'HIS', 'CD', 'GLN', 8.39), ('CD2', 'HIS', 'OE1', 'GLN', 8.88), ('CD2', 'HIS', 'NE2', 'GLN', 8.39), ('CD2', 'HIS', 'O', 'GLN', 6.9), ('CD2', 'HIS', 'C', 'GLN', 7.96), ('CD2', 'HIS', 'CA', 'GLN', 9.03), ('CD2', 'HIS', 'N', 'GLN', 10.34)], [('CE1', 'HIS', 'CB', 'GLN', 7.13), ('CE1', 'HIS', 'CG', 'GLN', 6.18), ('CE1', 'HIS', 'CD', 'GLN', 6.32), ('CE1', 'HIS', 'OE1', 'GLN', 6.97), ('CE1', 'HIS', 'NE2', 'GLN', 6.3), ('CE1', 'HIS', 'O', 'GLN', 5.31), ('CE1', 'HIS', 'C', 'GLN', 6.18), ('CE1', 'HIS', 'CA', 'GLN', 7.16), ('CE1', 'HIS', 'N', 'GLN', 8.5)], [('NE2', 'HIS', 'CB', 'GLN', 8.37), ('NE2', 'HIS', 'CG', 'GLN', 7.32), ('NE2', 'HIS', 'CD', 'GLN', 7.28), ('NE2', 'HIS', 'OE1', 'GLN', 7.74), ('NE2', 'HIS', 'NE2', 'GLN', 7.21), ('NE2', 'HIS', 'O', 'GLN', 6.57), ('NE2', 'HIS', 'C', 'GLN', 7.47), ('NE2', 'HIS', 'CA', 'GLN', 8.46), ('NE2', 'HIS', 'N', 'GLN', 9.81)]]}
SER_HIS = { 
	'distances':
		[[9.0, 7.56, 7.26, 6.65, 6.08, 5.62], [8.42, 6.93, 6.57, 6.02, 5.29, 4.83]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.0), ('CB', 'SER', 'CG', 'HIS', 7.56), ('CB', 'SER', 'ND1', 'HIS', 7.26), ('CB', 'SER', 'CD2', 'HIS', 6.65), ('CB', 'SER', 'CE1', 'HIS', 6.08), ('CB', 'SER', 'NE2', 'HIS', 5.62)], [('OG', 'SER', 'CB', 'HIS', 8.42), ('OG', 'SER', 'CG', 'HIS', 6.93), ('OG', 'SER', 'ND1', 'HIS', 6.57), ('OG', 'SER', 'CD2', 'HIS', 6.02), ('OG', 'SER', 'CE1', 'HIS', 5.29), ('OG', 'SER', 'NE2', 'HIS', 4.83)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_GLN, d, 'A_1mla_2_3_1_39')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLN, d, 'A_1mla_2_3_1_39')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'A_1mla_2_3_1_39')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_GLN' :  match1,
		'HIS_GLN' :  match2,
		'SER_HIS' :  match3}