from brownie import FundMe, network, accounts, config
from brownie import MockV3Aggregator as Mock
from dotenv import load_dotenv
from web3 import Web3 as w

env = load_dotenv()

# addr = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"

def funding():
	account = get_account()
	if network.show_active() != "development":
		pricefeed_addr = config["networks"][network.show_active()]["eth_usd_pricefeed"]
	else:
		print(f"Active network: {network.show_active()}")
		print("mock contract is being deployed...")
		mock = Mock.deploy(18, w.toWei(2000, "ether"), {"from": account})
		pricefeed_addr = mock.address
		print("mock deployment complete")
	
	funding = FundMe.deploy(pricefeed_addr, {"from": account},
				publish_source=config["networks"][network.show_active()].get("verify"))
	print(f"deployed to {funding.address}")



def main():
	funding()


def get_account():
	if network.show_active() == "development":
		acct = accounts[1]
		return acct
	else:
		return accounts.add(config["wallets"]["from_keys"])
