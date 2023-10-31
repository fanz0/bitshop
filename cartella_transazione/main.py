from configparser import ConfigParser
from web3 import Web3
from web3.middleware import geth_poa_middleware

# read config.ini
config = ConfigParser()
configFilePath = "cartella_transazione\config.ini"
config.read(configFilePath)

# accoun details section
account = config.get('Account_Details', 'account')
private_key = config.get('Account_Details', 'private_key')

#connection details section
http_rpc_url = config.get('Connection_Details', 'http_rpc_url')

# connect the ethereum blockchain
w3 = Web3(Web3.HTTPProvider(http_rpc_url))

# middleware - between public web3 and provider(node)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# basic web3
def web3_basics():
    print("Block Number: ", w3.eth.block_number)
    print("Account Balance: ", w3.from_wei(w3.eth.get_balance(account), 'ether'))
    print("Account Transaction (nonce): ", w3.eth.get_transaction_count(account))

# transfer ETH
def transfer_eth():
    
    # nonce
    nonce = w3.eth.get_transaction_count(account)
    
    # create a transaction
    transaction = {
        'nonce': nonce,
        'to': "0xAFC5c04D023334F42B370DE4990550708a08e511", # recipient account address
        'value': w3.to_wei(0.1, 'ether'), # eth amount in wei
        'gas': 2000000,
        'gasPrice': 20000000000
    }
    
    # sign transaction
    signed_trx = w3.eth.account.sign_transaction(transaction, private_key)
    
    # send signed transaction
    trx_hash = w3.eth.send_raw_transaction(signed_trx.rawTransaction)
    print("ETH transfer transaction hash: ", w3.to_hex(trx_hash))

    # some other functions
    print("Transaction: " ,w3.eth.get_transaction(trx_hash))
    w3.eth.wait_for_transaction_receipt(trx_hash)
    print("Transaction Receipt: ", w3.eth.get_transaction_receipt(trx_hash))

# transfer erc20
def transfer_erc20():
    token_address = "0xb50c4BCFF34458ef0b579e257925A269c25c9765"
    token_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"},{"name":"data","type":"bytes"}],"name":"ApproveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]'
    token_contract = w3.eth.contract(token_address, abi=token_abi)

    # token balance
    token_balance = token_contract.functions.balanceOf(account).call()
    print("Token Balance: ", token_balance/100)

    # token details
    print("Token Name: ", token_contract.functions.name().call())
    print("Token Symbol: ", token_contract.functions.symbol().call())
    print("Total Supply: ", token_contract.functions.totalSupply().call())

    # erc20 transfer
    nonce = w3.eth.get_transaction_count(account)
    transaction = token_contract.functions.transfer('0x16710B3a974dae516045Faa94a2BD796139a632D', 100).build_transaction({
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    trx_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    print("ERC20 transfer transaction hash: ", w3.to_hex(trx_hash))


if __name__ == '__main__':
    # web3_basics()
    # transfer_eth()
    transfer_erc20()