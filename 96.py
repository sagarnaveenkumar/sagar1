def wrapper(f):
    def fun(l):
        lst = []
        for no in l:
            phone_num = no[::-1][:10][::-1]
            correct_format_num = "+91" + " " + phone_num[:5] + " " + phone_num[5:]
            lst.append(correct_format_num)
        f(lst)
            
    return fun
