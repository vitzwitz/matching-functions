'''
FUNC:Jab_1bcr_3_4_16_6
PDB:1bcr
EC:3.4.16.6
RESI:gly,ser,tyr,asp,his
LOCI:a-53,146,147;b-338,397;
'''
jesstemp0 ='n.  n  '
cmd.select('jessatom0', '(('+jesstemp0+'))')
jesstemp1 ='n.  ca '
jesstemp2 ='jessatom0 x. %s'%(1.464500+(d*0.300000))
jesstemp3 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp1+')&('+jesstemp2+')&('+jesstemp3+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.464500+(d*0.300000)))
jesstemp4 ='r. ser'
jesstemp5 ='r. thr'
jesstemp6 ='jessatom0 x. %s'%(6.352900+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(7.474000+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp1+')&('+jesstemp4+'))|(('+jesstemp1+')&('+jesstemp5+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(6.352900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.474000+(d*0.300000)))
jesstemp8 ='n.  cb '
jesstemp9 ='jessatom0 x. %s'%(5.423700+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(6.453900+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp8+')&('+jesstemp4+'))|(('+jesstemp8+')&('+jesstemp5+')))&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.423700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.453900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp13 ='n.  n  '
jesstemp14 ='jessatom0 x. %s'%(4.646000+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(5.757000+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(2.474500+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(2.727000+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.646000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.757000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.727000+(d*0.300000)))
jesstemp18 ='jessatom1 x. %s'%(5.676200+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(3.868300+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(4.191500+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.474600+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp1+')&('+jesstemp14+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.646000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.868300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.191500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.474600+(d*0.300000)))
jesstemp23 ='r. asp'
jesstemp24 ='r. glu'
jesstemp25 ='jessatom0 x. %s'%(15.119700+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(15.564100+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(10.877700+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(10.574700+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(12.917900+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(14.271300+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp1+')&('+jesstemp23+'))|(('+jesstemp1+')&('+jesstemp24+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(15.119700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(15.564100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.877700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.574700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(12.917900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(14.271300+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(13.988500+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(14.544000+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(9.443500+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(9.241500+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(11.574600+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(12.948200+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.565500+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp8+')&('+jesstemp23+'))|(('+jesstemp8+')&('+jesstemp24+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(13.988500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(14.544000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.443500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(11.574600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(12.948200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.565500+(d*0.300000)))
jesstemp39 ='r. his'
jesstemp40 ='jessatom0 x. %s'%(11.877600+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(12.554300+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(8.019400+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(7.494200+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(10.170700+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(11.645300+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(4.928800+(d*0.300000))
jesstemp47 ='jessatom7 x. %s'%(3.908700+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp1+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(11.877600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(12.554300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.019400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.494200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(10.170700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(11.645300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(3.908700+(d*0.300000)))
jesstemp48 ='jessatom0 x. %s'%(10.908000+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(11.463500+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(7.625500+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(6.868000+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(9.554600+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(11.009000+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(5.161100+(d*0.300000))
jesstemp55 ='jessatom7 x. %s'%(4.272300+(d*0.300000))
jesstemp56 ='jessatom8 x. %s'%(1.515000+(d*0.300000))
jesstemp57 ='br. jessatom8'
cmd.select('jessatom9', '(('+jesstemp8+')&('+jesstemp39+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(10.908000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(7.625500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(6.868000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.554600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(11.009000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(5.161100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.272300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(1.515000+(d*0.300000)))
cmd.select('Jab_1bcr_3_4_16_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
