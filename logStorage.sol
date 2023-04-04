pragma solidity ^0.8.0;

contract LogChainify {
    struct LogEntry {
        uint256 timestamp;
        address sender;
        string data;
        uint256 user;
    }

    LogEntry[] public logEntries;

    event LogDataStored(address indexed _from, uint256 _timestamp, string _data);

    function storeData(uint256 _userId, string memory _data) public {
            LogEntry memory newEntry = LogEntry({
                timestamp: block.timestamp,
                sender: msg.sender,
                data: _data,
                user:_userId
            });
            logEntries.push(newEntry);
            emit LogDataStored(msg.sender, block.timestamp, _data);
    }

    function getLogEntries(uint256 userId) public view returns (uint256[] memory, address[] memory, string[] memory, uint256[] memory) {
        uint256 count = 0;
        for (uint256 i = 0; i < logEntries.length; i++) {
            if (logEntries[i].user == userId) {
                count++;
            }
        }
        uint256[] memory timestamps = new uint256[](count);
        address[] memory senders = new address[](count);
        string[] memory datas = new string[](count);
        uint256[] memory users = new uint256[](count);
        uint256 j = 0;
        for (uint256 i = 0; i < logEntries.length; i++) {
            if (logEntries[i].user == userId) {
                timestamps[j] = logEntries[i].timestamp;
                senders[j] = logEntries[i].sender;
                datas[j] = logEntries[i].data;
                users[j] = logEntries[i].user;
                j++;
            }
        }
        return (timestamps, senders, datas, users);
    }

    function getLogCountByUser(uint256 _user) public view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < logEntries.length; i++) {
            if (logEntries[i].user == _user) {
                count++;
            }
        }
        return count;
    }
}
