

***⚠️USE THIS REPO AT YOUR OWN RISK***


 
***Telegram Botu [Telegram YaramazRobot](http://telegram.dog/YaramazRobot)***




[![YaramazRobot](https://i.hizliresim.com/3m7Efj.jpg)]


## Kurulum

Kolay Yöntem Heroku Deploy Etmek🤗.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/matesa/YaramazRobot.git)





## Credits
Thanks for;
[intiqam](https://t.me/intiqam)







### Yapılandırma


Botunuzu yapılandırmanın iki olası yolu vardır: config.py dosyası veya ENV değişkenleri.

Tercih edilen sürüm, config.pytüm ayarlarınızı bir arada gruplandırılmış olarak görmeyi kolaylaştırdığı için bir dosya kullanmaktır . Bu dosya tg_bot , __main__.pydosyanın yanında klasörünüze yerleştirilmelidir . Bot jetonunuzun, veritabanı URI'nizin (bir veritabanı kullanıyorsanız) ve diğer ayarlarınızın çoğunun yükleneceği yer burasıdır.

Yapılandırmanızın sample_config'de ayarlanan tüm varsayılanları içermesini sağlayacağı için, sample_config'i içe aktarmanız ve Config sınıfını genişletmeniz önerilir, böylece yükseltmeyi kolaylaştırır.

Örnek bir config.pydosya şunlar olabilir:
```
from YaramazRobot.sample_config import Config


class Development(Config):
    OWNER_ID = 736706850  # my telegram ID
    OWNER_USERNAME = "Charlie_jin"  # my telegram username
    CASH_API_KEY = None # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = None # Get one from https://timezonedb.com/register
    API_OPENWEATHER = False #Get API_OPENWEATHER FROM OFFICAL SITE https://da.gd/VAW3
    AI_API_KEY = None # Coffeehouse chatbot api key, get one from https://coffeehouse.intellivoid.info/
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-418132342' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [736706850 1199252608]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
```

Bir config.py dosyanız yoksa (heroku üzerinde EG), ortam değişkenlerini kullanmak da mümkündür. Aşağıdaki env değişkenleri desteklenir:
 - `ENV`: Bunu HERHANGİ BİR ŞEY olarak ayarlamak, ortam değişkenlerini etkinleştirir

 - `CASH_API_KEY`:Get one from https://www.alphavantage.co/support/#api-key
 - `TIME_API_KEY`:Get one from https://timezonedb.com/register
 - `API_OPENWEATHER`:Get API_OPENWEATHER FROM OFFICAL SITE https://da.gd/VAW3
 - `AI_API_KEY`:Coffeehouse chatbot api key, get one from https://coffeehouse.intellivoid.info/
 - `WALL_API`:Get one from https://wall.alphacoders.com/api.php

 - `TOKEN`: Your bot token, as a string.
 - `OWNER_ID`: An integer of consisting of your owner ID
 - `OWNER_USERNAME`: Your username

 - `DATABASE_URL`: Your database URL
 - `MESSAGE_DUMP`: optional: a chat where your replied saved messages are stored, to stop people deleting their old 
 - `LOAD`: Space separated list of modules you would like to load
 - `NO_LOAD`: Space separated list of modules you would like NOT to load
 - `WEBHOOK`: Setting this to ANYTHING will enable webhooks when in env mode
 messages
 - `URL`: The URL your webhook should connect to (only needed for webhook mode)

 - `SUDO_USERS`: A space separated list of user_ids which should be considered sudo users
 - `SUPPORT_USERS`: A space separated list of user_ids which should be considered support users (can gban/ungban,
 nothing else)
 - `WHITELIST_USERS`: A space separated list of user_ids which should be considered whitelisted - they can't be banned.
 - `CERT_PATH`: Path to your webhook certificate
 - `PORT`: Port to use for your webhooks
 - `DEL_CMDS`: Whether to delete commands from users which don't have rights to use that command
 - `STRICT_GBAN`: Enforce gbans across new groups as well as old groups. When a gbanned user talks, he will be banned.
 - `WORKERS`: Number of threads to use. 8 is the recommended (and default) amount, but your experience may vary.
 __Note__ that going crazy with more threads wont necessarily speed up your bot, given the large amount of sql data 
 accesses, and the way python asynchronous calls work.
 - `BAN_STICKER`: Which sticker to use when banning people.
 - `ALLOW_EXCL`: Whether to allow using exclamation marks ! for commands as well as /.

### Veri tabanı

Veritabanına bağlı bir modül kullanmak istiyorsanız (örneğin: kilitler, notlar, kullanıcı bilgileri, kullanıcılar, filtreler, karşılama), sisteminize kurulu bir veritabanı olması gerekir. Postgres kullanıyorum, bu yüzden optimum uyumluluk için kullanmanızı tavsiye ederim.

Postgres söz konusu olduğunda, bir debian / ubuntu sistemindeki bir veritabanını böyle kurarsınız. Diğer dağıtımlar değişebilir.

- postgresql yükleyin:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and db name.

***Credits - [İntiqam](https://t.me/intiqam)***
