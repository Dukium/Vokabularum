


lat=["amicitia","ara","ara","cura","cura","femina","forma","iniuria","mensa","patientia","statua","superbia","superbia","agricola","epulae","amica","aqua","bestia","causa","causa","concordia","dea","dextra","discipula","epistola","epistula","fabula","fama","filia","flamma","flamma","fortuna","fortuna","invidia","ira","ira","lupa","machina","machina","magistra","miseria","miseria","ora","ripa","patria","porta","potentia","potentia","procella","puella","pugna","regina","ruina","ruina","schola","silva","sponsa","terra","unda","via","victoria","vita","incola","poeta","nauta","amicus","avus","campus","ager","deus","discipulus","dolus","dominus","equus","filius","fluvius","hortus","mundus","murus","patruus",
     "pontus","populus","servus","socius","socius","posteri","magister","liber","puer","vir","vir","bellum","consilium","donum","donum","exemplum","maledictum","maledictum","officium","officium","oppidum","regnum","saeculum","signum","solium","templum","verbum","verum","arma","aedifico","ambulo","amo","amo","canto","clamo","voro","do","dono","dono","educo","expecto","expecto","firmo","impero","impugno","intro","laudo","narro","narro","navigo","orno","orno","paro","praeparo","porto","pugno","puto","cogito","regno","regno","saluto","servo","servo","sono","sono","specto","specto","supero","vasto","voco","compleo",
     "fleo","fleo","habeo","moneo","moneo","praebeo","praebeo","sedeo","timeo","video","amitto","condo","credo","cresco","decerno","dico","dico","discedo","decedo","duco","expello","gigno","mitto","quaero","reddo","relinquo","relinquo","vinco","accipio","accipio","capio","capio","cupio","facio","facio","fugio","fugio","iacio","interficio","neco","rapio","rapio","punio","venio","nutrio","alo","invenio","audio","audio","finio","scio","nescio","altus","antiquus","bonus","clarus","clarus","futurus","geminus","infortunatus","fortunatus","laetus","longus","magnus","malus","malus","multus","notus","novus","parvus","plenus","primigenitus","primus",
     "solus","solus","splendidus","verus","verus","miser","miser","pulcher","meus","tuus","suus","noster","vester"]


hrv=["prijateljstvo","žrtvenik","oltar","briga","njega","žena","oblik","nepravda","stol","strpljivost","kip","oholost","ponos","ratar","gozba","prijateljica","voda","zvijer","uzrok","povod","sloga","božica","desnica","učenica","pismo","pismo","priča","glas","kćer","plamen","vatra","sreća","sudbina","zavist","srdžba","gnjev","vučica","stroj","naprava","učiteljica","jad","nesreća","obala","obala rijeke","domovina","vrata","moć","snaga","oluja","djevojka","bitka","kraljica","ruševina","propast","škola","šuma","zaručnica","zemlja","val","put","pobjeda","život","stanovnik","pjesnik","mornar","prijatelj","djed","polje","polje","bog","učenik","varka","gospodar","konj","sin","rijeka","vrt","svijet","zid","stric",
     "more","narod","rob","drug","pratitelj","potomci","učitelj","knjiga","dječak","muškarac","junak","rat","savjet","poklon","dar","primjer","kletva","psovka","dužnost","zadaća","grad","kraljevstvo","stoljeće","znak","prijestolje","hram","riječ","istina","oružje","graditi","šetati","voljeti","zavoljeti","pjevati","vikati","proždirati","dati","darovati","pokloniti","odgajati","očekivati","nadati se","jačati","zapovjediti","napadati","ulaziti","hvaliti","pripovijedati","pričati","ploviti","ukrašavati","kititi","pripremiti","pripremiti","nositi","boriti se","misliti","smatrati","kraljevati","vladati","pozdravljati","čuvati","paziti","zvečkati","odjekivati","gledati","promatrati","nadvladati","pustošiti","zvati","ispuniti",
     "plakati","oplakivati","imati","opominjati","upozoravati","pružiti","pokazati","sjediti","bojati se","vidjeti","izgubiti","osnovati","vjerovati","rasti","odlučiti","reći","govoriti","otići","udaljiti se","voditi","protjerati","roditi","slati","tražiti","vratiti","ostaviti","napustiti","pobijediti","primiti","prihvatiti","uhvatiti","zarobiti","željeti","činiti","raditi","bježati","pobjeći","baciti","ubiti","ubiti","ugrabiti","oteti","kazniti","doći","hraniti","hraniti","pronaći","slušati","slušati","završiti","znati","ne znati","visok","star","dobar","slavan","jasan","budući","blizanac","nesretan","sretan","veseo","dug","velik","loš","zao","mnogi","poznat","nov","malen","pun","prvorođeni","prvi",
     "jedini","sam","sjajan","istinski","pravi","jadan","bijedan","lijep","moj","tvoj","svoj","naš","vaš"]


print(len(lat),len(hrv))
#for i in range(len(lat)):
#    if lat[i]=="":
#        print(i)
#        break




lat_copy=lat.copy()
hrv_copy=hrv.copy()

pon=[]


for i in range(len(lat)-1):
    if lat[i]==lat[i+1]:
        pon.append(lat[i])
    if hrv[i]==hrv[i+1]:
        pon.append(hrv[i])
    

bod=0
bodovi=0


import random

while 1>0:
    broj=random.randint(0,len(lat)-1)
    jezik=random.randint(1,2)




####
    if jezik==1:
        print(lat[broj])
        odg=input()
        odg=odg.lower()
        bodovi+=1
        
        if lat[broj] in pon:
            if broj!=0 and lat[broj]==lat[broj-1]:
                if odg==hrv[broj-1] or odg==hrv[broj] or odg=="fs":
                    print("Tocno!")
                    bod+=1
                    broj-=1
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
                elif odg!="stop":
                    print("Krivo, tocno je:",hrv[broj-1],",",hrv[broj])

            elif lat[broj]==lat[broj+1]:
                if odg==hrv[broj+1] or odg==hrv[broj] or odg=="fs":
                    print("Tocno!")
                    bod+=1
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
                elif odg!="stop":
                    print("Krivo, tocno je:",hrv[broj+1],",",hrv[broj])

        
        elif hrv[broj] in pon:
            if odg==hrv[broj] or odg=="fs":
                print("Tocno!")
                bod+=1
                if broj!=0 and hrv[broj]==hrv[broj-1]:
                    broj-=1
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
                else:
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
            elif odg!="stop":
                print("Krivo, tocno je:",hrv[broj])

        elif odg==hrv[broj] or odg=="fs":
            print("Tocno!")
            bod+=1
            lat.pop(broj)
            hrv.pop(broj) 

        elif odg!="stop":
            print("Krivo, tocno je:",hrv[broj])
        print()


    



#####
        
    if jezik==2:
        print(hrv[broj])
        odg=input()
        odg=odg.lower()
        bodovi+=1
        
        if hrv[broj] in pon:
            if broj!=0 and hrv[broj]==hrv[broj-1]:
                if odg==lat[broj-1] or odg==lat[broj] or odg=="fs":
                    print("Tocno!")
                    bod+=1
                    broj-=1
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
                elif odg!="stop":
                    print("Krivo, tocno je:",lat[broj-1],",",lat[broj])

            elif hrv[broj]==hrv[broj+1]:
                if odg==lat[broj+1] or odg==lat[broj] or odg=="fs":
                    print("Tocno!")
                    bod+=1
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
                elif odg!="stop":
                    print("Krivo, tocno je:",lat[broj+1],",",lat[broj])

        
        elif lat[broj] in pon:
            if odg==lat[broj] or odg=="fs":
                print("Tocno!")
                bod+=1
                if broj!=0 and lat[broj]==lat[broj-1]:
                    broj-=1
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
                else:
                    lat.pop(broj)
                    hrv.pop(broj)
                    lat.pop(broj)
                    hrv.pop(broj)
            elif odg!="stop":
                print("Krivo, tocno je:",lat[broj])

        elif odg==lat[broj] or odg=="fs":
            print("Tocno!")
            bod+=1
            lat.pop(broj)
            hrv.pop(broj)
            

        elif odg!="stop":
            print("Krivo, tocno je:",lat[broj])
        print()

###


    if odg=="stop":
        break

    if len(lat)==0:
        lat=lat_copy.copy()
        hrv=hrv_copy.copy()
    
#########
print("Score:", bod,"/",bodovi-1," --> ",round((bod/(bodovi-1)),2)*100,"%")

if (round((bod/(bodovi-1)),2)*100)<50:
    print("Jadni ti roditelji!")
if (round((bod/(bodovi-1)),2)*100)>95:
    print("GG")




    
