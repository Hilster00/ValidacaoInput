def validacao(**kwargs):
    if kwargs.get("tipo")!=None:
        mensagem =kwargs.get("mensagem") if kwargs.get("mensagem")!=None else ":"
        while True: 
            try:
                interacao=input(mensagem)
                interacao=kwargs["tipo"](interacao)
                return interacao
            except:
                ...
    else:
        return None
    
