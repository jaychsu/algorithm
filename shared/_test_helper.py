MSG_TEMPLATE = {
    'starting': 'starting tests...',
    'finished': 'finished tests.',
}

def show_msg(status, *, msg_type=None, msg_custom=None):
    if not msg_type or not msg_custom:
        return

    msg = []

    if msg_type and msg_type in MSG_TEMPLATE:
        msg.append(MSG_TEMPLATE[msg_type])

    if msg_custom:
        msg.append(str(msg_custom))

    template = '{0}: {1}' if len(msg) == 1 else '{0}: {1} {2}'
    print(template.format(status, *msg))
