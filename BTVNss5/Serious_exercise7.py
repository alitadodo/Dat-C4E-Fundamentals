def remove_dollar_sign(s):
    remove = s.replace("$","")
    return remove
text ="You can 1 $"
print(remove_dollar_sign(text))