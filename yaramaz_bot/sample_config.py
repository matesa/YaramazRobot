# Yeni bir config.py oluşturun veya bunu aynı dizindeki config.py dosyası olarak yeniden adlandırın ve içe aktarın, ardından bu sınıfı genişletin.
import json
import os

def get_user_list(config, key):
    with open('{}/yaramaz_robot/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Yeni bir config.py oluşturun veya bunu aynı dizindeki config.py dosyası olarak yeniden adlandırın ve içe aktarın, ardından bu sınıfı genişletin.
class Config(object):
    LOGGER = True

    # GEREKLİDİR
    API_KEY = "BOT TOKEN BURAYA"
    OWNER_ID = "KENDİ İD NUMARANIZ"  # Bilmiyorsanız, botu çalıştırın ve onunla özel sohbetinizde do / id
    OWNER_USERNAME = "BURAYA KULLANICI ADINIZI"

    # ÖNERİLEN
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # herhangi bir veritabanı modülü için gerekli
    MESSAGE_DUMP = None  # mesaj inat 'dan tasarruf' emin olmak için gereken
    GBAN_LOGS = None #KANAL ID BURAYA -
    LOAD = []
    NO_LOAD = ['translation', 'rss']   
    WEBHOOK = False
    URL = None

    # İSTEĞE BAĞLI
    #ID Ayırma biçimi  [1,2,3,4]
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')  # Bot'a sudo erişimi olan kullanıcılar için id'lerin listesi - (kullanıcı adları değil).
    DEV_USERS = get_user_list('elevated_users.json', 'devs')  # Sahiple aynı izinlere sahip olacak geliştiriciler için kimlik listesi - (kullanıcı adları değil)
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')  # gban'a izin verilen, ancak aynı zamanda yasaklanabilen kullanıcılar için id'lerin (kullanıcı adları değil) listesi.
    WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')  # Bot tarafından yasaklanmayan / atılmayan kullanıcılar için kimliklerin (kullanıcı adları değil) listesi.
    CERT_PATH = None
    PORT = 5000 
    DEL_CMDS = False  #Delete, yönetici olmayan birinin kullanması durumunda silme / yasaklama gibi kullanıcıların erişemediği komutlar.
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Kullanılacak alt iş parçacığı sayısı. İşlemcinizin kullandığı iş parçacığı sayısı olarak ayarlayın
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie çıkartması
    ALLOW_EXCL = False  # İzin Ver! komutların yanı sıra /
    CASH_API_KEY = None # https://www.alphavantage.co/support/#api-key adresinden bir tane alın
    TIME_API_KEY = None # https://timezonedb.com/register adresinden bir tane alın
    API_OPENWEATHER = False #Get API_OPENWEATHER RESMİ SİTEDEN ALIN https://da.gd/VAW3
    AI_API_KEY = None # Coffeehouse chatbot api anahtarı https://coffeehouse.intellivoid.info/ adresinden bir tane alın
    WALL_API = None # https://wall.alphacoders.com/api.php adresinden bir tane alın


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
