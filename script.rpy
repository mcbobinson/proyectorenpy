# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image bg fondo1 = "bgtown.jpg"
image bg fondo2 = "fondo2.png"
image bg hamburguesa = "hamburger.png"
image jigglypuff jiggly = "Jigglypuff.png"
image bg ashfinaljpg = "ashfinaljpg.jpg"

image misdreavus misd = "Misdreavus.png"

image pikachu pika = "Pikachu.png"

image ash primero = "ash.png"
image ash segundo = "ash2.png"

image profoak prof = "Profesor_Oak.png"



# Los personajes del juego
define a = Character('Ash', color="#873617")
define o = Character('Prof. Oak', color="#748281")
define p = Character('Pikachu',color="#374818")
define j = Character('Jigglypuff', color="#287462")
define m = Character('Misdreavus', color="#645372")
define n = Character('Narrador', color="#647583")

init:
    $ left = Position(xpos=0.185, xanchor='left')  
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=0.825, xanchor='right')
    
# The game starts here.
# - El juego comienza aquí.
label start:
        
    scene bg fondo1 
    with fade
    show ash primero 
    play music "palettetown.mp3"
    
    a "Hola! Mi nombre es Ash Ketchum de Pueblo Paleta y mi meta es ser el mejor entrenador Pokemon!"
    a "Sere el mejor entrenador Pokemon de todos los tiempos, tenganlo por seguro!"
    hide ash primero
    
    n "A pesar de que Ash quiere ser el mejor entrenador de todos, solo tiene un problema para poder alcanzar
     su meta, y ese es que no ha capturado a su primer Pokemon."
    n "Aun asi Ash no se rinde, el es muy perseverante y continua intentando"
    
    scene bg fondo2
    stop music
    play music "forest.mp3"
    n "Ash normalmente sale todos los dias a la casa de su amigo que queda en el pueblo mas cercano, Viridian City, 
     pero en el camino, nunca se espero que se encontraria con algo que cambiaria su vida."
    
    a "Que dia tan tranquilo... Espero que cuando llegue a la ciudad pueda ir a comer una buena Hamburguesa... El hambre me esta matando."
    
    n "Ash se apresura para ir a la ciudad, pero just a la mitad de su camino empieza a escuchar gritos de ayuda en el bosque"
    
    menu: 
        
        "Ir a ayudar":
            jump ayuda 
        
        "Seguir con su camino":
            jump caminoNormal
        
label caminoNormal:

    a "Ignorare esos gritos y continuare con mi camino... Uno nunca sabe que podra ser"
    
    n "Despues de caminar un rato mas, a Ash le comienza a pesar su conciencia por no haber ido a ayudar..."
    
    menu: 
        
        "Volver para ayudar":
            jump ayuda
            
        "Seguir con su camino":
            jump malapersona
        
label malapersona:
    a "Seguire con mi camino... Tengo demasiada hambre como para ir a meterme a muchos lios."
    stop music
    play music "viridian.mp3"
    scene black
    with dissolve
    n "Cuando Ash llega a la ciudad se encuentra con su amigo, con el que va a compartir una enorme hamburguesa al famoso 
     restaurante Carlitos Jr."
    
    n "Cuando Ash va de regreso a su casa se da cuenta que quien estaba gritando por ayuda era el Prof. Oak, quien tenia pensado
     obsequiarle su primer Pokemon, pero despues de que Ash no lo quiso ayudar decidio no darle nada."
   
    n ".:. Fin"
    
    return
    
label ayuda:
    stop music
    play music "forest.mp3"
    
    o "Alguien ayuda!!"
    
    n "Cuando Ash se acerca se da cuenta que el profesor esta siendo atacado por un Jigglypuff salvaje"
   
    a "Prof. Oak?? Es usted??"
    o "Deja de hablar y toma la primera Pokebola que veas en mi mochila! Hay dos, asi que escoge cualquiera!"
   
    n "Ash se acerca y toma la pokebola"
        
    menu: 
        
        "Escoger Pikachu":
            jump Pikachu
            
        "Escoger Misdreavus":
            jump Misdreavus
        
         
label Pikachu:
    stop music
    play music "forest.mp3"
    a "Que pokemon hay aqui profesor"
    o "Es un Pikachu, apresurate y pelea!"
    stop music
    play music "battle.mp3"
    show ash segundo at right 
    a "Pikachu... Yo te elijo!"
    show pikachu pika at left
    p "Pika pika!"
    n "El Jigglypuff salvaje nota a Ash y Pikachu y se voltea para luchar contra ellos"
    show jigglypuff jiggly at center
    j "Jiggly!"
    a "Pikachu! Usa Ataque Rapido!"
    p "Pikaaa..."
    n "Jigglypuff recibe un fuerte golpe y queda aturdido"
    a "Ya lo tienes! Ahora utiliza Impactrueno!"
    p "Chuuu!!"
    n "Debido a la potente corriente electrica, Jigglypuff queda semirostizado en el suelo"
    hide jigglypuff jiggly
    stop music
    play music "victory.mp3"
    hide pikachu pika
    hide ash segundo
    show ash primero
    show profoak prof
    o "Ash, bien hecho! Me salvaste!"
    o "Como regalo, puedes quedarte con el Pikachu que utilizaste para tu batalla"
    a "Enserio?! Profesor muchisimas gracias!"
    a "Porfin puedo comenzar con mi sueño de volverme el mejor entrenador Pokemon de todos los tiempos!"
    hide ash primero
    hide profoak prof
    jump final1
    
    
label Misdreavus:
    a "Que pokemon hay en esta pokebola profesor?"
    o "Es un Misdreavus, ahora apresurate y pelea!"
    stop music
    play music "battle.mp3"
    a "Misdreavus, Yo te elijo!"
    show misdreavus misd at left
    show jigglypuff jiggly at center
    show ash segundo at right
    m "Misdreavuss"
    a "Misdreavus rapido! Utiliza Rayo Confuso!"
    n "El Jigglypuff salvaje queda confundido, tambaleandose por todas partes desorientadamente"
    a "Bien hecho! Ahora rapido utiliza Bola Sombra!"
    n "Misdreavus lanza un poderoso ataque oscuro que acaba con la pelea"
    n "El Jigglypuff salvaje queda desmayado en el suelo"
    hide jigglypuff jiggly 
    hide misdreavus misd
    stop music
    play music "victory.mp3"
    hide ash segundo
    show ash primero at right
    show profoak prof at center
    o "Ash, me acabas de salvar la vida... Como recompensa, puedes quedarte con el Misdreavus que
       utilizaste para batallar"
    a "Profesor muchisimas gracias! Misdreavus siempre ha sido mi Pokemon favorito y al fin puedo comenzar
       con mi sueño de volverme el mejor entrenador Pokemon de todos los tiempos!"
    o "Te deseo mucha suerte en tu camino jovencito, animos!"
    hide ash segundo
    hide profoak prof
    jump final1
    
label final1:
    show bg hamburguesa
    with dissolve 
    stop music 
    play music "viridian.mp3"
    n "Despues de un largo dia lleno de aventuras, Ash siguio con su camino a Viridian City y 
     comio la hamburguesa mas grande de toda la ciudad"
    scene bg ashfinaljpg
    n ".:. Fin"
    return 