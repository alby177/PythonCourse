# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:51:33 2018

@author: USER
"""

# -*- coding: utf-8 -

def pippo():
    print("My name is Pluto")
    
    
def __main():
    # QUi posso fargli fare quello che serve a me per la computazione del modulo,e questa roba non verrà visualizzata grazie alla stringa dopo
    # Tutto ciò che accade qui dentro la funzione main non è accessibile dall'esterno
    print("Sono adesso qui in pluto")
    
# Grazie a questa porzione di codice lui esegue questa porzione solo quando il mpodulo viene eseguito, ma non se viene importato
# all'interno di un programma python        
if __name__=="__main__":
    __main()