#fitting-ON
########  Set the Device Parameters  ###########
de = 30 * 10**-9            #Electrode thickness in meters #done
do = 6 * 10**-9             #Oxide thickness in meters #done
Lwf = 2.44 * 10**-8         #Wiedemann-Franz constant
Trt = 296                   #Ambient temperature in Kelvin #done
######## End of Parameters Section ###########
#out:
#"ke, sigSat, and Tc values:"
#rmax "radius at the end of the ON switching:"
[  1.94997306e+02   2.44013731e+05   2.99999986e+03]
radius at the end of the ON switching:
1.14698650897e-11
ke, sigSat, and Tc values:
[  1.95886846e+02   2.47697152e+05   2.99999992e+03]
radius at the end of the ON switching:
4.39157495093e-10
#nea peiramata
ke, sigSat, and Tc values:
[  1.42102173e+02   3.89663484e+05   2.99999794e+03]
radius at the end of the ON switching:
4.9911519869e-09


#fitting-OFF
#These should all be the same as will be used in the simulation code
########  Set the Device Parameters  ###########
sigSat = 3.89663484e+05                       #Saturation conductivity was previously found from fitting the ON switching data @fitting-ON
numberOfShells = 200                            #Number of Grids in the Radial Direction
thickness = 6 * 10**-9                         #Vertical Thickness in the z direction
simRadiusRange = 20 * 10**-9                    #The full spacial range of the simulation
shellSize = simRadiusRange/numberOfShells       #Calculate GridSpacing

rmax = 4.9911519869e-09                     #@ON #This is the radius that was previously found from fitting the ON switching data @fitting-ON
######## End of Parameters Section ###########
#out:
the a and b values are:
[  8.81773536e-10   9.06984790e-01]
the a and b values are:
[  1.06946442e-13   7.08532181e-01]
#nea peiramata
the a and b values are:
[  8.23604156e-10   9.27822710e-01]
the a and b values are:
[ 0.03086161  0.10000065]
the a and b values are:
[  4.04217926e-06   2.31860943e+00]

#fitting-final
########  Set the Device Parameters  ###########
delT = 1186                     #Activation temperature in degrees C from the ambient temperature
Trt = 296                       #done #Ambient temperature in degrees C
de = 30 * 10**-9                #done #Electrode thickness
do = 6 * 10**-9                	#done #Oxide thickness
ke = 1.42102173e+02             #done1 #@fittin-ON #Effective electrode thermal conductivity - Usually higher than bulk values due to spreading effects 
Lwf = 2.44 * 10**-8             #Wiedemann-Franz constant

sigSat = 3.89663484e+05           #@fittin-ON #Saturation Conductivity in the Filament 
maxConc = 100                   #The maximum concentration of oxygen vacancies or dopants in arbitrary units #de_mas_noiazei
minConc = 50                    #The minimum concentration of oxygen vacancies or dopants in arbitrary units #de_mas_noiazei
a = 8.23604156e-10                     #@OFF #Amplitude coefficient for Poole-Frenkel contribution
b = 9.27822710e-01                     #@OFF #Nonlinearity coefficient for Poole-Frenkel contribution 
######## End of Parameters Section ###########