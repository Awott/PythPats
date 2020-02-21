with open ('words.txt','r') as wl:
    w = wl.read().split(' ')
i = len(w)
while ( i > 0 ):
    sb = 0
    sg = 0
    for x in w[i-1]:
        if ( x == 'r' or x == 'R' or x == 'f' or x == 'F' or x =='c' or x == 'C' or x == 'k' or x== 'K' ):
            sb += 1
        elif ( x == 'a' or x == 'A' or x == 'e' or x == 'E' or x == 'i' or x == 'I' or x == 'o' or x == 'O' or x == 'u' or x == 'U' or x == 'y' or x == 'Y' ):
            #Εδώ υπάρχει το παράδοξο πως το y καμία φορά θεωρείται και σύμφωνο αλλά έπρεπε κάπου να το κατατάξω οπότε το έβαλα στα φωνήεντα...
            sb = sb #ξέρω οτι αυτό δεν κάνει τ'ιποτα αλλά δεν ήθελα να το αφήσω κενό XD
        else:
            sg += 1
        if ( sg >= sb ):
            w[i-1] = "good"
        else:
            w[i-1] = "bad"
    i = i - 1    
#print(w)             
             
