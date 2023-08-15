import os 



files = os.listdir("folder")
i=1
for file in files:
    if file.endswith(".png"):   #print onl yfiles which ends with .png 
        print(file)  #prints all the files in the folder 
        os.rename(f"folder/{file}","folder/{i}.txt") #to rename all the files which ends with .txt 
        i +=1 
