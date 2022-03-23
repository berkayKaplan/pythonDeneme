# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("---baseCalculator---")
print("Hoşgeldiniz lütfen işlem yapılacak 2 sayı giriniz")
s1=int(input("1.sayıyı giriniz:"))
s2=int(input("2.sayıyı giriniz:"))
print("--------------")
print("Sayılarınız toplamı",s1 + s2)
print("Sayılarınız çarpımı",s1 * s2)
print("Sayılarınız farkı",s1 - s2)
print("Sayılarınız bölümü",s1 / s2)
print("---baseWalcome---")
a=input("İsminizi Giriniz: ")
print(a,"Hoşgeldiniz")
print("---basenote")
Vize=int(input("Vize notunu giriniz:"))
Final=int(input("final notunuzu giriniz:"))
ort=Vize*0.4+Final*0.6
print("Ders notunuz :",format(ort))
print("---basegoortbad---")
Vize=int(input("Vize notunu giriniz:"))
Final=int(input("final notunuzu giriniz:"))
ort=Vize*0.4+Final*0.6
if(ort>=50):
    print("Ders notunuz:",format(ort)+"-dersten geçtin")
else:
        print("Ders notunuz:",format(ort)+"-Dersten kaldın")
        
print("---tekorçift---")
print("Sayı giriniz:")
a=int(input("Sayı giriniz"))
if(a%2==0):
    print("girdiğiniz sayı çifttir")
else:
    print("girdiğiniz sayı tektir")
print("---sayı girmmeme---")
a=input("İsminizi Giriniz: ")
if(a%2==0):
     print("girdiğiniz değer sayıdır...")
else:
    print(a,"Hoşgeldiniz")
        
    

        
        
    
