# blockchain_ledger
## Usage
![PyChain with added blocks](https://github.com/billysco/blockchain_ledger/blob/main/Screenshots/Pychain.PNG)

![Validated Blockchain](https://github.com/billysco/blockchain_ledger/blob/main/Screenshots/pychain_validated.PNG)
This project aims to create a fully functional blockchain. To start, a 'Record' class is created, which stores the sender id, the recipient id, and the amount that the sender wants to send. Next, a block class is created, which contains the recod class, the creator id of the creator of the clock, the hash of the previous block, and the nonce (number only used once) of the block. Also included in the block class is the hash_block method. This method uses the sha256 function to encrypt the record, creator id, timestamp, previous hash, and nonce. The final class created is the blockchain itself. This class consists of the chain, which is a list of the blocks, and the mining difficulty. This class also consists of several methods. The first is proof_of_work, this method determines the has dificulty and prints 'winning hash' once the correct hash has been calculated. The second method is add_block, this method adds the block to the blockchain once the block is returned from proof_of_work. The final method within the PyChain class is is_valid, this method ensures that the block hashes do not change and is validated every time a new block is added. Finally, this project includes streamlit code to turn the project into a web application to be used by other users. As shown in the above images, the webpage allows users to enter values for sender, recipient, value (how much of the currency they want to send), add the block, adjust the mining dificulty (the length of the hash), and test the validity of the whole blockchain.

## Technologies
This is written in python using hashlib, streamlit, dataclasses, typing, and pandas.

## Creator
William Scolinos | billyscolinos1@gmail.com
