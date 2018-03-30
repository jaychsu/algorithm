"""
OO Design
设计一个剧院的订座系统，user一次可以query不多于5个座位，
这个系统要能return相应数量并尽可能相连的座位。
用户可以选择订或不订这些位子，订的话这些位子就不available了，
没订的话位子就都还available，
但要求这位用户下次query还是return这些位子（防止用户不停刷系统以拿到他们想要的位子），
除非下次query前这些位子里k个被别人订了，那系统再生成k个available的位子。

My understanding
r1 => 尽可能相连的座位 => MUST be in same row
r2 => requery => same seats if seats are also available,
    otherwise find new available seats and still follow (r1)
"""


class Reservation:
    def __init__(self, m, n):
        pass

    def get_seats(self, user_id, n=0):
        pass
