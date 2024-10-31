tempo = int(input())
hr = tempo//3600
tempo = tempo%3600
minu = tempo//60
seg = tempo%60
print("%i:%i:%i"%(hr,minu,seg))
