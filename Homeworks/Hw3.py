#%%

prime_list =[]
def prime_first(i):

    if i > 1:

        for j in range (2, i):

            if (i % j) == 0:

                break
        else:

            prime_list.append(i)


def prime_second(i):

    if i > 1:

        for j in range (2, i):

            if (i % j) == 0:

                break
        else:

            prime_list.append(i)


for i in range(0,1001):

    if 0 <=i<=500:

        prime_first(i)

    else:

        prime_second(i)

print(prime_list)
# %%
