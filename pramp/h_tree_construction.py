def draw_line(x1, y1, x2, y2):
    pass


def draw_h_tree(x, y, length, depth):
    """iteration
    :type x: float
    :type y: float
    :type length: float
    :type depth: float
    :rtype: void
    """
    queue, _queue = [(x, y)], []

    for _ in range(depth):
        for x, y in queue:
            x1 = x - length / 2
            y1 = y + length / 2
            x2 = x + length / 2
            y2 = y - length / 2

            draw_line(x1, y1, x1, y2)
            draw_line(x2, y1, x2, y2)
            draw_line(x1, y, x2, y)

            _queue.append((x1, y1))
            _queue.append((x1, y2))
            _queue.append((x2, y1))
            _queue.append((x2, y2))

        queue, _queue = _queue, []
        length /= 2 ** 0.5


def draw_h_tree2(x, y, length, depth):
    """recursion
    :type x: float
    :type y: float
    :type length: float
    :type depth: float
    :rtype: void
    """
    if depth == 0:
        return

    x1 = x - length / 2
    y1 = y + length / 2
    x2 = x + length / 2
    y2 = y - length / 2

    draw_line(x1, y1, x1, y2)
    draw_line(x2, y1, x2, y2)
    draw_line(x1, y, x2, y)

    _length = length / (2 ** 0.5)
    _depth = depth - 1

    draw_h_tree2(x1, y1, _length, _depth)
    draw_h_tree2(x1, y2, _length, _depth)
    draw_h_tree2(x2, y1, _length, _depth)
    draw_h_tree2(x2, y2, _length, _depth)
