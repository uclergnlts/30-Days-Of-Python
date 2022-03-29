import math


print("Hello Word!")

print(3 + 4); #7
print(3 - 4); #-1
print(3 * 4); #12
print(3 % 4); #3
print(3 / 4); #0.75
print(3 ** 4); #81
print(3 // 4); #0

print("Üçler") 
print("Soyadın") 
print("Ankara")  
print("Ben 30 Günde Python öğreniyorum")

print(type(10))  #int
print(type(9.8)) #float
print(type(3.14)) #float
print(type(4-4j)) #complex
print(type(["Asabeneh","Python","Finland"])) #list
print(type("Adın")) #str
print(type("Soyadın")) #str
print(type("Ülken")) #str


print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex number
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


#Öklit Uzaklığı Hesaplama
x = 2
y = 3
a = 10
b = 8

t = x - y
z = a - b

#math.sqrt özelliği bir sayının karaköküünü almamıza yarıyor.
oklit = (t * t) + (z * z)
print(math.sqrt(oklit)) #2.23606