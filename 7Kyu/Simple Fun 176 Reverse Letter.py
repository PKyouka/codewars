def reverse_letter(st):
    for i in st:
        if i.isalpha() == False:
            st = st.replace(i, '')
    return st[::-1]