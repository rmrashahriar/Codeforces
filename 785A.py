poly_names = ['Tetrahedron', 'Cube', 'Octahedron', 'Dodecahedron', 'Icosahedron']
poly_vales = [4, 6, 8, 12, 20]

n = int(input())

count = 0

for x in range(n):
    inp = input()
    id = poly_names.index(inp)
    count = count + poly_vales[id]
    
print(count)