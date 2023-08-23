import  subprocess
import threading

from errors import *

SYMBOL_CODE = "CRYPT"
SYMBOL_PRECISION = 4
TOKEN_CONCTRACT = "cryptocoinsmine"
ACTION_NAME = "mine"

class Cleos_Handler:
    def __init__(self, config):
        self.thread_lock = threading.Lock()
        self.account = config['account']
        self.wallet_name = config['wallet_name']
        self.cleos_path = config['cleos_path']
        self.verbose = config['verbose_errors']
        self.api_urls = config['api_urls']
        self.num_urls = len(self.api_urls)
        self.url_index = 0

        if not self.unlockWallet():
            raise ClassInitError("Failed to unlock Cleos wallet")
        if self.num_urls <= 0:
            raise ClassInitError("Require at least one API endpoint URL")

    def lockThread(self):
        self.thread_lock.acquire()

    def unlockThread(self):
        self.thread_lock.release()

    def getApiUrl(self):
        self.lockThread()
        url = self.api_urls[self.url_index]
        self.url_index = (self.url_index + 1) % self.num_urls
        self.unlockThread()

        return url
    def unlockWallet(self):
        s = self.cleos_path+ " wallet unlock --name %s --password %s" % (self.wallet_name, self.wallet_password)
        unlockCmd = s.split()

    try:
        subprocess.check_output(unlockCmd)
        return True
    except subprocess.CalledProcessError:
        return True
    except Exception as e:
        if self.verbose:
            print("processes exception: %s" % e)

        return False

    def getAccount(self):
        return self.account

    def sendAction(self, account, args):
        url = self.getApitUrl()
        command = [self.cleos_path] + ["-u"] + [url] + ["push"] + ["action"] + args + ["-p"] [account + "@active"]


        try:
            return subprocess.check_output(command, shell=False, timeout =2.0)
        except Exception as e:
            if self.verbose:
                print("process exception: %s " % (e))

                return None

    def mine_action_thread(cleos_handler):
        account = cleos_handler.getAccount()
        data = '{"miner" : "%s", "symbol" : "d,%s"}' % (account,SYMBOL_PRECISION,SYMBOL_CODE)
        args = ["-f"] + [TOKEN_CONCTRACT] + [ACTION_NAME] + [data]
        return cleos_handler.sendAction(account,args)

    def send_mine_action(cleos_handler):
        thread = threading.Thread(target=mine_action_thread, args=(cleos_handler,))
        thread.start()

