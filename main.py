import sys
from dateutil.utils import today

from service.ExportService import export_to_excel
from service.searchingService import find_files


baseDir = sys.argv[1]
exportFileName = sys.argv[2] if (len(sys.argv) > 2) else "duplicates_" + today().strftime("%d-%m-%Y") + ".xlsx"
print(exportFileName)

filesInfo = find_files(baseDir)

duplicatedFiles = []
repeated = []
for i in range(0, len(filesInfo)):
    ext = filesInfo[i]
    for j in range(i+1, len(filesInfo)):
        int = filesInfo[j]
        hash = ext.hash
        if hash == int.hash:
            repeated.append(int)
            repeated.append(ext)
            print(f"{i},{j}\t {ext.path}\t {ext.hash}\t {int.hash}\t {int.path}")



#for l in duplicatedFiles:
#    print(l)

export_to_excel(repeated, exportFileName)

sum = 0
for file in repeated:
    print(file.size)
    sum = sum + file.size

sum = (sum/(1024*1024*1024))
print(f"Total duplicates file size:  {sum}Gb")


