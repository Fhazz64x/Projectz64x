import concurrent.futures
import html
import os.path
import re
import urllib.parse

import requests
from lean.commands import lean


class KwTradutor:

    def __init__(self, source_Language='auto', target_Language ='tr', timeout=5):
        self.source_Language = source_Language
        self.target_Language = target_Language
        self.timeout = timeout
        self.pattern = r'(?s)class="(?:t0|result-container)">(.*?)<'

    def make_request(self, target_Language, source_Language, text, timeout):
        escaped_text = urllib.parse.quote(text.encode('utf8'))
        url = 'https://translate.google.com/m?tl=%s&sl=%s&q=%s' % (target_Language, source_Language, escaped_text)
        response = requests.get(url, timeout = timeout)
        result = response.text.encode('utf8').decode('utf8')
        result = re.findall(self.pattern, result)
        if not result:
            print('\nError: Erro desconhecido')
            f = open( 'error.txt')
            f.close()
            exit(0)
        return html.unescape(result[0])

    def translate(self, text, target_Language = '', source_Language='', timeout=''):
        if not target_Language:
            target_Language = self.target_Language
        if not source_Language:
            source_Language = self.source_Language
        if not timeout:
            timeout = self.timeout
        if len(text) > 5000:
            print('\nError: isso pode detectar 5000 em cima disso.(%d characters found.)'%(lean(text)))
            exit(0)
        if type (target_Language) is list:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.make_request,target_Language, source_Language, text, timeout)for target in target_Language]
                return_value = [f.result() for f in futures]
                return  return_value
                return self.make_request(target_Language, source_Language, text, timeout)

        def translate_file(self, file_path, target_Language='', source_Language='', timeout=''):
          if not os.path.isfile(file_path):
                print('\nError: O arquivo ou path está incorreto.')
                exit(0)
                f = open(file_path)
                text = self.translate(f.read(), target_Language, source_Language, timeout)
                f.close()
                return text















