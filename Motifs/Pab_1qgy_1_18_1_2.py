'''
FUNC:Pab_1qgy_1_18_1_2
PDB:1qgy
EC:1.18.1.2
RESI:ser,cys,glu
LOCI:a-80,261,301;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. cys'%(d*8.81))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. SG&r. cys'%(d*7.24))
cmd.select('ser3', 'n. OG&r. ser w. %s of n. CB&r. cys'%(d*8.06))
cmd.select('ser4', 'n. OG&r. ser w. %s of n. SG&r. cys'%(d*6.34))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*9.10))
cmd.select('ser6', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*8.28))
cmd.select('ser7', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*6.98))
cmd.select('ser8', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*7.28))
cmd.select('ser9', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*5.91))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*8.02))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*7.09))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*5.94))
cmd.select('ser13', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*6.49))
cmd.select('ser14', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*4.74))
cmd.select('ser', 'br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&ser'%(d*8.81))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. OG&ser'%(d*8.06))
cmd.select('cys3', 'n. SG&r. cys w. %s of n. CB&ser'%(d*7.24))
cmd.select('cys4', 'n. SG&r. cys w. %s of n. OG&ser'%(d*6.34))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*6.84))
cmd.select('cys6', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*7.45))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*7.56))
cmd.select('cys8', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*8.32))
cmd.select('cys9', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*7.31))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*6.25))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*6.37))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*6.25))
cmd.select('cys13', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*7.15))
cmd.select('cys14', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*5.73))
cmd.select('cys', 'br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*9.10))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*8.02))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*8.28))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*7.09))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*6.98))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*5.94))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*7.28))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*6.49))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*5.91))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*4.74))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&cys'%(d*6.84))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. SG&cys'%(d*6.25))
cmd.select('glu13', 'n. CG&r. glu w. %s of n. CB&cys'%(d*7.45))
cmd.select('glu14', 'n. CG&r. glu w. %s of n. SG&cys'%(d*6.37))
cmd.select('glu15', 'n. CD&r. glu w. %s of n. CB&cys'%(d*7.56))
cmd.select('glu16', 'n. CD&r. glu w. %s of n. SG&cys'%(d*6.25))
cmd.select('glu17', 'n. OE1&r. glu w. %s of n. CB&cys'%(d*8.32))
cmd.select('glu18', 'n. OE1&r. glu w. %s of n. SG&cys'%(d*7.15))
cmd.select('glu19', 'n. OE2&r. glu w. %s of n. CB&cys'%(d*7.31))
cmd.select('glu20', 'n. OE2&r. glu w. %s of n. SG&cys'%(d*5.73))
cmd.select('glu', 'br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.select('Pab_1qgy_1_18_1_2', 'ser|cys|glu')
cmd.delete('ser')
cmd.delete('cys')
cmd.delete('glu')
