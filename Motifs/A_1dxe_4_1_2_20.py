'''
FUNC:A_1dxe_4_1_2_20
PDB:1dxe
EC:4.1.2.20
RESI:his,arg
LOCI:a-50,75;
'''
import motifFunctions as cmd
ARG_HIS = { 
	'distances':
		[[10.04, 10.27, 11.5, 9.66, 11.69, 10.65], [9.81, 9.78, 10.96, 8.96, 10.96, 9.82], [8.67, 8.5, 9.61, 7.65, 9.55, 8.43], [7.36, 7.31, 8.52, 6.56, 8.62, 7.54], [7.12, 6.95, 8.17, 6.07, 8.2, 7.05], [8.16, 7.76, 8.87, 6.69, 8.68, 7.42], [6.15, 6.15, 7.45, 5.48, 7.66, 6.64]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 10.04), ('CB', 'ARG', 'CG', 'HIS', 10.27), ('CB', 'ARG', 'ND1', 'HIS', 11.5), ('CB', 'ARG', 'CD2', 'HIS', 9.66), ('CB', 'ARG', 'CE1', 'HIS', 11.69), ('CB', 'ARG', 'NE2', 'HIS', 10.65)], [('CG', 'ARG', 'CB', 'HIS', 9.81), ('CG', 'ARG', 'CG', 'HIS', 9.78), ('CG', 'ARG', 'ND1', 'HIS', 10.96), ('CG', 'ARG', 'CD2', 'HIS', 8.96), ('CG', 'ARG', 'CE1', 'HIS', 10.96), ('CG', 'ARG', 'NE2', 'HIS', 9.82)], [('CD', 'ARG', 'CB', 'HIS', 8.67), ('CD', 'ARG', 'CG', 'HIS', 8.5), ('CD', 'ARG', 'ND1', 'HIS', 9.61), ('CD', 'ARG', 'CD2', 'HIS', 7.65), ('CD', 'ARG', 'CE1', 'HIS', 9.55), ('CD', 'ARG', 'NE2', 'HIS', 8.43)], [('NE', 'ARG', 'CB', 'HIS', 7.36), ('NE', 'ARG', 'CG', 'HIS', 7.31), ('NE', 'ARG', 'ND1', 'HIS', 8.52), ('NE', 'ARG', 'CD2', 'HIS', 6.56), ('NE', 'ARG', 'CE1', 'HIS', 8.62), ('NE', 'ARG', 'NE2', 'HIS', 7.54)], [('CZ', 'ARG', 'CB', 'HIS', 7.12), ('CZ', 'ARG', 'CG', 'HIS', 6.95), ('CZ', 'ARG', 'ND1', 'HIS', 8.17), ('CZ', 'ARG', 'CD2', 'HIS', 6.07), ('CZ', 'ARG', 'CE1', 'HIS', 8.2), ('CZ', 'ARG', 'NE2', 'HIS', 7.05)], [('NH1', 'ARG', 'CB', 'HIS', 8.16), ('NH1', 'ARG', 'CG', 'HIS', 7.76), ('NH1', 'ARG', 'ND1', 'HIS', 8.87), ('NH1', 'ARG', 'CD2', 'HIS', 6.69), ('NH1', 'ARG', 'CE1', 'HIS', 8.68), ('NH1', 'ARG', 'NE2', 'HIS', 7.42)], [('NH2', 'ARG', 'CB', 'HIS', 6.15), ('NH2', 'ARG', 'CG', 'HIS', 6.15), ('NH2', 'ARG', 'ND1', 'HIS', 7.45), ('NH2', 'ARG', 'CD2', 'HIS', 5.48), ('NH2', 'ARG', 'CE1', 'HIS', 7.66), ('NH2', 'ARG', 'NE2', 'HIS', 6.64)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_HIS, d, 'A_1dxe_4_1_2_20')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_HIS' :  match1}