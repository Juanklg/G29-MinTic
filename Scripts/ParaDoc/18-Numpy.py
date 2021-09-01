print("Numpy".center(60,'-'))
    m1 = np.array([1,2,3])    
    print(m1)
    fn.detailVar(m1)
    print(m1.shape)
    print(m1[1])
    print("Vectores para rango 2".center(60,'-'))
    v1=list(range(4))
    v2=[1,2,3,4]
    v3=[5,6,7,8]
    v4=[9,0,7,6]

    m2 = np.array([v1,v2,v3,v4])
    print(m2,m2.shape)
    print(m2[3,1])

    print("Matrices automaticas".center(60,'-'))
    mOnes = np.ones((7,7))
    mZero = np.zeros((7,7))
    mFull = np.full((7,7),7)
    mRandom = np.random.random((3,3))
    mIdentidad = np.eye(7)    
    print(mIdentidad)
    print(np.fliplr(mIdentidad))

    print("Rebanadas".center(60,'-'))    
    print(m2)
    rebanada = m2[1:3,1:3]
    print(rebanada)
    print(rebanada[0,1])
    rebanada[0,1]+=9
    print(rebanada)
    print("Matriz general".center(60,'-'))    
    print(m2)

    print("Indexacion filas".center(60,'-'))
    row1=m2[1,:]
    row2=m2[1:2,:]
    print(row1,row1.shape)
    print(row2,row1.shape)

    print("Indexacion columnas".center(60,'-'))
    col1=m2[:,2]
    col2=m2[:,2:3]
    print(col1,col1.shape)
    print(col2,col2.shape)

    print("Indexacion por numeros enteros".center(60,'-'))
    print(m2)    
    y=[0,1,3,3]
    x=[0,2,3,0]
    print(m2[y,x])

    print("Indexacion por numeros enteros juntos".center(60,'-'))
    print(m2)    
    y=[0,1,3,3]
    x=[0,2,3,0]
    print([m2[0,0],m2[1,2],m2[3,3],m2[3,0]])
    print(m2[[0,0],[1,2]])

    print("Indexacion truco".center(60,'-'))
    print(m2,m2.shape)
    #creamos un vector
    b=np.array([0,2,0,1])
    c=np.arange(4)
    print(b,b.shape)
    print(c,c.shape)
    m4 = m2[c,b]
    print(m4,m4.shape)
    m2[c,b]+=10
    print(m2)

    print("Indexacion Bool".center(60,'-'))
    print(m2)
    boolIndex = (m2>5)
    print(boolIndex)

    print(m2[boolIndex])

    print(m2[m2<2])

    print("Operaciones entre Matrices".center(60,'-'))
    x=np.array([[1,2],[3,4]],dtype=np.float64)
    y=np.array([[5,6],[7,8]],dtype=np.float64)
    print(x)
    print(y)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)

    print("Producto punto".center(60,'-'))
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])
    v = np.array([9,10])
    w = np.array([11,12])

    print(x)
    print(y)
    print(v)
    print(w)

    print(v.dot(w))
    print(np.dot(v,w))

    print(x.dot(v))
    print(np.dot(x,v))

    print(x.dot(y))
    print(np.dot(x,y))

    print("Sum".center(60,'-'))
    x = np.array([[1,2],[3,4]])    
    print(np.sum(x))
    print(np.sum(x,axis=0))
    print(np.sum(x,axis=1))

    print("Trasnpuesta".center(60,'-'))
    print(m2)
    print(m2.T)

    print("Broadcasting".center(60,'-'))
    print(m2)
    v = np.array([0,1,1,2])
    vv = np.tile(v,(4,1))
    print(vv)
    print(vv+m2)