# PyBancoFutbol 📊⚽

API REST completa para gestión de **presidentes de clubes**, **jugadores** y **pagos** con autenticación JWT + MongoDB. Cliente interactivo con tablas ASCII.

## ✨ Características

- 🔐 **Autenticación JWT** (login/register)
- 👥 **Roles** (admin/user)
- 👑 **CRUD Presidentes** (nombre, presupuesto)
- ⚽ **CRUD Jugadores** (referencia a presidente)
- 💰 **Pagos** (jugador → presidente, cantidad, estado)
- 📊 **Tablas bonitas** en consola
- 🛡️ **Validaciones** completas

👤 Usuario: pybanco_user
🔑 Contraseña: PyB4nc0P@ss2026!
🗄️ Database: pybancodb
☁️ Collections: users, presidentes, jugadores, pagos

| Email            | Password | Rol   |
| ---------------- | -------- | ----- |
| donnie@gmail.com | 1234     | user  |
| tebas@laliga.es  | 1234     | admin |

## ✨ Como Instalar

```python -m virtualenv venv``` En la carpeta contenedora del proyecto para crear el entorno virtual

```venv/scripts/activate``` Para activar el entorno virtual

```cd ./LaLigaManagement/server``` y ```pip install -r ./requirements.txt``` Para instalar las dependencias del servidor

```python ./application.py``` Para lanzar el servidor

Seleccionar un interprete distinto al del entorno virtual y ```cd ..```

```cd ./client``` y ```pip install -r ./requirements.txt``` Para instalar las dependencias del cliente

Ejecutar el archivo ```main.py```