import pushover

PUSHOVER_USER_KEY = "enterkeyhere"
PUSHOVER_APP_TOKEN = "entertokenhere"

sshlogin = open('monitorlog', 'r').read()

pushover.init(PUSHOVER_APP_TOKEN)

pushover.Client(PUSHOVER_USER_KEY).send_message("Login " + sshlogin)

