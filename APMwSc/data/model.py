class User:
     def __init__(self,fullname,username,password,email,iddpt,idrole):
            self.fullname = fullname
            self.username = username
            self.password = password
            self.email    = email
            self.iddpt    = iddpt
            self.idrole   = idrole
class Dpt:
     def __init__(self,iddpt,namedpt):
            self.iddpt    = iddpt
            self.namedpt  = namedpt
class Rol:
     def __init__(self,idrole,namerole):
            self.idrole     = idrole
            self.namerole   = namerole
            
    
