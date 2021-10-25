from ibapi.client import EClient # handles all outgoing requests
from ibapi.wrapper import EWrapper # handles all incoming messages (responses)
from ibapi.contract import Contract

import threading
import time

#import for rest api
import json
import requests

class IBapi(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self,self)
        # EClient.reqMarketDataType(self,4) # 1 is live, 2 is frozen, 3 is delayed, 4 is delayed frozen
    def tickPrice(self,reqId, tickType, price, attrib):
        if tickType == 2 and reqId == 1:
            print("the current ask price is: ", price)

def run_loop():
    app.run()

# def client_api_method(): #https://interactivebrokers.github.io/cpwebapi/
#     url = "s"
#     ticker={}
#     ticker.update({ 
#         "apikey":"P7N1B5FEY6HFBIMTFYBC0SHMAWPX9DX5",
#         "symbol":"SPY",
#         "contractType":"", # if the API doesn't recognise the key, it just doesn't reply anything. So no worries about excess keys.
#     })
#     return (json.dumps(requests.get(url,params=ticker).json(),indent=4))


if __name__ == "__main__":
    try: 
        app = IBapi()
        app.connect('127.0.0.1', 7497, 123)
        app.reqMarketDataType(3)

        api_thread = threading.Thread(target=run_loop, daemon=True)
        api_thread.start()

        time.sleep(1) # give time to connect

        apple_contract = Contract()
        apple_contract.symbol = 'AAPL'
        apple_contract.secType = 'STK'
        apple_contract.exchange = 'SMART'
        apple_contract.currency = 'USD'

        """Request market data (non-live). 
        Params: 
            ReqId [int]: user-assigned int to the request which will be included in the response
            Contract Object
            tickType [string]: (optional)if we want to specify the kind of data  https://interactivebrokers.github.io/tws-api/tick_types.html
            Unsubscribed Snapshot [bool]: put false or you pay money
            Subscribed Snapshot [bool]: put false or you pay money
            Internal Use [list]: leave empty
        """
        app.reqMktData(25, apple_contract, '', False, False, [])
        print("now waiting...")
        time.sleep(10)
        app.disconnect()
        
    except KeyboardInterrupt:
        app.disconnect()
        print("end")
    