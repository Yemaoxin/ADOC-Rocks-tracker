# convert instat info to csv
import queue
import os.path as path
import os
import re
def  get_info_2_csv(path,dir):
    fwrite=open(dir+"/iostat.csv","w")
    fwrite.write("time,read_rate,write_rate\n")
    with open(path)as fread:
        fread.seek(0,2)
        loc=fread.tell()
        fread.seek(0,0)
        time_count=0
        while (fread.tell()<loc):
            line=fread.readline()
            if ("Device" in line):
                line=fread.readline()
                time_count+=1
                stat_line =line.strip()
                read_rate=re.split(r"[ ]+",stat_line)[2]
                write_rate=re.split(r"[ ]+",stat_line)[3]
                
                fwrite.write(str(time_count)+","+read_rate+","+write_rate+"\n")
    fwrite.close()
                        
if __name__ == "__main__":
    if not path.exists("./effect_testing") :
        print(" Run your code to get results first!")
        exit(-1)
    # 广度优先遍历获取最深的路径下的所有iostat.txt
    dir_queue = queue.Queue(-1)
    os.chdir(path.abspath("./effect_testing"))
    for dir in path.os.listdir(path.abspath(".")):
        dir_queue.put(path.abspath(dir))
    while dir_queue.qsize()>0:
        dir = dir_queue.get()
        os.chdir(dir)
        for di in path.os.listdir(dir):
            if(path.isdir(di)):
                dir_queue.put(path.abspath(di))
            else:
                if( "iostat.txt" in di):
                    print(path.abspath(di))
                    get_info_2_csv(path.abspath(di),dir)
                    
                  