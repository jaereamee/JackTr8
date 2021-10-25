# Instructions
1. Download the API from [Interactive Brokers](https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/)

# Algotrading
Thus it is good that I’m learning options using their platform, familiarises with their tools. When migrating to algo trading (quick note: I think best to use limited upside and downside strats when algo trading, if not will quickly snowball), I can quickly integrate the 2 worlds. 

Algo for income! Just keep doing iron condors. 1 month rolling everyweek. Look, S&P doesn’t fluctuate more than 10% a month. 

Algo can also be used to automate closing strategies, these help close positions quickly.
1. however, I am worried about volume, strike prices far out have low vol and hence liquidity.
https://github.com/quantopian/zipline 

## Interactive Brokers (IBKR) API
Might be good, can trade sg and hk markets (certain shares can).
https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/ 
http://interactivebrokers.github.io/tws-api/order_submission.html 
Can use this, if TD Ameritrade proves unusable
https://www.youtube.com/watch?v=-UdWguw90g4 ← haha nice

1. port changed from 7496 to 7497 (for demo)
2. *Must i have the TWS open in order to use it? Why?*
   1. yes need. This is an Access Method.
   2. You can use TWS for dev, then transit to [IB Gateway](https://www.interactivebrokers.com/en/index.php?f=1539&p=comparison2), which is a GUI-less access method that can keep running on your com
   3. Alternatively, look at Client Portal API which uses standard RESTful API.
3. Basic task: request stock price. Use the `reqMktData()` method
   1. Wa, i think each market data request is a snapshot request, which they charge $0.01 per request.
      1. <mark>Oh ok, its only for Regulatory Snapshots. These are the exact live quotes, the default is Streaming Data Snapshots which are free.</mark>
   2. `354 Requested market data is not subscribed.Delayed market data is available.`
      1. Need to specify delayed data via RTD [link](https://interactivebrokers.github.io/tws-api/delayed_data.html) 
      2. set this on the EClient class via reqMarketDataType
         1. I set it after instantiating the class. Not in the class itself. *But actually it should work within the class definition too what*

## OTHER APIs I EXPLORED

### TD Ameritrade APIs
https://developer.tdameritrade.com/content/getting-started –> TD Ameritrade API.
https://pypi.org/project/td-ameritrade-python-api/ 
The sales tells me there’s a 6+ week wait time. Shag.
1. accounts and trading
	1. create an account to obtain the Consumer Key or client_id
	2. Also get the OAuth User ID
		1. when I used the testing browser page, it pulled this: P7N1B5FEY6HFBIMTFYBC0SHMAWPX9DX5. Is this my perma OAuth token?
			1. <mark>No this is just your client ID. You still nid your bearer access token.</mark>
	3. Access token: https://developer.tdameritrade.com/authentication/apis/post/token-0: get an access token. And also to supply the “resource URL” which will specify your accountId.
		1. That link will help you get. They have 2 types. “Refresh token” and “authorization code”.
			1. https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#:~:text=The%20OAuth%202.0%20authorization%20code%20flow%20is%20described%20in%20section,apps%2C%20and%20natively%20installed%20apps. 
			2. ![authentication flow](flow.png)
		2. Response type: code, token, id_token and combinations of each. https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html 
		3. <mark>What is “URL Decoded Auth Code”??? (this is for the “code” field in the API reference website). Use a URL Decoder to decode the response you get. </mark>
		4. How to get refresh token.
			1. Yes it expires after 30min.
			2. The python lib by alex reed does it automatically :)
	4. <mark>I had to open localhost to the web.</mark>
		1. <mark>Control Panel > Programs > Turn Windows features on or Off > Check on “Internet information Services” and “Internet information Services Hostable Web core” </mark>
	5. When doing this authenticaiton with a local app. Follow this: https://developer.tdameritrade.com/content/simple-auth-local-apps 
		1. make the app call the “authentication” URL there.

2. You can use the SG account with it. Separately you need to create a developer account.
3. Redirect URI? Consumer key?
	1. Consumer key is created once your TD Ameritrade app is successfully registered. It is also known as the client_id
	2. Redirect URI – for now I just put 127.0.0.1 (localhost)
4. Calling from python script: flask or django
	1. https://www.youtube.com/watch?v=jpWZyd4fU7c → python program that makes HTTP requests to TD ameritrade’s API.
   
https://tlc.thinkorswim.com/center/reference/thinkScript → thinkScript.
	ThinkScript is not an API, just a language that you use in their platform.

### Tiger Brokers API
https://quant.itiger.com/openapi/py-docs/zh-cn/docs/intro/framework.html#method 
https://quant.itiger.com/openapi/py-docs/zh-cn/docs/intro/quickstart.html 
actually don’t think its very comprehensive.. they have scraps of code here and there