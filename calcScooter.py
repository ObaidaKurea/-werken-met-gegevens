Budget = 113
AantalBanden = 2 
BandPrijs = 47.98 
BandArbeid = 15.00

saldo = Budget - AantalBanden * ( BandPrijs + BandArbeid )
isreparatiebetaalbaar = saldo >= 0
print(isreparatiebetaalbaar)
print(type(isreparatiebetaalbaar))

print('is de scooteropknapbeurt betaalbaar?')
if isreparatiebetaalbaar: print ('ja, want de kosten passen in het budget')

else: 
    print ('Nee, ga maar sparen voor een nieuwe scooter')