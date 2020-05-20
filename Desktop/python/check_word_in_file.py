def wordcount(filename,listwords):
    try:
        file=open(filename,"r")
        read=file.readlines()
        file.close()
        for word in listwords:
            lower=word.lower()
            count=0
            for sentence in read:
                line=sentence.split()
                for each in line:
                    line2=each.lower()
                    line2=line2.strip("!@#$%^&*(()_+=")
                    if lower == line2:
                        count+=1
                print(lower,":",count)
    except FileNotFoundError:
        print("the file is not there")
wordcount("mo.txt",["mo"])
