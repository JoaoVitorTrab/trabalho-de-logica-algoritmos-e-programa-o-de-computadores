def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print("Bem-vindo, Administrador")
    else:
        print("bem-vindo, Usuário")

loginUsuario("admin")
loginUsuario("admin")
loginUsuario("user")
loginUsuario("usuário")
loginUsuario("administrador")