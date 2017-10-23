'''
FUNC:A_1daa_2_6_1_21
PDB:1daa
EC:2.6.1.21
RESI:lys,glu,leu
LOCI:a-145,177,201;
'''
import motifFunctions as cmd
LYS_GLU = { 
	'distances':
		[[14.12, 13.3, 11.82, 11.27, 11.31], [13.7, 12.92, 11.52, 10.93, 11.11], [13.95, 13.36, 11.98, 11.24, 11.74], [14.12, 13.61, 12.33, 11.57, 12.2], [12.92, 12.42, 11.22, 10.48, 11.15]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 14.12), ('CB', 'LYS', 'CG', 'GLU', 13.3), ('CB', 'LYS', 'CD', 'GLU', 11.82), ('CB', 'LYS', 'OE1', 'GLU', 11.27), ('CB', 'LYS', 'OE2', 'GLU', 11.31)], [('CG', 'LYS', 'CB', 'GLU', 13.7), ('CG', 'LYS', 'CG', 'GLU', 12.92), ('CG', 'LYS', 'CD', 'GLU', 11.52), ('CG', 'LYS', 'OE1', 'GLU', 10.93), ('CG', 'LYS', 'OE2', 'GLU', 11.11)], [('CD', 'LYS', 'CB', 'GLU', 13.95), ('CD', 'LYS', 'CG', 'GLU', 13.36), ('CD', 'LYS', 'CD', 'GLU', 11.98), ('CD', 'LYS', 'OE1', 'GLU', 11.24), ('CD', 'LYS', 'OE2', 'GLU', 11.74)], [('CE', 'LYS', 'CB', 'GLU', 14.12), ('CE', 'LYS', 'CG', 'GLU', 13.61), ('CE', 'LYS', 'CD', 'GLU', 12.33), ('CE', 'LYS', 'OE1', 'GLU', 11.57), ('CE', 'LYS', 'OE2', 'GLU', 12.2)], [('NZ', 'LYS', 'CB', 'GLU', 12.92), ('NZ', 'LYS', 'CG', 'GLU', 12.42), ('NZ', 'LYS', 'CD', 'GLU', 11.22), ('NZ', 'LYS', 'OE1', 'GLU', 10.48), ('NZ', 'LYS', 'OE2', 'GLU', 11.15)]]}
LEU_LYS = { 
	'distances':
		[[7.87, 7.89, 8.14, 8.91, 8.26], [6.88, 6.95, 6.97, 7.84, 7.42], [5.94, 6.44, 6.71, 7.89, 7.76], [6.51, 6.13, 5.96, 6.57, 6.0]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'LYS', 7.87), ('CB', 'LEU', 'CG', 'LYS', 7.89), ('CB', 'LEU', 'CD', 'LYS', 8.14), ('CB', 'LEU', 'CE', 'LYS', 8.91), ('CB', 'LEU', 'NZ', 'LYS', 8.26)], [('CG', 'LEU', 'CB', 'LYS', 6.88), ('CG', 'LEU', 'CG', 'LYS', 6.95), ('CG', 'LEU', 'CD', 'LYS', 6.97), ('CG', 'LEU', 'CE', 'LYS', 7.84), ('CG', 'LEU', 'NZ', 'LYS', 7.42)], [('CD1', 'LEU', 'CB', 'LYS', 5.94), ('CD1', 'LEU', 'CG', 'LYS', 6.44), ('CD1', 'LEU', 'CD', 'LYS', 6.71), ('CD1', 'LEU', 'CE', 'LYS', 7.89), ('CD1', 'LEU', 'NZ', 'LYS', 7.76)], [('CD2', 'LEU', 'CB', 'LYS', 6.51), ('CD2', 'LEU', 'CG', 'LYS', 6.13), ('CD2', 'LEU', 'CD', 'LYS', 5.96), ('CD2', 'LEU', 'CE', 'LYS', 6.57), ('CD2', 'LEU', 'NZ', 'LYS', 6.0)]]}
LEU_GLU = { 
	'distances':
		[[8.72, 8.17, 6.69, 5.89, 6.57], [10.06, 9.6, 8.14, 7.26, 8.04], [11.19, 10.57, 9.06, 8.34, 8.73], [10.3, 9.87, 8.47, 7.56, 8.45]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'GLU', 8.72), ('CB', 'LEU', 'CG', 'GLU', 8.17), ('CB', 'LEU', 'CD', 'GLU', 6.69), ('CB', 'LEU', 'OE1', 'GLU', 5.89), ('CB', 'LEU', 'OE2', 'GLU', 6.57)], [('CG', 'LEU', 'CB', 'GLU', 10.06), ('CG', 'LEU', 'CG', 'GLU', 9.6), ('CG', 'LEU', 'CD', 'GLU', 8.14), ('CG', 'LEU', 'OE1', 'GLU', 7.26), ('CG', 'LEU', 'OE2', 'GLU', 8.04)], [('CD1', 'LEU', 'CB', 'GLU', 11.19), ('CD1', 'LEU', 'CG', 'GLU', 10.57), ('CD1', 'LEU', 'CD', 'GLU', 9.06), ('CD1', 'LEU', 'OE1', 'GLU', 8.34), ('CD1', 'LEU', 'OE2', 'GLU', 8.73)], [('CD2', 'LEU', 'CB', 'GLU', 10.3), ('CD2', 'LEU', 'CG', 'GLU', 9.87), ('CD2', 'LEU', 'CD', 'GLU', 8.47), ('CD2', 'LEU', 'OE1', 'GLU', 7.56), ('CD2', 'LEU', 'OE2', 'GLU', 8.45)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_GLU, d, 'A_1daa_2_6_1_21')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LEU_LYS, d, 'A_1daa_2_6_1_21')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LEU_GLU, d, 'A_1daa_2_6_1_21')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_GLU' :  match1,
		'LEU_LYS' :  match2,
		'LEU_GLU' :  match3}