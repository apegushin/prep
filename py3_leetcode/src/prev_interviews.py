from collections import deque

def cd_dir(cur_wd: str, cdto: str) -> str:
    if len(cdto) == 0: return cur_wd

    if cdto.startswith('/'):
        cur_wd = ''
        cdto = cdto[1:]

    res_stack = deque(cur_wd[1:].split('/') if len(cur_wd) > 1 else [])
    for e in cdto.split('/'):
        if e == '.' or (e == '..' and len(res_stack) == 0):
            continue
        elif e == '..' and len(res_stack) > 0:
            res_stack.pop()
        else:
            res_stack.append(e)
    return '/' + '/'.join(list(res_stack))
