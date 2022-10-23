elma=5
kivi=8
seftali=3
su=1
bez=2.5
poset=0.25
peynir=28
cikolata=3
plastikTop=5
meyveSuyu=2


urun1=input("1. ürünü giriniz :")
urun2=input("2. ürünü giriniz :")
urun3=input("3. ürünü giriniz :")
urun4=input("4. ürünü giriniz :")

urunn1=eval(urun1)
urunn2=eval(urun2)
urunn3=eval(urun3)
urunn4=eval(urun4)
toplamTutar=urunn1+urunn2+urunn3+urunn4

para=int(input("Müşterinin verdiği para :"))
print("-"*100)
print("Toplam tutar :",toplamTutar)
paraUstu=para-toplamTutar
print("Para Üstü :",paraUstu)
