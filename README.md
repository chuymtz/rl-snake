# Snake Game

This project is a simple implementation of the classic Snake game.

## Features
- Control the snake using arrow keys.
- Eat food to grow the snake.
- Avoid running into the walls or the snake's own body.

## How to Execute
1. Clone the repository:
    ```sh
    git clone https://github.com/chuymtz/snake.git
    ```
2. Navigate to the project directory:
    ```sh
    cd snake
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the game:
    ```sh
    python main.py
    ```

Enjoy playing the Snake game!

## Next Steps

The next step in this project is to use it for a simple demonstration of Reinforcement Learning (RL). The goal is to train an RL agent to play the Snake game autonomously. This involves:
- Defining the state and action space for the RL agent.
- Implementing a reward function to guide the agent's learning process.
- Using an RL algorithm (e.g., Q-learning, Deep Q-Network) to train the agent.

Stay tuned for updates on this exciting development!
