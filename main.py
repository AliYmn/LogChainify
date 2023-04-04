# import hashlib

# from web3 import Web3

# # Alchemy ile bağlantıyı kurun
# provider_url = 'https://eth-sepolia.g.alchemy.com/v2/HlNOBPDY2HkiEMjsURLkvVsqLr62xSdX'
# w3 = Web3(Web3.HTTPProvider(provider_url))

# # Özel anahtarınızı ve hesap adresinizi kullanarak hesabınıza erişin
# private_key = '8f2deb54b49343260ccd099a2b1378dcda3895e24ab2221ba494a2381fc01bd0'
# account = w3.eth.account.from_key(private_key)

# # Akıllı sözleşmenin adresini ve ABI'sini sağla
# contract_address = '0x8a8a68da704B7552aE5F776d0CD5719B46a4d03a'  # Remix IDE'den aldığınız adres
# contract_abi = [
#     {
#         "anonymous": False,
#         "inputs": [
#             {"indexed": True, "internalType": "address", "name": "_from", "type": "address"},
#             {"indexed": False, "internalType": "uint256", "name": "_timestamp", "type": "uint256"},
#             {"indexed": False, "internalType": "string", "name": "_data", "type": "string"},
#         ],
#         "name": "LogDataStored",
#         "type": "event",
#     },
#     {
#         "inputs": [
#             {"internalType": "uint256", "name": "_userId", "type": "uint256"},
#             {"internalType": "string", "name": "_data", "type": "string"},
#         ],
#         "name": "storeData",
#         "outputs": [],
#         "stateMutability": "nonpayable",
#         "type": "function",
#     },
#     {
#         "inputs": [{"internalType": "uint256", "name": "_user", "type": "uint256"}],
#         "name": "getLogCountByUser",
#         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
#         "stateMutability": "view",
#         "type": "function",
#     },
#     {
#         "inputs": [{"internalType": "uint256", "name": "userId", "type": "uint256"}],
#         "name": "getLogEntries",
#         "outputs": [
#             {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
#             {"internalType": "address[]", "name": "", "type": "address[]"},
#             {"internalType": "string[]", "name": "", "type": "string[]"},
#             {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
#         ],
#         "stateMutability": "view",
#         "type": "function",
#     },
#     {
#         "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
#         "name": "logEntries",
#         "outputs": [
#             {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
#             {"internalType": "address", "name": "sender", "type": "address"},
#             {"internalType": "string", "name": "data", "type": "string"},
#             {"internalType": "uint256", "name": "user", "type": "uint256"},
#         ],
#         "stateMutability": "view",
#         "type": "function",
#     },
# ]

# # Akıllı sözleşmeye bağlan
# contract = w3.eth.contract(address=contract_address, abi=contract_abi)


# # Log verisi gönderme fonksiyonunu tanımla
# def get_log_entry(user_id):
#     result = contract.functions.getLogEntries(user_id).call()
#     timestamps, senders, datas, users = result
#     return list(zip(timestamps, senders, datas, users))


# def get_log_count(user_id):
#     count = contract.functions.getLogCountByUser(user_id).call()
#     return count


# def send_log_data(user_id, log_data):
#     nonce = w3.eth.get_transaction_count(account.address)
#     transaction = contract.functions.storeData(user_id, log_data).build_transaction(
#         {
#             'gas': 300000,
#             'gasPrice': w3.to_wei('50', 'gwei'),
#             'nonce': nonce,
#         }
#     )
#     signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
#     txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
#     # txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

#     print(f'Log verisi gönderildi. İşlem hash: {txn_hash.hex()}')
#     print(f'link: https://sepolia.etherscan.io//tx/{txn_hash.hex()}')


# balance = w3.eth.get_balance(account.address)
# print(f"Hesap bakiyesi: {w3.from_wei(balance, 'ether')} Ether")

# # Test log verisi gönderin
# user_id = 123345352  # Örnek kullanıcı ID'si
# log_content = str(user_id) + "12345 deneme logasdqwe"
# log_data = hashlib.sha256(log_content.encode('utf-8')).hexdigest()

# send_log_data(user_id, log_data)

# user_address = account.address  # Kullanıcı adresini hesap adresi olarak kullan
# log_count = get_log_count(user_id)
# print(f'Toplam log sayısı (kullanıcı adresine göxre): {log_count}\n')

# entries = get_log_entry(user_id)

# for i, entry in enumerate(entries):
#     timestamp, sender, data, user = entry
#     print(f'Log {i + 1}:')
#     print(f'\tKullanıcı ID: {user}')
#     print(f'\tZaman damgası: {timestamp}')
#     print(f'\tGönderen adres: {sender}')
#     print(f'\tVeri: {data}')
