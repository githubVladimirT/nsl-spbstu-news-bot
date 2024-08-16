import modules.sitelookup as sitelookup
import modules.vkgrouplookup as vkgrouplookup

msg = """<u>{}</u>

<b>{}</b>

{}
___
@nslspbstu &#8592; Новости ЕНЛ СПБГПУ
"""


def mk_msg_site() -> (list, str|None):
    messages = []

    site_news, err = sitelookup.lookup_for_updates()
    if err:
        return [], err
    for new in site_news:
        site_message = msg.format(*new.values())
        messages.append(site_message)

    return messages, None
