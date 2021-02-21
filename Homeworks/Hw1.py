
# %%  Girilen aralıkta mevcut asal sayılardan istenen boyuttaki n*n matrise rastgele yazan program

lower = int(input("Alt Değeri Giriniz: "))  
upper = int(input("Üst Değeri Giriniz: "))  
dim = int(input("Kare Matrisin Boyutunu Giriniz: "))
prime_list=[]
  
for prime in range(lower,upper + 1):  
   if prime > 1:  
       for i in range(2,prime):  
           if (prime % i) == 0:  
               break  
       else:  
           prime_list.append(prime) #programa girilen aralıktaki tüm asal sayıların listesi
# %%
import random
primelist_index = []
choices = list(range(len(prime_list))) 
random.shuffle(choices)
i=0
while i<dim**2:
    primelist_index.append(choices[i]) #tüm asal sayılardan rastgele seçilecek n*n adet asal sayının ana listedeki index değerleri
    i=i+1
# %%
i=0
j=0
selected_primes = []

for i in range(len(primelist_index)):
    selected_primes.append(prime_list[primelist_index[i]]) # tüm asal sayılar içinden n*n adet rastgele asal sayıdan oluşan liste
#%%
mat = [[0]* dim for i in range(dim)]
i=0
j=0
k=0
for i in range(dim):
    for j in range(dim):
        mat[i][j]=selected_primes[k]   #n*n adet asal sayının n*n boyutlu matrise yazdırılması
        k=k+1
for row in mat:
    print(' '.join([str(elem) for elem in row]))  #oluşturulan n*n boyutlu matrisin ekrana yazdırılması

# %%
