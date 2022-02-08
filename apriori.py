

def TumAltKumeler(kume):
    result = [[]]
    for x in kume:
        z = [y + [x] for y in result]
        result = result + z

    result.sort()
    result.sort(key=len)
    return result

#print(TumAltKumeler(['A','B','C','D']))
      
def AltKumeler(kume, n):
    if n not in range(1, len(kume)+1):
       print('Hata. Kümenin, alt küme eleman sayısı hatalı')
       return
        
    fullset = TumAltKumeler(kume)
    result = [x for x in fullset if len(x) == n]
    return result

def test():
    s=['Seker','Un','Yag','Tuz','Biber']
    for j in range(1, len(s)+1):
        r = AltKumeler(s,j)
        print(j,'.li altkümeler')
        print('='*15)
        for i,v in enumerate(r,1):print(i,'.',v)
        print()

def intOku(mesaj, ilkdeger, sondeger):
    bilgi = "\t\t %s (%d - %d):" % (mesaj, ilkdeger, sondeger)
    while True:
        a = input(bilgi)
        if a.isdigit() and int(a) in range(ilkdeger,sondeger+1):
            break
        else:
            print('Lütfen geçerli bir değer giriniz!')
    return int(a)

def dataOku():
    data = []
    with open('data.txt','r') as f:
        for line in f:
            satir = line.strip().split(',')
            data.append(satir)

    max_satir = len(data)
    destek = intOku('Asgari Destek (frekans)',1,max_satir)
    guven  = intOku('Guven',0,100)
    
    return data, destek, guven

def dataUret():

    baha = [['Seker','Cay','Ekmek'],
            ['Ekmek','Peynir','Zeytin','Makarna'],
            ['Seker','Peynir','Deterjan','Ekmek','Makarna'],
            ['Ekmek','Peynir','Cay','Makarna'],
            ['Peynir','Makarna','Seker','Icecek']]
    baha_destek = 3
    baha_guven = 60
    
    org = [['Bread', 'Milk'], 
            ['Bread', 'Diapers', 'Beer', 'Eggs'], 
            ['Milk', 'Diapers', 'Beer', 'Coke'], 
            ['Bread', 'Milk', 'Diapers', 'Beer'], 
            ['Bread', 'Milk', 'Diapers', 'Coke']]
    org_destek = 3
    org_guven = 80

    if False:
        data = org, org_destek, org_guven
    else:
        data = baha, baha_destek, baha_guven

    return data

def kalemleriBul(data, goster=False):
    sonuc = []
    for satir in data:
        for kalem in satir:
            if kalem not in sonuc:
                sonuc.append(kalem)
    sonuc = sorted(sonuc)

    if goster:
        print()
        print(sonuc)

    return sonuc

def adetBul(data, kume, goster=False):
    sonuc = {}
    for e in kume:
        adet = 0
        alt = set(e)
        for satir in data:
            tum = set(satir)
            if alt.issubset(tum): adet += 1
        sonuc[tuple(e)]=adet

    if goster:
        print()
        for k,v in sonuc.items():
            print(k,'==>',v,' adet')

    return sonuc

def destekUstunuBul(data, kalemler, destek, goster=False):
    tamami={}
   
    for i in range(1,len(kalemler)+1):
        kalem_i = AltKumeler(kalemler, i)
        #print('i=',i,'kalem:',kalem_i)
        sonuc = adetBul(data, kalem_i)
        tamami.update(sonuc)

    donen = {k:v for k,v in tamami.items() if v >= destek}

    if goster:
        print()
        for k,v in donen.items():
            print(k,'==>',v,' adet')

    return donen
    
def hesapYap(sozluk, goster=False):
    sonuc = {}
    for k,v in sozluk.items():
        boy = len(k)
        if boy == 1:continue
        for j in range(1,boy):
            alt = AltKumeler(k, j)
            for i in alt:
                adet = sozluk[tuple(i)]
                oran = int(v / adet * 100)
                izah = ','.join(k) + '-->' + ','.join(i)
                hesap = '('+str(v)+'/'+str(adet)+')=%'+str(oran)
                isim = izah+hesap 
                sonuc[isim] = oran

                if goster:
                    print('-'*60)
                    
                    print(isim)
                    #print('sonuc:',sonuc)

    return sonuc
    
def neticeBul(sozluk, guven, goster=True):
    sonuc = [k for k,v in sozluk.items() if v >= guven]

    if goster:
        print()
        print('='*60)
        print('Sonuc:')
        print('='*60)
        for k in sonuc:
            print(k)
            
        print('='*60)

    return sonuc

    
#data, destek, guven = dataUret()
data, destek, guven = dataOku()

kalemler = kalemleriBul(data, goster=False)
destekUstu = destekUstunuBul(data, kalemler, destek, goster=False)
hesap = hesapYap(destekUstu, goster=True)
netice = neticeBul(hesap, guven)


