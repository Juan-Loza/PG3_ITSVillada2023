import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_users():
    response = requests.get("https://reqres.in/api/users")
    data = response.json()["data"]
    return data

def create_user(name, job):
    new_user = {"name": name, "job": job}
    response = requests.post("https://reqres.in/api/users", data=new_user)
    return response.json()

def update_user(user_id, name, job):
    updated_user = {"name": name, "job": job}
    response = requests.put(f"https://reqres.in/api/users/{user_id}", data=updated_user)
    return response.json()

def get_user_by_id(user_id):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    return response.json()

def get_users_with_params(page, per_page):
    params = {"page": page, "per_page": per_page}
    response = requests.get("https://reqres.in/api/users", params=params)
    return response.json()["data"]

def get_users_logical():
    response = requests.get("https://reqres.in/api/users?page=2&per_page=6")
    users = response.json()["data"]
    filtered_users = [user for user in users if user["id"] > 5]
    return filtered_users

def generate_pdf(users):
    c = canvas.Canvas("reqres_users.pdf", pagesize=letter)
    y = 750
    c.drawString(100, y, "Usuarios de Reqres")
    y -= 20
    for user in users:
        y -= 20
        c.drawString(100, y, f"ID: {user['id']}")
        c.drawString(200, y, f"Nombre: {user['first_name']}")
        c.drawString(350, y, f"Apellido: {user['last_name']}")
        c.drawString(500, y, f"Avatar: {user['avatar']}")
    c.save()

def main():
    # Obtener todos los usuarios
    users = get_users()
    print("Todos los usuarios:")
    for user in users:
        print(user)
    print("\n")

    # Crear un nuevo usuario
    new_user_response = create_user("John", "Engineer")
    print("Nuevo usuario creado:")
    print(new_user_response)
    print("\n")

    # Actualizar un usuario existente
    update_response = update_user(2, "John Doe", "Senior Engineer")
    print("Usuario actualizado:")
    print(update_response)
    print("\n")

    # Obtener un usuario por ID
    user_by_id = get_user_by_id(2)
    print("Usuario por ID:")
    print(user_by_id)
    print("\n")

    # Obtener usuarios con parámetros
    users_with_params = get_users_with_params(2, 3)
    print("Usuarios con parámetros:")
    for user in users_with_params:
        print(user)
    print("\n")

    # Obtener usuarios con búsqueda lógica
    logical_users = get_users_logical()
    print("Usuarios con búsqueda lógica (ID > 5):")
    for user in logical_users:
        print(user)
    print("\n")

    # Generar PDF
    generate_pdf(users)

if __name__ == "__main__":
    main()
