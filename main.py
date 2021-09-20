import mod.cytron as cy
import mod.ColorPrint as cprint

class sys:
    def info(msg):
        cprint.colorprint("|end| ",color=cprint.Colors.cyan,end=False)
        cprint(msg,color=cprint.Colors.blanc)

    def gen_err(msg):
        cprint.colorprint("|err| ",color=cprint.Colors.rouge,end=False)
        cprint(msg,color=cprint.Colors.blanc)

class init:
    def lsprog():
        cprint.colorprint("\nWhich program to convert: ",color=cprint.Colors.blanc)
        ls_liste = cy.ls("/contener")
        for element in ls_liste:
            ext = element.split(".")[len(element.split("."))-1]
            cprint.colorprint(" ",color=cprint.Colors.none,end=False)
            if ext == "py": cprint.colorprint(element,color=cprint.Colors.bleu)
            elif ext == "txt": cprint.colorprint(element,color=cprint.Colors.jaune)
            elif ext == "gld": cprint.colorprint(element,color=cprint.Colors.vert)
            elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.magenta)
            else: cprint.colorprint(element,color=cprint.Colors.blanc)
        return(input("~} "))

    def main():
        global todo
        no_done = True
        while no_done:
            todo = init.lsprog()
            if cy.rfil_rela("/contener",todo) != None: no_done = False
            else: sys.gen_err("non-existent or unreadable file")

class maker:
    def main():
        name = str(todo.split(".")[len(todo.split("."))-1]) + ".cpp"
        cy.mkfil("/conteneur",name,"".join((l+"\n") for l in EXIT))

class converter:
    def edit_l(l):

        l = str(l)
        if l.startswith("if "):
            cont = l.split("if ")[1] #on enleve le 'if '
            cont = cont.split(":")[len(cont.split(":"))-2] #on enleve le ':'

            print(cont)
            EXIT.append("if(" + cont + ")")
            EXIT.append("{")


    def main():
        fichier = cy.rfil_rela("/contener",todo)
        ligues = fichier.split("\n")

        global EXIT
        EXIT = []

        for l in ligues:
            converter.edit_l(l)
        


init.main()
sys.info("initialization")
converter.main()
sys.info("compilation")
maker.main()
sys.info("writing")