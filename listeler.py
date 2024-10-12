#pythonda listenin herhangi bir yerine eleman eklemek için insert() kullanılır
#pythonda listenin sonuna eleman eklemek için append() kullanılır
list=[1,2,"zorbey",5]
list.insert(1,"ahmet") #1den sonra ahmet yazıcak sonra 2 yazcak
print(list)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#pythonda 2 listeyi birleştrimek için extend() kullanılır (+= de bu görevi görmektedir)
#1.yönetm
liste=["ahmet",1,6,8,98,4]
yeniliste=["mehmet",32,123,43]
liste.extend(yeniliste)
print(liste)

#2. yöntem
liste=["ahmet",1,6,8,98,4]
yeniliste=["mehmet",32,123,43]
liste+=yeniliste
print(liste)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#listeden eleman silmek için remove() kullanılır aynı veriden 2 tane varsa her zaman önce geleni siler elemanı silmek için eleman değeri aynen yazılır
#listede silinen bir eleamnın değerini yazdırmak için pop() kullanılır
liste=["ahmet",1,6,8,98,4]
liste.remove(8)
print(liste) #8silindi
liste.pop()
print(liste)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#listede elemanın hangi sırada olduğunu görmek için index() kullanılır
liste=["ahmet",1,6,8,98,4]
print(liste.index(6))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#listedeki elemanları alfabetik olarak sıralamak için sort() kullanılır
#listedeki elamnaların sırasını tersine çevirmek için reverse kullanılır
liste=["ahmet",1,6,8,98,4]
liste.sort()
liste.reverse()
print(liste)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#bir listenin içerisinde herhangi bir elemanın liste içerisinde kaç defa kullandığını görmek için count() kullanılır
liste=["ahmet",1,6,8,98,4,1,6,6]
print(liste.count(1))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#listede istediğimiz yere istediğimiz kadar eleman eklemek için : kulllanılır ancak köşeli parantezlerle birlikte olmak şartıyla birinci parametre eklenecek index numarasını 2.parametre ise eklenecek elemandan sonra kaç adet eleman silineceğini belirtir
#aşağıda listenin sıfırıncı index numarasına 4 eleman eklenmiştir ve eklenecek index numarasından itibaren listede olan 1 değer silinmiştir
liste=["ahmet",1,6,8,98,4]
liste[0:1]=["can","furkan",55,33]
#1.parametre:sırayı, 2.parametre ise silinecek eleman sayısını gösterir
print(liste)


#listedeki herhangi bir elemanı silmek için o elemana ait ayırt edici özellik olan anahtar ifadesini "del" komutu ile birlikte kullanırız
telefon={"ahmet":"0545 453 63 76","salih":"0578 879 89 07"} 
del telefon["ahmet"] #ahmet anahtarı ve değeri varsa silinir
print(telefon)
