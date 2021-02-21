#%%

num_st = int(input("Öğrenci Sayısını Giriniz : "))
name_st = []
mid_st =[]
fin_st = []
hw_st = []

for i in range(num_st):
    name_st.append(input("Öğrencinin adını ve soyadını giriniz: "))
    mid_st.append(int(input("Öğrencinin Vize Notunu Giriniz: ")))
    fin_st.append(int(input("Öğrencinin Final Notunu Giriniz: ")))
    hw_st.append(int(input("Öğrencinin Ödev Notunu Giriniz")))
#%%

i=0
grd_st =[]
for i in range(num_st):
    grd_st.append(0.25*mid_st[i]+0.50*fin_st[i]+0.25*hw_st[i])

# %%

data_st ={}
i=0

for i in range(num_st):
    data_st[grd_st[i]] = name_st[i]


# %%

sorted_data_st=sorted(data_st.items(), reverse=True)
#%%
print ("En Yüksek Not   Öğrenci Adı")
print (sorted_data_st[0])
# %%
