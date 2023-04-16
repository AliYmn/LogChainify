import hashlib

from web3 import Web3

private_key = '8f2deb54b49343260ccd099a2b1378dcda3895e24ab2221ba494a2381fc01bd0'
provider_url = 'https://eth-sepolia.g.alchemy.com/v2/HlNOBPDY2HkiEMjsURLkvVsqLr62xSdX'
contract_address = '0x8a8a68da704B7552aE5F776d0CD5719B46a4d03a'
contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "_from", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "_timestamp", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "_data", "type": "string"},
        ],
        "name": "LogDataStored",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_userId", "type": "uint256"},
            {"internalType": "string", "name": "_data", "type": "string"},
        ],
        "name": "storeData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_user", "type": "uint256"}],
        "name": "getLogCountByUser",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "userId", "type": "uint256"}],
        "name": "getLogEntries",
        "outputs": [
            {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
            {"internalType": "address[]", "name": "", "type": "address[]"},
            {"internalType": "string[]", "name": "", "type": "string[]"},
            {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "logEntries",
        "outputs": [
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "string", "name": "data", "type": "string"},
            {"internalType": "uint256", "name": "user", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


class EthereumService:
    def __init__(self, unqiue_id, log_content):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.account = self.w3.eth.account.from_key(private_key)
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def get_log_entry(self, user_id):
        result = self.contract.functions.getLogEntries(user_id).call()
        timestamps, senders, datas, users = result
        return list(zip(timestamps, senders, datas, users))

    def get_log_count(self, user_id):
        count = self.contract.functions.getLogCountByUser(user_id).call()
        return count

    def send_log_data(self, user_id, log_data):
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        transaction = self.contract.functions.storeData(user_id, log_data).build_transaction(
            {
                'gas': 300000,
                'gasPrice': self.w3.to_wei('50', 'gwei'),
                'nonce': nonce,
            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return {
            "hash": txn_hash.hex(),
            "hex": txn_hash.hex(),
        }

    def get_balance(self):
        balance = self.w3.eth.get_balance(self.account.address)
        return self.w3.from_wei(balance, 'ether')
