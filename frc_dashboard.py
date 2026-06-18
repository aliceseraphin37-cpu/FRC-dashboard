import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")
st.markdown("""
<style>
.stApp {
   background-color: #0B1026;
   color: white;
   }
   </style>
   """, unsafe_allow_html=True)

data = pd.DataFrame({
    "Team Name": ["Sisters 1st", "MORT", "MXS Bulldog Bots", "MORT Beta", "The Pascack PI-oneers", "Killer Kardinals 2"],
    "Rank": [1, 2, 3, 4, 5, 30],
    "Ranking Points": [2.87, 2.82, 2.29, 2.16, 1.87, 0.16],
    "Auto Points": [39.78, 15.31, 44.53, 6.97, 6.90, 2.40],
    "Teleop Points": [150.49, 112.86, 91.89, 88.94, 78.50, 5.72],
    "Tower Points": [-0.63, 0.27, -0.07, -0.04, 0.16, 0.40],
    "Foul Points": [1.34, 6.69, 0.45, 3.46, 9.39, -1.29],
    "Total Points": [191.61, 134.86, 136.87, 99.37, 94.79, 6.83],
    })
st.set_page_config(
    page_title="FRC Dashboard",
    layout="wide"
    )
st.title("Mount Olive FIRST Robotics Team Analysis Dashboard🦿")
st.write("Compare Killer Kardinals 2 Againist Top Teams")

metric = st.selectbox("Select a Scoring Category",
                      [
                          "Rank",
                          "Ranking Points",
                          "Auto Points",
                          "Teleop Points",
                          "Tower Points",
                          "Foul Points",
                          "Total Points",
                          ]
                      )
st.subheader("Data Table🗂️")

st.dataframe(
    data[["Team Name", metric]]
    )
sorted_data = data.sort_values(by=metric, ascending=False)
fig, ax = plt.subplots(figsize=(10,5))
st.divider()
st.subheader("Data Chart📊")
colors = [
    "#1B1F3B",
    "#3D348B",
    "#7678ED",
    "#9D4EDD",
    "#C77DFF",
    "#F72585"
    ]
ax.barh(
    sorted_data["Team Name"],
    sorted_data[metric],
    color=colors
    )
ax.set_title(f"{metric} Comparison")
ax.tick_params(axis="x", labelrotation=45)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
st.pyplot(fig)
st.divider()
st.markdown("""
### Insight

Based off the data on each category it is clear Killer Kardinals 2 is performing poorly due to it's low Teleop points. The top teams are doing better because of their teleop scoring,if Killer Kardinals can improve it's offense capability, the team will have a greater chance at ranking higher. Another thing Killer Kardinals 2 needs to improve on is Auto points,it isn't the highest priority but it does add up when we see the total points. Lastly, Killer Kardinals 2 is the only team that has negative foul points, essentially giving the opposing team extra points. """
)


                          
