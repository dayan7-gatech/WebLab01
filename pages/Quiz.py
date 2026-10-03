# ==========================================================
# Name: Dora Ayan
# Class: CS 1301
# Program: Interactive Algebra Quiz
# ==========================================================
# Program Description:
# This program uses Streamlit.
# This program asks algebra questions, displays graphs, and calculates a final score.
# ==========================================================
# Streamlit Info:
# Streamlit is a Python library
# Streamlit converts a Python program into an interactive web app.
# Streamlit creates buttons, sliders, quizzes, graphs, and input boxes.
# ==========================================================
# Import the Streamlit library
import streamlit as st
# ==========================================================
# Import NumPy for graph calculations
import numpy as np
# ==========================================================
# Import Matplotlib for creating graphs
# pyplot is the part of Matplotlib that lets you create and display graphs
# you are importing only the pyplot module from the Matplotlib package, not the entire package.
import matplotlib.pyplot as plt
# ==========================================================
# Display the title of the application
st.title("📚 Algebra Quiz")
# ==========================================================
# Display instructions for the user
st.write("Answer the six questions below and submit your quiz.")
# ==========================================================
# Create a variable to keep track of the score
score = 0
# ==========================================================
# GRAPH 1
# ==========================================================
# Create x-values from -10 to 10
# np=NumPy library
# linspace = "linearly spaced numbers"
# -10 = starting value
# 10 = ending value
# 100 = number of values to create
# So, it creates 100 evenly spaced numbers between -10 and 10 and stores them in x.
x = np.linspace(-10, 10, 100)
# ==========================================================
# Create y-values for the line y = x + 2
# you're generating 100 points on the line image001.png.
y1 = x + 2
# ==========================================================
# creates a figure and an axis for your graph.
# fig1 = the whole graph window (the canvas)
# ax1 = the area where you draw the graph
# plt.subplots() is a Matplotlib function that creates a figure
fig1, ax1 = plt.subplots()
# ==========================================================
# tells Matplotlib to draw a graph using the x-values and y-values.
# ax1 = the graph area (axis)
# .plot() = draw a line graph
# x = values on the horizontal axis
# y1 = values on the vertical axis
ax1.plot(x, y1)
# ==========================================================
# Add a title to the graph
ax1.set_title("Graph 1: y = x + 2")
# ==========================================================
# Display the graph in Streamlit
# st.pyplot(fig1) is a Streamlit function that displays a Matplotlib graph
st.pyplot(fig1)
# ==========================================================
# QUESTION 1 (RADIO BUTTON)
# ==========================================================
# uses the Streamlit function st.radio() to create a multiple-choice question with radio buttons.
# [1, 2, 3, 4] is a list in Python. It contains the answer choices that will appear as radio buttons.
q1 = st.radio(
    "1. What is the slope of y = x + 2?",
    [1, 2, 3, 4]
)
# ==========================================================
# QUESTION 2 (NUMBER INPUT)
# ==========================================================
# Ask the user to solve an equation
# Creates a box where the user can enter a number.
# The up and down arrows increase or decrease the value by 1 each time.
q2 = st.number_input(
    "2. Solve: 2x + 3 = 11",
    min_value=0,
    step=1
)
# ==========================================================
# GRAPH 2
# ==========================================================
# Create y-values for y = x²
y2 = x**2
# Create a figure
fig2, ax2 = plt.subplots()
# Plot the parabola
ax2.plot(x, y2)
# Add title
ax2.set_title("Graph 2: y = x²")
# Display graph
st.pyplot(fig2)
# ==========================================================
# QUESTION 3 (SELECTBOX)
# ==========================================================
# Ask a selectbox question
q3 = st.selectbox(
    "3. Which graph shape represents y = x² ?",
    ["Line", "Parabola", "Circle", "Triangle"]
)
# ==========================================================
# QUESTION 4 (MULTISELECT)
# ==========================================================
# Ask a question with multiple correct answers
q4 = st.multiselect(
    "4. Select all solutions of x² = 9",
    ["-3", "-1", "1", "3"]
)
# ==========================================================
# GRAPH 3
# ==========================================================
# Create y-values for the cubic function
y3 = x**3
# Create another figure
fig3, ax3 = plt.subplots()
# Plot the cubic graph
ax3.plot(x, y3)
# Add graph title
ax3.set_title("Graph 3: y = x³")
# Display graph
st.pyplot(fig3)
# ==========================================================
# QUESTION 5 (SLIDER)
# ==========================================================
# Ask the user to choose a value using a slider
q5 = st.slider(
    "5. Choose the value of x that makes 3x = 12",
    min_value=0,
    max_value=10
)
# ==========================================================
# QUESTION 6 (RADIO BUTTON)
# ==========================================================
# Ask which graph is cubic
q6 = st.radio(
    "6. Which graph shown above is the cubic function?",
    ["Graph 1", "Graph 2", "Graph 3"]
)
# ==========================================================
# SUBMIT BUTTON
# ==========================================================
# Create a button to submit the quiz
if st.button("Submit Quiz"):
    # Reset score before grading
    score = 0
    # Check Question 1
    if q1 == 1:
        score += 1
    # Check Question 2
    if q2 == 4:
        score += 1
    # Check Question 3
    if q3 == "Parabola":
        score += 1
    # Check Question 4
    if set(q4) == {"-3", "3"}:
        score += 1
    # Check Question 5
    if q5 == 4:
        score += 1
    # Check Question 6
    if q6 == "Graph 3":
        score += 1
    # Display the final score
    st.success(f"Your score is {score} out of 6")
    # Give feedback based on the score
    if score == 6:
        # Display balloons animation
        st.balloons()
        st.write("Excellent! Perfect score! 🎉")
    elif score >= 4:
        st.write("Great job! 👍")
    else:
        st.write("Keep practicing Algebra! 📖")
 
