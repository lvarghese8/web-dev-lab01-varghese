import streamlit as st
import pandas as pd

st.header("What Type of Household Pet Are You?")
st.write("Answer the questions below to discover what pet matches you best.")

## result scores
dog = 0
cat = 0
fish = 0
bunny = 0

st.image("Images/Pets.jpg", width=200) #NEW

##question 1
q1 = st.slider("Rate how much you enjoy spending time outdoors", 1, 10) #NEW

##question 2
q2 = st.radio("What's your favorite season?", ["Spring", "Summer", "Autumn", "Winter"]) #NEW

##question 3
q3 = st.selectbox("What genre of music do you prefer?", ["Rock", "Jazz", "Indie", "Pop"])#NEW

st.image("Images/music.jpg", width=300)

##question 4
q4 = st.number_input("How many hours per week do you spend studying?",
                     min_value=0, max_value=40) #NEW

##question 5
q5 = st.selectbox("Which meal would you pick?", ["Steak and mashed potatoes", "Tuna salad sandwich", "Spicy seaweed salad", "Pasta with roasted carrots"])


##result
if st.button("See My Result!"):

                  ##q1
                  if q1 <= 2:
                      cat += 1
                  elif 3 <= q1 <= 5:
                      fish += 1
                  elif 6 <= q1 <= 8:
                      bunny +=1
                  else:
                      dog += 1

                  ##q2
                  if q2 == "Spring":
                      bunny += 2
                  elif q2 == "Summer":
                      fish += 2
                  elif q3 == "Autumn":
                      dog += 2
                  else:
                      cat += 2

                  ##q3
                  if q2 == "Spring":
                      bunny += 2
                  elif q2 == "Summer":
                      fish += 2
                  elif q3 == "Autumn":
                      dog += 2
                  else:
                      cat += 2

                  ##q4
                  if q4 >= 30:
                      cat += 1
                  elif 20 <= q4 < 30:
                      dog += 1
                  elif 10 <= q4 < 20:
                      bunny += 1
                  else:
                      fish += 1

                  ##q5
                  if q5 == "Steak and mashed potatoes":
                      dog += 1
                  elif q5 == "Tuna salad sandwich":
                      cat += 1
                  elif q5 == "Spicy seaweed sald":
                      fish += 1
                  else:
                      bunny += 1
##display results

                  if dog >= cat and dog >= bunny and dog >= fish:
                        st.success("You are a DOG!")
                        st.image("Images/dog.jpg", width=300)
                        st.balloons() #NEW

                  elif cat >= dog and cat >= bunny and cat >= fish:
                        st.success("You are a CAT!")
                        st.image("Images/cat.jpg", width=300)
                        st.balloons()
                  elif fish >= dog and fish >= bunny and fish >= cat:
                        st.success("You are a FISH!")
                        st.image("Images/fish.jpg", width=300)
                        st.balloons()
                  elif bunny >= dog and bunny >= cat and bunny >= fish:
                        st.success("You are a BUNNY!")
                        st.image("Images/bunny.jpg", width=300)
                        st.balloons()
##reset
                  if st.button("Reset Quiz"):
                      st.rerun() #NEW

    

    
        
                  
                  
                      
            

                  
                  
                      

              





    
    
