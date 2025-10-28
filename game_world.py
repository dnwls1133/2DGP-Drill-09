# layer 0: Background Objects
# layer 1: Character Objects
# layer 2 : Foreground Objects

world = [[],[]]

# 월드에 객체 추가
def add_object(o,depth=0):
    world[depth].append(o)

def add_objects(ol,depth=0):
    world[depth] += ol

# 월드 전체의 객체들을 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

# 월드 전체의 객체들을 렌더링
def render():
    for layer in world:
        for o in layer:
            o.draw()
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    else:
        print("객체가 월드에 없습니다.")