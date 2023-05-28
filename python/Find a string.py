def count_substring(string, sub_string):
    count=0
    ls=len(string)
    lss=len(sub_string)
    for i in range(0,ls-lss+1):
        if string[i:i+lss]==sub_string:
            count+=1
    return count