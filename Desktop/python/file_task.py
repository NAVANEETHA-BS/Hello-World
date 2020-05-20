import re,os,sys
def main(infilename,outfilename):
    if not os.path.exists(infilename):
        print("ERROR. input file does not exist")
        sys.exist()
    with open(infilename,'r') as infile:
        lines=infile.readlines()
    pattern = re.compile(r'^(.+ +.+)$')
    with open(outfilename,'w')as outfile:
        for line in lines:
            match=re.match(pattern,line)
            if match:
                newline=re.sub(pattern,r'"\g<1>"',line)
                outfile.write(newline)
            #else:
                #outfile.write(line)


if __name__=="__main__":
    if not len(sys.argv)==3:
        print("usage:{} input_file output_file".format(sys.argv[0]))
        main(sys.argv[1],sys.argv[2])
                         

