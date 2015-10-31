import requests
import json
import r_error as r

NUMBER_OF_WORDS = 6
UNIQUE_WORDS = True
RANDOM_ORG_API_KEY = None # your API key here

def formulate_JSON():
    def read_max():
        with open("lst_mx_vl.txt") as f:
            for ln in f:
                return ln
    max = read_max()
    return json.dumps({"jsonrpc": "2.0",
                "method": "generateIntegers",
                "params": {
                    "apiKey": RANDOM_ORG_API_KEY,
                    "n": NUMBER_OF_WORDS,
                    "min": 0,
                    "max": max,
                    "replacement": UNIQUE_WORDS,
                    "base": 10
                },
                "id": 420
                })

def get_response():
    response = json.loads(requests.post("https://api.random.org/json-rpc/1/invoke", data = formulate_JSON()).text)
    try:
        data = response["result"]["random"]["data"]
    except KeyError:
        code, msg = response["error"]["code"], response["error"]["message"]
        raise r.r_error(code, msg)
    return set(data)

def get_words():
    nmbrs = get_response()
    pswd = ""
    with open("words.txt", 'r') as f:
        for indx, wrd in enumerate(f):
            if nmbrs:
                if indx in nmbrs:
                    pswd += wrd.strip() + " "
                    nmbrs.remove(indx)
            else:
                break
    return pswd[:-1]

if __name__ == "__main__":
    print(get_words())
