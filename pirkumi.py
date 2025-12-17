class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity
        

class ShoppingCart:

    def __init__(self):
        self.preces = []

    def add_product_to_cart(self, produkts):
        self.preces.append(produkts)
        return f"{produkts.name} pievienots grozam"
    
    def remove_product_from_cart(self, produkts):
        self.preces.remove(produkts)
        return f"{produkts.name} izņemts no groza"
    
    def get_total_price(self):
        kopeja_cena = 0
        for i in self.preces:
            kopeja_cena += i.get_total_price()
        return f"Kopējā summa: {kopeja_cena}"

class SystemUser:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def set_user_info(self, lietotajs, parole, epasts):
        # nomaina esošo informāciju
        self.username = lietotajs
        self.password = parole
        self.email = epasts
        print("Informācija ir nomainīta") 

    def get_user_info(self):
        # iegūst eksistējošo informāciju un parāda lietotājam
        print("---Informācija par lietotāju---") 
        print(f"Lietotājvārds: {self.username}")   
        print(f"Parole: {self.password}") 
        print(f"E-pasts: {self.email}") 


class Customer(SystemUser):

    def __init__(self, username, password, email, customer_id, purchase_history, membership_status):
        super().__init__(username, password, email) #manto atribūtus no vecāka klases
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status

    def set_user_info(self, lietotajs, parole, epasts, liet_id, pirkumu_vesture, klienta_statuss):
        super().set_user_info(lietotajs, parole, epasts)
        self.customer_id = liet_id
        self.purchase_history = pirkumu_vesture
        self.membership_status = klienta_statuss

    def get_user_info(self):
        super().get_user_info()
        print(f"Klienta ID: {self.customer_id}")
        print(f"Pirkumu vēsture: {self.purchase_history}")
        print(f"Piederība klientu programmai: {self.membership_status}")


# no 1. uzdevuma
produkts1 = Product("Ķieģeļi", 3, 50)
print(produkts1.get_total_price())

produkts2 = Product("Cements", 12.99, 2)
print(produkts2.get_total_price())
print()

# no 2. uzdevuma
grozs = ShoppingCart()

print(grozs.add_product_to_cart(produkts1))
print(grozs.add_product_to_cart(produkts2))
print(grozs.get_total_price())
print(grozs.remove_product_from_cart(produkts1))
print(grozs.get_total_price())
print()

# no 3. uzdevuma

liet1 = SystemUser("Kārlis", "12345", "karlis@karlis.com")
liet1.set_user_info("Kārlis", "s1vsk-4@pr", "karlis@karlis.lv")
liet1.get_user_info()
print()


# no 4. uzdevuma
klients1 = Customer("Ilze", "parole", "ilze@gmail.com", 211, "", "Nav")
klients1.set_user_info("Ilze", "p@role", "ilze@gmail.com", 211, "Lāpsta", "Ir") 
klients1.get_user_info()  