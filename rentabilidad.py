from aulas import projeto
arq = 'producto.txt'
arq1 = 'rentabilidad.txt'
if projeto.abrir(arq) == True:
    print('Arquivo encontrado')
else:
    projeto.criar(arq)
    projeto.criar(arq1)
projeto.linha()
codigos=[1,2,3,4]
m = 0

# Ciclo de repetición que confirma si el código inserido está programado
while True:
    projeto.cabecalho('Menú')
    print('''
    [1] - Mostrar lista de productos
    [2] - Cadastrar nuevo producto y calcular precio de costo
    [3] - Calcular y cadstrar rentabilidad
    [3] - Salir''')
    projeto.linha()
    m = input('Insira un código válido: ')
    if m.isnumeric():
        m = int(m)
    while m not in codigos:
        m = input('ERROR, Insira un código válido: ')
        if m.isnumeric():
            m = int(m)


    # Opción 1
    if m == 1:
        projeto.cabecalho('OPCIÓN 1')
        projeto.lerarquivop(arq)
        print()
        projeto.lerarquivop(arq1)
        print()
    #Opción 2
    if m == 2:
        projeto.cabecalho('Opción 2')
        n = 1
        prod = dict()
        productos = []
        while True:
            while True:
                p = input(f'Nombre del producto {n}: ')
                if p.isalpha():
                    break
            prod['nome'] = p

            while True:
                q = input(f'Precio del producto {n}: ')
                if q.isnumeric():
                    break
            q = float(q)
            prod['precio'] = q

            while True:
                r = input(f'Cantidad del producto[g/cc] {n}: ')
                if r.isnumeric():
                    break
            r = float(r)
            prod['cantidad'] = r

            while True:
                s = input(f'Cantidad del producto {n} utilizada en la receta[g]: ')
                if s.isnumeric():
                    break
            s = float(s)
            prod['cantidad utilizada'] = s

            preciocos = (prod["cantidad utilizada"] * prod["precio"])/prod["cantidad"]
            prod['precio de costo'] = preciocos
            productos.append(prod.copy())
            prod.clear()
            n += 1
            t = input('Vos querés agregar más productos[S/N] ?').strip().upper()[0]
            while t not in 'SN':
                t = input('Vos querés agregar más productos[S/N] ?').strip().upper()[0]
            if t == 'N':
                break
        projeto.cadastrarp(arq, productos)

    if m == 3:
        dat = dict()
        datos = []
        while True:
            a = input('Nombre del producto: ')
            if a.isalpha():
                break
        dat['nombre'] = a
        while True:
            b = input(f'Precio de costo del producto: ')
            if b.isnumeric():
                break
        b = float(b)
        dat['costo'] = b
        while True:
            c = input(f'Meta de renta a ser atingida: ')
            if c.isnumeric():
                break
        c = float(c)
        dat['meta'] = c
        while True:
            d = input(f'Precio de venta: ')
            if d.isnumeric():
                break
        d = float(d)
        dat['venta'] = d

        luceo = dat["venta"] - dat["costo"]
        dat['lucro'] = luceo
        dat['cantidad_de_ventas_mensuales'] = dat['meta']/dat['lucro']
        dat['cantidad_de_ventas_semanales'] = dat['cantidad_de_ventas_mensuales'] / 4
        datos.append(dat.copy())
        dat.clear()
        projeto.cadastrarp(arq1,datos)
        projeto.lerarquivop(arq1)
    # salir del programa
    if m == 4:
        projeto.cabecalho('Nos vemos pronto!!!')
        break