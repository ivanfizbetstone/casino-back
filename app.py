import re
from flask import Flask, jsonify, request, Response, Blueprint
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json
from flask_cors import CORS, cross_origin
from passlib.hash import sha256_crypt
from os import urandom
import requests 
from datetime import datetime, timedelta
import jwt
import calendar
from werkzeug.middleware.proxy_fix import ProxyFix
import random, string


app = Flask(__name__)

CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

#Base de datos
app.config['MONGO_URI'] = 'mongodb+srv://PythonUser:Lb_GTzdY2-HWF1m_ImZ@cluster0.vkhw2.mongodb.net/Casino?retryWrites=true&w=majority'
app.config['CORS_HEADERS'] = 'Content-Type'

Diego234569 = [
    "AnaPauR",
    "JoseG",
    "PattyG",
    "MaryCav",
    "Lupita2022",
    "HoracioGzz",
    "ErnestoGzz",
    "Jimmy2022",
    "CarlosC2022",
    "JuveRdz",
    "Adrianal",
    "MRefugio",
    "DanielaT",
    "LidiaG",
    "KarenGar",
    "GeraMarrero",
    "AmericoV",
    "ValeGarza",
    "NoraRedendez",
    "Lara",
    "MrFlores",
    "CarlosSald",
    "Cam2021",
    "Kike2021",
    "ValentinMiravalle",
    "AdrianaTorres",
    "JavierLee",
    "RobertoFlo",
    "ElsaRo",
    "DianaMoto",
    "ArmandoFdz",
    "Vic2020",
    "GerardoR",
    "Selvin",
    "CaciliaR",
    "JorgeObregon",
    "RossyB",
    "MyriamAyub",
    "SantiagoT",
    "EfrenM",
    "RodrigoCruz",
    "AdrianG",
    "Coque12",
    "DanielGzz",
    "AndresTrev",
    "DiegoMendoza",
    "QuenoG",
    "GibranO",
    "CharlieCOD",
    "LizGarcia",
    "HugoLeon",
    "MireyaFdz",
    "AleMerrero",
    "RolandoR",
    "OrlandoF",
    "ErnestinaR",
    "Jacuzzi",
    "AdrianMtz",
    "DanielMo",
    "JosefinaF",
    "MariaMo",
    "NellyLu",
    "ErikaR",
    "Patricia",
    "Hugo2020",
    "BerthaSi",
    "AndresG",
    "PrimoS",
    "PabloG",
    "AlanGarcia",
    "JessicaMtz",
    "Gisel",
    "MarcoGaAv",
    "KevinR",
    "Paquito",
    "DavidC",
    "JosueE",
    "RobertoR",
    "Richi",
    "BebeAlessa",
    "DemoOmar",
    "Yitani",
    "Luis777",
    "ValenteM01",
    "EasTaw",
    "Manuel2345",
    "MadeFlores",
    "testDiego",
    "OraliaL",
    "NancyL",
    "LauraL2017",
    "MagalyL",
    "Alan",
    "PanchoA1",
    "DavidRamos",
    "Smack",
    "BrisGarza1",
    "MarioGzz",
    "HomeroFlores",
    "RobertoFlores",
    "SergioFernandez",
    "MarthaSotelo1",
    "JorgeMireles",
    "SilviaGarza",
    "ValeriaRangel"
]

Adriana234590 = ["LUCEROB",
"SAULC",
"NicolM",
"OC0041138264",
"Leomontverd",
"MarlenL",
"JanethR",
"ALONSOR",
"ADELIA",
"RENER",
"LUISL",
"ROCIOC",
"JOSEL",
"CELINAV",
"Alexisg",
"Monivav",
"Floral",
"Pauloc",
"Felipeg",
"Silvias",
"Almagg",
"Patriciaa",
"Celiag",
"Noemiv",
"Berenicem",
"Almao",
"Mirellav",
"maangeles",
"Malenaa"]

Alejandro234600 = ["dania",
"dany",
"marthadi",
"evarosa",
"demian",
"guerrero",
"julioce",
"cabotti"]

Dana234592 = ["IvanFM",
"RosalvaAL",
"BlancaLA",
"MaribelAL",
"YadiraGpe",
"Hernandez",
"CeciMN",
"EnriqueLC",
"MaJesusHC",
"MaVelarde",
"ConcepcionS",
"MaPena",
"AdelaidaMS",
"DjackelinO",
"DulceMa",
"MarcoAR",
"IvanDJ",
"EnriqueZ",
"JoseManM",
"EsmeraldaPim",
"JoseManuelRR",
"RosaIselaG",
"LilianaIsaAM",
"ClaudiaAng",
"AntonioAng",
"JesusAntonio",
"RosaRG",
"IgnacioAAS",
"MaribelBL"]

Edi234565 = ["Corazones2",
"LetiNansen",
"Alva",
"KaiaG",
"ErnestoVale",
"LeticiaMat",
"AlvaSolis",
"MarinaRodriguez",
"prueba2020"]

Gilberto234582 = ["rogelioairada",
"Esthelalopez",
"Marthaper",
"kesiaperez",
"estela",
"marilu",
"claucarri",
"javama",
"OC0040376386",
"solcas",
"SILOR",
"Jose2015",
"solpad",
"marbar",
"licar",
"auga",
"rosllanes",
"camga",
"maferos",
"sansouza",
"mazatlan",
"josper",
"marpere",
"gabror",
"ingren",
"alevalen",
"eriren"]

Javier234594 = ["Brenda10",
"Leticia08",
"Ansel07",
"Isela05",
"02Maria",
"01karla",
"Manuel06",
"Francisca04",
"Maria05",
"Maguy03",
"MArtin02",
"karla01"]

Marcia234584 = ["servandorendon",
"evarosas",
"Carmina",
"luisfernando",
"prispalma",
"patycampos",
"mariaemma",
"erikahamed",
"mariao",
"josemaria",
"benjaminsoto",
"almanohemi",
"mariaguadalupe",
"blancafabiola",
"berthaalicia",
"rosaelva",
"fcagarcia",
"denisseelizalde",
"itzelyunibe",
"jesuslorena",
"raulacuriel",
"betoarias",
"lichavalenzuela",
"jesuspedro",
"silviagomez",
"josearmandocerecer",
"anagabymichel",
"albertoromanarias",
"raulvigueria",
"franciscojauregui",
"imeldamorales",
"fredisoto",
"antoniosobarzo",
"yeseniaespinoza",
"raulcurielrendon",
"armentamyrna",
"lourdescerecer",
"angelesguerrero",
"jorgecerecer"]

Marisela234598 =["VERONICAV",
"FRANCISCOB",
"CSABORI",
"ECAMACHO",
"ARNULFOAR",
"HECTORB",
"SAMUELZ",
"YESSICAMS",
"MSIQUEIROS",
"GLORIAPERAZA",
"LEYLAK",
"JULIOCH",
"KASSANDRAA",
"ELIUT",
"ANTONIOGB",
"JESUSMONGE",
"GERARDOSOQUI",
"GUILLEA",
"DELIAOL",
"ROLANDOV",
"ERICKG",
"SANTOSD",
"MAGDAPINZON",
"MARIGAMEZ",
"MIREYA11",
"MARIAAMM",
"ALEGRACIA",
"AMARODAN",
"JOSEBASTIAN",
"JORGEAMADOR",
"SUELO",
"FLORYADIRA",
"JOVANAH",
"EMILIOCUEVAS",
"DEVLOP",
"JOAOROMERO",
"CRISTIAN1",
"JOSELUNA",
"ARACELICARRILLO",
"AIDEEM",
"PEDROLUNA",
"JORGEPEREZ",
"MIGUELZO",
"EMAFLORES",
"ROSAN",
"JUDITLORETO",
"ENRIQUES",
"CARLOSMEZA",
"LUISROMERO1",
"AARONAMAVIZCA",
"MARIAGALAZ",
"GUILLERMINAO",
"MANUELARMENTA",
"LILIANARUIZ",
"RAMONHERRERA",
"DIANASOTO",
"CRISACUNA",
"ARONLOPEZ",
"JUANPABLO",
"LUISROBLES1",
"ERIKAMTZ",
"JONACUNA",
"CARLOSN",
"LUCIAGON",
"KELVING",
"FERGALLEGOS",
"YOHALIG",
"PEDROESPARZA",
"KATHYCHAVARRIA",
"EDUARDOVAZQUEZ",
"MANUELG",
"EUNICERIOS",
"HECTORAMADOR",
"BEREPEDREGO",
"JAVIERSOSA",
"OSCARCANO1",
"JESUSOZ",
"JENNIFER1",
"JOSEMORENO",
"ALONDRADURAN",
"PEDRORIVERA",
"ROSAVALDEZ",
"NUBIAGON",
"JESUSAMADOR",
"MIRIAMRDZ",
"HECTORLOBATO",
"SANDRASOTO1",
"MARIAMADOR",
"ESTEBANAMADOR",
"CECILIARIV",
"ANDRESHDZ",
"CONSUELOPEZ",
"LUISSBRAC",
"LUISDONALDO",
"FLUVIANO1",
"EDGARVANEGAS",
"OSMANM",
"MAYRAMTZ",
"JAVIERMONT",
"JOSESOTO",
"MARCOPEREZ",
"ADILENEE",
"CLAUDIAURIAS",
"MARCOCTAVIO",
"JOSEIBARRA1",
"ANDREACHAVEZ",
"STEPHANIEY",
"ELENAVARRO",
"YESENIAC",
"SUJEYVILLANUEVA",
"LUISNORIEGA",
"ELIZABETH1",
"GILCORONADO",
"JESUSNORIEGA",
"ANACUNA",
"FACUNDOM",
"SHEYLAB",
"DAIRYENCINAS",
"JANSELVALEN",
"JORGEVENEGAS",
"FRANCISCO1",
"IDOLINATORRES",
"GUILLERMOFELIX",
"OSCARAMADOR",
"JOHANAM",
"LEONARDO1",
"BERNARDOSOQUI1",
"MARIAPARADA",
"BLANCALOPEZ1",
"JUANITA1",
"MIRNAMADRID",
"YAMELICHAVEZ",
"ROSALVAV",
"ANGELICAR",
"LETICIASILVA",
"IVONESAMA",
"ELIZAIBARRA",
"FRANCISCOL",
"CLAUDIALEYVA",
"JUANCANTUA",
"ARMANDO1",
"LCRUZA",
"ALEROMO",
"JOSERUBEN",
"SILVIAN",
"ANACHRIS",
"CESARANAY",
"JJOSE",
"DULCESALAZAR",
"HECTORG",
"ROSALVAB",
"KORAIMAB",
"RAULCHAVEZ",
"MARIABARAJAS",
"DULCESSALGADO",
"CLAUDIOSOSA",
"JANETH1",
"JAQUELINEG",
"NORMASUAREZ",
"KARINAGON",
"CONSUELOP",
"ADANOLIVAS",
"ANAOLIVAS",
"YADIRAGA",
"MNIEBLAS",
"FBLAINE",
"LAGUNAS1",
"ADILENE1",
"SAMMA1",
"ALEVAZQUEZ",
"JLIRA",
"JORGECHAVEZ",
"SPADILLA1",
"TERESAPINON",
"ALAN1",
"MROSARIO1",
"GREER1",
"LUCIMORENO",
"CHARBELVARGAS",
"ROSAMACH",
"MARCOACUNA1",
"ALMAJACKSON",
"ARRIZON1",
"TOLEDO1",
"PEDROLIRA",
"JOSEROMO",
"MARIAQUIROZ1",
"JUANVALE",
"GLENDASOSA1",
"JESUS1",
"ROSA1",
"ALBERTOMTZ",
"RAQUELM",
"MARCOQ",
"IRENECOTA",
"SERGIO1",
"ARTURO1",
"FCOCORONA",
"CHAVEZ1",
"MONSERRAT1",
"GABRIELA1",
"NATAREN1",
"MARIBEL1",
"ZUJEILY1",
"ERIK1",
"MARIOLEOS",
"ROBERTOVAL",
"BENJACASTRO1",
"LUISALBERTO1",
"TERESA1",
"REYNALDOF1",
"FIGUEROA1",
"YAMELITZA1",
"JORGE1",
"MANUELOLIV",
"MARIAOLIV",
"AURORA1",
"MARCOANTONIO",
"CONCEPCION1",
"KARINACHAV",
"SANTOSB",
"AMADAMORALES",
"JOELULISES",
"GERARDO1",
"AVILA2",
"RAFAELARVIZU1",
"GUADALUPE1",
"ARACELI1",
"NIDIAMORA",
"ARIELMTZ",
"stephanie1",
"ALEGAMEZ",
"JULZACARIAS",
"FERNANDOVALE",
"MARCOVALE",
"BIANCAVALE",
"ALONDRAGLEZ",
"CHAMA",
"DULCEBARAJAS",
"RUELASCARLOS",
"CARLOSMARRUFO1",
"DALIAOLIVARES1",
"IBARRA",
"ACASIOMORENO1",
"GRISGRACIA",
"SALSILVAS",
"ANGELES",
"ELVIRAVARE1",
"YEPSON",
"ALECRUZ",
"JULACUNA",
"FCOESCA",
"RAULDURON1",
"MIGUELESCALANTE1",
"NORBELTRAN",
"MADURAN",
"GILDURAN",
"ZAMCLAUDIA",
"VALTREVIZO",
"TERRYOLIVAR",
"RICANAYA",
"FERESTRADA",
"MISCASTILLO",
"EMMACRUZ",
"GILLOLIVARRIA",
"MAUROSILVAS1",
"PAUCRUZ",
"ANGELBIELMA2",
"ARAESTRADA",
"JONVARELA",
"SILVIALOPEZZ",
"CAMPOSERGIO",
"ALEICEDO",
"ANAFELIX",
"YESZAYAS",
"ALIPENAFLOR",
"MARTAPENAFLOR",
"JOSEFINACHAV",
"SANDRAHIGUERA",
"LAURIANA",
"ANAOLIV",
"RUBENFIMBRES",
"JORGELOYA",
"CESARGASCA",
"ESTEFAGUILAR",
"MARIAQUINONES",
"BRYANVEGAS",
"OMARPEREZ",
"KARLAAGUAYO",
"JOELMONTANO",
"ARMANDOHERMOSILLO",
"JOSEANGULO",
"CARLOSQUIJADA",
"JAVIERFIGUEROA",
"CARLOSNORIEGAF",
"MARIAQUIJADAM",
"ADRIANNSOTO",
"ARACELIALVAREZT",
"BERTHARMENTA",
"DELFINAFIGUEROAA",
"LUISANGELRODRIGUEZ",
"ROSALIABORQUEZ",
"JOSEMARTINEZG",
"JESUSVALENZUELAL",
"RAYMUNDOSERNAM",
"ALDODURAZOM",
"JOSELUISALVAREZ",
"NANCYGARCIACU",
"CARLOSRENDONN",
"KARLADUROND",
"JUANCFOMPEROSA",
"RAMONLUNAA",
"RAMONAATORRES",
"ANAISABELRAMOS",
"LUISOROZCOO",
"OBIELLVALENZUELA",
"JUANNCRUZ",
"MANUELGONZALEZB",
"JESSICAWATSONL",
"ADANNORIEGA",
"CELSAFRANCOC",
"MARIAIVALENZUELA",
"JOSELOPEZGZ",
"MARIAAGONZALEZ",
"ANGELLGONZALEZ",
"CAROLMONTOYA",
"JESUSGARCIAA",
"MARTHALOPEZZ",
"JOSEEAGUIRRE",
"JOSEULICESSIL",
"LEONORMADRIDD",
"JOSEVILLEGASVAZ",
"MARITZALEYVAA",
"BLANCAFRISBYY",
"ROSALIAMTZL",
"ANICCONTRERAS",
"LEOPOLDOURC"]

Rebeca235535= ["luis202020",
"Rebeca2020"]

Sheila235134 = ["JulioMendez",
"LaloFerrer"]

Efren235364=["MarthaGzz",
"Cecilia19",
"CharlieS",
"Valente",
"Marcela",
"Lorena",
"Karina",
"Anahi30",
"Benjamin6",
"Maria67",
"Sylvia25",
"Mary15",
"Memo",
"JuanyS",
"Rosy",
"Imelda",
"Paty",
"IdaliaS",
"Memo22",
"Irisgb",
"Ruby14",
"Rosy50",
"Efren11",
"GabrielM"]

Hector234945 =["Betogza77",
"DanielM20",
"JocelinG2020",
"RosalbaG2020",
"FernandoG20",
"RitaBri",
"Hector74",
"Arianna2020"]

Magic236084 = ["MUSGLY",
"drods",
"preynoso",
"sarai",
"emontane",
"eliatorres",
"cynthiacel",
"carocantu",
"ianaragon",
"mlara",
"valeriaherr",
"dtorres",
"sampayoana",
"thernandez",
"tandrade",
"wgarza",
"sarahit",
"mlozano",
"keryzuniga",
"juanjovill",
"dulcegc",
"deborahzu",
"jacyayala",
"pgalvan",
"marichuy",
"rvillanueva",
"klara",
"estrellardz",
"rlopez",
"garridoe",
"OC0040907448",
"ltovar",
"noradmtz",
"areyes",
"mlreyes",
"chapaivone",
"aalmaguer",
"ragde",
"magalydlg",
"rbrondo",
"mayaaba",
"nalicia",
"amargarita",
"tfrancisco",
"clarivel",
"skat",
"amandavillarreal",
"ahide",
"hildamorales",
"erocha",
"elvgarza",
"rinask",
"OC0040855808",
"dsolis",
"hmorales",
"risela",
"sophiee",
"juanydgarcia",
"dmtz",
"nellymtz",
"edufigueroa",
"caarlaa",
"munozmartinez",
"marymansillas",
"sanchezjuany",
"ckssaenz",
"mmargarita",
"yulaitan",
"wnunez",
"yeseniaavila",
"roosi",
"sibarra",
"bethmedina",
"yakellin",
"berthana",
"orozcoros",
"psolis",
"marijoserdz",
"lrodriguez",
"rositaji",
"carrubal",
"amaldonado",
"moraleslinda",
"silviar",
"ferbenavides",
"aleleon",
"martrod",
"morelalejandra",
"anaad",
"zaletaavila",
"elizondoluz",
"amontalvo",
"Lgarcia02",
"mflores",
"amorales",
"mperez",
"marysolis",
"verogalvan",
"bcamacho",
"alanisv",
"gloriaestrada",
"menriquez",
"mcisneros",
"aari",
"amitis",
"brendarg",
"palvarado",
"bpena",
"zulma",
"sidummi",
"veroal",
"OC0040768482",
"agmaria",
"zapienochoa",
"mariaze",
"freyes",
"joanahndz",
"kzamora",
"terep",
"malvarado",
"OC0040759684",
"America",
"juanigzz",
"claurod",
"evemir",
"rebefuza",
"aidalia",
"ramospaty",
"esmecastane",
"mimargarett",
"rmaria",
"vanevill",
"malu",
"silra",
"lupitadelatorre",
"marthaalva",
"nramirez",
"marlo",
"claususan",
"sergiobla",
"yolafarias",
"patriciam",
"OC0040732890",
"karlario",
"mayrae",
"rericka",
"mmartinez",
"sayuric",
"dianae",
"letysn",
"maldonadoross",
"claurdz",
"erasmop",
"enoch",
"irmacortes",
"wendisara",
"evans",
"lvilla",
"teresalaz",
"mariadelosangelesro",
"dollly",
"isaluna",
"masanjuana",
"brensolis",
"piligarci",
"teremar",
"grisb",
"magavi",
"MIREYAVILL",
"JOSEMARIA1",
"cindyt",
"ANACATALINA",
"maelenam",
"OC0040683765",
"valdez",
"karlayu",
"mherrera",
"araceliaa",
"Mariaelenagzz",
"ALEXANA",
"JOSEGUADALUPER",
"Cathy016"]

Omar237595 = ["MONICAM1",
"FCAVAZOS",
"SILVAR",
"PEREYNOSO1",
"mtz001",
"garzajesus",
"jbecerra",
"drods1",
"OC0041363483",
"destrada",
"dtorres1",
"armandina",
"acatalina01",
"kesquivel",
"ocardoza",
"esthepanie",
"karolc",
"mvillarreal1",
"marthayantonio",
"lgarcia01",
"cesquivel1",
"mmlara",
"erodriguez",
"MUSGLY1",
"rgonzalez",
"allison",
"Apena",
"bvillagomez",
"avillagom",
"javierp",
"almacer",
"mcervantes",
"OC0041038792",
"malvarado1",
"ALEXARF",
"jrodriguez",
"mgonzalez",
"Claurod1",
"valeriag",
"Mherrera01",
"Cathy0016"]

Daniel235092 = ["Zulema",
"danmor82"]

Warner234571 = ["aguilar",
"TRINO",
"SANDRITA",
"Avalos",
"ErnCazares",
"Zuly",
"ClarisaN",
"ColumbaM",
"IsaiOtz",
"BerthaF",
"AdelaHdz",
"EduardoGlvz",
"FranciscoHdz",
"PatyLarios",
"JuanCSanchez",
"AngelicaH",
"ClauMorales",
"MichelleM",
"GuadalupeS",
"JLLarios",
"JoseMRmz",
"GerrdoT",
"EvelinO"]


Faro234553 = ["F109",
"F108",
"F107",
"F106",
"F105",
"F104",
"F103",
"F102",
"F101",
"F100",
"F99",
"F98",
"F97",
"F96",
"F95",
"F94",
"F93",
"F92",
"F91",
"F90",
"F89",
"F88",
"F87",
"F86",
"F85",
"F84",
"F83",
"F82",
"F81",
"F80",
"F79",
"F78",
"F77",
"F76",
"F75",
"F73",
"F72",
"F71",
"F70",
"F69",
"F68",
"F67",
"F66",
"F65",
"F63",
"F62",
"F61",
"F60",
"F59",
"F58",
"F57",
"F55",
"F54",
"F53",
"F52",
"F51",
"F50",
"F49",
"F48",
"F47",
"F46",
"F45",
"F44",
"F43",
"F42",
"F41",
"F40",
"F39",
"F38",
"F37",
"F36",
"F35",
"F34",
"F33",
"F32",
"F31",
"F30",
"F29",
"F28",
"F27",
"F24",
"F26",
"F23",
"F22",
"F21",
"F20",
"F19",
"F18",
"F17",
"F16",
"F15",
"F14",
"F13",
"F12",
"F11",
"F10",
"F09",
"F08",
"F07",
"F06",
"F05",
"F04",
"F03",
"F02",
"F01"]

Mty238567=["OC0041277318",
"Rosario2"]

Monclova234649 = ["OC0041369700",
"OC0041363121",
"OC0041114452",
"OC0041114451",
"OC0041114450",
"OC0041114449",
"OC0041114448",
"OC0040968107",
"OC0040968104",
"OC0040968103",
"OC0040733169",
"OC0040224860",
"OC0040224856",
"OC0040224855",
"OC0040224854",
"OC0040224848",
"OC0040224845",
"OC0040224843",
"OC0040224841",
"OC0040224840",
"OC0040224838",
"OC0040224835",
"OC0040224833",
"OC0040224831",
"OC0040224829",
"OC0040224822",
"OC0040224819",
"OC0040224817",
"OC0040224815",
"OC0040224808",
"OC0040224806",
"OC0040224802",
"OC0040224801",
"OC0040224800",
"OC0040224798",
"OC0040224796",
"OC0040224794",
"OC0040224791",
"OC0040224788",
"OC0040224786",
"OC0040224783",
"OC0040224780",
"OC0040224778",
"OC0040224773",
"OC0040224769",
"OC0040224768",
"OC0040224765",
"OC0040224762",
"OC0040224760",
"OC0040224759",
"OC0040224757",
"OC0040224755",
"OC0040224751"]

Monterrey234647 =["OC0041183515",
"OC0041183514",
"OC0040224622",
"OC0040224611",
"OC0040224602"]

secretkey = "fsefnejdhnfDFEFSDf21335fref$#%^gdrgefqwerefewfefgrgGREGDRSGERgfw3u7u76iyjk21e42edwdEFEWFWE2131257687JITFSHDF"
mongo = PyMongo(app)

key = b'B2BFlaskApplication'

#URL para token de API
url = "https://sts-lonetm.k2net.io/connect/token"

#Datos para obtener token
data_req = {"client_id": 'api_agent', "client_secret": "161b6eb0c6df47848fc15034a936b3",
                    "grant_type": "client_credentials"}

def get_data(request):
    agent = mongo.db.agents.find_one({'agent': request.headers['Agent']})
    data = {"client_id": request.headers['Agent'], "client_secret": agent['key'],
    "grant_type": "client_credentials"}
    return data

#Ruta base
basepath ="https://api-lonetm.k2net.io/api/v1/"

@app.route('/api', methods=['GET'])
@cross_origin()
def index():
    #Se realiza petición
    #header = {"Authorization": str(str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token']))} 
    #games = requests.get(basepath+'agents/api_agent/games', headers=header).json()
    #Se da una respuesta
    response = jsonify({
        'games': "games"
    })
    response.status_code = 200
    return response

@app.route('/api/GetGames', methods=['POST', 'GET'])
@cross_origin()
def GetGames():
    

    #Se realiza petición
    #header = {"Authorization": str(str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token']))} 
    #games = requests.get(basepath+'agents/api_agent/games', headers=header).json()
    #Se da una respuesta

    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")

    print(requests.post(url, get_data(request)).json())

    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")

    
    header = {"Authorization": str(str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token']))} 
    games = requests.get(basepath+'agents/'+request.headers['Agent']+'/games', headers=header).json()
    response = jsonify({
        'games': games
    })
    response.status_code = 200
    return response

@app.route('/api/GetAgents', methods=['GET'])
@cross_origin()
def GetAgentList():
    agents = []
    for agent in  mongo.db.agents.find():
        agents.append(agent['agent'])

    response = jsonify({
        'agents':agents
    })
    response.status_code = 201
    return response

@app.route('/api/GetGameCategories', methods=['POST', 'GET'])
@cross_origin()
def GetGameCategories():
    #Se realiza petición
    header = {"Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])} 
    games = requests.get(basepath+'agents/'+request.headers['Agent']+'/games', headers=header).json()
    categories = []
    #Se da una respuesta
    for game in games:
        categories.append(game['gameCategoryName'])
    categories = list(dict.fromkeys(categories))
    
    finalcategories=[]

    for categorie in categories:
        finalcategories.append({'gameCategoryName': categorie})

    response = jsonify({
        'categories': finalcategories
    })
    response.status_code = 200
    return response

@app.route('/api/signup', methods=['POST'])
@cross_origin()
def Signup():
    print("ok")
    try:
        userName = request.json['userName']
        agent = request.json['agent']
        password = request.json['password']
        email = request.json['email']
        name = request.json['name']
        lastName = request.json['lastName']
        direction1 = request.json['direction1']
        direction2 = request.json['direction2']
        city = request.json['city']
        pc = request.json['pc']
        state = request.json['state']
        phone = request.json['phone']
        now = datetime.now()
        
        hashed_password = sha256_crypt.hash(password)

        mongo.db.users.create_index("email", unique=True)
        mongo.db.users.create_index("userName", unique=True)
        mongo.db.users.create_index("phone", unique=True)
        print("ok2")


        if False:
            response = jsonify({
                'message': "El correo de tu cajero no existe, por favor contactalo para verificar esto."
            })
            response.status_code = 200
            return response
        else:
            print("ok3")
            if mongo.db.users.find_one({'userName':userName}) is None:
                idu = mongo.db.users.insert_one({
                    'userName' : userName,
                    'agent' : agent,
                    'password' : hashed_password,
                    'email' : email,
                    'name' : name,
                    'lastName' : lastName,
                    'direction1' : direction1,
                    'direction2' : direction2,
                    'city' : city,
                    'pc' : pc,
                    'state' : state,
                    'phone' : phone,
                    'Utype': 'playeruser',
                    'FechaDeCreacion': now
                })
                user = {"playerId": userName}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                    } 
                session = requests.Session()
                session.post(basepath+'agents/'+agent+'/players',headers=header,data=user)
                response = jsonify({
                    'message': "Registro exitoso"
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                'message': "El nombre de usuario que elgiste ya se encuentra ocupado"
                })
                response.status_code = 200
                return response
    except Exception as e: 
        print(e)
        response = jsonify({
            'message': "Sus datos ya se encuentran en uso",
            "error": e
        })
        response.status_code = 500
        return response


@app.route('/api/signupMigration', methods=['POST'])
@cross_origin()
def SignupMigration():
    print("ok")
    try:
        userName = request.json['userName']
        password = request.json['password']
        now = datetime.now()
        mail = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

        
        hashed_password = sha256_crypt.hash(password)

        mongo.db.users.create_index("userName", unique=True)


        if userName in Diego234569:
            agent = "Diego234569"
        elif userName in Adriana234590:
            agent = "Adriana234590"
        elif userName in Alejandro234600:
            agent = "Alejandro234600"
        elif userName in Dana234592:
            agent = "Dana234592"
        elif userName in Edi234565:
            agent = "Edi234565"
        elif userName in Gilberto234582:
            agent = "Gilberto234582"
        elif userName in Javier234594:
            agent = "Javier234594"
        elif userName in Marcia234584:
            agent = "Marcia234584"
        elif userName in Marisela234598:
            agent = "Marisela234598"
        elif userName in Rebeca235535:
            agent = "Rebeca235535"
        elif userName in Sheila235134:
            agent = "Sheila235134"
        elif userName in Efren235364:
            agent = "Efren235364"
        elif userName in Hector234945:
            agent = "Hector234945"
        elif userName in Magic236084:
            agent = "Magic236084"
        elif userName in Omar237595:
            agent = "Omar237595"
        elif userName in Daniel235092:
            agent = "Daniel235092"
        elif userName in Warner234571:
            agent = "Warner234571"
        elif userName in Faro234553:
            agent = "Faro234553"
        elif userName in Mty238567:
            agent = "Mty238567"
        elif userName in Monclova234649:
            agent = "Monclova234649"
        elif userName in Monterrey234647:
            agent = "Monterrey234647"

        if False:
            response = jsonify({
                'message': "El correo de tu cajero no existe, por favor contactalo para verificar esto."
            })
            response.status_code = 200
            return response
        else:
            print("ok3")
            if mongo.db.users.find_one({'userName':userName}) is None:

                agentUser = mongo.db.agents.find_one({'agent': agent})

                gameData = {"contentCode": "SMG_108Heroes", "platform": "desktop", "langCode": "es"}
                data = {"client_id": agent, "client_secret": agentUser['key'],
                    "grant_type": "client_credentials"}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, data).json()['token_type'])+ " " + str(requests.post(url, data).json()['access_token'])
                } 
                reqpath ="https://api-lonetm.k2net.io/api/v1/agents/"+agent+"/players/"+userName+"/Sessions"
                session = requests.Session()
                answer = session.post(reqpath,headers=header,data=gameData)
                print(answer.json())

                idu = mongo.db.users.insert_one({
                    'userName' : userName,
                    'email': mail,
                    'phone': mail,
                    'agent' : agent,
                    'password' : hashed_password,
                    'Utype': 'playeruser',
                    'FechaDeCreacion': now
                })
                
                response = jsonify({
                    'message': "Registro exitoso"
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                'message': "El nombre de usuario que elgiste ya se encuentra ocupado"
                })
                response.status_code = 200
                return response
    except Exception as e: 
        print(e)
        response = jsonify({
            'message': "Usuario no disponible para migrar",
            "error": e
        })
        response.status_code = 500
        return response


@app.route('/api/login', methods=['POST'])
@cross_origin()
def Login():
    print("ok")
    try:
        userName = request.json['userName']
        password = request.json['password']
        ip = request.json['ip']
        now = datetime.now()
        print("ok2")

        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
            'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            if sha256_crypt.verify(password, user['password']):
                token = urandom(16).hex()
                mongo_id = str(user.get('_id'))
                encoded_jwt = jwt.encode({"token": token, "id": userName}, secretkey, algorithm="HS256")
                print("ok5")

                updatedquery = { '$set': {
                    'token': token,
                    'lastLogin': now,
                    'active': 1
                }}
                mongo.db.users.update_one({'userName':userName}, updatedquery)
                idip = mongo.db.ip.insert_one({
                    'uId' : userName,
                    'ip': ip,
                    'Ingreso': now
                })
                print(encoded_jwt)
                response = jsonify({
                    'userName': userName,
                    'token': encoded_jwt,
                    'agent': user['agent']
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'message': "Error por favor verifica tus credenciales"
                })
                response.status_code = 401
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/getGame', methods=['POST'])
@cross_origin()
def GetGame():
    print("token")
    userName = request.json['userName']
    game = request.json['game']
    print(game)
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            if user['token'] == decodedToken['token'] and user['active'] ==1:
                gameData = {"contentCode": game, "platform": "desktop", "langCode": "es"}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                    } 
                session = requests.Session()
                answer = session.post(basepath+'agents/'+request.headers['Agent']+'/players/'+decodedToken['id']+'/sessions',headers=header,data=gameData)
                response = jsonify({
                    'url': answer.json()['url']
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'message': "Verifica tus credenciales"
                })
                response.status_code = 200
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/migrate', methods=['GET'])
@cross_origin()
def migrate():
    for agent in  mongo.db.agents.find():
        gameData = {"contentCode": "SMG_108Heroes", "platform": "desktop", "langCode": "es"}
        data = {"client_id": agent['agent'], "client_secret": agent['key'],
            "grant_type": "client_credentials"}
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            "Authorization": str(requests.post(url, data).json()['token_type'])+ " " + str(requests.post(url, data).json()['access_token'])
        } 
        reqpath ="https://api-lonetm.k2net.io/api/v1/agents/"+agent['agent']+"/players/"+agent['agent']+"/Sessions"
        session = requests.Session()
        answer = session.post(reqpath,headers=header,data=gameData)
        print(answer.json())
    response = jsonify({
        'message': "success"
    })
    response.status_code = 201
    return response

@app.route('/api/migratesingle', methods=['GET'])
@cross_origin()
def migrate1():
    gameData = {"contentCode": "SMG_108Heroes", "platform": "desktop", "langCode": "es"}
    data = {"client_id": "Jaime245332", "client_secret": "4aa99a843f3f4283b9e59892523333",
        "grant_type": "client_credentials"}
    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Authorization": str(requests.post(url, data).json()['token_type'])+ " " + str(requests.post(url, data).json()['access_token'])
    } 
    reqpath ="https://api-lonetm.k2net.io/api/v1/agents/Jaime245332/players/gloms/Sessions"
    session = requests.Session()
    answer = session.post(reqpath,headers=header,data=gameData)
    print(answer.json())
    response = jsonify({
        'message': "success"
    })
    response.status_code = 201
    return response

@app.route('/api/migratesingle2', methods=['GET'])
@cross_origin()
def migrate2():
    gameData = {"contentCode": "SMG_108Heroes", "platform": "desktop", "langCode": "es"}
    data = {"client_id": "Jaime245332", "client_secret": "4aa99a843f3f4283b9e59892523333",
        "grant_type": "client_credentials"}
    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Authorization": str(requests.post(url, data).json()['token_type'])+ " " + str(requests.post(url, data).json()['access_token'])
    } 
    reqpath ="https://api-lonetm.k2net.io/api/v1/agents/Jaime245332/players/jleon/Sessions"
    session = requests.Session()
    answer = session.post(reqpath,headers=header,data=gameData)
    print(answer.json())
    response = jsonify({
        'message': "success"
    })
    response.status_code = 201
    return response

@app.route('/api/addCredit', methods=['POST'])
@cross_origin()
def AddCredit():
    userName = request.json['userName']
    token = request.json['token']
    amount = request.json['deposit']
    userToken = request.json['userToken']
    now = datetime.now()
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    udecodedToken = jwt.decode(userToken, secretkey, algorithms="HS256")
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            if user['token'] == decodedToken['token'] and user['active'] ==1:
                jsonreqdata = {"playerId": udecodedToken['id'], "type": "Deposit", "amount": amount}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                    } 
                session = requests.Session()
                answer = session.post(basepath+'agents/api_agent/WalletTransactions',headers=header,data=jsonreqdata)
                jsonreqdata2 = {"playerId": decodedToken['id'], "type": "Withdraw", "amount": amount}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                    } 
                session2 = requests.Session()
                answer2 = session2.post(basepath+'agents/api_agent/WalletTransactions',headers=header,data=jsonreqdata2)
                idcr = mongo.db.transactions.insert_one({
                    'uId' : str(udecodedToken['id']),
                    'aId' : str(decodedToken['id']),
                    'date': now,
                    'type': 'deposit',
                    'amount': amount
                })
                response = jsonify({
                    'message': 'ok'
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'message': "Verifica tus credenciales"
                })
                response.status_code = 200
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/addCreditadmin', methods=['POST'])
@cross_origin()
def AddCreditAdmin():
    userName = request.json['userName']
    token = request.json['token']
    amount = request.json['deposit']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            if user['token'] == decodedToken['token'] and user['active'] ==1:
                jsonreqdata = {"playerId": decodedToken['id'], "type": "Deposit", "amount": amount}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                    } 
                session = requests.Session()
                answer = session.post(basepath+'agents/api_agent/WalletTransactions',headers=header,data=jsonreqdata)
                response = jsonify({
                    'message': 'ok'
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'message': "Verifica tus credenciales"
                })
                response.status_code = 200
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/withdrawCredit', methods=['POST'])
@cross_origin()
def withdrawCredit():
    userName = request.json['userName']
    token = request.json['token']
    now = datetime.now()
    amount = request.json['withdraw']
    userToken = request.json['userToken']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    udecodedToken = jwt.decode(userToken, secretkey, algorithms="HS256")
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            if user['token'] == decodedToken['token'] and user['active'] ==1:
                print(amount)
                jsonreqdata = {"playerId": decodedToken['id'], "type": "Deposit", "amount": amount}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                } 
                session = requests.Session()
                answer = session.post(basepath+'agents/api_agent/WalletTransactions',headers=header,data=jsonreqdata)
                print("ok")
                jsonreqdata2 = {"playerId": udecodedToken['id'], "type": "Withdraw", "amount": amount}
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                } 
                session2 = requests.Session()
                answer2 = session2.post(basepath+'agents/api_agent/WalletTransactions',headers=header,data=jsonreqdata2)
                print("ok2")
                
                idcr = mongo.db.transactions.insert_one({
                    'uId' : str(udecodedToken['id']),
                    'aId' : str(decodedToken['id']),
                    'date': now,
                    'type': 'Withdraw',
                    'amount': amount
                })
                response = jsonify({
                    'message': 'ok'
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'message': "Verifica tus credenciales"
                })
                response.status_code = 200
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/logout', methods=['POST'])
@cross_origin()
def Logout():
    userName = request.json['userName']
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            if user['token'] == decodedToken['token'] and user['active'] ==1:
                updatedquery = { '$set': {
                    'token': '',
                    'lastLogout': now,
                    'active': 0
                }}
                mongo.db.users.update_one({'userName':userName}, updatedquery)
                response = jsonify({
                    'message': "Cerrado de sesion exitosamente"
                })
                response.status_code = 201
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetMasterAgents', methods=['POST'])
@cross_origin()
def GetMasterAgents():
    userName = request.json['userName']
    print(userName)
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    print("1")
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            print("2")
            user = mongo.db.users.find_one({'userName': userName})
            users=[]
            print("3")
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                print("4")
                for usero in  mongo.db.users.find({'Utype':'masteragent'}):
                    print("5")
                    encoded_id = jwt.encode({"id": str(usero.get('_id'))}, secretkey, algorithm="HS256")
                    print(encoded_id)
                    usero['_id'] = encoded_id
                    print("7")

                    usero['password'] = ''
                    users.append(usero)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'mssage':"Acceso restringido"
                })
                response.status_code = 403
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetAgentsList', methods=['POST'])
@cross_origin()
def GetAgents():
    userName = request.json['userName']
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            users=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                for usero in  mongo.db.users.find({'Utype':'agent'}):
                    encoded_id = jwt.encode({"id": str(usero.get('_id'))}, secretkey, algorithm="HS256")
                    usero['_id'] = encoded_id
                    usero['password'] = ''
                    users.append(usero)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                for usero in  mongo.db.users.find({'Utype':'masteragent'}):
                    for user1 in  mongo.db.users.find({'Utype':'agent'}):
                        encoded_id = jwt.encode({"id": str(user1.get('_id'))}, secretkey, algorithm="HS256")
                        user1['_id'] = encoded_id
                        user1['password'] = ''
                        users.append(user1)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'mssage':"Acceso restringido"
                })
                response.status_code = 403
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetCashiers', methods=['POST'])
@cross_origin()
def GetCashiers():
    userName = request.json['userName']
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            users=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='agent':
                for usero in  mongo.db.users.find({'Utype':'cashier'}):
                    encoded_id = jwt.encode({"id": str(usero.get('_id'))}, secretkey, algorithm="HS256")
                    usero['_id'] = encoded_id
                    usero['password'] = ''
                    users.append(usero)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                for user2 in  mongo.db.users.find({'Utype':'masteragent'}):
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            encoded_id = jwt.encode({"id": str(user1.get('_id'))}, secretkey, algorithm="HS256")
                            user1['_id'] = encoded_id
                            user1['password'] = ''
                            users.append(user1)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                for usero in  mongo.db.users.find({'Utype':'agent'}):
                    for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                        encoded_id = jwt.encode({"id": str(user1.get('_id'))}, secretkey, algorithm="HS256")
                        user1['_id'] = encoded_id
                        user1['password'] = ''
                        users.append(user1)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'mssage':"Acceso restringido"
                })
                response.status_code = 403
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetPlayers', methods=['POST'])
@cross_origin()
def GetPlayers():
    userName = request.json['userName']
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            users=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='cashier':
                for usero in  mongo.db.users.find({'Utype':'player'}):
                    encoded_id = jwt.encode({"id": str(usero.get('_id'))}, secretkey, algorithm="HS256")
                    usero['_id'] = encoded_id
                    usero['password'] = ''
                    users.append(usero)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='agent':
                for usero in  mongo.db.users.find({'Utype':'cashier'}):
                    for user1 in  mongo.db.users.find({'Utype':'player'}):
                        encoded_id = jwt.encode({"id": str(user1.get('_id'))}, secretkey, algorithm="HS256")
                        user1['_id'] = encoded_id
                        user1['password'] = ''
                        users.append(user1)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                for user2 in  mongo.db.users.find({'Utype':'masteragent'}):
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                encoded_id = jwt.encode({"id": str(user3.get('_id'))}, secretkey, algorithm="HS256")
                                user3['_id'] = encoded_id
                                user3['password'] = ''
                                users.append(user3)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                for usero in  mongo.db.users.find({'Utype':'agent'}):
                    for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                        for user3 in  mongo.db.users.find({'Utype':'player'}):
                            encoded_id = jwt.encode({"id": str(user3.get('_id'))}, secretkey, algorithm="HS256")
                            user3['_id'] = encoded_id
                            user3['password'] = ''
                            users.append(user3)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response

            else:
                response = jsonify({
                    'mssage':"Acceso restringido"
                })
                response.status_code = 403
                return response

    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetUsers', methods=['POST'])
@cross_origin()
def GetUsers():
    userName = request.json['userName']
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            users=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =="admin":
                for usero in  mongo.db.users.find():
                    print(usero.get('_id'))
                    encoded_id = jwt.encode({"id": str(usero.get('_id'))}, secretkey, algorithm="HS256")
                    print(encoded_id)

                    usero['_id'] = encoded_id
                    usero['password'] = ''
                    #print(usero)
                    users.append(usero)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetUserData', methods=['POST'])
@cross_origin()
def GetUserData():
    usertoken = request.json['usertoken']
    decodedusertoken = jwt.decode(usertoken, secretkey, algorithms="HS256")
    try:
        if mongo.db.users.find_one({'userName': decodedusertoken['id']}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': decodedusertoken['id']})
            ips=[]
            for ipp in mongo.db.ip.find({'uId': decodedusertoken['id']},{'_id':0, 'ip':1, 'Ingreso':1}):
                    ips.append(ipp)
            trans=[]
            for tra in mongo.db.transactions.find({'uId': decodedusertoken['id'], },{'_id':0, 'type':1, 'date':1, 'amount':1}):
                    trans.append(tra)
            header = {"Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])} 
            session = requests.Session()
            resume =  session.get(basepath+'agents/'+request.headers['Agent']+'/players/'+decodedusertoken['id']+'/?properties=balance', headers=header)
            print(resume.json()['balance']['total'])
            ips.reverse()
            trans.reverse()
            response = jsonify({
                'userName':user['userName'],
                'name':user['name'],
                'email':user['email'],
                'phone':user['phone'],
                'uType':user['Utype'],
                'ips':ips,
                'transactions':trans,
                'credit': resume.json()['balance']['total']
            })
            response.status_code = 201
            return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/verifySession', methods=['POST'])
@cross_origin()
def VerifySession():
    pass

@app.route('/api/getIPlog', methods=['POST'])
@cross_origin()
def getIPlog():
    userName = request.json['userName']
    token = request.json['token']
    typeq = request.json['typeq']
    firstdate = request.json['firstdate']
    seconddate = request.json['seconddate']
    onlydate = request.json['onlydate']
    
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            ips=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                if typeq == 'historic':
                    for ip in  mongo.db.ip.find({},{"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='today':
                    end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='yesterday':
                    end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='this month':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='last month':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    lastmonth = now.replace(month=now.month-1)
                    end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='period':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                    seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                    end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='specific':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                    end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response

            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                if typeq == 'historic':
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id'])}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id'])}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id'])}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                elif typeq == 'today':
                    end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                elif typeq == 'yesterday':
                    end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                elif typeq == 'this month':
                    end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                elif typeq == 'last month':
                    lastmonth = now.replace(month=now.month-1)
                    end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                elif typeq == 'period':
                    firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                    seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                    end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                elif typeq == 'specific':
                    onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                    end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    ips.append(ip)

                response = jsonify({
                    'ips':ips
                })
                response.status_code = 201
                return response

    except Exception as e: 
        print(e)
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/getuserprofile', methods=['POST'])
@cross_origin()
def getuserprofile():
    usertoken = request.json['usertoken']
    decodedusertoken = jwt.decode(usertoken, secretkey, algorithms="HS256")
    try:
        if mongo.db.users.find_one({'userName': decodedusertoken['id']}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': decodedusertoken['id']})
            header = {"Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])} 
            session = requests.Session()
            resume =  session.get(basepath+'agents/'+request.headers['Agent']+'/players/'+decodedusertoken['id']+'/?properties=balance', headers=header)
            print(resume.json()['balance']['total'])
            response = jsonify({
                'userName':user['userName'],
                'credits': resume.json()['balance']['total']
            })
            response.status_code = 201
            return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/changepassword', methods=['POST'])
@cross_origin()
def changepassword():
    usertoken = request.json['usertoken']
    password = request.json['password']
    passwordnew = request.json['passwordnew']
    decodedusertoken = jwt.decode(usertoken, secretkey, algorithms="HS256")
    try:
        if mongo.db.users.find_one({'userName': decodedusertoken['id']}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': decodedusertoken['id']})
            if sha256_crypt.verify(password, user['password']):
                hashed_password = sha256_crypt.hash(passwordnew)
                updatedquery = { '$set': {
                    'password': hashed_password
                }}
                mongo.db.users.update_one({'userName':user['userName']}, updatedquery)
                response = jsonify({
                    'message': 'password changed'
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({
                    'message': "Error por favor verifica tus credenciales"
                })
                response.status_code = 401
                return response
    except:
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

#http://www.geoplugin.net/json.gp?ip=<Ip del usuario>
@app.route('/api/getLocationlog', methods=['POST'])
@cross_origin()
def getLocationlog():
    userName = request.json['userName']
    token = request.json['token']
    typeq = request.json['typeq']
    firstdate = request.json['firstdate']
    seconddate = request.json['seconddate']
    onlydate = request.json['onlydate']
    
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            ips=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                if typeq == 'historic':
                    for ip in  mongo.db.ip.find({},{"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='today':
                    end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='yesterday':
                    end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='this month':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='last month':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    lastmonth = now.replace(month=now.month-1)
                    end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='period':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                    seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                    end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response
                elif typeq=='specific':
                    #print(calendar.monthrange(now.year, now.month)[1])
                    onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                    end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for ip in  mongo.db.ip.find({'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):
                        ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                        ip['uId'] =""
                        session = requests.Session()
                        resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                        ip['country'] = resume.json()['geoplugin_countryName']
                        ip['city'] = resume.json()['geoplugin_city']
                        ips.append(ip)
                    ips.reverse()
                    print(ips)
                    response = jsonify({
                        'ips':ips
                    })
                    response.status_code = 201
                    return response

            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                if typeq == 'historic':
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id'])}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id'])}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id'])}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                elif typeq == 'today':
                    end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                elif typeq == 'yesterday':
                    end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                elif typeq == 'this month':
                    end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                elif typeq == 'last month':
                    lastmonth = now.replace(month=now.month-1)
                    end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                    start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                elif typeq == 'period':
                    firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                    seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                    end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                elif typeq == 'specific':
                    onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                    end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                    start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for ip in  mongo.db.ip.find({'uId':str(usero['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for ip in  mongo.db.ip.find({'uId':str(user1['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                ip['uId'] =""
                                session = requests.Session()
                                resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                ip['country'] = resume.json()['geoplugin_countryName']
                                ip['city'] = resume.json()['geoplugin_city']
                                ips.append(ip)
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                for ip in  mongo.db.ip.find({'uId':str(user3['_id']), 'Ingreso':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "ip":1, "Ingreso":1}):    
                                    ip['userName'] = mongo.db.users.find_one({"_id": ObjectId(ip['uId'])})['userName']
                                    ip['uId'] =""
                                    session = requests.Session()
                                    resume =  session.get('http://www.geoplugin.net/json.gp?ip='+ip['ip'])
                                    ip['country'] = resume.json()['geoplugin_countryName']
                                    ip['city'] = resume.json()['geoplugin_city']
                                    ips.append(ip)

                response = jsonify({
                    'ips':ips
                })
                response.status_code = 201
                return response

    except Exception as e: 
        print(e)
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/gettranslog', methods=['POST'])
@cross_origin()
def gettranslog():
    userName = request.json['userName']
    token = request.json['token']
    typeq = request.json['typeq']
    firstdate = request.json['firstdate']
    seconddate = request.json['seconddate']
    userUserName = request.json['userUserName']
    onlydate = request.json['onlydate']
    typetrans = request.json['type']
    
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            transactions=[]
            if typetrans != "":
                if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                    if typeq == 'historic':
                        for transaction in  mongo.db.transactions.find({"type": typetrans},{"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='today':
                        end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}, "type": typetrans}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='yesterday':
                        end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}, "type": typetrans}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='this month':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                        start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}, "type": typetrans}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='last month':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        lastmonth = now.replace(month=now.month-1)
                        end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                        start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}, "type": typetrans}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='period':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                        seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                        end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}, "type": typetrans}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='specific':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                        end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start},"type": typetrans}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response

            else:
                if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                    if typeq == 'historic':
                        for transaction in  mongo.db.transactions.find({},{"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='today':
                        end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='yesterday':
                        end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='this month':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                        start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='last month':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        lastmonth = now.replace(month=now.month-1)
                        end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                        start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='period':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                        seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                        end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                    elif typeq=='specific':
                        #print(calendar.monthrange(now.year, now.month)[1])
                        onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                        end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                        for transaction in  mongo.db.transactions.find({'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):
                            transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                            transaction['uId'] =""
                            transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                            transaction['aId'] =""
                            transactions.append(transaction)
                        transactions.reverse()
                        print(transactions)
                        response = jsonify({
                            'transactions':transactions
                        })
                        response.status_code = 201
                        return response
                elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                    if typeq == 'historic':
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id'])}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id'])}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id'])}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                    elif typeq == 'today':
                        end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                    elif typeq == 'yesterday':
                        end = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                    transaction['aId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                    elif typeq == 'this month':
                        end = now.replace(day=calendar.monthrange(now.year, now.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                        start = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                    transaction['aId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                    elif typeq == 'last month':
                        lastmonth = now.replace(month=now.month-1)
                        end = lastmonth.replace(day=calendar.monthrange(lastmonth.year, lastmonth.month)[1],hour=23, minute=59, second=59, microsecond=999999)
                        start = lastmonth.replace(day=1,hour=0, minute=0, second=0, microsecond=0)
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                    transaction['aId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                    elif typeq == 'period':
                        firstdate = datetime.strptime(firstdate, '%Y-%m-%d')
                        seconddate = datetime.strptime(seconddate, '%Y-%m-%d')
                        end = seconddate.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = firstdate.replace(hour=0, minute=0, second=0, microsecond=0)
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                    transaction['aId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                    elif typeq == 'specific':
                        onlydate = datetime.strptime(onlydate, '%Y-%m-%d')
                        end = onlydate.replace(hour=23, minute=59, second=59, microsecond=999999)
                        start = onlydate.replace(hour=0, minute=0, second=0, microsecond=0)
                        for usero in  mongo.db.users.find({'Utype':'agent'}):
                            for transaction in  mongo.db.transactions.find({'uId':str(usero['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)
                            for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                                for transaction in  mongo.db.transactions.find({'uId':str(user1['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                    transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                    transaction['uId'] =""
                                    transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                    transaction['aId'] =""
                                    transactions.append(transaction)
                                for user3 in  mongo.db.users.find({'Utype':'player'}):
                                    for transaction in  mongo.db.transactions.find({'uId':str(user3['_id']), 'date':{'$lt': end, '$gte': start}}, {"_id": 0, "uId": 1, "aId":1, "date":1, "type":1, "amount":1}):    
                                        transaction['userName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['uId'])})['userName']
                                        transaction['uId'] =""
                                        transaction['agentName'] = mongo.db.users.find_one({"_id": ObjectId(transaction['aId'])})['userName']
                                        transaction['aId'] =""
                                        transactions.append(transaction)

                    response = jsonify({
                        'transactions':transactions
                    })
                    response.status_code = 201
                    return response

    except Exception as e: 
        print(e)
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response

@app.route('/api/GetPlayCheck', methods=['POST'])
@cross_origin()
def GetPlayCheck():
    userName = request.json['userName']
    token = request.json['token']
    decodedToken = jwt.decode(token, secretkey, algorithms="HS256")
    now = datetime.now()
    try:
        if mongo.db.users.find_one({'userName':userName}) is None:
            response = jsonify({
                'message': "Verifica tus credenciales"
            })
            response.status_code = 200
            return response
        else:
            user = mongo.db.users.find_one({'userName': userName})
            users=[]
            if user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='admin':
                for user2 in  mongo.db.users.find({'Utype':'masteragent'}):
                    for usero in  mongo.db.users.find({'Utype':'agent'}):
                        for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                            for user3 in  mongo.db.users.find({'Utype':'player'}):
                                playdata = {"utcOffset": -6, "langCode": "es"}
                                header = {
                                    'Accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                    "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                                    } 
                                session = requests.Session()
                                answer = session.post(basepath+'agents/api_agent/players/'+str(user3['_id'])+'/betVisualizers',headers=header,data=playdata)
                                print(answer.json()[1])
                                user3['url'] = answer.json()[1]['url']
                                encoded_id = jwt.encode({"id": str(user3.get('_id'))}, secretkey, algorithm="HS256")
                                user3['_id'] = encoded_id
                                user3['password'] = ''
                                users.append(user3)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response
            elif user['token'] == decodedToken['token'] and user['active'] ==1 and user['Utype'] =='masteragent':
                for usero in  mongo.db.users.find({'Utype':'agent'}):
                    for user1 in  mongo.db.users.find({'Utype':'cashier'}):
                        for user3 in  mongo.db.users.find({'Utype':'player'}):
                            playdata = {"utcOffset ": -6, "langCode ": "es"}
                            header = {
                                'Accept': 'application/json',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "Authorization": str(requests.post(url, get_data(request)).json()['token_type'])+ " " + str(requests.post(url, get_data(request)).json()['access_token'])
                                } 
                            session = requests.Session()
                            answer = session.post(basepath+'agents/api_agent/players/'+str(user3['_id'])+'/betVisualizers',headers=header,data=playdata)
                            user3['url'] = answer.json()['url']
                            encoded_id = jwt.encode({"id": str(user3.get('_id'))}, secretkey, algorithm="HS256")
                            user3['_id'] = encoded_id
                            user3['password'] = ''
                            users.append(user3)
                users.reverse()
                print(users)
                response = jsonify({
                    'users':users
                })
                response.status_code = 201
                return response

            else:
                response = jsonify({
                    'mssage':"Acceso restringido"
                })
                response.status_code = 403
                return response

    except Exception as e: 
        print(e)
        response = jsonify({
            'message': "Verifica tus credenciales"
        })
        response.status_code = 500
        return response



#correr aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)