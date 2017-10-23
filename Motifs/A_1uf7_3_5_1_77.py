'''
FUNC:A_1uf7_3_5_1_77
PDB:1uf7
EC:3.5.1.77
RESI:glu,lys,ala
LOCI:a-46,126,171;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[9.88, 9.6, 8.65, 8.67, 8.1], [9.08, 8.83, 7.73, 7.85, 7.14], [8.95, 8.41, 7.13, 6.92, 5.98], [10.05, 9.37, 8.07, 7.61, 6.52], [7.96, 7.33, 5.98, 5.77, 4.8]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 9.88), ('CB', 'GLU', 'CG', 'LYS', 9.6), ('CB', 'GLU', 'CD', 'LYS', 8.65), ('CB', 'GLU', 'CE', 'LYS', 8.67), ('CB', 'GLU', 'NZ', 'LYS', 8.1)], [('CG', 'GLU', 'CB', 'LYS', 9.08), ('CG', 'GLU', 'CG', 'LYS', 8.83), ('CG', 'GLU', 'CD', 'LYS', 7.73), ('CG', 'GLU', 'CE', 'LYS', 7.85), ('CG', 'GLU', 'NZ', 'LYS', 7.14)], [('CD', 'GLU', 'CB', 'LYS', 8.95), ('CD', 'GLU', 'CG', 'LYS', 8.41), ('CD', 'GLU', 'CD', 'LYS', 7.13), ('CD', 'GLU', 'CE', 'LYS', 6.92), ('CD', 'GLU', 'NZ', 'LYS', 5.98)], [('OE1', 'GLU', 'CB', 'LYS', 10.05), ('OE1', 'GLU', 'CG', 'LYS', 9.37), ('OE1', 'GLU', 'CD', 'LYS', 8.07), ('OE1', 'GLU', 'CE', 'LYS', 7.61), ('OE1', 'GLU', 'NZ', 'LYS', 6.52)], [('OE2', 'GLU', 'CB', 'LYS', 7.96), ('OE2', 'GLU', 'CG', 'LYS', 7.33), ('OE2', 'GLU', 'CD', 'LYS', 5.98), ('OE2', 'GLU', 'CE', 'LYS', 5.77), ('OE2', 'GLU', 'NZ', 'LYS', 4.8)]]}
GLU_ALA = { 
	'distances':
		[[6.66], [6.64], [5.59], [5.5], [5.43]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ALA', 6.66)], [('CG', 'GLU', 'CB', 'ALA', 6.64)], [('CD', 'GLU', 'CB', 'ALA', 5.59)], [('OE1', 'GLU', 'CB', 'ALA', 5.5)], [('OE2', 'GLU', 'CB', 'ALA', 5.43)]]}
ALA_LYS = { 
	'distances':
		[9.07, 7.95, 7.07, 6.07, 5.65],
	'comparisons':
		[('CB', 'ALA', 'CB', 'LYS', 9.07), ('CB', 'ALA', 'CG', 'LYS', 7.95), ('CB', 'ALA', 'CD', 'LYS', 7.07), ('CB', 'ALA', 'CE', 'LYS', 6.07), ('CB', 'ALA', 'NZ', 'LYS', 5.65)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_1uf7_3_5_1_77')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ALA, d, 'A_1uf7_3_5_1_77')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_LYS, d, 'A_1uf7_3_5_1_77')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'GLU_ALA' :  match2,
		'ALA_LYS' :  match3}