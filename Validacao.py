def validacao(**kwargs):
    if kwargs.get("tipo")!=None:
        mensagem =kwargs.get("mensagem") if kwargs.get("mensagem")!=None else ":"
        mensagem =mensagem if mensagem[-1]==":" else mensagem+":"
        while True: 
            try:
                interacao=input(mensagem)
                interacao=kwargs["tipo"](interacao)
                return interacao
            except:
                if kwargs.get("erro") != None:
                    print(kwargs["erro"])
                else:
                    print("ERRO")
    else:
        return None
        
    
