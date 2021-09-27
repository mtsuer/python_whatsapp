import pandas as pd # excel içindeki verileri okumak için kullanacağımız kütüphane
import pywhatkit as pyt #mesajları göndermek için kullanacağımız kütüphane.
#pywhatkit yerine aslında "'https://web.whatsapp.com/send?phone=' +
# phone_no + '&text=' + parsed_message" şekline gönderim yapılabirdi. zaten diğer programlama dillerini kullanacak
#olsaydım eğer bu adresi kullanırdım. Ancak hazır kütüphane varken maceraya gerek yok :)
from datetime import datetime #excel içinden alınacak saati parçalamak için kullanacağımız kütüphane.



cols= [1,2,3,4] #satırlar seçmek için oluşturduk

df = pd.read_excel("liste.xlsx",usecols=cols) #excelden okuduğumuz verileri dataframe tipindeki nesnemize aktardık.
df.sort_values(by='VAKİT\n("Saat:Dakika" biçiminde yazınız)',inplace=True) #Saat dakika sütununa göre sıralama yaptırdık. Tabloyu görmek istedim.
print(df) # Tabloyu yazdırdık.



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
            
    
            print() #Satırlardaki okumalar doğrumu diye kontrol amaçlı oluşturduğum printler.
            print(f"+{int(telefon_numarasi)}")
            print(mesajim)
            print(saat_dakika)

            now = saat_dakika # excel içinden alınan datetime tipindeki değeri aktarıyoruz. 
            #aslında now değişkenine gerek yoktu ancak bozmak istemedim.
            saat = now.strftime("%H") # Saati aldık
            dakika = now.strftime("%M") # Dakikayı aldık
            
            
            now = datetime.now() # excel içinden alınan datetime tipindeki değeri aktarıyoruz. 
            #aslında now değişkenine gerek yoktu ancak bozmak istemedim.
            s_saat = now.strftime("%H") # Saati aldık
            s_dakika = now.strftime("%M") # Dakikayı aldık
            s_dakika =  int(s_dakika)+1 #bir dakikayı kasten ekledim. pywhatkit sorun çıkardı.

            if(str(telefon_numarasi)=="") and (str(mesajim)=="") and (str(saat)=="") and (str(saat_dakika)==""):
                #Sütunlardan herhangi birisinin boş olmasına karşılık önlem alındı.
                print("Lütfen tüm sütunları doldurunuz!!!!")
            else:              
                if (int(s_saat) >= int(saat)):
                    if(int(s_dakika)>=int(dakika)):
                        print("Dakika olarak geç kaldı.")
                    else:                    
                        pyt.sendwhatmsg("+" + str(telefon_numarasi),str(mesajim),int(saat),int(dakika),20) # final bölümümüz .
                else:
                    print("Saat olarak geç kaldı.")

    """"
    Kaynaklar:
https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
https://veribilimcisi.com/2017/07/14/pandasa-hizli-baslangic/
https://www.cagrigungor.com/python-pandas-excel-ve-csv-okuma-acma/
https://xlsxwriter.readthedocs.io/working_with_pandas.html
https://www.datacamp.com/community/tutorials/python-select-columns
https://pypi.org/project/pywhatkit/
https://python-ogren.readthedocs.io/en/latest/for_loops.html
    """