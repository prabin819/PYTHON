with open("old.txt","r") as f:
    content = f.read()


with open("old_renamed.txt","w") as f:
    f.write(content)