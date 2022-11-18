print("OBS: mata in minst 100, och mata in bara hundratal och tusental")
pengar=int(input("Mata in hur manga hundra kronor du vill ha: "))
femhundra=pengar%500
fem=(pengar-femhundra)/500

tvahundra=femhundra%200
tva=(femhundra-tvahundra)/200

etthundra=tvahundra%100
ett=(tvahundra-etthundra)/100


if fem==0 and tva==0:
    print("Du kommer att fa utt etthundra lapp")
elif fem==0 and tva>0 and ett==0:
    print("Du kommer att fa utt", tva, "tvahundra lappar")
elif fem==0 and tva>0 and ett==1:
    print("Du kommer att fa utt", tva, "tvahundra lappar och etthundra lapp")
elif fem>0 and tva==0 and ett==0:
    print("Du kommer att fa utt", fem, "femhundra lappar")
elif fem>0 and tva==0 and ett==1:
    print("Du kommer att fa utt", fem, "femhundra lappar och etthundra lapp")
elif fem>0 and tva>0 and ett==0:
    print("Du kommer att fa utt", fem, "femhundra lappar och", tva, "tvahundra lappar")
elif fem>0 and tva>0 and ett==1:
    print("Du kommer fa ut", fem, "femhundra lappar,", tva, "tvahundra lappar och", ett, "hundra lapp")
else:
    print("Du har mattat in mindre an hundratal")