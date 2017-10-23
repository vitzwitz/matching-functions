'''
FUNC:M_2ahj_4_2_1_84
PDB:2ahj
EC:4.2.1.84
RESI:fe,ser,arg
LOCI:a-300;c-113;d-56;
'''
import motifFunctions as cmd
ARG_SER = { 
	'distances':
		[[11.86, 11.0], [11.01, 10.06], [10.84, 10.03], [10.27, 9.4], [11.1, 10.16], [12.4, 11.43], [10.71, 9.74]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 11.86), ('CB', 'ARG', 'OG', 'SER', 11.0)], [('CG', 'ARG', 'CB', 'SER', 11.01), ('CG', 'ARG', 'OG', 'SER', 10.06)], [('CD', 'ARG', 'CB', 'SER', 10.84), ('CD', 'ARG', 'OG', 'SER', 10.03)], [('NE', 'ARG', 'CB', 'SER', 10.27), ('NE', 'ARG', 'OG', 'SER', 9.4)], [('CZ', 'ARG', 'CB', 'SER', 11.1), ('CZ', 'ARG', 'OG', 'SER', 10.16)], [('NH1', 'ARG', 'CB', 'SER', 12.4), ('NH1', 'ARG', 'OG', 'SER', 11.43)], [('NH2', 'ARG', 'CB', 'SER', 10.71), ('NH2', 'ARG', 'OG', 'SER', 9.74)]]}
ARG_FE = { 
	'distances':
		[[35.84], [36.97], [36.89], [38.01], [39.25], [39.67], [40.17]],
	'comparisons':
		[[('CB', 'ARG', 'FE', 'FE', 35.84)], [('CG', 'ARG', 'FE', 'FE', 36.97)], [('CD', 'ARG', 'FE', 'FE', 36.89)], [('NE', 'ARG', 'FE', 'FE', 38.01)], [('CZ', 'ARG', 'FE', 'FE', 39.25)], [('NH1', 'ARG', 'FE', 'FE', 39.67)], [('NH2', 'ARG', 'FE', 'FE', 40.17)]]}
SER_FE = { 
	'distances':
		[[36.94], [37.62]],
	'comparisons':
		[[('CB', 'SER', 'FE', 'FE', 36.94)], [('OG', 'SER', 'FE', 'FE', 37.62)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_SER, d, 'M_2ahj_4_2_1_84')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_FE, d, 'M_2ahj_4_2_1_84')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_FE, d, 'M_2ahj_4_2_1_84')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_SER' :  match1,
		'ARG_FE' :  match2,
		'SER_FE' :  match3}