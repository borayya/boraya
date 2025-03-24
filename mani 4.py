def bobblesort(a):
    n=len(a)
    for i in range(n):
     for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[34,46,95,65,15,55,99]
print("before sorting:",x)
bobblesort(x);
print("after sorting:",x)

