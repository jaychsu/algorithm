def merge_mail(data):
    """group owners if their mails got a connection
    >>> merge_mail({
    ...     'A1': ['a1@gmail.com', 'a2@gmail.com'],
    ...     'A2': ['b1@gmail.com', 'a2@gmail.com'],
    ...     'A3': ['c1@gmail.com'],
    ...     'A4': ['c1@gmail.com', 'd1@gmail.com'],
    ...     'A5': ['b1@gmail.com', 'e1@gmail.com'],
    ... })
    [['A1', 'A2', 'A5'], ['A3', 'A4']]

    >>> merge_mail({
    ...     'A1': ['a1@gmail.com', 'a2@gmail.com'],
    ...     'A2': ['b1@gmail.com', 'a2@gmail.com'],
    ...     'A3': ['b1@gmail.com', 'c1@gmail.com'],
    ...     'A4': ['c1@gmail.com', 'd1@gmail.com'],
    ...     'A5': ['b1@gmail.com', 'e1@gmail.com'],
    ... })
    [['A1', 'A2', 'A3', 'A4', 'A5']]
    """
    owners = {}  # owners
    mail2owners = {}  # mail to owners

    for owner, mails in data.items():
        find(owners, owner)
        for mail in mails:
            if mail not in mail2owners:
                mail2owners[mail] = owner
                continue
            mail2owners[mail] = connect(
                owners, owner, mail2owners[mail]
            )

    ans = {}
    for k, v in owners.items():
        if v not in ans:
            ans[v] = []
        ans[v].append(k)
    return list(ans.values())

def connect(nodes, a, b):
    _a = find(nodes, a)
    _b = find(nodes, b)
    if _a is not _b:
        nodes[_a] = _b
    return _b

def find(nodes, a):
    if a not in nodes:
        nodes[a] = a
        return a
    if nodes[a] is a:
        return a
    nodes[a] = find(nodes, nodes[a])
    return nodes[a]
