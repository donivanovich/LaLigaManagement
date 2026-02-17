import requests
BASE_URL = "http://localhost:5000"

def login():
    print("\n=== LOGIN ===")
    email = input("Email: ")
    password = input("Contraseña: ")

    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})

    try:
        if response.status_code == 200:
            token = response.json()['token']
            data = requests.get(f"{BASE_URL}/users", headers={"Authorization": f"Bearer {token}"})
            users = data.json()

            for user in users:
                if user['email'] == email:
                    role = user['role']
                    print("✅ Login OK - Role:", role)
                    return token, role

            print("❌ Usuario no encontrado")

        else:
            print("❌ Error:", response.json()['msg'])

    except:
        print("❌ Server error")

    return None, None

def register():
    print("\n👤 === CREAR USUARIO ===")
    
    email = input("Nuevo email: ").strip()
    password = input("Nueva contraseña (mín 4): ").strip()
    
    if len(password) < 4:
        print("❌ Mínimo 4 caracteres")
        return False
    
    response = requests.post(f"{BASE_URL}/register", json={
        'email': email, 'password': password, 'role': 'user'
    })
    
    if response.status_code == 201:
        print(f"✅ Usuario creado!")
        print(f"   Email: {email}")
        return True
    else:
        print(f"❌ {response.json()['msg']}")
        return False

def leerPresidentes(token):
    data = requests.get(f"{BASE_URL}/presidentes", headers={"Authorization": f"Bearer {token}"})
    presidentes = data.json()

    return presidentes if presidentes else None

def leerJugadores(token):
    data = requests.get(f"{BASE_URL}/jugadores", headers={"Authorization": f"Bearer {token}"})
    jugadores = data.json()
    return jugadores if jugadores else None

def leerPagos(token):
    data = requests.get(f"{BASE_URL}/pagos", headers={"Authorization": f"Bearer {token}"})
    pagos = data.json()
    return pagos if pagos else None

def crearPago(token):
    print("\n🎯 CREANDO PAGO")
    
    jugadores = leerJugadores(token)
    imprimir(jugadores, "JUGADORES")
    
    if not jugadores:
        print("❌ No hay jugadores")
        return
    
    pos_jug = int(input(f"\n📝 Jugador (1-{len(jugadores)}): ")) - 1
    jugador = jugadores[pos_jug]
    jugador_id = jugador['id']
    presidente_id = jugador.get('presidente_id')
    
    if not presidente_id:
        print("❌ Jugador sin presidente asignado")
        return
    
    print(f"✅ Jugador: {jugador.get('nombre', 'N/A')} (Presidente ID: {presidente_id})")
    
    try:
        cantidad = float(input("💰 Cantidad: "))
        estado = input("📝 Estado/Observaciones: ").strip()
    except:
        print("❌ Datos inválidos")
        return
    
    pago_data = {
        'jugador_id': jugador_id,
        'presidente_id': presidente_id,
        'cantidad': cantidad,
        'estado': estado
    }
    
    response = requests.post(
        f"{BASE_URL}/pagos",
        json=pago_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    if response.status_code == 201:
        print(f"\n✅ Pago #{response.json()['pago_id']} creado!")
    else:
        print("❌ Error:", response.json().get('msg', 'Desconocido'))

def imprimir(data, titulo):
    if data is None:
        print(f"\n📋 {titulo.upper()}")
        print("➤ No existen registros")
        return
    
    claves_orden = []
    anchos = {}
    for item in data:
        for clave in item:
            if clave not in claves_orden:
                claves_orden.append(clave)
            texto = str(item[clave])[:30]
            anchos[clave] = max(anchos.get(clave, len(clave.upper())), len(texto))
    
    lineas = []
    
    header_vals = [clave.upper().ljust(anchos[clave]) for clave in claves_orden]
    linea_header = "│ " + " │ ".join(header_vals) + " │"
    lineas.append(linea_header)
    
    seps_cols = "┼".join(["─" * anchos[clave] for clave in claves_orden])
    sep_num = "─" * 4
    linea_sep = "├" + sep_num + seps_cols + "┤"
    lineas.append(linea_sep)
    
    for i in range(len(data)):
        valores = [str(data[i].get(clave, ''))[:30].ljust(anchos[clave]) for clave in claves_orden]
        linea_data = f"│ {i+1:2d}. " + " │ ".join(valores) + " │"
        lineas.append(linea_data)
    
    ancho_total = max(len(linea) for linea in lineas)
    
    print(f"\n📋 {titulo.upper()} ({len(data)})")
    print("┌" + "─" * (ancho_total - 2) + "┐")
    # print(linea_header.ljust(ancho_total))
    
    # print(linea_sep.ljust(ancho_total))
    
    for linea_data in lineas[2:]:
        print(linea_data.ljust(ancho_total))
    
    print("└" + "─" * (ancho_total - 2) + "┘")

def eliminarJugador(token):
    print("\n🗑️ ELIMINANDO JUGADOR")
    
    jugadores = leerJugadores(token)
    imprimir(jugadores, "JUGADORES")
    
    if not jugadores:
        print("❌ No hay jugadores")
        return
    
    try:
        pos = int(input(f"\n📝 Jugador a eliminar (1-{len(jugadores)}): ")) - 1
        if pos < 0 or pos >= len(jugadores):
            print("❌ Posición inválida")
            return
        
        jugador = jugadores[pos]
        print(f"\n⚠️  ¿Eliminar '{jugador.get('nombre', 'N/A')}' (ID: {jugador['id']})?")
        
        confirm = input("Confirma (s/N): ").lower().strip()
        if confirm != 's':
            print("❌ Cancelado")
            return
        
        response = requests.delete(
            f"{BASE_URL}/jugadores/{jugador['id']}",
            headers={"Authorization": f"Bearer {token}"}
        )
        
        if response.status_code == 200:
            print(f"\n✅ Jugador {jugador['id']} eliminado!")
        else:
            print("❌ Error:", response.json().get('msg', 'Desconocido'))
            
    except ValueError:
        print("❌ Ingresa un número válido")
    except Exception as e:
        print(f"❌ Error: {e}")

def actualizarPresidente(token):
    print("\n✏️ ACTUALIZAR PRESIDENTE")
    
    presidentes = leerPresidentes(token)
    imprimir(presidentes, "PRESIDENTES")
    
    if not presidentes:
        print("❌ No hay presidentes")
        return
    
    try:
        pos = int(input(f"\n📝 Presidente (1-{len(presidentes)}): ")) - 1
        if pos < 0 or pos >= len(presidentes):
            print("❌ Posición inválida")
            return
        
        presi = presidentes[pos]
        print(f"\n👤 Actual: {presi.get('nombre', 'N/A')} | 💰 Presupuesto: {presi.get('presupuesto', 0)}")
        
        nuevo_nombre = input("📝 Nuevo nombre: ").strip()
        if not nuevo_nombre:
            print("❌ Nombre requerido")
            return
        
        try:
            nuevo_presupuesto = float(input("💰 Nuevo presupuesto: "))
        except:
            print("❌ Presupuesto inválido")
            return
        
        update_data = {
            'nombre': nuevo_nombre,
            'presupuesto': nuevo_presupuesto
        }
        
        response = requests.put(
            f"{BASE_URL}/presidentes/{presi['id']}",
            json=update_data,
            headers={"Authorization": f"Bearer {token}"}
        )
        
        if response.status_code == 200:
            print(f"\n✅ Presidente {presi['id']} actualizado!")
        else:
            print("❌ Error:", response.json().get('msg', 'Desconocido'))
            
    except ValueError:
        print("❌ Ingresa números válidos")

def menu_user(token):
    while True:
        print("\n=== USER MENU ===")
        print("1. Ver Presidentes")
        print("2. Ver Jugadores")
        print("3. Ver Pagos")
        print("4. Actualizar Contraseña")
        print("5. Logout")

        opcion = input("Elige (1-5): ")

        if opcion == "1":
            imprimir(leerPresidentes(token), "PRESIDENTES")

        elif opcion == "2":
            imprimir(leerJugadores(token), "JUGADORES")

        elif opcion == "3":
            imprimir(leerPagos(token), "PAGOS")

        elif opcion == "4":
            print("\n🔐 === CAMBIAR CONTRASEÑA ===")
    
            print("Ingresa tu contraseña ACTUAL:")
            current_pass = input("Contraseña actual: ").strip()
            
            print("Ingresa tu nueva contraseña:")
            new_pass = input("Nueva contraseña: ").strip()
            confirm_pass = input("Confirmar nueva contraseña: ").strip()
            
            if new_pass != confirm_pass:
                print("❌ Las contraseñas no coinciden")
                return
            
            if len(new_pass) < 4:
                print("❌ La contraseña debe tener al menos 4 caracteres")
                return
            
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.put(
                f"{BASE_URL}/user/change-password",
                json={
                    'current_password': current_pass,
                    'new_password': new_pass
                },
                headers=headers
            )
            
            if response.status_code == 200:
                print("✅ ¡Contraseña cambiada correctamente!")
            else:
                try:
                    error_msg = response.json()['msg']
                except:
                    error_msg = "Error desconocido"
                print(f"❌ Error: {error_msg}")

        elif opcion == "5":
            print("Logout")
            break

        else:
            print("❌ Opción inválida")

def menu_admin(token):
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Crear un Pago")
        print("2. Leer Datos")
        print("3. Actualizar un Presidente")
        print("4. Borrar un Jugador")
        print("5. Logout")
        opcion = input("Elige (1-5): ")
        
        if opcion == "1":
            crearPago(token)
        elif opcion == "2":
            menu_user(token)
        elif opcion == "3":
            actualizarPresidente(token)
        elif opcion == "4":
            eliminarJugador(token)
        elif opcion == "5":
            print("Logout")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    while True:
        print("\nLaLiga Management")
        print("1. Login")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Elige (1-3): ")
        
        if opcion == "1":
            token, role = login()
            if token and role:
                if role == 'admin':
                    menu_admin(token)
                else:
                    menu_user(token)
        elif opcion == "2":
            register()

        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida")
