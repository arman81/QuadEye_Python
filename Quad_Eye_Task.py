import numpy as np
import pandas as pd
import os
class DB():
    df = pd.DataFrame(np.nan, index=[], columns=[])
    seq = 0
    st = [] 
    len = 0
    def _init_(self,fName):
        self.seq = 0
    def getIndex(self):
        if self.len == 0 :
            self.seq = self.seq + 1
            return self.seq-1
        else :
            ret = self.st[self.len-1]
            self.len = self.len-1
            self.st.pop();
            return ret
    def addIndex(self,val):
        self.st.appen(val);
    def create(self,stri):
        data = stri.split(" ")
        for temp in data:
            self.df[temp] = self.df.index; #inserting column
 
    def add(self,stri): #adding row
        ii = self.getIndex()
        li = []
        data = stri.split(" ")
        for temp in data:
            li.append(temp)
        self.df.loc[ii] = li
 
    def search(self,stri):
        data = stri.split(" ")
        f = False
        f2 = False
        col_name = ""
        some_value = ""
        for temp in data:          
            if f2 == True :
                f2 = False
                some_value = temp
            if f == True:
                f = False
                col_name = temp
            if(temp == 'where'):
                f = True
            if(temp == '=='):
                f2 = True
        print self.df.loc[self.df[col_name] == some_value]
        l = len(self.df.loc[self.df[col_name] == some_value].index)
        if l > 0: return l
        else : return False
    def delete(self,stri):
        data = stri.split(" ")
        f = False
        f2 = False
        col_name = ""
        some_value = ""
        for temp in data:          
            if f2 == True :
                f2 = False
                some_value = temp
            if f == True:
                f = False
                col_name = temp
            if(temp == 'where'):
                f = True
            if(temp == '=='):
                f2 = True
        #print self.df.loc[self.df[col_name] == some_value]
        l = len(self.df.loc[self.df[col_name] == some_value].index)
        if(l == 0): print "There is not a single tuple matching those parameter"
        else: del self.df.loc[self.df[col_name] == some_value]
 
if __name__ == "__main__":
    obj = DB();
    print (obj.df)
    print "Enter the attribute list: "
    col = raw_input()
    print col
    #col = "A B C D"
    obj.create(col) # here column works as a attribute list
    print (obj.df)
    print "Enter no of tuple to add in table :"
    noOfTuple = input()
    cur = 0
    while(noOfTuple > cur):
    	stri = raw_input()
    	obj.add(stri)
        #obj.add("F D G H")
	    #obj.add("F D G H")
	    #obj.add("I 3 1 H")
	    #obj.add("J 8 2 H")
	    #obj.add("L 5 3 H")
	    #obj.add("K S 4 H")
	    #obj.add("H F 5 H")
	    #obj.add("T B 6 H")
	    #obj.add("R S 7 H")
	    #obj.add("X Z 8 H")
	    cur = cur + 1
    print "After adding all tuple table content: "	
    print (obj.df)
    print "Enter search query"
    #seq = "select * from tane where B == 3"
    seq = raw_input()
    obj.search(seq)
    #base_filename = 'Values.txt'
    #with open(os.path.join(WorkingFolder, base_filename),'w') as outfile:
     #   pd.to_string(outfile)
    filename = "F:/Task/in.txt"
    file = open(filename, "w")
    stri = col.split(" ")
    for index, row in obj.df.iterrows() :
       for temp in stri :
           file.write(row[temp])
           file.write(" ")
       file.write("\n")
    file.close()
    obj.df.drop(obj.df.index, inplace=True)
    #obj.df = obj.df.drop
    os.remove(filename)
    print "Deletion complete"
    #os.remove(obj.df)
    #np.savetxt(r'C:\Users\hp\Desktop\todaya\np.txt',obj.df.values, fmt='%d')
    #"fileName.txt"
 