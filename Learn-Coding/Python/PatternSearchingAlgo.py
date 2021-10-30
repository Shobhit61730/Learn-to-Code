'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) 
that prints all occurrences of pat[] in txt[]. You may assume that n > m. 

Examples: 

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

'''

def search(pat,txt):
    txt_list,pat_list = list(txt),list(pat)
    len_pat = len(pat_list)
    for i in range(0,len(txt_list)):
        if pat_list[0] == txt_list[i]:
            temp=txt_list[i:i+len_pat]
            if pat_list==temp:
                print("Pattern found at index: ", i)
            


if __name__ == '__main__':
    txt = "AABAACAADAABAABA"
    pat = "AABA"
    search(pat, txt)