class matrix:

    # 2. Matrix Representation

    #2a.
    def constant(n,m,c):
        matrix=[]
        for i in range (n):
            matrixcol=[]
            for j in range (m):
                matrixcol.append(c)
            matrix.append(matrixcol)   
        return matrix        

    #2b.
    def zeros(n,m):
        matrix=constant(n,m,0.)
        return matrix
    def ones(n,m):
        matrix=constant(n,m,1.)
        return matrix

    #2c.
    def eye(n):
        matrix=[]
        for i in range (n):
            matrixcol=[]
            for j in range (n):
                if i==j:
                    matrixcol.append(1)
                else:
                    matrixcol.append(0)
            matrix.append(matrixcol)       
        return matrix  

    #3. Slicing

    #3a.
    def shape(M):
        for i in range(len(M)):
            if len(M[0])!=len(M[i]):
                return False
        return len(M),(len(M[0]))

    #3b.
    def row(M,n):
        mat=[]
        for i in range(len(M)):
            mat.append(M[i][n-1])
        return mat 
    def column(M,n):
        return M[n-1]

    #3c.
    def block(M,n_0,n_1,m_0,m_1):
        M1=[]
        for i in range(n_0-1,n_1):
            M1temp=[]
            for j in range(m_0-1,m_1):
                M1temp.append(M[i][j])
            M1.append(M1temp)    
        return M1

    #4. Matrix Operations

    #4a.
    def transpose(M):
        MT=[]
        for i in range(len(M[0])):
            MTtemp=[]
            for j in range(len(M)):
                MTtemp.append(M[j][i])
            MT.append(MTtemp)    
        return MT

    #4b.
    def scalarmul(M,c):
        MS=[]
        for i in range(len(M)):
            MStemp=[]
            for j in range(len(M[0])):
                MStemp.append((M[i][j])*c)
            MS.append(MStemp)    
        return MS

    #4c.
    def add(M,N):
        if len(M)!=len(N):
            return False
        for i in range(len(M)):
            if len(M[i])!=len(N[i]):
                return False
        MA=[]
        for i in range(len(M)):
            MAtemp=[]
            for j in range(len(M[0])):
                MAtemp.append((M[i][j])+N[i][j])
            MA.append(MAtemp)    
        return MA

    #4d.
    def sub(M,N):
        if len(M)!=len(N):
            return False
        for i in range(len(M)):
            if len(M[i])!=len(N[i]):
                return False
        MSu=[]
        for i in range(len(M)):
            MSutemp=[]
            for j in range(len(M[0])):
                MSutemp.append((M[i][j])-N[i][j])
            MSu.append(MSutemp) 
        return MSu

    #4e.
    def elementmult(M,N):
        if len(M)!=len(N):
            return False
        for i in range(len(M)):
            if len(M[i])!=len(N[i]):
                return False
        ME=[]
        for i in range(len(M)):
            MEtemp=[]
            for j in range(len(M[0])):
                MEtemp.append((M[i][j])*N[i][j])
            ME.append(MEtemp) 
        return ME

    #4f.
    def matmult(M,N):
        if len(M[0])!=len(N):
            return False
        MM=[]
        for i in range(len(M)):
            MMtemp=[]
            for j in range(len(N[0])):
                MMtemp.append(M[i][j]*N[i][j])
            MM.append(MMtemp)
        return MM

    #4g.
    def dot(A,B):
        if len(A)!=len(B):
            return False
        MD=0
        for i in range(len(A)):
            MD+=A[i]*B[i]
        return MD
    def outer(A,B):
        if len(A)!=len(B):
            return False
        MO=[]
        for i in range(len(A)):
            MOtemp=[]
            for j in range(len(B)):
                MOtemp.append((A[i])*B[j])
            MO.append(MOtemp) 
        return MO

    #5. Norms

    #5a.
    def norm(M,i):
        MN=0
        for j in range(len(M)):
            for k in range(len(M[0])):
                MN+=M[j][k]**(i)       
        MN=MN**(1./i)
        return MN

    #6. Linear Algebra

    #6a.
