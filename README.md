# ReCoal GUI Testnet Wallet

This is a fork of the **Sumokoin GUI Wallet**: https://github.com/sumoprojects/SumoGUIWallet
It is changed to be compatible with ReCoal.


1. Install dependencies (with Python 2.7):

	* Generally, you can use Python `pip` to install required components:
		
			pip install PySide, requests, psutil
	
	* or
			
			pip install -r requirements.txt 
	
	* On some OSes, PySide may be required to install from pre-built packages. For example, on Ubuntu 16.04, install PySide with the following command:
			
			sudo apt install python-pyside


2. Build/download ReCoal binaries from [ReCoal repo](https://github.com/ReCoal/recoal/releases) and put it to `Resources/bin` sub-directory.

3. Run the wallet (Python 2.7):
		
		cd /path/to/RecoalGUIWallet
		python wallet.py

4. Contribution

	Pull-requests and help is always welcome. If you want to buy me a beer:
	
	XMR and BTC donations can be made to **donate.recoal.org**
	
		The Monero donation address is: 41iFUpFHqSnSoxJEADGPTihZXTtCpJUTLiaSh19Hdp5QePmVQ8DmdxgbfqCUUHH9CPC9t2Fwnwgg8cFs18jNvKUxAi4vrhJ 
		(viewkey: 1a79b8bf1159417d183f4c7ec473051e889f42b0d7f7d40a1457bc3663ee3f01)

		The Bitcoin donation address is: 19R69NNM4BAwSTcuJ8UjUCxcLBPyek9K8a
		The BitcoinCash donation address is: 1HWx1jcp4jhcBe3ztMZstMw939rP2DJag9
		The Litecoin donation address is: LbjuGwve9PwfSSkA4VZBANzuFNDfBc17Wx
