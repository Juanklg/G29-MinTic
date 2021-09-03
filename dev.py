from funciones import isLogin
#------------------------------------------------------
def consultarProyecto(usuario):
    proyecto={}
    if usuario == 'juan':
        proyecto['texto'] = '''Proyecto de Juan'''
        proyecto['nombre'] = '''Words Selector'''
    return proyecto

def consultarConstantes():
    diccionarios = {
        'estudiantes':{
            'proyectos':[{},{}],
            'user':'',
            'correo':'',
            'nombre':'',
            'grupo':'',
            'state':'',
        },
        'proyecto' : {
            'Texto':'',
            'Palabras':[{}],
            'Listas':[{}],
            'Version':0.1
        },
        'lista' : {
            'nombre':'',
            'palabras':[],
            'color':''
        },
        'palabras' : {
            'lista':'',
            'color':'',
            'palabra':'',
            'state':'nuevas',
        }
    }
    cte = {
        'estudiantes_state':('Activo','Invitado','Desconectado','Inactivo','Desactivado'),
        'estuiantes_grupo':('29','48','61'),
        'listas_default':[
            {'nombre':'roles','palabras':[],'color':'#0000ff'},
            {'nombre':'acciones','palabras':[],'color':'#00ff00'},
            {'nombre':'objetos','palabras':[],'color':'#ff0000'},
            {'nombre':'nuevas','palabras':[],'color':'#ffffff'},
            {'nombre':'nulos','palabras':[],'color':'#000000'},
        ],        
        'palabras_state' : ('nuevas','clasificadas'),
        
    }
    return cte

def consultarRedes():
    redes = {
        "Google":{
            "Web":"www.web.de",
            "Apps":{
                "Drive": "DriveLink",
                "Dropbox": "DropboxLink"
            },
            "Google Main":"http://mail.google.com",
            "G+":"http://plus.google.com"
        },  
        "Social":{
            "Facebook":"http://www.facebook.de",
            "G+":"https://plus.google.com",
            "Xing":"http://www.xing.de",
            "LinkedIn":"http://www.linkedin.com",
            "Tumblr":"http://www.tumblr.com"
        },
        "Fun":{
            "Reddit":"http://www.reddit.com"
        }
    }
    return redes











#------------------------------------------------------

