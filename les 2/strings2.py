# We gaan het hebben over strings in Python. 
# String bestaan uit woorden en uit zinnen maar ook uit losse letters. 
# Die gaan we in dit bestand bewerken en aanpassen. 
# Met logica, conditions en loops. 
# Success!



# Opdracht 1: Lees de individuele letters
# a) run de code in je terminal wat zie je en wat moet jij nog doen, lees hieronder...
# b) print de twee hoofdletters van het woord op het scherm 
# c) print van beide woorden de laatse letters op het scherm
# d) bepaal de lengte van beide woorden met behulp van de functie len()
# e) Concatenate (aan elkaar rijgen) beide woorden aan elkaar met een + teken

def ao_string():
    s1 = 'Applicatie'
    s2 = 'Ontwikkelaar'
    s1[0] # A
    s2[0] # O
  
    antwoord = s1[0]
    print(antwoord)

ao_string()

# Opdracht 2: Maak gebruik van woorden en cijfers
# a) Print de string op het scherm
# b) print pi op het scherm met de functie str()  // de string functie van Python
# c) Concatenate (aan elkaar rijgen) beide woorden aan elkaar met een + teken

def laat_pi_zien():
    s = 'De waarde van pi is'
    pi = 3.14
  
  #jouw code hier
  
laat_pi_zien()

# Opdracht 3: Een string opknippen
# a) Lees de uitleg hieronder
# b) Print de string op het scherm
# c) print 'ulp' op het scherm met de string slice methode (zie uitleg)
# d) print 'Pulp' op het scherm met de string slice methode (zie uitleg)
# e) print 'p F' op het scherm met de string slice methode (zie uitleg)
# f) print 'ion' op het scherm met de string slice methode (zie uitleg)
# g) print 'Pulp Fiction' op het scherm met de string slice methode (zie uitleg)

# UITLEG:
# String:  H E L L O
# Positie  0 1 2 3 4  | van link naar rechts 
# Positie  5 4 3 2 1  | van rechts naar links
s = 'Hello' 
s1 = s[1:4]    # 'ell'   vanaf de eerste letter tellen tot aan de DERDE karakter (de vierde wordt dus niet meegeteld)
s2 = s[1:]     # 'ello'  vanaf de eerste letter tellen tot aan de laatste
s3 = s[:]      # 'Hello' De gehele string wordt gekozen
s4 = s[1:100]  # 'ello'  vanaf de eerste letter tellen tot aan de laatste (lengte van de string wordt automatisch ingevuld bij overschrijding)

def string_splitten():
  
  s = 'Pulp Fiction'
  
  #jouw code hier

string_splitten()


# Opdracht 4: Boete voor te snel rijden
# a) Lees de uitleg hieronder
# b) Print de string op het scherm
# c) Als de auto een hogere snelheid heeft dan 100 dan print je de volgende string: 'U bent aan de kant gezet, uw rijbewijs aub!'
# d) Als de auto een hogere snelheid heeft dan 160 dan print je de volgende string: 'U bent aan de kant gezet, uw auto aub!'
# e) Als de auto een hogere snelheid heeft dan 100 maar geen gewone auto is (een politieauto) dan print je: 'Iedereen aan de kant, ik moet er langs!'

# UITLEG:
# if statements kunnen ook in Python geschreven worden. We maken echter geen gebruik van haakjes of accolades enzo.
# een if statement schrijf je zo:
leeftijd = 18
student = True
if leeftijd >= 18:
    print ('je bent ouder dan 18')
    if(student == True ):
        print ('deze persoon is niet leerplichtig maar studeert nog wel')
    elif(student == False and leeftijd > 24):
        print ('deze persoon is niet meer kwalificatieplichtig')
else:
    print ('deze persoon is leerplichtig')

# opdracht 4 hieronder coderen
def boete_geven():
    u = 'Een auto rijdt te hard over de weg'
    w = 'gewone auto'
    s = 100

  
    
  
  #jouw code hier
  
boete_geven()