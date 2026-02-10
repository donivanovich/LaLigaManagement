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
            r = requests.get(f"{BASE_URL}/users", headers={"Authorization": f"Bearer {token}"})
            users = r.json()
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

def menu_user(token):
    while True:
        print("\n=== USER MENU ===")
        print("1. Ver Presidentes")
        print("2. Ver Jugadores")
        print("3. Ver Pagos")
        print("4. Logout")
        opcion = input("Elige (1-4): ")
        
        if opcion == "1":
            r = requests.get(f"{BASE_URL}/presidentes", headers={"Authorization": f"Bearer {token}"})
            print("PRESIDENTES:", r.json())
        elif opcion == "2":
            r = requests.get(f"{BASE_URL}/jugadores", headers={"Authorization": f"Bearer {token}"})
            print("JUGADORES:", r.json())
        elif opcion == "3":
            r = requests.get(f"{BASE_URL}/pagos", headers={"Authorization": f"Bearer {token}"})
            print("PAGOS:", r.json())
        elif opcion == "4":
            print("Logout")
            break
        else:
            print("❌ Opción inválida")

def menu_admin(token):
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Crear")
        print("2. Ver")
        print("3. Actualizar")
        print("4. Borrar")
        print("5. Logout")
        opcion = input("Elige (1-5): ")
        
        if opcion == "1":
            print("Crear")
        elif opcion == "2":
            print("Ver")
        elif opcion == "3":
            print("Actualizar")
        elif opcion == "4":
            print("Borrar")
        elif opcion == "5":
            print("Logout")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    while True:
        print("\n🎯 PyBanco Fútbol")
        print("1. Login")
        print("2. Salir")
        opcion = input("Elige (1-2): ")
        
        if opcion == "1":
            token, role = login()
            if token and role:
                if role == 'admin':
                    menu_admin(token)
                else:
                    menu_user(token)
        elif opcion == "2":
            break
        else:
            print("❌ Opción inválida")
