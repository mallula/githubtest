import requests
import hashlib
import sys

def request_api_char(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char

    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'error fetching{res.status_code},check the api and run again')
    return res

def passwords_leaks_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())

    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    first5_char,tail=sha1password[:5],sha1password[5:]
    response=request_api_char(first5_char)

    return passwords_leaks_count(response,tail)
def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times,you should consider other password')
        else:
            print(f'{password} is not found. good Choice!')
    return

if __name__=='__main__':
    main(sys.argv[1:])