#streamlit
 
import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge")
st.title("Growth Mindset Challenge: Web App With Streamlit")

st.header("Welcome To Your Growth Journey!")
st.write("Turn challenges into opportunities, learn from every setback, and unlock your full potential. This AI-powered app helps you develop a growth mindset through reflection, challenges, and achievements!")

# Quotes Section 

st.header("Today's Quote ")
st.write('"The only way to do great work is to love what you do." - Steve Jobs')

# Challenge Section
st.header("What's The Challenge Today?")
user_input = st.text_input("Describe the Challenge you're facing:")

#Condition


if user_input:
    st.success(f"You're facing: {user_input}. and remember, every challenge is a step forward. Stay persistent—you're learning and improving with every attempt! ")
else:
    st.warning("Tell us about your challenge to get started!")    


# Reflection
st.header("Reflect On Your Learning ")
reflection = st.text_input("Write about your learning through this challenge here:")


if reflection:
    st.success(f"Every challenge, big or small, is a step toward growth. What you've learned:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")


# Achievements

st.header("Celebrate Your Wins!")
achievement = st.text_input("Share Something You Have recently Accomplished:")

if achievement:
    st.success("Congrats on Your Achievement! Every step forward is a win—keep pushing toward greatness!")
else:
    st.info("Big or Small, Every Achievement Counts! Share One Now!")


# Footer

st.write("_ _ _")
st.write("Trust yourself and keep going. Growth is a journey, not a race.") 
st.write("Created By Ahmed Faraz")
