'''
FUNC:P_1daa_2_6_1_21
PDB:1daa
EC:2.6.1.21
RESI:lys,glu,leu
LOCI:a-145,177,201;
'''
import motifFunctions as cmd
LYS_LEU = { 
	'distances':
		[[7.8, 6.83, 5.91, 6.43], [7.86, 6.89, 6.44, 6.03], [7.9, 6.67, 6.41, 5.71], [8.83, 7.66, 7.69, 6.44], [8.4, 7.42, 7.82, 6.0]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LEU', 7.8), ('CB', 'LYS', 'CG', 'LEU', 6.83), ('CB', 'LYS', 'CD1', 'LEU', 5.91), ('CB', 'LYS', 'CD2', 'LEU', 6.43)], [('CG', 'LYS', 'CB', 'LEU', 7.86), ('CG', 'LYS', 'CG', 'LEU', 6.89), ('CG', 'LYS', 'CD1', 'LEU', 6.44), ('CG', 'LYS', 'CD2', 'LEU', 6.03)], [('CD', 'LYS', 'CB', 'LEU', 7.9), ('CD', 'LYS', 'CG', 'LEU', 6.67), ('CD', 'LYS', 'CD1', 'LEU', 6.41), ('CD', 'LYS', 'CD2', 'LEU', 5.71)], [('CE', 'LYS', 'CB', 'LEU', 8.83), ('CE', 'LYS', 'CG', 'LEU', 7.66), ('CE', 'LYS', 'CD1', 'LEU', 7.69), ('CE', 'LYS', 'CD2', 'LEU', 6.44)], [('NZ', 'LYS', 'CB', 'LEU', 8.4), ('NZ', 'LYS', 'CG', 'LEU', 7.42), ('NZ', 'LYS', 'CD1', 'LEU', 7.82), ('NZ', 'LYS', 'CD2', 'LEU', 6.0)]]}
LYS_GLU = { 
	'distances':
		[[13.76, 12.92, 11.5, 10.92, 11.1], [13.41, 12.61, 11.27, 10.66, 10.99], [13.5, 12.88, 11.57, 10.8, 11.47], [13.9, 13.34, 12.15, 11.36, 12.16], [12.87, 12.35, 11.26, 10.48, 11.37]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 13.76), ('CB', 'LYS', 'CG', 'GLU', 12.92), ('CB', 'LYS', 'CD', 'GLU', 11.5), ('CB', 'LYS', 'OE1', 'GLU', 10.92), ('CB', 'LYS', 'OE2', 'GLU', 11.1)], [('CG', 'LYS', 'CB', 'GLU', 13.41), ('CG', 'LYS', 'CG', 'GLU', 12.61), ('CG', 'LYS', 'CD', 'GLU', 11.27), ('CG', 'LYS', 'OE1', 'GLU', 10.66), ('CG', 'LYS', 'OE2', 'GLU', 10.99)], [('CD', 'LYS', 'CB', 'GLU', 13.5), ('CD', 'LYS', 'CG', 'GLU', 12.88), ('CD', 'LYS', 'CD', 'GLU', 11.57), ('CD', 'LYS', 'OE1', 'GLU', 10.8), ('CD', 'LYS', 'OE2', 'GLU', 11.47)], [('CE', 'LYS', 'CB', 'GLU', 13.9), ('CE', 'LYS', 'CG', 'GLU', 13.34), ('CE', 'LYS', 'CD', 'GLU', 12.15), ('CE', 'LYS', 'OE1', 'GLU', 11.36), ('CE', 'LYS', 'OE2', 'GLU', 12.16)], [('NZ', 'LYS', 'CB', 'GLU', 12.87), ('NZ', 'LYS', 'CG', 'GLU', 12.35), ('NZ', 'LYS', 'CD', 'GLU', 11.26), ('NZ', 'LYS', 'OE1', 'GLU', 10.48), ('NZ', 'LYS', 'OE2', 'GLU', 11.37)]]}
GLU_LEU = { 
	'distances':
		[[8.4, 9.72, 10.92, 9.97], [7.89, 9.3, 10.37, 9.5], [6.44, 7.89, 8.88, 8.18], [5.58, 6.96, 8.1, 7.26], [6.44, 7.93, 8.69, 8.29]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LEU', 8.4), ('CB', 'GLU', 'CG', 'LEU', 9.72), ('CB', 'GLU', 'CD1', 'LEU', 10.92), ('CB', 'GLU', 'CD2', 'LEU', 9.97)], [('CG', 'GLU', 'CB', 'LEU', 7.89), ('CG', 'GLU', 'CG', 'LEU', 9.3), ('CG', 'GLU', 'CD1', 'LEU', 10.37), ('CG', 'GLU', 'CD2', 'LEU', 9.5)], [('CD', 'GLU', 'CB', 'LEU', 6.44), ('CD', 'GLU', 'CG', 'LEU', 7.89), ('CD', 'GLU', 'CD1', 'LEU', 8.88), ('CD', 'GLU', 'CD2', 'LEU', 8.18)], [('OE1', 'GLU', 'CB', 'LEU', 5.58), ('OE1', 'GLU', 'CG', 'LEU', 6.96), ('OE1', 'GLU', 'CD1', 'LEU', 8.1), ('OE1', 'GLU', 'CD2', 'LEU', 7.26)], [('OE2', 'GLU', 'CB', 'LEU', 6.44), ('OE2', 'GLU', 'CG', 'LEU', 7.93), ('OE2', 'GLU', 'CD1', 'LEU', 8.69), ('OE2', 'GLU', 'CD2', 'LEU', 8.29)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_LEU, d, 'P_1daa_2_6_1_21')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_GLU, d, 'P_1daa_2_6_1_21')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_LEU, d, 'P_1daa_2_6_1_21')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_LEU' :  match1,
		'LYS_GLU' :  match2,
		'GLU_LEU' :  match3}