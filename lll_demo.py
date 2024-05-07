import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt

# We are creating an app that will help demonstrate the Law of Large Numbers. We will do this by simulating a coin flip or dice roll in differing amounts. The user will get to select the number of sides to simulate. 

st.title("Simulating the Law of Large Numbers")
st.subheader("An App by Christopher Stephenson")
st.write(("This is an app to help simulate the Law of Large numbers which states that over the *long run* the probability of an event occuring will make itself apparent. For example, when rolling a 6-sided die 15 times, we wouldn't expect the die to land on each side evenly. However, over the long term (think 100,000 dice rolls), each side will move closer to the expected average of a six-sided dice (each side has about a 17% of appearing on one dice roll)"))

num_sides = st.number_input(label="Number of sides on the dice", min_value=2, max_value=100, value=6)

# Simulate the rolling of a fair n-sided dice 10 times
dice_rolls = [random.randint(1,num_sides) for i in range(10)]

# Count the occurences of each outcome 
counts = [dice_rolls.count(i) for i in range (1, num_sides+1)]
outcomes = list(range(1, num_sides+1))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the results on the axis
ax.bar(outcomes, counts)
ax.set_title('Results of Rolling a Fair N-Sided Dice 10 Times')
ax.set_xlabel('Outcome')
ax.set_ylabel('Frequency')
ax.set_xticks(outcomes)

# Set y-axis ticks to integer values
ax.set_yticks(range(max(counts) + 1))

# Set y-axis tick labels to integers
ax.set_yticklabels([int(i) for i in ax.get_yticks()])

# Display the plot in Streamlit
st.pyplot(fig)

##################################################################################################################
##################################################################################################################

# Simulate the rolling of a fair n-sided dice 100 times
dice_rolls = [random.randint(1,num_sides) for i in range(100)]

# Count the occurences of each outcome 
counts = [dice_rolls.count(i) for i in range (1, num_sides+1)]
outcomes = list(range(1, num_sides+1))

# Create a figure and axis
fig2, ax2 = plt.subplots()

# Plot the results on the axis
ax2.bar(outcomes, counts)
ax2.set_title('Results of Rolling a Fair N-Sided Dice 100 Times')
ax2.set_xlabel('Outcome')
ax2.set_ylabel('Frequency')
ax2.set_xticks(outcomes)

# Calculate the maximum count in increments of 10
max_count_10 = (max(counts) // 10 + 1) * 10

# Set y-axis ticks to integer values in increments of 10
ax2.set_yticks(range(0, max_count_10 + 1, 10))

# Display the plot in Streamlit
st.pyplot(fig2)

##################################################################################################################
##################################################################################################################

# Simulate the rolling of a fair n-sided dice 10,000 times
dice_rolls = [random.randint(1,num_sides) for i in range(10000)]

# Count the occurences of each outcome 
counts = [dice_rolls.count(i) for i in range (1, num_sides+1)]
outcomes = list(range(1, num_sides+1))

# Create a figure and axis
fig3, ax3 = plt.subplots()

# Plot the results on the axis
ax3.bar(outcomes, counts)
ax3.set_title('Results of Rolling a Fair N-Sided Dice 10,000 Times')
ax3.set_xlabel('Outcome')
ax3.set_ylabel('Frequency')
ax3.set_xticks(outcomes)

# Calculate the maximum count in increments of 1,000
max_count_10k = (max(counts) // 1000 + 1) * 1000

# Set y-axis ticks to integer values in increments of 1,000
ax3.set_yticks(range(0, max_count_10k + 1, 1000))

# Display the plot in Streamlit
st.pyplot(fig3)

##################################################################################################################
##################################################################################################################

# Simulate the rolling of a fair n-sided dice 100,000 times
dice_rolls = [random.randint(1,num_sides) for i in range(100000)]

# Count the occurences of each outcome 
counts = [dice_rolls.count(i) for i in range (1, num_sides+1)]
outcomes = list(range(1, num_sides+1))

# Create a figure and axis
fig4, ax4 = plt.subplots()

# Plot the results on the axis
ax4.bar(outcomes, counts)
ax4.set_title('Results of Rolling a Fair N-Sided Dice 100,000 Times')
ax4.set_xlabel('Outcome')
ax4.set_ylabel('Frequency')
ax4.set_xticks(outcomes)

# Calculate the maximum count in increments of 100,000
max_count_100k = (max(counts) // 10000 + 1) * 10000

# Set y-axis ticks to integer values in increments of 100,000
ax4.set_yticks(range(0, max_count_100k + 1, 10000))

# Display the plot in Streamlit
st.pyplot(fig4)