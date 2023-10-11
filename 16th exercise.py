Population_of_Marrakech=1000000
Population_of_Agadir=500000
years=0
while Population_of_Agadir <= Population_of_Marrakech :
    Population_of_Marrakech=Population_of_Marrakech+500000
    Population_of_Agadir=Population_of_Agadir+Population_of_Agadir*0.08
    years=years+1
print('The population of Agadir will exceed that of Marrakech in',years,'years')