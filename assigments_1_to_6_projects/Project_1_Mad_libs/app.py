import streamlit as st
import random

st.set_page_config(page_title="Mad Libs Game", page_icon="📝")

st.title("🎮 Mad Libs Game")
st.markdown("Fill in the blanks to create a funny story!")

# Different story templates
stories = [
    {
        "title": "A Day at the Zoo",
        "template": "Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree. It {verb} {adverb} through the large tunnel that led to its {adjective2} {noun2}. I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. Feeding that animal made me {emotion}!",
        "inputs": ["adjective", "noun", "verb", "adverb", "adjective2", "noun2", "noun3", "emotion"]
    },
    {
        "title": "The Haunted House",
        "template": "Last night, I went to a {adjective} haunted house. The door {verb} open with a {sound} sound. Inside, I saw {number} {noun} floating in the air. A {adjective2} ghost appeared and said '{exclamation}!' I felt so {emotion} that I {verb2} all the way home!",
        "inputs": ["adjective", "verb", "sound", "number", "noun", "adjective2", "exclamation", "emotion", "verb2"]
    },
    {
        "title": "Space Adventure",
        "template": "I'm an astronaut traveling to {planet}. My spaceship is powered by {plural_noun}. When I landed, I met a {adjective} alien with {number} eyes. It offered me some {food} to eat. The alien spoke in a {adjective2} language, but somehow I {adverb} understood. We became {adjective3} friends and explored the {noun} mountains together.",
        "inputs": ["planet", "plural_noun", "adjective", "number", "food", "adjective2", "adverb", "adjective3", "noun"]
    }
]

# Sidebar for story selection
with st.sidebar:
    st.header("Choose a Story")
    story_index = st.radio("Select a story template:", 
                          options=range(len(stories)), 
                          format_func=lambda x: stories[x]["title"])
    
    if st.button("Random Story"):
        story_index = random.randint(0, len(stories) - 1)
        st.rerun()
    
    st.divider()
    st.markdown("### How to Play")
    st.markdown("1. Select a story template")
    st.markdown("2. Fill in the word blanks")
    st.markdown("3. Click 'Generate Story' to see your creation!")

selected_story = stories[story_index]

# Create form for word inputs
with st.form("mad_libs_form"):
    st.subheader(f"Fill in the blanks for: {selected_story['title']}")
    
    # Dictionary to store user inputs
    user_inputs = {}
    
    # Create two columns for inputs to save space
    cols = st.columns(2)
    
    # Generate input fields
    for i, word_type in enumerate(selected_story["inputs"]):
        col_idx = i % 2  # Alternate between columns
        with cols[col_idx]:
            # Format the label to be more readable
            label = word_type.replace("_", " ").title()
            # Add hints for different word types
            hints = {
                "adjective": "(describing word, e.g., silly, purple, soft)",
                "noun": "(person, place, or thing)",
                "verb": "(action word, e.g., run, jump, eat)",
                "adverb": "(describes a verb, usually ends in -ly)",
                "emotion": "(feeling, e.g., happy, scared, excited)"
            }
            hint = hints.get(word_type, "")
            if hint:
                label += f" {hint}"
            
            user_inputs[word_type] = st.text_input(label, key=f"{word_type}_{i}")
    
    # Submit button
    submit_button = st.form_submit_button("Generate Story")

# Display the completed story when form is submitted
if submit_button:
    # Check if all fields are filled
    if all(user_inputs.values()):
        st.success("Story generated successfully!")
        
        # Fill in the template with user inputs
        completed_story = selected_story["template"]
        for word_type, word in user_inputs.items():
            completed_story = completed_story.replace("{" + word_type + "}", word)
        
        # Display the story in a nice container
        st.subheader("Your Mad Libs Story:")
        st.markdown("---")
        st.markdown(f"## {selected_story['title']}")
        st.markdown(completed_story)
        st.markdown("---")
        
        # Add a button to share or save
        if st.button("Create New Story"):
            st.rerun()
    else:
        st.error("Please fill in all the blanks to generate your story!")

# Add some styling and instructions at the bottom
st.markdown("---")
st.markdown("### What are Mad Libs?")
st.markdown("""
Mad Libs is a phrasal template word game where one player prompts another for a list of words to substitute for blanks in a story. 
The game is frequently played as a party game or as a pastime.
""")