# Encryption Chaos

Encryption Chaos is a fun and interactive Python program that simulates the process of sanitizing text input by randomly shuffling and displaying characters before matching them with the input text. This creates an interesting and somewhat chaotic visual effect as the text is being processed.

## Features

- Converts input text to lowercase
- Randomly shuffles characters
- Simulates a delay for each character to create a visual effect
- Supports alphanumeric characters and basic punctuation (! and ?)

## How It Works

The program takes a string input from the user, converts it to lowercase, and then processes each character by:
1. Randomly shuffling a predefined list of characters.
2. Iterating through the shuffled list and displaying each character until the correct one is found.
3. Adding the matched character to the output string.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/encryption-chaos.git
    ```
2. Navigate to the project directory:
    ```sh
    cd encryption-chaos
    ```

### Usage

1. Run the script:
    ```sh
    python main.py
    ```
2. Enter the word you want to sanitize when prompted:
    ```
    Write word: yourword
    ```
3. Watch the chaotic encryption process in action!

### Example

Write word: he

hj

h3

h2

h0

hs

hf

he
...        
