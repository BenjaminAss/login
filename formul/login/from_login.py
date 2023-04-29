import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import utileri.generic as utl
from formul.master.from_master import MasterPanel
from formul.master.lde import Lde
from formul.login.from_login_designer import FormLoginDesigner
from persistence.model import Auth_User
import utileri.encording_decoding as end_dec
from persistence.repository.auth_user_repository import AuthUserRepository
from formul.registracion.form import FormRegister

class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def verificar(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if (self.inUser(user_db)):
            self.isPassword(self.password.get(), user_db)

    def userRegister(self):
        FormRegister().mainloop()

    def inUser(self, user:Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe por favor registrese", title="Mensaje")
        return status
    
    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.root.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")
