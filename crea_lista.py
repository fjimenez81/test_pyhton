def CreaLista(k):
    L = []
    for i in range(k+1):
        L.append(0)
    return L

def CountingSort(A,k):
    C=CreaLista(k)
    B=CreaLista(len(A)-1)
    for j in range(1, len(A)):
        C[A[j]] = C[A[j]]+1
    for i in range(1, k+1):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1,0,-1):
        B[C[A[j]]]=A[j]
        C[A[j]]=C[A[j]]-1
    return B

lista = [0,9,7,81,4,5,68,3,541]
k = max(lista[1:])
print(CountingSort(lista, k))