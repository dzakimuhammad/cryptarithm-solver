# NAMA : DZAKI MUHAMMAD
# NIM : 13519049
# KELAS : K-1
# DESKRIPSI : TUGAS KECIL 1 STRATEGI ALGORITMA

# PENYELESAIAN CRYPTARITHMETIC DENGAN ALGORITMA BRUTE FORCE

# FUNGSI DAN PROSEDUR

# fungsi permutasi dari array bilangan 0-9
def permutate(num_array):
    perm_result = []
    length=len(num_array)
    if length <= 1:
        return [num_array]
    else:
        for i in range(length):
             for p in permutate(num_array[:i] + num_array[i+1:]):
                 perm_result.append([num_array[i]] + p)
        return perm_result

# fungsi konversi kata menjadi bilangan
def word_to_int(num_array, let_array, word_array):
    int_array = []
    for word in word_array:
        int_string = ""
        for char in word :
            i = 0
            while let_array[i] != "?":
                if char == let_array[i] :
                    int_string += str(num_array[i])
                i += 1
                if i ==10:
                    break
        int_array.append(int(int_string))
    return int_array

# fungsi memeriksa apakah kondisi huruf pertama terpenuhi
def firstlet_check(firstlet_array, num_array, let_array):
    i=0
    while let_array[i] != "?":
        if let_array[i] in firstlet_array and num_array[i] == 0:
            return False
        i+=1
        if i==10:
            break
    return True


def solve(num_array, let_array, word_array, firstlet_array):
    valid = False
    test_sum = 0
    perm_num = permutate(num_array)
    for arr in perm_num:
        test_sum +=1
        if firstlet_check(firstlet_array, arr, let_array): 
            int_arr = word_to_int(arr, let_array, word_array)
            length = len(int_arr)
            sums = 0
            result = int_arr[length-1]
            for i in range(length-1):
                sums += int_arr[i]
            if sums == result :
                valid = True
                break
        
    if valid :
        print("\nPERSOALAN :")
        i = 0
        while(i!=length-2):
            print(word_array[i])
            i+=1
        print(word_array[i] +"+")
        print("------")
        print(word_array[length-1])

        print("\n")
        print("SOLUSI :")
        i = 0
        while(i!=length-2):
            print(int_arr[i])
            i+=1
        print(str(int_arr[i]) +"+")
        print("------")
        print(int_arr[length-1])
    
    else:
        print("persoalan tidak dapat diselesaikan") 
    
    print("\n")
    print("waktu eksekusi program : %s detik" % (time.time() - start_time))
    print('total tes yang dilakukan : %s tes' %(test_sum))


# PROGRAM UTAMA
import time

nama_file = input("Masukkan nama file yang akan dibaca : ")     #input nama file
text = open(nama_file,'r')     #membuka file dan merekamnya dalam variabel arsip
start_time = time.time()
lines = text.readlines()

# inisialisasi array
arr_word = []
arr_firstlet = []
arr_letter = ['?' for i in range(10)]
arr_num = [1,2,3,4,5,6,7,8,9,0]

# menyimpan kata-kata yang dibaca ke dalam sebuah array
for line in lines : 
    line = line[:-1]    #untuk menghilangkan newline di akhir string
    if line != "------" :
        length = len(line)
        if line[length-1] == "+":
            line = line[:-1]    #menghilangkan tanda "+"
        arr_word.append(line)

# mengisi array huruf 
list_of_char =[]
for word in arr_word:
    i=0
    for char in word:
        if i==0:
            arr_firstlet.append(char)
        if char not in list_of_char :
            list_of_char.append(char)
        i+=1

for i in range (len(list_of_char)) :
    arr_letter[i] = list_of_char[i]

# menyelesaikan persoalan
solve(arr_num, arr_letter, arr_word, arr_firstlet)
