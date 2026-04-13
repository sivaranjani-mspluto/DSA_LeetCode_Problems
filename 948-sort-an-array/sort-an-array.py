class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,L,R,M):
            lefta,righta=arr[L:M+1],arr[M+1:R+1]

            i,j,k=0,0,L
            while i<len(lefta) and j<len(righta):
                if lefta[i]<righta[j]:
                    arr[k]=lefta[i]
                    i+=1
                else:
                    arr[k]=righta[j]
                    j+=1
                k+=1
            while i<len(lefta):
                arr[k]=lefta[i]
                i+=1
                k+=1
            while j<len(righta):
                arr[k]=righta[j]
                j+=1
                k+=1
    
        def mergeSort(arr,l,r):
            if l==r: #single ele
                return arr
            m=(l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,r,m)
            return arr
        
        return mergeSort(nums,0,len(nums)-1)