from ast import List

class IntentionUser:
    def __init__(params : List):
        print("Realizar configuraciones con los parametros.")
        print("Llamada de funciones útiles.")     

    cambiar = ["navegar", "cambiar", "ir", "llevar", "mover", "transladar", "desplazar"]
    reproducir = ["reproducir", "poner", "enseñar"]

    seccion = ["seccion", "pagina", "parte"]

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def predict_user_intention(text):

        #TOKENAISE
        text_tok = nltk.word_tokenize(text)
        i = 0

        for word in text_tok:
            for word2 in cambiar:
                if (word == word2):
                    text_tok[i] = "cambi"

            for word2 in reproducir:
                if (word == word2):
                    text_tok[i] = "reproduc"

            for word2 in seccion:
                if (word == word2):
                    text_tok[i] = "pag"        

            i += 1

        #STOPWORDS
        stopWords = ['vuelva','realizar','vimos','semana','pasada','luego','dices','k','poner','hablamos','favor','sale','digo','miro','tarde','saludo','dejan','dado','quería','necesitaría','decir','día','hacerlo','hace','muchas','pedimos','ido','genial','preguntar','quedo','pasa','días','tardes','buenas','necesito','buenos','hola','gracias','quieres','quiero','de','la','que','el','en','y','a','los','del','se','las','por','un','para','con','no','una','su','al','lo','como','más','pero','sus','le','ya','o','este','sí','porque','esta','entre','cuando','muy','sin','sobre','también','me','hasta','hay','donde','quien','desde','todo','nos','durante','todos','uno','les','ni','contra','otros','ese','eso','ante','ellos','e','esto','mí','antes','algunos','qué','unos','yo','otro','otras','otra','él','tanto','esa','estos','mucho','quienes','nada','muchos','cual','poco','ella','estar','estas','algunas','algo','nosotros','mi','mis','tú','te','ti','tu','tus','ellas','nosotras','vosotros','vosotras','os','mío','mía','míos','mías','tuyo','tuya','tuyos','tuyas','suyo','suya','suyos','suyas','nuestro','nuestra','nuestros','nuestras','vuestro','vuestra','vuestros','vuestras','esos','esas','estoy','estás','está','estamos','estáis','están','esté','estés','estemos','estéis','estén','estaré','estarás','estará','estaremos','estaréis','estarán','estaría','estarías','estaríamos','estaríais','estarían','estaba','estabas','estábamos','estabais','estaban','estuve','estuviste','estuvo','estuvimos','estuvisteis','estuvieron','estuviera','estuvieras','estuviéramos','estuvierais','estuvieran','estuviese','estuvieses','estuviésemos','estuvieseis','estuviesen','estando','estado','estada','estados','estadas','estad','he','has','ha','hemos','habéis','han','haya','hayas','hayamos','hayáis','hayan','habré','habrás','habrá','habremos','habréis','habrán','habría','habrías','habríamos','habríais','habrían','había','habías','habíamos','habíais','habían','hube','hubiste','hubo','hubimos','hubisteis','hubieron','hubiera','hubieras','hubiéramos','hubierais','hubieran','hubiese','hubieses','hubiésemos','hubieseis','hubiesen','habiendo','habido','habida','habidos','habidas','soy','eres','es','somos','sois','son','sea','seas','seamos','seáis','sean','seré','serás','será','seremos','seréis','serán','sería','serías','seríamos','seríais','serían','era','eras','éramos','erais','eran','fui','fuiste','fue','fuimos','fuisteis','fueron','fuera','fueras','fuéramos','fuerais','fueran','fuese','fueses','fuésemos','fueseis','fuesen','siendo','sido','tengo','tienes','tiene','tenemos','tenéis','tienen','tenga','tengas','tengamos','tengáis','tengan','tendré','tendrás','tendrá','tendremos','tendréis','tendrán','tendría','tendrías','tendríamos','tendríais','tendrían','tenía','tenías','teníamos','teníais','tenían','tuve','tuviste','tuvo','tuvimos','tuvisteis','tuvieron','tuviera','tuvieras','tuviéramos','tuvierais','tuvieran','tuviese','tuvieses','tuviésemos','tuvieseis','tuviesen','teniendo','tenido','tenida','tenidos','tenidas','tened','ahí','ajena','ajeno','ajenas','ajenos','algúna','allá','ambos','aquello','aquellas','aquellos','así','atrás','aun','aunque','bajo','bastante','bien','cabe','cada','casi','cierto','cierta','ciertos','ciertas','conmigo','conseguimos','conseguir','consigo','consigue','consiguen','consigues','cualquier','cualquiera','cualquieras','cuan','cuanto','cuanta','cuantas','cuantos','de','dejar','demás','demasiadas','demasiados','dentro','dos','ello','emplean','emplear','empleas','encima','entonces','era','eras','eramos','eses','estes','gueno','hacer','hacemos','hacia','hago','incluso','intenta','intentas','intentamos','intentan','intento','ir','mismo','ningúno','nunca','parecer','podemos','podría','podrías','podríais','podríamos','podrían','primero','puedes','pueden','pues','querer','quiénes','quienesquiera','quienquiera','quizás','sabe','sabes','saben','sabéis','sabemos','saber','sino','solo','esta','tampoco','tan','tanta','tantas','tantos','tener','tiempo','toda','todas','tomar','trabaja','trabajas','tras','último','ultimo','última','ultima','unas','ustedes','variasos','verdadera','pocas','pocos','podéis','podemos','poder','podría','podrías','podríais','podríamos','podrían','primero','puede','puedo','pueda','pues','querer','quiénes','quienesquiera','quienquiera','quizás','mas','sabe','sabes','saben','sabéis','sabemos','saber','según','ser','si','siempre','sino','so','solamente','solo','sólo','sr','sra','sres','sta','tal','tales','tampoco','tan','tanta','tantas','tantos','tener','tiempo','toda','den','queria','todas','tomar','trabaja','trabajo','trabajáis','trabajamos','trabajan','trabajar','trabajas','tras','último','ultimo','unas','usa','usas','usáis','usamos','usan','usar','uso','usted','ustedes','va','van','vais','valor','vamos','varias','varias','varios','vaya','verdadera','voy','vez','más','ok'];
        text_tok_sw = [word for word in text_tok if word not in stopWords]

        #############################################################################################
        def cambiaPag (text_tok_sw):
            n = ['1', '2', '3']

            for number in text_tok_sw:
                if number in n:
                    print("cambiar a la pagina", number)

        def cambiar(text_tok_sw):
            cambios = {
            "pag" : cambiaPag,
            "tema" : "cambiaTema"
            }

            for word in text_tok_sw:
                if word in cambios:
                    cambios[word](text_tok_sw)

        def reproducir():
            print("reproduciendo")

        def abrir():
            print("abriendo")

        
            comportamiento = {
                'cambi'     : cambiar,
                'reproduc'  : reproducir, 
                'abrir'     : abrir 
            }          
        #############################################################################################

        for word in text_tok_sw:
            if word in comportamiento:
                comportamiento[word](text_tok_sw)    