from brownie import FundMe, network, accounts, config
from brownie import MockV3Aggregator as Mock
from dotenv import load_dotenv
from web3 import Web3 as w

env = load_dotenv()

# addr = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
LOCAL_BLOCKCHAIN_ENV = ["development", "local-ganache"]
DECIMAL = 18
STARTING_PRICE = 200000000000



def deploy_funding():
	account = get_account()
	if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
		pricefeed_addr = config["networks"][network.show_active()]["eth_usd_pricefeed"]
	else:
		deploy_mock()
		pricefeed_addr = Mock[-1].address

	funding = FundMe.deploy(pricefeed_addr, {"from": account},
				publish_source=config["networks"][network.show_active()].get("verify"))
	print(f"deployed to {funding.address}")




def main():
	deploy_funding()

##### useful functions #####

def get_account():
	if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
		acct = accounts[1]
		return acct
	else:
		return accounts.add(config["wallets"]["from_keys"])

def deploy_mock():
	print(f"Active network: {network.show_active()}")
	print("mock contract is being deployed...")
	if len(Mock) <= 0:
		Mock.deploy(DECIMAL, STARTING_PRICE, {"from": get_account()})
	print("mock deployment complete")
