import numpy as np
def calculate_avg_ic(period,filename):
        freq_period = [0]*26
        sum_freq =0
        N = len(filename)-1
        for n in range(1,period):
                val = n
                for i in range(0,len(filename)//period):
                        num = ord(filename[val]) - ord('A')
                        if num >= 0 and num <= 25:
                                freq_period[num] = freq_period[num] + 1
                        val=val+period 
                temp =0
                for al in range(0,26):
                        temp = temp + (freq_period[al]*(freq_period[al]-1))
                temp = temp/(N*(N-1))
                sum_freq = sum_freq + temp
        sum_freq = sum_freq / period
        return sum_freq

def calculate_chi(key,filename):
        # Complete chi square statistic

def main():
        file_decr = open('vigenere-text.txt').read()
        n = len(file_decr)-1
        period_num = 10
        ic_avg = [0 for i in range(period_num+1)]
        for i in range(1,period_num+1):
                ic_for_i = calculate_avg_ic(i,file_decr)
                ic_avg[i] = ic_for_i
        arr = np.array(ic_avg)
        arr = np.argpartition(arr, -4)[-4:]
        arr = sorted(arr.tolist())
        key = arr[0]

        
        
main()


        


