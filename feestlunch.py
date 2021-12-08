aantalcroissantjes = 17
prijscroissantjes = 0.39
aantalstokbroden = 2
prijsstokbroden = 2.78
kortingsbonnen = 1.50

bedrag = ( aantalcroissantjes * prijscroissantjes + ( aantalstokbroden * prijsstokbroden ) - kortingsbonnen ) 

print (bedrag)

print ("De feestlunch kost je bij de bakker: " + str (bedrag) + " euro voor de " + str (aantalcroissantjes) + ' croissantjes ' + str ( aantalstokbroden) + 
' stokbroden'  " als de 3 kortingsbonnen nog geldig zijn!")