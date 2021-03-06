class Vector:
    def __init__(self, d):
        if (type(d) == int):
            self.coords = [0]*d
        else:
            self.coords = d
        
    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val
        
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self==other)
    
    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
    
    def __repr__(self):
        return str(self)
    
    def __neg__ (self):
        newVec = Vector(self.coords[:])
        for i in range(len(self.coords)):
            newVec.coords[i] *= (-1)
        return newVec
    
    def __sub__(self, other):
        self.coords + __neg__(other)
        return self.coords

    def __mul__(self,n):
        newVec = Vector(self.coords[:])
        tot = 0
        if type(n)==int:
            for i in range(len(newVec.coords)):
                newVec.coords[i] *= n
            return newVec
        elif type(n) == Vector:
            Vec2 = Vector(len(self))
            for x in range(len(self)):
                newVec[x] = self.coords[x]*n.coords[x]
                tot = newVec[x]+tot
            return tot

    def __rmul__(self, n):
        return self*n

    
def main():
    v1 = Vector(5)
    v1[1]=10
    v1[-1]=10
    print(v1)

    v2 = Vector([2,4,6,8,10])
    print(v2)

    u1 = v1+v2
    print(u1)

    u2 = -v2
    print(u2)

    u3 = v2 * 3
    print(u3)

    u4 = 3 * v2
    print(u4)

    u5 = v1 * v2
    print(u5)
    

    
main()
    
