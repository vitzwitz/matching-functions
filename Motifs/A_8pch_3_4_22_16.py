'''
FUNC:A_8pch_3_4_22_16
PDB:8pch
EC:3.4.22.16
RESI:gln,cys,his
LOCI:a-19,25,159;
'''
import motifFunctions as cmd
CYS_GLN = { 
	'distances':
		[[7.59, 7.35, 5.97, 5.33, 5.91], [8.62, 8.2, 6.8, 6.54, 6.22]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 7.59), ('CB', 'CYS', 'CG', 'GLN', 7.35), ('CB', 'CYS', 'CD', 'GLN', 5.97), ('CB', 'CYS', 'OE1', 'GLN', 5.33), ('CB', 'CYS', 'NE2', 'GLN', 5.91)], [('SG', 'CYS', 'CB', 'GLN', 8.62), ('SG', 'CYS', 'CG', 'GLN', 8.2), ('SG', 'CYS', 'CD', 'GLN', 6.8), ('SG', 'CYS', 'OE1', 'GLN', 6.54), ('SG', 'CYS', 'NE2', 'GLN', 6.22)]]}
CYS_HIS = { 
	'distances':
		[[7.47, 7.82, 8.98, 7.54, 9.39, 8.62], [6.55, 6.71, 7.68, 6.57, 8.09, 7.5]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.47), ('CB', 'CYS', 'CG', 'HIS', 7.82), ('CB', 'CYS', 'ND1', 'HIS', 8.98), ('CB', 'CYS', 'CD2', 'HIS', 7.54), ('CB', 'CYS', 'CE1', 'HIS', 9.39), ('CB', 'CYS', 'NE2', 'HIS', 8.62)], [('SG', 'CYS', 'CB', 'HIS', 6.55), ('SG', 'CYS', 'CG', 'HIS', 6.71), ('SG', 'CYS', 'ND1', 'HIS', 7.68), ('SG', 'CYS', 'CD2', 'HIS', 6.57), ('SG', 'CYS', 'CE1', 'HIS', 8.09), ('SG', 'CYS', 'NE2', 'HIS', 7.5)]]}
HIS_GLN = { 
	'distances':
		[[12.32, 11.46, 9.99, 9.6, 9.34], [12.09, 11.09, 9.68, 9.5, 8.86], [13.1, 12.06, 10.7, 10.65, 9.76], [11.17, 10.06, 8.72, 8.66, 7.86], [12.91, 11.77, 10.52, 10.63, 9.49], [11.76, 10.57, 9.35, 9.49, 8.35]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 12.32), ('CB', 'HIS', 'CG', 'GLN', 11.46), ('CB', 'HIS', 'CD', 'GLN', 9.99), ('CB', 'HIS', 'OE1', 'GLN', 9.6), ('CB', 'HIS', 'NE2', 'GLN', 9.34)], [('CG', 'HIS', 'CB', 'GLN', 12.09), ('CG', 'HIS', 'CG', 'GLN', 11.09), ('CG', 'HIS', 'CD', 'GLN', 9.68), ('CG', 'HIS', 'OE1', 'GLN', 9.5), ('CG', 'HIS', 'NE2', 'GLN', 8.86)], [('ND1', 'HIS', 'CB', 'GLN', 13.1), ('ND1', 'HIS', 'CG', 'GLN', 12.06), ('ND1', 'HIS', 'CD', 'GLN', 10.7), ('ND1', 'HIS', 'OE1', 'GLN', 10.65), ('ND1', 'HIS', 'NE2', 'GLN', 9.76)], [('CD2', 'HIS', 'CB', 'GLN', 11.17), ('CD2', 'HIS', 'CG', 'GLN', 10.06), ('CD2', 'HIS', 'CD', 'GLN', 8.72), ('CD2', 'HIS', 'OE1', 'GLN', 8.66), ('CD2', 'HIS', 'NE2', 'GLN', 7.86)], [('CE1', 'HIS', 'CB', 'GLN', 12.91), ('CE1', 'HIS', 'CG', 'GLN', 11.77), ('CE1', 'HIS', 'CD', 'GLN', 10.52), ('CE1', 'HIS', 'OE1', 'GLN', 10.63), ('CE1', 'HIS', 'NE2', 'GLN', 9.49)], [('NE2', 'HIS', 'CB', 'GLN', 11.76), ('NE2', 'HIS', 'CG', 'GLN', 10.57), ('NE2', 'HIS', 'CD', 'GLN', 9.35), ('NE2', 'HIS', 'OE1', 'GLN', 9.49), ('NE2', 'HIS', 'NE2', 'GLN', 8.35)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLN, d, 'A_8pch_3_4_22_16')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_HIS, d, 'A_8pch_3_4_22_16')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLN, d, 'A_8pch_3_4_22_16')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLN' :  match1,
		'CYS_HIS' :  match2,
		'HIS_GLN' :  match3}