# -*- coding: utf-8 -

def pippo():
    print("My name is Pippo")
    
    
def main():
    # QUi posso fargli fare quello che serve a me per la computazione del modulo,e questa roba non verrà visualizzata grazie alla stringa dopo
    # Tutto ciò che accade qui dentro la funzione main non è accessibile dall'esterno
    print("Sono adesso qu in pippo")
    
# Grazie a questa porzione di codice lui esegue questa porzione solo quando il mpodulo viene eseguito, ma non se viene importato
# all'interno di un programma python        
if __name__=="__main__":
    main()
        
