'''
FUNC:A_1hfs_3_4_24_17
PDB:1hfs
EC:3.4.24.17
RESI:glu,met
LOCI:a-202,219;
'''
import motifFunctions as cmd
MET_GLU = { 
	'distances':
		[[11.67, 11.95, 11.4, 11.76, 10.83, 10.58, 10.42, 10.23, 9.44], [10.97, 11.44, 11.07, 11.42, 10.65, 9.63, 9.47, 9.48, 8.71], [9.16, 9.66, 9.35, 9.74, 9.0, 7.98, 7.73, 7.68, 6.91], [8.9, 9.38, 8.82, 8.97, 8.54, 7.42, 7.45, 7.41, 6.99], [12.37, 12.3, 11.45, 11.77, 10.65, 11.77, 11.63, 11.1, 10.36], [12.15, 12.07, 11.36, 11.81, 10.52, 11.72, 11.45, 10.88, 9.99], [11.39, 11.49, 10.95, 11.44, 10.23, 10.8, 10.48, 10.06, 9.11], [11.84, 11.95, 11.59, 12.21, 10.87, 11.39, 10.94, 10.54, 9.43]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'GLU', 11.67), ('CB', 'MET', 'CG', 'GLU', 11.95), ('CB', 'MET', 'CD', 'GLU', 11.4), ('CB', 'MET', 'OE1', 'GLU', 11.76), ('CB', 'MET', 'OE2', 'GLU', 10.83), ('CB', 'MET', 'O', 'GLU', 10.58), ('CB', 'MET', 'C', 'GLU', 10.42), ('CB', 'MET', 'CA', 'GLU', 10.23), ('CB', 'MET', 'N', 'GLU', 9.44)], [('CG', 'MET', 'CB', 'GLU', 10.97), ('CG', 'MET', 'CG', 'GLU', 11.44), ('CG', 'MET', 'CD', 'GLU', 11.07), ('CG', 'MET', 'OE1', 'GLU', 11.42), ('CG', 'MET', 'OE2', 'GLU', 10.65), ('CG', 'MET', 'O', 'GLU', 9.63), ('CG', 'MET', 'C', 'GLU', 9.47), ('CG', 'MET', 'CA', 'GLU', 9.48), ('CG', 'MET', 'N', 'GLU', 8.71)], [('SD', 'MET', 'CB', 'GLU', 9.16), ('SD', 'MET', 'CG', 'GLU', 9.66), ('SD', 'MET', 'CD', 'GLU', 9.35), ('SD', 'MET', 'OE1', 'GLU', 9.74), ('SD', 'MET', 'OE2', 'GLU', 9.0), ('SD', 'MET', 'O', 'GLU', 7.98), ('SD', 'MET', 'C', 'GLU', 7.73), ('SD', 'MET', 'CA', 'GLU', 7.68), ('SD', 'MET', 'N', 'GLU', 6.91)], [('CE', 'MET', 'CB', 'GLU', 8.9), ('CE', 'MET', 'CG', 'GLU', 9.38), ('CE', 'MET', 'CD', 'GLU', 8.82), ('CE', 'MET', 'OE1', 'GLU', 8.97), ('CE', 'MET', 'OE2', 'GLU', 8.54), ('CE', 'MET', 'O', 'GLU', 7.42), ('CE', 'MET', 'C', 'GLU', 7.45), ('CE', 'MET', 'CA', 'GLU', 7.41), ('CE', 'MET', 'N', 'GLU', 6.99)], [('O', 'MET', 'CB', 'GLU', 12.37), ('O', 'MET', 'CG', 'GLU', 12.3), ('O', 'MET', 'CD', 'GLU', 11.45), ('O', 'MET', 'OE1', 'GLU', 11.77), ('O', 'MET', 'OE2', 'GLU', 10.65), ('O', 'MET', 'O', 'GLU', 11.77), ('O', 'MET', 'C', 'GLU', 11.63), ('O', 'MET', 'CA', 'GLU', 11.1), ('O', 'MET', 'N', 'GLU', 10.36)], [('C', 'MET', 'CB', 'GLU', 12.15), ('C', 'MET', 'CG', 'GLU', 12.07), ('C', 'MET', 'CD', 'GLU', 11.36), ('C', 'MET', 'OE1', 'GLU', 11.81), ('C', 'MET', 'OE2', 'GLU', 10.52), ('C', 'MET', 'O', 'GLU', 11.72), ('C', 'MET', 'C', 'GLU', 11.45), ('C', 'MET', 'CA', 'GLU', 10.88), ('C', 'MET', 'N', 'GLU', 9.99)], [('CA', 'MET', 'CB', 'GLU', 11.39), ('CA', 'MET', 'CG', 'GLU', 11.49), ('CA', 'MET', 'CD', 'GLU', 10.95), ('CA', 'MET', 'OE1', 'GLU', 11.44), ('CA', 'MET', 'OE2', 'GLU', 10.23), ('CA', 'MET', 'O', 'GLU', 10.8), ('CA', 'MET', 'C', 'GLU', 10.48), ('CA', 'MET', 'CA', 'GLU', 10.06), ('CA', 'MET', 'N', 'GLU', 9.11)], [('N', 'MET', 'CB', 'GLU', 11.84), ('N', 'MET', 'CG', 'GLU', 11.95), ('N', 'MET', 'CD', 'GLU', 11.59), ('N', 'MET', 'OE1', 'GLU', 12.21), ('N', 'MET', 'OE2', 'GLU', 10.87), ('N', 'MET', 'O', 'GLU', 11.39), ('N', 'MET', 'C', 'GLU', 10.94), ('N', 'MET', 'CA', 'GLU', 10.54), ('N', 'MET', 'N', 'GLU', 9.43)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MET_GLU, d, 'A_1hfs_3_4_24_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MET_GLU' :  match1}