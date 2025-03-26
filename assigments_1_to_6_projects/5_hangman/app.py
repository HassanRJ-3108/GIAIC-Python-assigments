import streamlit as st
import random
import string

# Set page configuration
st.set_page_config(page_title="Hangman Game", page_icon="🎮")

st.title("Hangman Game")
st.subheader("Guess the word before the hangman is complete!")

# Word list
WORDS = [
    "python", "streamlit", "hangman", "computer", "programming", 
    "keyboard", "developer", "challenge", "learning", "algorithm",
    "software", "hardware", "internet", "database", "function",
    "variable", "condition", "loop", "framework", "debugging",
    "frontend", "backend", "fullstack", "deployment", "repository",
    "terminal", "javascript", "typescript", "artificial", "intelligence",
    "machine", "learning", "neural", "network", "recursion",
    "optimization", "encryption", "cybersecurity", "authentication",
    "authorization", "cloud", "server", "hosting", "domain",
    "container", "docker", "kubernetes", "scalability", "performance",
    "responsive", "interface", "experience", "user", "design",
    "database", "query", "sql", "nosql", "schema", "migration",
    "testing", "unittest", "pytest", "debug", "logging"
]


# Initialize session state variables
if 'word' not in st.session_state:
    st.session_state.word = random.choice(WORDS)
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = set()
if 'wrong_guesses' not in st.session_state:
    st.session_state.wrong_guesses = 0
if 'max_wrong_guesses' not in st.session_state:
    st.session_state.max_wrong_guesses = 6
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'win' not in st.session_state:
    st.session_state.win = False

# Function to reset the game
def reset_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed_letters = set()
    st.session_state.wrong_guesses = 0
    st.session_state.game_over = False
    st.session_state.win = False

# Function to display hangman ASCII art
def display_hangman(wrong_guesses):
    stages = [
    """
                    ----------
                    |              |
                    |        
                    |        
                    |        
                    |        
    """,
    """
                    ----------
                    |              |
                    |              O  
                    |        
                    |        
                    |        
    """,
    """
                    ----------
                    |              |
                    |              O  
                    |              |  
                    |        
                    |        
    """,
    """
                    ----------
                    |              |
                    |              O  
                    |             /|  
                    |        
                    |        
    """,
    """
                    ----------
                    |              |
                    |              O  
                    |             /|\\  
                    |        
                    |        
    """,
    """
                    ----------
                    |              |
                    |              O  
                    |             /|\\  
                    |             /    
                    |        
    """,
    """
                    ----------
                    |              |
                    |              O  
                    |             /|\\  
                    |             / \\  
                    |        
    """
    ]

    return stages[wrong_guesses]

# Sidebar with game instructions
with st.sidebar:
    st.header("Game Instructions")
    st.markdown("""
    1. Try to guess the hidden word one letter at a time
    2. Each incorrect guess adds a part to the hangman
    3. You can make 6 incorrect guesses before the game ends
    4. Guess the word before the hangman is complete to win!
    """)
    
    # New game button
    if st.button("New Game"):
        reset_game()
        st.rerun()

# Main game area
col1, col2 = st.columns([3, 2])

with col1:
    # Display the word with guessed letters revealed
    st.subheader("Guess the Word:")
    
    word_display = ""
    all_guessed = True
    
    for letter in st.session_state.word:
        if letter in st.session_state.guessed_letters:
            word_display += letter + " "
        else:
            word_display += "_ "
            all_guessed = False
    
    # Check if player has won
    if all_guessed and not st.session_state.game_over:
        st.session_state.game_over = True
        st.session_state.win = True
    
    # Display word with large, spaced letters
    st.markdown(f"<h1 style='letter-spacing: 5px;'>{word_display}</h1>", unsafe_allow_html=True)
    
    # Display game status
    st.markdown(f"**Wrong Guesses:** {st.session_state.wrong_guesses}/{st.session_state.max_wrong_guesses}")
    
    # Progress bar for wrong guesses
    wrong_progress = st.session_state.wrong_guesses / st.session_state.max_wrong_guesses
    st.progress(wrong_progress)
    
    # Display letters for selection
    if not st.session_state.game_over:
        st.markdown("### Select a letter:")
        
        # Create 3 rows of letters
        alphabet = string.ascii_lowercase
        rows = [alphabet[:9], alphabet[9:18], alphabet[18:]]
        
        for row in rows:
            cols = st.columns(len(row))
            for i, letter in enumerate(row):
                with cols[i]:
                    # Disable button if letter already guessed
                    disabled = letter in st.session_state.guessed_letters
                    
                    # Create the button
                    if st.button(
                        letter.upper(),
                        key=f"btn_{letter}",
                        disabled=disabled,
                        use_container_width=True
                    ):
                        # Add letter to guessed letters
                        st.session_state.guessed_letters.add(letter)
                        
                        # Check if letter is in the word
                        if letter not in st.session_state.word:
                            st.session_state.wrong_guesses += 1
                            
                            # Check if player has lost
                            if st.session_state.wrong_guesses >= st.session_state.max_wrong_guesses:
                                st.session_state.game_over = True
                        
                        st.rerun()
    
    # Game over message
    if st.session_state.game_over:
        if st.session_state.win:
            st.success("🎉 Congratulations! You guessed the word correctly!")
            st.balloons()
        else:
            st.error("😢 Game Over! You ran out of attempts.")
            st.markdown(f"The word was: **{st.session_state.word.upper()}**")
        
        # Play again button
        if st.button("Play Again"):
            reset_game()
            st.rerun()

with col2:
    # Display hangman ASCII art
    st.subheader("Hangman:")
    st.text(display_hangman(st.session_state.wrong_guesses))
    
    # Display guessed letters
    st.subheader("Guessed Letters:")
    
    if st.session_state.guessed_letters:
        # Separate correct and incorrect guesses
        correct_guesses = [letter for letter in st.session_state.guessed_letters if letter in st.session_state.word]
        incorrect_guesses = [letter for letter in st.session_state.guessed_letters if letter not in st.session_state.word]
        
        # Display correct guesses
        if correct_guesses:
            st.markdown("**Correct:**")
            correct_str = " ".join([letter.upper() for letter in sorted(correct_guesses)])
            st.markdown(f"<p style='color:green; font-size:20px;'>{correct_str}</p>", unsafe_allow_html=True)
        
        # Display incorrect guesses
        if incorrect_guesses:
            st.markdown("**Incorrect:**")
            incorrect_str = " ".join([letter.upper() for letter in sorted(incorrect_guesses)])
            st.markdown(f"<p style='color:red; font-size:20px;'>{incorrect_str}</p>", unsafe_allow_html=True)
    else:
        st.write("No letters guessed yet.")
