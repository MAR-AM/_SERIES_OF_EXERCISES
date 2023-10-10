print('le temps en jours, heures, minutes et secondes.')
T=int(input('veillez saisir un temps en secondes : '))
j=T//(24*60*60)
R=T%(24*60*60)
h=R//(60*60)
m=R//60
s=T%60
print('le temps est :',j,'jours',h,'heures',m,'minutes',s,'seconds')