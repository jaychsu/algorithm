MSG_TEMPLATE = {
    'starting': 'starting tests...',
    'finished': 'finished tests.',
}

def show_msg(status, msg_custom=None, *, msg_type=None, add_break=False):
    if not msg_type and not msg_custom:
        return

    msg = []

    if msg_type and msg_type in MSG_TEMPLATE:
        msg.append(MSG_TEMPLATE[msg_type])

    if msg_custom:
        msg.append(str(msg_custom))

    msg = ' '.join(msg)
    template = '{0}: {1}'

    if add_break:
        template += '\n'

    msg = template.format(status, msg)

    print(msg)
    return msg

def starting_test(status):
    show_msg(status, msg_type='starting')

def finished_test(status):
    show_msg(status, msg_type='finished', add_break=True)
