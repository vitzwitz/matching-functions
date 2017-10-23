'''
FUNC:A_2bx4_2_7_7_48
PDB:2bx4
EC:2.7.7.48
RESI:his,cys
LOCI:a-41,145;
'''
import motifFunctions as cmd
CYS_HIS = { 
	'distances':
		[[9.34, 7.86, 7.11, 7.22, 5.84, 5.88], [9.17, 7.68, 7.03, 6.95, 5.73, 5.63], [11.42, 10.07, 9.33, 9.51, 8.25, 8.35], [11.05, 9.67, 8.78, 9.23, 7.69, 7.98], [10.69, 9.23, 8.35, 8.69, 7.13, 7.35], [11.82, 10.33, 9.55, 9.63, 8.27, 8.29]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 9.34), ('CB', 'CYS', 'CG', 'HIS', 7.86), ('CB', 'CYS', 'ND1', 'HIS', 7.11), ('CB', 'CYS', 'CD2', 'HIS', 7.22), ('CB', 'CYS', 'CE1', 'HIS', 5.84), ('CB', 'CYS', 'NE2', 'HIS', 5.88)], [('SG', 'CYS', 'CB', 'HIS', 9.17), ('SG', 'CYS', 'CG', 'HIS', 7.68), ('SG', 'CYS', 'ND1', 'HIS', 7.03), ('SG', 'CYS', 'CD2', 'HIS', 6.95), ('SG', 'CYS', 'CE1', 'HIS', 5.73), ('SG', 'CYS', 'NE2', 'HIS', 5.63)], [('O', 'CYS', 'CB', 'HIS', 11.42), ('O', 'CYS', 'CG', 'HIS', 10.07), ('O', 'CYS', 'ND1', 'HIS', 9.33), ('O', 'CYS', 'CD2', 'HIS', 9.51), ('O', 'CYS', 'CE1', 'HIS', 8.25), ('O', 'CYS', 'NE2', 'HIS', 8.35)], [('C', 'CYS', 'CB', 'HIS', 11.05), ('C', 'CYS', 'CG', 'HIS', 9.67), ('C', 'CYS', 'ND1', 'HIS', 8.78), ('C', 'CYS', 'CD2', 'HIS', 9.23), ('C', 'CYS', 'CE1', 'HIS', 7.69), ('C', 'CYS', 'NE2', 'HIS', 7.98)], [('CA', 'CYS', 'CB', 'HIS', 10.69), ('CA', 'CYS', 'CG', 'HIS', 9.23), ('CA', 'CYS', 'ND1', 'HIS', 8.35), ('CA', 'CYS', 'CD2', 'HIS', 8.69), ('CA', 'CYS', 'CE1', 'HIS', 7.13), ('CA', 'CYS', 'NE2', 'HIS', 7.35)], [('N', 'CYS', 'CB', 'HIS', 11.82), ('N', 'CYS', 'CG', 'HIS', 10.33), ('N', 'CYS', 'ND1', 'HIS', 9.55), ('N', 'CYS', 'CD2', 'HIS', 9.63), ('N', 'CYS', 'CE1', 'HIS', 8.27), ('N', 'CYS', 'NE2', 'HIS', 8.29)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_HIS, d, 'A_2bx4_2_7_7_48')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_HIS' :  match1}