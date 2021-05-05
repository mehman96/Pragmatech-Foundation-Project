# turntouppercase icinde funtion otururem
 # function return result adinda deyisenin icerisine yaziram
    #   boyuk herfe cevirmek ucun upper string metodu 
    #   newResult retun eliyirk

# 1. getname =func
# 2. getname icra eliyir return u olacaq mehman mirzeyev result icinde
# 3.string metodu upper onu eliyir olur MEHMAN MIRZEYEV
# 4. inner metodu axirda alinan neticeni yeni MEHMAN MIRZEYEV Return
# 5.print(type(decorator))=function ()-qoyulmalidi
# decorate funksiyasi neticeni gormek ucun yazmaq
def turnToUpperCase(func):
     def inner():
       result=func()
       newResult=result.upper()
       return newResult
     return inner 
     #  eger decorator  elave etmek istiyirsense @ qoy
@turnToUpperCase 
def getname():
   return 'mehman mirzeyev'
# mehman mirzeyev sozunu boyuk herfle yazir.terminalda py decorator.py

# uzunlugunu olcmek ucun decarator
# @countStringChar
def getsurname():
    return'hecimirzeyev'
# decorator=turnToUpperCase(getname)
# print(decorator())

print(getname())
# print(getsurname())

# decorator-metodun icini deyismede istifade ede bilirem

