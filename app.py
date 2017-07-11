import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('MTn2latTZ4NmBnuah67007iRDPdliDVKkpxR1yb5IGpzTARdjzAqSnLmhkvew0EqfNs3wDSQuTc8j/DUfKCoPFpV3ECtur1KUxyiRd1jZjeS9JA7yJXlkuK6l6/WkCJEKDybBDiRMdFbYxtFlRYOmQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('adbb3952c8bc75b90664aa5ededbbbec')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

	# hadist
            if '/hd' in msg:
                arg = msg.split('-');
                if len(arg) > 1:
                    imam = arg[0][3:].strip();
                    nom = arg[1].strip();
                    x='wget http://hadits.stiba.ac.id/\?imam\='+imam+'\&no\='+nom+'\&type\=hadits -qO - | awk \''+'BEGIN{IGNORECASE=1;FS=\"<div class=\\"ja-newsitem\\"'+' style=\\"width: 100%;\\">|</div>";RS=EOF} {print $13}\''
                    proc=subprocess.Popen(x, shell=True, stdout=subprocess.PIPE) 
                    xx=proc.communicate()[0].strip();
                    pr = xx.replace('<p class="arab">','')
                    pr = pr.replace('<p class="indo">','')
                    pr = pr.replace('<h3>Terjemahan</h3>','Terjemahan : ')
                    pr = pr.replace('</p>','')
                    pr = pr.replace('<p>','')
                    if len(pr) == 51:
                        receiver.sendMessage('Not Found')
                    else:
                        receiver.sendMessage(pr)
                else :
                    helps  = '== help ==\n'
                    helps += '[*]tirmidzi => (At Tirmidzi) \n[*]abudaud => (Abu Daud)\n[*]ahmad => (Ahmad)\n[*]bukhari => (Bukhari)\n[*]darimi => (Ad Darimi)\n[*]ibnumajah => (Ibnu Majah) \n[*]malik => (Malik)\n[*]muslim => (Muslim)\n[*]nasai => (An Nasa\'i)\n\ncontoh: /hd darimi-63\n\n* mencari hadist imam (ad darimi) nomer 63'
                    receiver.sendMessage(helps)
