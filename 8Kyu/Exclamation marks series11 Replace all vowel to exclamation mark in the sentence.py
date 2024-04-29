def replace_exclamation(st):
    for i in "aeiouAEIOU":
        st = st.replace(i, "!")
    return st