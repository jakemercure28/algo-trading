# algo-trading

This is an algoithmic trading simulation that utilizes moving average stock price to determine buy and sell orders.

Installation instructions:

linux

*In terminal*

  1. xcode-select --install
  2. sudo apt install python3
  3. git clone https://github.com/jakemercure28/algo-trading
  4. python3 main.py
  
  
Mac
  Install xcode command line arguments and homebrew
    1. xcode-select --install
    2. /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  Run program
    1. brew install python3
    2. git clone https://github.com/jakemercure28/algo-trading
    3. python3 main.py
  

Results:


Cash: 26563
Stock quan: 334
Stock equity: 7014
Algo Total: 33577

Cash 2: 9392
Stock quan 2: 0
Stock equity 2: 0
HODL Total: 9392

Both accounts start with $10,000 and endure the same stock movement. The algo trader makes trades as the price moves while the
HODL method stricly buys and sells at the end of the period. 
