import operator
import csv
tmpFilePath = r"D:\ProjectsInGitHub\AWS_Tutorial\pratice\tmp.txt"
with open(tmpFilePath,'r',newline="\r\n") as f:
    reader = csv.reader(f,delimiter=',')
    result = sorted(reader, key=operator.itemgetter(0))
print(result)