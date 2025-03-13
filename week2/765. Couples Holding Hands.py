class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        output=0
        for i in range(len(row)-1):
            if(i%2==0): #進行查看是否要換座位?
                if(row[i]%2==1):
                    if(row[i]-1==row[i+1]): #他們是情侶
                        continue
                    else:
                        # print('1')
                        for j in range(i ,len(row)):
                            if(row[i]==row[j]+1):
                                # print('2')
                                temp=row[j]
                                row[j]=row[i+1]
                                row[i+1]=temp
                                output+=1
                                break
                if(row[i]%2==0):
                    if(row[i]+1 ==row[i+1]):
                        continue
                    else:
                        # print('3')
                        for j in range(i+1 ,len(row)):
                            if(row[i] ==row[j]-1):
                                # print('4')
                                temp=row[j]
                                row[j]=row[i+1]
                                row[i+1]=temp
                                output+=1
                                break
        # print(row)
        return output