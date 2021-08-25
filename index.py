# import funciones
# print(dir(funciones))
from funciones import isLogin, detailArch, detailArchZip
import crud as cd

user = "Login"
isLogin(user)
#------------------------------------------------------    
## solo se ejecuta esto si el usuario es = 'Login'
print("Inicia la App")

cd.Read()


