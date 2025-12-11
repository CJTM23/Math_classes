dreligiones = {
"ecuador-quito": ["Catolicismo", "Cristianismo evangélico"],
"ecuador-guayaquil": ["Catolicismo", "Cristianismo evangélico"],
"mexico-ciudad_de_mexico": ["Catolicismo", "Protestantismo", "No religiones"],
"mexico-guadalajara": ["Catolicismo", "Protestantismo"],
"argentina-buenos_aires": ["Catolicismo", "Agnosticismo", "Judaismo"],
"argentina-cordoba": ["Catolicismo", "Agnosticismo"],
"colombia-bogota": ["Catolicismo", "Cristianismo evangélico"],
"colombia-medellin": ["Catolicismo", "Cristianismo evangélico"],
"chile-santiago": ["Catolicismo", "Protestantismo", "Agnosticismo"],
"peru-lima": ["Catolicismo", "Protestantismo"],
"brasil-rio_de_janeiro": ["Catolicismo", "Protestantismo", "Espiritismo"],
"brasil-sao_paulo": ["Catolicismo", "Protestantismo"],
"españa-madrid": ["Catolicismo", "Islam", "Agnosticismo"],
"españa-barcelona": ["Catolicismo", "Agnosticismo", "Islam"],
"francia-paris": ["Catolicismo", "Islam", "Agnosticismo", "Judaismo"],
"alemania-berlin": ["Protestantismo", "Catolicismo", "Agnosticismo"],
"italia-roma": ["Catolicismo", "Agnosticismo"],
"portugal-lisboa": ["Catolicismo", "Agnosticismo"],
"inglaterra-londres": ["Cristianismo", "Islam", "Hinduismo", "Sikhismo"],
"estados_unidos-nueva_york": ["Cristianismo", "Judaismo", "Islam", "No religiones"],
"estados_unidos-los_angeles": ["Cristianismo", "No religiones", "Budismo"],
"canada-toronto": ["Cristianismo", "Islam", "Hinduismo"],
"canada-vancouver": ["Cristianismo", "No religiones"],
"india-nueva_delhi": ["Hinduismo", "Islam", "Sijismo", "Cristianismo"],
"india-mumbai": ["Hinduismo", "Islam", "Cristianismo", "Budismo"],
"china-beijing": ["Budismo", "Taoísmo", "Confucianismo"],
"china-shanghai": ["Budismo", "Taoísmo", "Cristianismo"],
"japon-tokio": ["Shintoísmo", "Budismo"],
"corea_del_sur-seul": ["Cristianismo", "Budismo", "No religiones"],
"australia-sydney": ["Cristianismo", "No religiones"],
"australia-melbourne": ["Cristianismo", "No religiones"],
"sudafrica-johannesburgo": ["Cristianismo", "Islam", "Hinduismo"],
"egipto-el_cairo": ["Islam", "Cristianismo copto"],
"turquia-estambul": ["Islam", "Cristianismo"],
"rusia-moscu": ["Cristianismo ortodoxo", "Islam"],
"ucrania-kiev": ["Cristianismo ortodoxo", "Catolicismo"],
"singapur-singapur": ["Budismo", "Cristianismo", "Islam", "Hinduismo"],
}
#crear funcion AgrupaReligiones(dreligiones) return nuevo diccionario con
#religion como clave, como valor, ciudades donde se practica. rel:[ciudad]
# def AgrupaReligiones(dreligiones):
#     d={}
#     for lugar in dreligiones:
#         pais,ciudad = lugar.split("-")
#         for religion in dreligiones[lugar]:
#             d[religion] = d.get(religion, [])+[ciudad]
#     return d
# print(AgrupaReligiones(dreligiones))

dpoblacion = {
"ecuador-quito": 2800000,
"ecuador-guayaquil": 3100000,
"mexico-ciudad_de_mexico": 9200000,
"mexico-guadalajara": 1500000,
"argentina-buenos_aires": 3000000,
"argentina-cordoba": 1400000,
"colombia-bogota": 7700000,
"colombia-medellin": 2600000,
"chile-santiago": 6100000,
"peru-lima": 9500000,
"brasil-rio_de_janeiro": 6700000,
"brasil-sao_paulo": 12300000,
"españa-madrid": 3300000,
"españa-barcelona": 1600000,
"francia-paris": 2200000,
"alemania-berlin": 3600000,
"italia-roma": 2800000,
"portugal-lisboa": 550000,
"inglaterra-londres": 8900000,
"estados_unidos-nueva_york": 8400000,
"estados_unidos-los_angeles": 3900000,
"canada-toronto": 2900000,
"canada-vancouver": 675000,
"india-nueva_delhi": 33000000, # área metropolitana
"india-mumbai": 21000000,
"china-beijing": 21500000,
"china-shanghai": 27000000,
"japon-tokio": 14000000, # ciudad principal
"corea_del_sur-seul": 9600000,
"australia-sydney": 5400000,
"australia-melbourne": 5100000,
"sudafrica-johannesburgo": 6000000,
"egipto-el_cairo": 10000000,
"turquia-estambul": 15700000,
"rusia-moscu": 12500000,
"ucrania-kiev": 3000000,
"singapur-singapur": 5700000,
}


#funcion llamada PoblacionReligion(dreligiones, dpoblacion)
#retorna un nuevo diccionario
#
# def PoblacionReligion(dreligiones, dpoblacion):
#     dpobrel={}
#     for lugar2,poblacion in dpoblacion.items():
#         for religion in dreligiones[lugar2]:
#             dpobrel[religion] = dpobrel.get(religion, 0) + int(poblacion)
#     return dpobrel
# print(PoblacionReligion(dreligiones, dpoblacion))

#recibe la lista de rel y devuelve un diccionaio religion:[pais,]
# def EncontrarPaises(dreligiones):
#     d = {}
#     for lugar in dreligiones:
#         pais, _ = lugar.split("-")
#         for religion in dreligiones[lugar]:
#             d[religion] = d.get(religion, []) + [pais]
#     return d
# print(EncontrarPaises(dreligiones))

def e(dreligiones):
    d = {}
    for lugar in dreligiones:
        pais, _ = lugar.split("-")
        for religion in dreligiones[lugar]:
            if pais not in d:
                d[pais] = [religion]
            else:
                if religion not in d[pais]:
                    d[pais] += [religion]
    return d
print(e(dreligiones))
