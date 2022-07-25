from bs4 import BeautifulSoup
import requests


for sayfaNo in range(1):
    url = "https://www.sahibinden.com/otomobil/erzincan"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    urunler = soup.find_all("tbody",attrs={"class":"searchResultsRowClass"})
    totalUrun = 0
    f = open("deneme.txt" ,'w')
        
    for urun in urunler:    
        try:
            currency = soup.find_all("div", {"class" : "listele table"})
            for attr in currency:
                dollar = soup.find_all("ul", {"class":"metin row"})
                result = dollar[1].getText() + " " + dollar[2].getText() + " " + dollar[3].getText() + " " + dollar[4].getText() + " " + dollar[5].getText() + " " + dollar[6].getText() + " " + dollar[7].getText() + " " + dollar[8].getText() 
                print(result)
            print("#"*60)	
        except:
           print("Hata Oluştu")


   
        
        
        #for  uru in urun:
            #print("Başlık : {} \nMarka: {} \nSeri: {} \nModel: {} \nRenk: {} \nYıl: {} \nKm: {} \nFiyat: {} \nMahalle: {}".format(ilanBaslik,marka,seri,model,renk,yil,km,fiyat,mahalle))
             
