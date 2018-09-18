# the csv module (Comma Separated Values) let read and write tabular data in csv format
import csv


# Clase con los datos de cada contacto
class Contact:

    # construct method
    def __init__(self, Pname, Pphone, Pemail):
        """
        :param Pname: Nombre del nuevo registro
        :param Pphone: Telefono del nuevo registro
        :param Pemail: Email del nuevo registro
        """
        self.name = Pname
        self.phone = Pphone
        self.email = Pemail


# Clase que contiene objetos de tipo Contact
class ContactBook:

    # construct method
    # inicializa el libro de contactos con una lista vacia
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        """
        Agrega a la lista un objeto de tipo Contact y lo guarda
        :param name: Nombre del nuevo registro
        :param phone: Telefono del nuevo registro
        :param email: Email del nuevo registro
        :return: none
        """
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
        print("**Registro exitoso.")

    def delete(self, name):
        """
        busca un contacto por su nombre y lo elimina, luego guarda el csv
        :param name: nombre del registro a borrar
        :return: none
        """
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                print("El contacto {} se elimino con exito.".format(contact.name))
                break
        else:
            self._not_found()

    def _save(self):
        """
        utiliza o crea un archivo contact.csv (w = write) y le escribe las lineas de
        cabecera, y luego un ciclo for para escribir todos los datos de contactos
        :return:
        """
        with open('contact.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        """
        metodo que imprime un contacto
        :param contact: contacto a imprimir
        :return: none
        """
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def show_all(self):
        """
        Imprime todos los contactos haciendo uso del metodo _print_contact
        :return: none
        """
        for contact in self._contacts:
            self._print_contact(contact)

    def search(self, name):
        """
        Busca un nombre en la lista de contactos
        cuando lo encuentra break
        :param name: nombre a buscar
        :return: none
        """
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name):
        """
        actualiza los datos de un contacto
        :param name: nombre de contacto a actualizar
        :return: none
        """
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.phone = str(input("Nuevo telefono: "))
                contact.email = str(input("Nuevo correo electronico: "))
                self._save()
                print("**Registro actualizado.")

    def _not_found(self):
        print('*******')
        print('No encontrado!')
        print('*******')


def run():
    # Creando una instancia de la clase ContactBook
    contact_book = ContactBook()

    # Abre un archivo llamado "contact.csv" (r = read) y extrae el contenido para
    # usarlo en la app de terminal, si toma la cabecera o linea vacia: continue
    with open('contact.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            if row == []:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input("""
            ¿Que desea hacer?
            
            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        """))

        if command == 'a':
            name = str(input("Escribe el nombre del contacto: "))
            phone = str(input("Escribe el telefono del contacto: "))
            email = str(input("Escribe el email del contacto: "))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input("Escribe el nombre del contacto: "))
            contact_book.update(name)

        elif command == 'b':
            name = str(input("Escribe el nombre del contacto: "))
            contact_book.search(name)

        elif command == 'e':
            name = str(input("Escribe el nombre del contacto a borrar: "))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break

        else:
            print('Comando no encontrado !')


# estas lineas sirven para ejecutar unicamente este archivo
# en caso hayan otros modulos de python importados
if __name__ == '__main__':
    print('W E L C O M E')
    run()