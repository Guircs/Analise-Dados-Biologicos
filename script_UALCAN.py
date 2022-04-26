import os
import datetime


dir_dados = "../Dados ualcan"            #Folder with the data files
dir_res = "../Resultados"                #folder where the results will be saved

data_hora = datetime.datetime.now().strftime("%y%m%d%H%M%S")    #String with date and time that the script was executed





def lista_pos_neg():           #Return the lists of files separeted by correlation (positive and negative)

    pos = []
    neg = []
    
    try:
        os.chdir(dir_dados)             #Access the folder with the files

        for i in os.listdir():

            if ".txt" in i:             #Selects only .txt files

                if "positive" in i:

                    pos.append(i)       #Appends the list of positive correlation
                
                else:

                    neg.append(i)       #Appends the list of negative correlation

        return pos, neg

    except :
        print("O diretório não é válido")

    

def Lista_Ocorrencias(lista, n):    #Return a list with the n first genes of each tumor in the given list

    res= []

    os.chdir(dir_dados)
    

    for arquivo in lista:

        contador = 0

        with open(arquivo) as arq:

            for linha in arq:

                lista_linha = linha.split('\t')

                if contador > 0 and contador <= n:

                    res.append(lista_linha[0])

                contador += 1

                
    return res                  
            

    
def Armazena_res(nome,dados):           #recieve a name (string) and a dataset(tuple with two lists) and saves the pairs line by line in an external file

    nome += data_hora

    try:
        os.chdir(dir_res)
        
    except:
        os.mkdir(dir_res)
        os.chdir(dir_res)
        
    finally:
        texto = ''
      
        
        for i in range(len(dados[0])):

            texto += dados[0][i] + ' : ' + str(dados[1][i]) + '\n'


        with open(nome+'.txt','w') as s:
            s.write(texto)
            
              
          
        

def ContaLista(lista):          #recieves a list and return a dictionary of genes (keys) and number of ocurrencies of each gene (value)

    dic = {}
    
    for i in lista:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    return dic



def OrdenaDic(dic):                 #orders the dictionary by number of ocurrencies of each gene in the set

    lista_chave = []
    lista_value = []

    for chave in sorted(dic, key=dic.get, reverse=True):

        lista_chave.append(chave)
        lista_value.append(dic[chave])

    return lista_chave, lista_value


    




#_________________________________________________________________________________


    
def main():                 #Main Function, get user's input to decide what data-set to use

    repeat = True

    positivo , negativo = lista_pos_neg()

       
    
    while repeat:

        name = input('Insert output file name(do not use /\?<>|:*"): ')
        lines = int(input("Insert the number of lines to be checked for each tumor (numbers only): "))
        corr = input("Insert the type of correlation (+ / - ): ")


        if corr=="+":

            correlation = positivo
            
        elif corr == "-":

            correlation = negativo

        else:
            print("Invalid Correlation")

        
        Armazena_res(name, OrdenaDic(ContaLista(Lista_Ocorrencias(correlation,lines))))

        print("Analysis Completed!")
        

        cont= input("Do you want to do another analysis?(Y/N): ")

        if cont=="Y" or cont=="y":
            repeat = True
            
        else:
            repeat = False


    print("End of script")
            
        

        
        

   

    


main()





    


