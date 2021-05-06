# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib


# Create a Record Data Class that consists of the `sender`, `receiver`, and
# `amount` attributes
@dataclass
class Record:
    sender_id: str
    reciever_id: str
    amount: float


################################################################################
# Step 2:
# Modify the Existing Block Data Class to Store Record Data

@dataclass
class Block:

    # Use an instance of the Record class
    record: Record
    # Set variables for creator_id, previous_hash, time, and nonce
    creator_id: int
    prev_hash: str = 0
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: str = 0
    # Create hash_block function to encrypt the block info
    def hash_block(self):
        # Define sha variable as the sha256 function
        sha = hashlib.sha256()
        # Encode the relevant info
        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)
        # Return hashes of all data attributes
        return sha.hexdigest()


@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    # Create proof_of_work function
    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True

# Streamlit Code
# Adds the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

# Add an input area where you can get a value for `sender` from the user.
sender = st.text_input('Please enter your sender id')

# Add an input area where you can get a value for `receiver` from the user.
receiever = st.text_input('Please enter your recipient id')

# Add an input area where you can get a value for `amount` from the user.
amount = st.text_input('How much would you like to send?')

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`,
    # and `amount` values
    new_block = Block(
        record=Record,
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()

# Streamlit Code (continues)

st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())

