from brownie import FundMe
from .deploy_funding import get_account



def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entry_fee = fund_me.getEntryFee()
    print("Entry fee: ", entry_fee)
    print("processing")
    fund_me.fund({"from": account, "value": entry_fee})

def withdraw():
    fund_me = FundMe[-1]
    acct = get_account()
    fund_me.withdraw({"from": acct})


def main():
    fund()
    withdraw()