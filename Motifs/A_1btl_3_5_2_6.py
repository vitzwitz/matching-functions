'''
FUNC:A_1btl_3_5_2_6
PDB:1btl
EC:3.5.2.6
RESI:ser,lys,ser,glu
LOCI:a-70,73,130,166;
'''
import motifFunctions as cmd
SER_LYS = { 
	'distances':
		[[9.21, 8.79, 7.36, 7.56, 6.52], [8.54, 8.16, 6.84, 7.1, 6.17], [7.39, 6.83, 6.11, 6.09, 5.75], [7.96, 7.07, 6.12, 5.6, 4.9]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 9.21), ('CB', 'SER', 'CG', 'LYS', 8.79), ('CB', 'SER', 'CD', 'LYS', 7.36), ('CB', 'SER', 'CE', 'LYS', 7.56), ('CB', 'SER', 'NZ', 'LYS', 6.52)], [('OG', 'SER', 'CB', 'LYS', 8.54), ('OG', 'SER', 'CG', 'LYS', 8.16), ('OG', 'SER', 'CD', 'LYS', 6.84), ('OG', 'SER', 'CE', 'LYS', 7.1), ('OG', 'SER', 'NZ', 'LYS', 6.17)], [('CB', 'SER', 'CB', 'LYS', 7.39), ('CB', 'SER', 'CG', 'LYS', 6.83), ('CB', 'SER', 'CD', 'LYS', 6.11), ('CB', 'SER', 'CE', 'LYS', 6.09), ('CB', 'SER', 'NZ', 'LYS', 5.75)], [('OG', 'SER', 'CB', 'LYS', 7.96), ('OG', 'SER', 'CG', 'LYS', 7.07), ('OG', 'SER', 'CD', 'LYS', 6.12), ('OG', 'SER', 'CE', 'LYS', 5.6), ('OG', 'SER', 'NZ', 'LYS', 4.9)]]}
SER_SER = { 
	'distances':
		[[6.83, 6.58], [5.55, 5.54], [6.83, 5.55], [6.58, 5.54]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'SER', 6.83), ('CB', 'SER', 'OG', 'SER', 6.58)], [('OG', 'SER', 'CB', 'SER', 5.55), ('OG', 'SER', 'OG', 'SER', 5.54)], [('CB', 'SER', 'CB', 'SER', 6.83), ('CB', 'SER', 'OG', 'SER', 5.55)], [('OG', 'SER', 'CB', 'SER', 6.58), ('OG', 'SER', 'OG', 'SER', 5.54)]]}
GLU_SERI = { 
	'distances':
		[[10.85, 9.68], [9.5, 8.42], [8.34, 7.2], [8.7, 7.48], [7.22, 6.19]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SERI', 10.85), ('CB', 'GLU', 'OG', 'SERI', 9.68)], [('CG', 'GLU', 'CB', 'SERI', 9.5), ('CG', 'GLU', 'OG', 'SERI', 8.42)], [('CD', 'GLU', 'CB', 'SERI', 8.34), ('CD', 'GLU', 'OG', 'SERI', 7.2)], [('OE1', 'GLU', 'CB', 'SERI', 8.7), ('OE1', 'GLU', 'OG', 'SERI', 7.48)], [('OE2', 'GLU', 'CB', 'SERI', 7.22), ('OE2', 'GLU', 'OG', 'SERI', 6.19)]]}
LYS_SERI = { 
	'distances':
		[[7.39, 7.96], [6.83, 7.07], [6.11, 6.12], [6.09, 5.6], [5.75, 4.9]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SERI', 7.39), ('CB', 'LYS', 'OG', 'SERI', 7.96)], [('CG', 'LYS', 'CB', 'SERI', 6.83), ('CG', 'LYS', 'OG', 'SERI', 7.07)], [('CD', 'LYS', 'CB', 'SERI', 6.11), ('CD', 'LYS', 'OG', 'SERI', 6.12)], [('CE', 'LYS', 'CB', 'SERI', 6.09), ('CE', 'LYS', 'OG', 'SERI', 5.6)], [('NZ', 'LYS', 'CB', 'SERI', 5.75), ('NZ', 'LYS', 'OG', 'SERI', 4.9)]]}
LYS_GLU = { 
	'distances':
		[[11.68, 10.19, 9.94, 10.98, 8.85], [10.13, 8.64, 8.42, 9.48, 7.35], [9.74, 8.3, 7.95, 8.92, 6.91], [8.25, 6.82, 6.43, 7.39, 5.44], [8.19, 6.91, 6.29, 7.01, 5.42]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 11.68), ('CB', 'LYS', 'CG', 'GLU', 10.19), ('CB', 'LYS', 'CD', 'GLU', 9.94), ('CB', 'LYS', 'OE1', 'GLU', 10.98), ('CB', 'LYS', 'OE2', 'GLU', 8.85)], [('CG', 'LYS', 'CB', 'GLU', 10.13), ('CG', 'LYS', 'CG', 'GLU', 8.64), ('CG', 'LYS', 'CD', 'GLU', 8.42), ('CG', 'LYS', 'OE1', 'GLU', 9.48), ('CG', 'LYS', 'OE2', 'GLU', 7.35)], [('CD', 'LYS', 'CB', 'GLU', 9.74), ('CD', 'LYS', 'CG', 'GLU', 8.3), ('CD', 'LYS', 'CD', 'GLU', 7.95), ('CD', 'LYS', 'OE1', 'GLU', 8.92), ('CD', 'LYS', 'OE2', 'GLU', 6.91)], [('CE', 'LYS', 'CB', 'GLU', 8.25), ('CE', 'LYS', 'CG', 'GLU', 6.82), ('CE', 'LYS', 'CD', 'GLU', 6.43), ('CE', 'LYS', 'OE1', 'GLU', 7.39), ('CE', 'LYS', 'OE2', 'GLU', 5.44)], [('NZ', 'LYS', 'CB', 'GLU', 8.19), ('NZ', 'LYS', 'CG', 'GLU', 6.91), ('NZ', 'LYS', 'CD', 'GLU', 6.29), ('NZ', 'LYS', 'OE1', 'GLU', 7.01), ('NZ', 'LYS', 'OE2', 'GLU', 5.42)]]}
SER_GLU = { 
	'distances':
		[[12.18, 11.15, 10.37, 10.68, 9.62], [12.03, 10.88, 9.96, 10.28, 9.08], [10.85, 9.5, 8.34, 8.7, 7.22], [9.68, 8.42, 7.2, 7.48, 6.19]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 12.18), ('CB', 'SER', 'CG', 'GLU', 11.15), ('CB', 'SER', 'CD', 'GLU', 10.37), ('CB', 'SER', 'OE1', 'GLU', 10.68), ('CB', 'SER', 'OE2', 'GLU', 9.62)], [('OG', 'SER', 'CB', 'GLU', 12.03), ('OG', 'SER', 'CG', 'GLU', 10.88), ('OG', 'SER', 'CD', 'GLU', 9.96), ('OG', 'SER', 'OE1', 'GLU', 10.28), ('OG', 'SER', 'OE2', 'GLU', 9.08)], [('CB', 'SER', 'CB', 'GLU', 10.85), ('CB', 'SER', 'CG', 'GLU', 9.5), ('CB', 'SER', 'CD', 'GLU', 8.34), ('CB', 'SER', 'OE1', 'GLU', 8.7), ('CB', 'SER', 'OE2', 'GLU', 7.22)], [('OG', 'SER', 'CB', 'GLU', 9.68), ('OG', 'SER', 'CG', 'GLU', 8.42), ('OG', 'SER', 'CD', 'GLU', 7.2), ('OG', 'SER', 'OE1', 'GLU', 7.48), ('OG', 'SER', 'OE2', 'GLU', 6.19)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_LYS, d, 'A_1btl_3_5_2_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_SER, d, 'A_1btl_3_5_2_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_SERI, d, 'A_1btl_3_5_2_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_SERI, d, 'A_1btl_3_5_2_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_GLU, d, 'A_1btl_3_5_2_6')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_GLU, d, 'A_1btl_3_5_2_6')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_LYS' :  match1,
		'SER_SER' :  match2,
		'GLU_SERI' :  match3,
		'LYS_SERI' :  match4,
		'LYS_GLU' :  match5,
		'SER_GLU' :  match6}