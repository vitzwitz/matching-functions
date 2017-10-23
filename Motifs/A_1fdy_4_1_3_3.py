'''
FUNC:A_1fdy_4_1_3_3
PDB:1fdy
EC:4.1.3.3
RESI:ser,thr,lys
LOCI:a-47,48,165;
'''
import motifFunctions as cmd
THR_LYS = { 
	'distances':
		[[13.6, 12.37, 11.11, 9.97, 8.91], [12.95, 11.65, 10.5, 9.22, 8.28], [14.79, 13.5, 12.3, 11.14, 10.19], [16.36, 15.25, 13.89, 12.87, 11.66], [15.2, 14.12, 12.74, 11.76, 10.52], [14.2, 13.06, 11.74, 10.65, 9.45], [13.25, 12.22, 10.85, 9.84, 8.55]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 13.6), ('CB', 'THR', 'CG', 'LYS', 12.37), ('CB', 'THR', 'CD', 'LYS', 11.11), ('CB', 'THR', 'CE', 'LYS', 9.97), ('CB', 'THR', 'NZ', 'LYS', 8.91)], [('OG1', 'THR', 'CB', 'LYS', 12.95), ('OG1', 'THR', 'CG', 'LYS', 11.65), ('OG1', 'THR', 'CD', 'LYS', 10.5), ('OG1', 'THR', 'CE', 'LYS', 9.22), ('OG1', 'THR', 'NZ', 'LYS', 8.28)], [('CG2', 'THR', 'CB', 'LYS', 14.79), ('CG2', 'THR', 'CG', 'LYS', 13.5), ('CG2', 'THR', 'CD', 'LYS', 12.3), ('CG2', 'THR', 'CE', 'LYS', 11.14), ('CG2', 'THR', 'NZ', 'LYS', 10.19)], [('O', 'THR', 'CB', 'LYS', 16.36), ('O', 'THR', 'CG', 'LYS', 15.25), ('O', 'THR', 'CD', 'LYS', 13.89), ('O', 'THR', 'CE', 'LYS', 12.87), ('O', 'THR', 'NZ', 'LYS', 11.66)], [('C', 'THR', 'CB', 'LYS', 15.2), ('C', 'THR', 'CG', 'LYS', 14.12), ('C', 'THR', 'CD', 'LYS', 12.74), ('C', 'THR', 'CE', 'LYS', 11.76), ('C', 'THR', 'NZ', 'LYS', 10.52)], [('CA', 'THR', 'CB', 'LYS', 14.2), ('CA', 'THR', 'CG', 'LYS', 13.06), ('CA', 'THR', 'CD', 'LYS', 11.74), ('CA', 'THR', 'CE', 'LYS', 10.65), ('CA', 'THR', 'NZ', 'LYS', 9.45)], [('N', 'THR', 'CB', 'LYS', 13.25), ('N', 'THR', 'CG', 'LYS', 12.22), ('N', 'THR', 'CD', 'LYS', 10.85), ('N', 'THR', 'CE', 'LYS', 9.84), ('N', 'THR', 'NZ', 'LYS', 8.55)]]}
SER_LYS = { 
	'distances':
		[[12.26, 11.44, 10.18, 9.27, 7.99], [11.55, 10.89, 9.68, 8.94, 7.7], [14.98, 14.05, 12.68, 11.73, 10.4], [13.76, 12.83, 11.45, 10.52, 9.17], [12.87, 12.08, 10.7, 9.9, 8.52], [11.94, 11.21, 9.77, 9.14, 7.7]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 12.26), ('CB', 'SER', 'CG', 'LYS', 11.44), ('CB', 'SER', 'CD', 'LYS', 10.18), ('CB', 'SER', 'CE', 'LYS', 9.27), ('CB', 'SER', 'NZ', 'LYS', 7.99)], [('OG', 'SER', 'CB', 'LYS', 11.55), ('OG', 'SER', 'CG', 'LYS', 10.89), ('OG', 'SER', 'CD', 'LYS', 9.68), ('OG', 'SER', 'CE', 'LYS', 8.94), ('OG', 'SER', 'NZ', 'LYS', 7.7)], [('O', 'SER', 'CB', 'LYS', 14.98), ('O', 'SER', 'CG', 'LYS', 14.05), ('O', 'SER', 'CD', 'LYS', 12.68), ('O', 'SER', 'CE', 'LYS', 11.73), ('O', 'SER', 'NZ', 'LYS', 10.4)], [('C', 'SER', 'CB', 'LYS', 13.76), ('C', 'SER', 'CG', 'LYS', 12.83), ('C', 'SER', 'CD', 'LYS', 11.45), ('C', 'SER', 'CE', 'LYS', 10.52), ('C', 'SER', 'NZ', 'LYS', 9.17)], [('CA', 'SER', 'CB', 'LYS', 12.87), ('CA', 'SER', 'CG', 'LYS', 12.08), ('CA', 'SER', 'CD', 'LYS', 10.7), ('CA', 'SER', 'CE', 'LYS', 9.9), ('CA', 'SER', 'NZ', 'LYS', 8.52)], [('N', 'SER', 'CB', 'LYS', 11.94), ('N', 'SER', 'CG', 'LYS', 11.21), ('N', 'SER', 'CD', 'LYS', 9.77), ('N', 'SER', 'CE', 'LYS', 9.14), ('N', 'SER', 'NZ', 'LYS', 7.7)]]}
SER_THR = { 
	'distances':
		[[7.23, 6.97, 8.65, 8.36, 7.4, 6.41, 5.09], [8.47, 8.14, 9.93, 9.71, 8.7, 7.76, 6.38], [6.29, 6.79, 7.25, 5.63, 5.03, 4.81, 4.27], [5.72, 6.11, 6.95, 5.96, 5.03, 4.45, 3.33], [6.84, 7.02, 8.22, 7.43, 6.43, 5.81, 4.43], [6.94, 7.22, 8.37, 7.84, 6.7, 6.21, 4.81]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'THR', 7.23), ('CB', 'SER', 'OG1', 'THR', 6.97), ('CB', 'SER', 'CG2', 'THR', 8.65), ('CB', 'SER', 'O', 'THR', 8.36), ('CB', 'SER', 'C', 'THR', 7.4), ('CB', 'SER', 'CA', 'THR', 6.41), ('CB', 'SER', 'N', 'THR', 5.09)], [('OG', 'SER', 'CB', 'THR', 8.47), ('OG', 'SER', 'OG1', 'THR', 8.14), ('OG', 'SER', 'CG2', 'THR', 9.93), ('OG', 'SER', 'O', 'THR', 9.71), ('OG', 'SER', 'C', 'THR', 8.7), ('OG', 'SER', 'CA', 'THR', 7.76), ('OG', 'SER', 'N', 'THR', 6.38)], [('O', 'SER', 'CB', 'THR', 6.29), ('O', 'SER', 'OG1', 'THR', 6.79), ('O', 'SER', 'CG2', 'THR', 7.25), ('O', 'SER', 'O', 'THR', 5.63), ('O', 'SER', 'C', 'THR', 5.03), ('O', 'SER', 'CA', 'THR', 4.81), ('O', 'SER', 'N', 'THR', 4.27)], [('C', 'SER', 'CB', 'THR', 5.72), ('C', 'SER', 'OG1', 'THR', 6.11), ('C', 'SER', 'CG2', 'THR', 6.95), ('C', 'SER', 'O', 'THR', 5.96), ('C', 'SER', 'C', 'THR', 5.03), ('C', 'SER', 'CA', 'THR', 4.45), ('C', 'SER', 'N', 'THR', 3.33)], [('CA', 'SER', 'CB', 'THR', 6.84), ('CA', 'SER', 'OG1', 'THR', 7.02), ('CA', 'SER', 'CG2', 'THR', 8.22), ('CA', 'SER', 'O', 'THR', 7.43), ('CA', 'SER', 'C', 'THR', 6.43), ('CA', 'SER', 'CA', 'THR', 5.81), ('CA', 'SER', 'N', 'THR', 4.43)], [('N', 'SER', 'CB', 'THR', 6.94), ('N', 'SER', 'OG1', 'THR', 7.22), ('N', 'SER', 'CG2', 'THR', 8.37), ('N', 'SER', 'O', 'THR', 7.84), ('N', 'SER', 'C', 'THR', 6.7), ('N', 'SER', 'CA', 'THR', 6.21), ('N', 'SER', 'N', 'THR', 4.81)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_LYS, d, 'A_1fdy_4_1_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_LYS, d, 'A_1fdy_4_1_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_THR, d, 'A_1fdy_4_1_3_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_LYS' :  match1,
		'SER_LYS' :  match2,
		'SER_THR' :  match3}