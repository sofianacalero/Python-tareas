class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' añadido correctamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto '{nombre}' editado correctamente.")
                return
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

    def cerrar_agenda(self):
        print("Agenda cerrada.")

# Ejemplo de uso
agenda = Agenda()
while True:
    print("\nMenú:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        email = input("Email del contacto: ")
        agenda.añadir_contacto(nombre, telefono, email)
    elif opcion == "2":
        agenda.listar_contactos()
    elif opcion == "3":
        nombre = input("Nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Nombre del contacto a editar: ")
        nuevo_telefono = input("Nuevo teléfono del contacto: ")
        nuevo_email = input("Nuevo email del contacto: ")
        agenda.editar_contacto(nombre, nuevo_telefono, nuevo_email)
    elif opcion == "5":
        agenda.cerrar_agenda()
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
