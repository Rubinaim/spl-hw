from DTOs import Hat, Supplier


class Hats:

    def __init__(self, conn):
        self.conn = conn

    def insert(self, hat):
        self.conn.execute("""INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
        """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def get_hat(self, top):
        c = self.conn.cursor()
        c.execute("""SELECT id,topping,supplier,quantity FROM hats WHERE topping = ?
        """, [top, ])
        hats = c.fetchall()
        s = 0
        i = 0
        t = 0
        q = 0
        for hat in hats:
            if hat[2] < s or s == 0:
                s = hat[2]
                i = hat[0]
                t = hat[1]
                q = hat[3]
        return Hat(i, t, s, q)

    def update(self, num):
        self.conn.execute("""UPDATE hats SET quantity=quantity-1 WHERE id = ?
        """, [num, ])

    def delete(self, num):
        self.conn.execute("""DELETE FROM hats WHERE id =?
        """, [num, ])

    def find(self):
        c = self.conn.cursor()
        c.execute("""SELECT id,topping,supplier,quantity FROM hats 
        """)
        sup = c.fetchall()
        return sup


class Suppliers:

    def __init__(self, conn):
        self.conn = conn

    def insert(self, supplier):
        self.conn.execute("""INSERT INTO suppliers (id, name) VALUES (?, ?)
        """, [supplier.id, supplier.name])

    def get_supplier(self, num):
        c = self.conn.cursor()
        c.execute("""SELECT name FROM suppliers WHERE id = ?
        """, [num, ])
        return Supplier(num, c.fetchall()[0][0])

    def find(self):
        c = self.conn.cursor()
        c.execute("""SELECT id,name FROM suppliers 
           """)
        sup = c.fetchall()
        return sup


class Orders:

    def __init__(self, conn):
        self.conn = conn

    def insert(self, id, loc, hat):
        self.conn.execute("""INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
        """, [id, loc, hat])

    def find(self):
        c = self.conn.cursor()
        c.execute("""SELECT id,location,hat FROM orders 
        """)
        sup = c.fetchall()
        return sup
