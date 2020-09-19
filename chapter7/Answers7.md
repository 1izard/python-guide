# Chapter 7 練習問題解答例

## Q 1

### Q 1 - 1

```python
class Task:
    def __init__(self, content, created, deadline):
        self.content = content
        self.created = created
        self.deadline = deadline
        self.finished = False

    def __repr__(self):
        return f"Task(content={self.content}, created={self.created}, deadline={self.deadline}, finished={self.finished})"

    def done(self):
        self.finished = True
```

### Q 1 - 2

```python
from enum import auto


class Task:
    def __init__(self, content, created, deadline):
        self.content = content
        self.created = created
        self.deadline = deadline
        self.finished = False

    def __repr__(self):
        return f"Task(content={self.content}, created={self.created}, deadline={self.deadline}, finished={self.finished})"

    def done(self):
        self.finished = True


class Schedule:
    CREATED = auto()
    DEADLINE = auto()

    def __init__(self, tasks):
        self.tasks = sorted(list(tasks), key=lambda x: x.deadline)

    def __len__(self):
        return len(self.tasks)

    def push(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.deadline)

    def get(self, index):
        return self.tasks[index]

    def top(self):
        return self.get(0)

    def sorted(self, option):
        if option is self.CREATED:
            return sorted(self.tasks, key=lambda x: x.created)
        elif option is self.DEADLINE:
            return list(self.tasks)
        else:
            raise ValueError("Invalid Argument: option must be a class attribute of Schedule.")
```

## Q 2

### Q 2 - 1

```python
class User:
    def __init__(self, email, password):
        self._email = email
        self.password = password
        self._userid = self._make_userid(self.email)

    def __repr__(self):
        return f"User(email={self._email}, password={self.password}, userid={self._userid})"

    def __str__(self):
        return self._userid

    def _make_userid(self, email):
        return email.split("@")[0]

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        self._userid = self._make_userid(self.email)

    @property
    def userid(self):
        return self._userid
```

### Q 2 - 2

```python
class LoginUser:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = passwor
```

### Q 2 - 3

```python
class UserSystem:
    users = []

    @classmethod
    def authorize(cls, login_user):
        for user in cls.users:
            if user.userid == login_user.userid and user.password == login_user.password:
                return user
        return None
```

## Q 3

実行部分は例 1 の場合です．  

```python
from collections import UserList
import random


class StatsList(UserList):
    def __init__(self, data):
        self.data = list(data)

    def mean(self):
        """平均を返す"""
        if len(self) == 0:
            return 0.0

        return sum(self) / len(self)

    def var(self):
        """分散を返す"""
        if len(self) == 0:
            return 0.0

        xm = self.mean()
        v = 0.0
        for x in self:
            v += (x - xm) ** 2
        return v / len(self)
        # (Extra) return sum([(x - xm) ** 2 for x in self])

    def std(self):
        """標準偏差を返す"""
        if len(self) == 0:
            return 0.0

        return self.var() ** 0.5


random.seed(0)
data = []
for _ in range(100_000)
# (Extra) data = [random.random() for _ in range(100_000)]
stats_lst = StatsList(data)

print(f"mean={stats_lst.mean()}")   # mean=0.4994751702579762
print(f"var={stats_lst.var()}")     # var=0.08361639460894141
print(f"std={stats_lst.std()}")     # std=0.28916499547652963
```

## Q 4

実行部分は例 1 の場合です．  

```python
from collections import UserList
from enum import Enum, auto


class Way(Enum):
    BUS = auto()
    TRAIN = auto()


class Direction:
    def __init__(self, name, way, duration, cost):
        self.name = name
        self.way = way
        self.duration = duration
        self.cost = cost


class Route(UserList):
    def __init__(self, directions):
        self.data = list(directions)

    def __str__(self):
        return "->".join([direction.name for direction in self])

    @property
    def durations(self):
        return sum([direction.duration for direction in self])

    @property
    def costs(self):
        return sum([direction.cost for direction in self])


class Navi:
    def __init__(self, routes):
        self.routes = routes

    def _filter(self, way):
        """与えられた交通手段の種類に合致する経路の list を返す"""
        routes = [] # 条件に合致した経路の list
        for route in self.routes:
            way_only = True # 交通手段の種類が way だけかどうかのフラグ
            for direction in route:
                if direction.way is not way:
                    way_only = False  # 経路の中の交通手段が 1 つでも way でないなら抜ける
                    break
            if way_only:
                routes.append(route)  # 交通手段の種類が way だけなら加える
        return routes

    def easiest(self, way=None):
        # Route クラスは UserList を継承しているので len 関数で交通手段の数が返る
        if self.routes is None or len(self.routes) == 0:
            return None

        if way is None:
            routes = self.routes  # way が None なら対象経路は保持している経路ぜんぶ
        elif way in list(Way):
            routes = self._filter(way)  # way が Way メンバーなら対象経路は way に合致する経路のみ
        else:   # None でも Way メンバーでもないなら ValueError 送出
            raise ValueError("Invalid Argument: way must be member of Way class.")

        if len(routes) == 0:
            return None   # 対象経路が 1 つもないなら None を返す

        easiest_route = routes[0]
        for route in self.routes[1:]:
            # 対象経路の中から最も乗り換えの少ない経路を見つける
            if len(route) < len(easiest_route): 
                easiest_route = route
        return easiest_route

    def fastest(self, way=None):
        if self.routes is None or len(self.routes) == 0:
            return None

        if way is None:
            routes = self.routes
        elif way in list(Way):
            routes = self._filter(way)
        else:
            raise ValueError("Invalid Argument: way must be member of Way class.")

        if len(routes) == 0:
            return None

        fastest_route = routes[0]
        for route in self.routes[1:]:
            # 対象経路の中から最も所要時間の短い経路を見つける
            if route.durations < fastest_route.durations:
                fastest_route = route
        return fastest_route

    def cheapest(self, way=None):
        if self.routes is None or len(self.routes) == 0:
            return None

        if way is None:
            routes = self.routes
        elif way in list(Way):
            routes = self._filter(way)
        else:
            raise ValueError("Invalid Argument: way must be member of Way class.")

        if len(routes) == 0:
            return None

        cheapest_route = routes[0]
        for route in self.routes[1:]:
            # 対象経路の中から最も費用の少ない経路を見つける
            if route.costs < cheapest_route.costs:
                cheapest_route = route
        return cheapest_route


route1 = Route([
    Direction("train1", Way.TRAIN, 30, 250),
    Direction("train2", Way.TRAIN, 20, 200),
    Direction("bus1", Way.BUS, 15, 200),
])

route2 = Route([
    Direction("train1", Way.TRAIN, 30, 250),
    Direction("train3", Way.TRAIN, 40, 450),
])

route3 = Route([
    Direction("train4", Way.TRAIN, 35, 300),
    Direction("train5", Way.TRAIN, 50, 400)
])


navi = Navi([route1, route2, route3])
print("easiest |", navi.easiest())      # easiest | train1->train3
print("fastest |", navi.fastest())      # fastest | train1->train2->bus1
print("cheapest |", navi.cheapest())    # cheapest | train1->train2->bus1
print("cheapest by train |", navi.cheapest(Way.TRAIN))     # cheapest by train | train1->train3
```

(Extra)  

TypeHint をつけると次のようになります．  

```python
from collections import UserList
from enum import Enum, auto
from typing import Iterable, List


class Way(Enum):
    BUS = auto()
    TRAIN = auto()


class Direction:
    def __init__(self, name: str, way: Way, duration: int, cost: int):
        self.name = name
        self.way = way
        self.duration = duration
        self.cost = cost


class Route(UserList):
    def __init__(self, directions: Iterable[int]):
        self.data = list(directions)
    
    def __repr__(self) -> str:
        return f"Route({str(self)})"

    def __str__(self) -> str:
        return "->".join([direction.name for direction in self])

    @property
    def durations(self) -> int:
        return sum([direction.duration for direction in self])

    @property
    def costs(self) -> int:
        return sum([direction.cost for direction in self])


class Navi:
    def __init__(self, routes: Iterable[Route]):
        self.routes = routes

    def _filter(self, way) -> List[Route]:
        routes = []
        for route in self.routes:
            only_way = True
            for direction in route:
                if direction.way is not way:
                    only_way = False
                    break
            if only_way:
                routes.append(route)
        return routes

    def easiest(self, way: Way or None = None) -> Route:
        if self.routes is None or len(self.routes) == 0:
            return None

        if way is None:
            routes = self.routes
        elif way in list(Way):
            routes = self._filter(way)
        else:
            raise ValueError("Invalid Argument: way must be member of Way class.")

        if len(routes) == 0:
            return None

        easiest_route = routes[0]
        for route in self.routes[1:]:
            if len(route) < len(easiest_route):
                easiest_route = route
        return easiest_route

    def fastest(self, way: Way or None = None) -> Route:
        if self.routes is None or len(self.routes) == 0:
            return None

        if way is None:
            routes = self.routes
        elif way in list(Way):
            routes = self._filter(way)
        else:
            raise ValueError("Invalid Argument: way must be member of Way class.")

        if len(routes) == 0:
            return None

        fastest_route = routes[0]
        for route in self.routes[1:]:
            if route.durations < fastest_route.durations:
                fastest_route = route
        return fastest_route

    def cheapest(self, way: Way or None = None) -> Route:
        if self.routes is None or len(self.routes) == 0:
            return None

        if way is None:
            routes = self.routes
        elif way in list(Way):
            routes = self._filter(way)
        else:
            raise ValueError("Invalid Argument: way must be member of Way class.")

        if len(routes) == 0:
            return None

        cheapest_route = routes[0]
        for route in self.routes[1:]:
            if route.costs < cheapest_route.costs:
                cheapest_route = route
        return cheapest_route


route1 = Route([
    Direction("train1", Way.TRAIN, 40, 350),
    Direction("train2", Way.TRAIN, 10, 200),
    Direction("bus1", Way.BUS, 10, 200),
])

route2 = Route([
    Direction("train1", Way.TRAIN, 40, 350),
    Direction("bus2", Way.BUS, 40, 350),
])

route3 = Route([
    Direction("train4", Way.TRAIN, 20, 200),
    Direction("bus3", Way.BUS, 30, 200),
    Direction("bus4", Way.BUS, 35, 250),
])


navi = Navi([route1, route2, route3])
print("easiest |", navi.easiest())      # easiest | train1->bus2
print("fastest |", navi.fastest())      # fastest | train1->train2->bus1
print("cheapest |", navi.cheapest())    # cheapest | train4->bus3->bus4
print("cheapest by train |", navi.cheapest(Way.TRAIN))  # cheapest by train | None
```

(ここまで Extra)  

<hr>

[Chapter 7 クラス](Chapter7.md)  
[Index](../README.md)
