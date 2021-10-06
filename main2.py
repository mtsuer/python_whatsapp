import pandas as pd
import numpy as np
from pandas.core.base import NoNewAttributesMixin
from pandas.core.frame import DataFrame # excel içindeki verileri okumak için kullanacağımız kütüphane
import pywhatkit as pyt #mesajları göndermek için kullanacağımız kütüphane.
#pywhatkit yerine aslında "'https://web.whatsapp.com/send?phone=' +
# phone_no + '&text=' + parsed_message" şekline gönderim yapılabirdi. zaten diğer programlama dillerini kullanacak
#olsaydım eğer bu adresi kullanırdım. Ancak hazır kütüphane varken maceraya gerek yok :)
from datetime import date, datetime #excel içinden alınacak saati parçalamak için kullanacağımız kütüphane.
import time

cols= [1,2,3,4] #satırlar seçmek için oluşturduk
df = pd.read_excel("liste.xlsx",usecols=cols) #excelden okuduğumuz verileri dataframe tipindeki nesnemize aktardık.
df.sort_values(by='VAKİT\n("Saat:Dakika" biçiminde yazınız)',inplace=True) #Saat dakika sütununa göre sıralama yaptırdık. Tabloyu görmek istedim.
df.reset_index(drop=True,inplace=True) #sort_values içerisine ignore_index=True,inplace=True yazmakta işe yarıyor
#print(df) # Tabloyu yazdırdık. Tablonun ilk hali
satir_sayim=len(df.index)#satır sayısı alındı.
col_one_arr = df['VAKİT\n("Saat:Dakika" biçiminde yazınız)'].to_numpy() # saatlerin olduğu sütün array şeklinde alındı.
col_one_arr.sort() #Küçükten büyüğe sıralama yaptık

now = datetime.now().time() # Şimdiki saatimizi aldık.
for say,x in enumerate(col_one_arr): # enumerate ile array listemizi indexliyoruz.     
    if x>now: #arraydan alınan saat eğer şuanki saatden büyükse eğer döngüdeki index numarası alınacak ve for duracak.
        kes=say
        break  
df=df.append(df.head(kes)) #listemize yukarıdan itibaren kesme işlemi uygulayacağımız satıra kadarki bölümü, listemizin sonuna ekliyoruz.
df.reset_index(drop=True,inplace=True)#indeximizi sıfırladık.
df = df.drop(df.index[0:kes])#sonra ise başdaki eklenenn bölümü sildik.
df.reset_index(drop=True,inplace=True)#indeximizi tekrar sıfırladık.
#buradaki amacımız programı 24 saat mantığı ile çalıştırmak.

print(df)#tablomuzun son hali
for y in range(len(df)): #1. döngümüz satırları döndürmek amaçlı oluşturuldu. "range(len(df))"" sıralı şekilde gitmesi için özellikle kullanıldı
    x=0 #Kendisi sütunların index numarasını almak için kullanacağımız değişkenimiz olur. 
    #En başa konulmasının özel debebi döngü her başa döndüğünde sıfırlanması için konuldu.
    for i in df.iloc[y]: # sütunlardaki verileri almak için oluşturduğumuz for döngümüz.
        x+=1 # sütun index numarasını sayıyor.
        if x == 2: #özellikle birinci sütunu atladım. Çünki excel içindeki isim sütunu benim işime yaramıyor.
            i = "+" + str(i)
            telefon_numarasi = i  #telefon numaramızı aldık
        elif x == 3:
            saat_dakika = i #saat dakika bir datetime tipinde olduğu için şimdilik bütün haline alındı.
        elif x == 4:
            mesajim=i #mesajı aldık.
    
            #print() #Satırlardaki okumalar doğrumu diye kontrol amaçlı oluşturduğum printler.
            #print(f"+{int(telefon_numarasi)}")
            #print(mesajim)
            #print(saat_dakika)

            now = saat_dakika # excel içinden alınan datetime tipindeki değeri aktarıyoruz. 
            #aslında now değişkenine gerek yoktu ancak bozmak istemedim.
            saat = now.strftime("%H") # Saati aldık
            dakika = now.strftime("%M") # Dakikayı aldık
            #now2 = time.strftime(r"%H:%M", time.localtime()) #datetime.time str olarak oluştu.
            #now2 = datetime.strptime(now2, '%H:%M').time() #burda ise datetime.time nesnesine dönüştürüyoruz.
               
            now = datetime.now().time() # excel içinden alınan datetime tipindeki değeri aktarıyoruz. 
            #buranın püf noktası .time() fonksiyonu!!!
            #aslında now değişkenine gerek yoktu ancak bozmak istemedim.
            s_saat = now.strftime("%H") # Saati aldık
            s_dakika = now.strftime("%M") # Dakikayı aldık
            s_dakika =  int(s_dakika)+1 #bir dakikayı kasten ekledim. pywhatkit sorun çıkardı.
            
            #print("saat dakika", type(saat_dakika))
            #print("now ", type(now))    

            if(str(telefon_numarasi)=="") and (str(mesajim)=="") and (str(saat)=="") and (str(saat_dakika)==""):
                #Sütunlardan herhangi birisinin boş olmasına karşılık önlem alındı.
                print("Lütfen tüm sütunları doldurunuz!!!!")
            else:            
                #print(str(saat_dakika)+":///// "+str(now))
                print(str(now)+" "+str(telefon_numarasi)+" numaralı telefona '"+ str(mesajim)+ "' içerikli mesajınız "+ str(saat)+":"+str(dakika)+" saatinde gönderilecektir.")                           
                pyt.sendwhatmsg("+" + str(telefon_numarasi),str(mesajim),int(saat),int(dakika),20) # final bölümümüz .
            
"""  
    
    Kaynaklar:
https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
https://veribilimcisi.com/2017/07/14/pandasa-hizli-baslangic/
https://www.cagrigungor.com/python-pandas-excel-ve-csv-okuma-acma/
https://xlsxwriter.readthedocs.io/working_with_pandas.html
https://www.datacamp.com/community/tutorials/python-select-columns
https://pypi.org/project/pywhatkit/
https://python-ogren.readthedocs.io/en/latest/for_loops.html
https://stackoverflow.com/questions/14295673/convert-string-into-datetime-time-object
https://stackoverflow.com/questions/25015711/time-data-does-not-match-format
https://www.journaldev.com/23365/python-string-to-datetime-strptime
https://www.reddit.com/r/learnpython/comments/ibhjlu/typeerror_not_supported_between_instances_of_str/
https://www.programiz.com/python-programming/datetime/strftime
https://stackoverflow.com/questions/30214693/python-generate-a-date-time-string-that-i-can-use-in-for-mysqlhttps://www.shanelynn.ie/pandas-drop-delete-dataframe-rows-columns/
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
https://stackoverflow.com/questions/33165734/update-index-after-sorting-data-frame
https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
https://www.geeksforgeeks.org/pandas-how-to-reset-index-in-a-given-dataframe/
https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column-or-row
    """