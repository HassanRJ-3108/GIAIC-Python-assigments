import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(page_title="Guess the Number (User)", page_icon="🎮")
 
st.title("Guess the Number Game")
st.subheader("Can you guess the secret number?")
 
# Initialize session state variables
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = 10
if 'guesses' not in st.session_state:
     st.session_state.guesses = []
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'win' not in st.session_state:
    st.session_state.win = False
if 'min_range' not in st.session_state:
    st.session_state.min_range = 1
if 'max_range' not in st.session_state:
    st.session_state.max_range = 100
if 'hints_used' not in st.session_state:
    st.session_state.hints_used = 0
if 'hint_penalty' not in st.session_state:
    st.session_state.hint_penalty = 2
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'high_scores' not in st.session_state:
    st.session_state.high_scores = []
if 'game_mode' not in st.session_state:
    st.session_state.game_mode = "normal"
if 'time_limit' not in st.session_state:
    st.session_state.time_limit = 60
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'remaining_time' not in st.session_state:
    st.session_state.remaining_time = None

# Function to reset the game
def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.game_started = False
    st.session_state.attempts = 0
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.hints_used = 0
    st.session_state.start_time = None
    st.session_state.remaining_time = None

# Function to calculate score
def calculate_score():
    base_score = 1000
    attempt_penalty = st.session_state.attempts * 50
    hint_penalty = st.session_state.hints_used * (st.session_state.hint_penalty * 50)
    time_bonus = 0
    
    if st.session_state.game_mode == "timed" and st.session_state.win:
        time_used = time.time() - st.session_state.start_time
        time_bonus = max(0, int((st.session_state.time_limit - time_used) * 10))
    
    difficulty_multiplier = {
        "easy": 0.5,
        "normal": 1.0,
        "hard": 1.5,
        "expert": 2.0
    }.get(st.session_state.difficulty, 1.0)
    
    final_score = int((base_score - attempt_penalty - hint_penalty + time_bonus) * difficulty_multiplier)
    return max(0, final_score)

# Function to provide a hint
def get_hint():
    st.session_state.hints_used += 1
    
    # Different types of hints
    hint_types = [
        "digit_sum",
        "even_odd",
        "prime",
        "multiple",
        "digit_count",
        "range_narrowing"
    ]
    
    # If we've used all hint types, start cycling through them again
    hint_type = hint_types[min(st.session_state.hints_used - 1, len(hint_types) - 1) % len(hint_types)]
    
    num = st.session_state.secret_number
    
    if hint_type == "digit_sum":
        digit_sum = sum(int(digit) for digit in str(num))
        return f"The sum of the digits is {digit_sum}."
    
    elif hint_type == "even_odd":
        if num % 2 == 0:
            return "The number is even."
        else:
            return "The number is odd."
    
    elif hint_type == "prime":
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        if is_prime(num):
            return "The number is prime."
        else:
            return "The number is not prime."
    
    elif hint_type == "multiple":
        factors = []
        for i in range(2, 10):
            if num % i == 0:
                factors.append(i)
        
        if factors:
            factor = random.choice(factors)
            return f"The number is a multiple of {factor}."
        else:
            return "The number is not a multiple of any single digit."
    
    elif hint_type == "digit_count":
        return f"The number has {len(str(num))} digit(s)."
    
    elif hint_type == "range_narrowing":
        # Narrow the range by 25%
        range_size = st.session_state.max_range - st.session_state.min_range
        if num < (st.session_state.min_range + range_size // 2):
           return f"The number is in the lower half of the current range."
        else:
            return f"The number is in the upper half of the current range."

# Sidebar with game instructions
with st.sidebar:
    st.header("Game Instructions")
    st.markdown("""
    1. I'm thinking of a number between 1 and 100
    2. Try to guess it in 10 attempts or less
    3. I'll tell you if your guess is too high or too low
    4. Good luck!
    """)
    
    # Display current game settings
    st.divider()
    st.write(f"Range: 1 to 100")
    st.write(f"Max Attempts: {st.session_state.max_attempts}")

# Main game area
# Display game status
st.markdown(f"### Attempts: {st.session_state.attempts}/{st.session_state.max_attempts}")

# Display progress bar
progress = st.session_state.attempts / st.session_state.max_attempts
st.progress(progress)


# Display previous guesses
if st.session_state.guesses:
    st.markdown("### Previous Guesses")
    
    # Text list of guesses with feedback
    for i, guess in enumerate(st.session_state.guesses):  # Yeh line ab sahi indent hui hai
        if guess < st.session_state.secret_number:
            st.markdown(f"Guess #{i+1}: **{guess}** is too low")
        elif guess > st.session_state.secret_number:
            st.markdown(f"Guess #{i+1}: **{guess}** is too high")
        else:
            st.markdown(f"Guess #{i+1}: **{guess}** is correct! 🎉")


# Game in progress
if not st.session_state.game_over:
    # Guess input
    guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=100,
        value=50,
        step=1
    )
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        st.session_state.guesses.append(guess)
        
        # Check if guess is correct
        if guess == st.session_state.secret_number:
            st.session_state.game_over = True
            st.session_state.win = True
            st.rerun()
        
        # Check if max attempts reached
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.session_state.game_over = True
            st.session_state.win = False
            st.rerun()
        else:
            st.rerun()

# Game over state
if st.session_state.game_over:
    # Display game result
    if st.session_state.win:
        st.balloons()
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} correctly!")
        st.markdown(f"You used {st.session_state.attempts} attempts.")
    else:
        st.error(f"😢 Game over! You've used all {st.session_state.max_attempts} attempts.")
        st.markdown(f"The secret number was **{st.session_state.secret_number}**.")
    
    # Play again button
    if st.button("Play Again"):
        reset_game()
        st.rerun()

