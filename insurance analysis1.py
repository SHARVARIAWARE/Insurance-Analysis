import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="District And Year Wise Analysis Of Insurance Data-Kharif Season", layout="wide")
df = pd.read_excel(r"Ashwin_Sharvari.xlsx")
df["Crop"] = df["Crop"] + df["Year"].astype(str)

st.title("🌾 District And Year Wise Analysis Of Insurance Data-Kharif Season")

st.sidebar.header("Please Select the Year:")
year = st.sidebar.multiselect("Select the Year:", options=df["Year"].unique())
df_selection1 = df[(df["Year"].isin(year))]
district = st.sidebar.multiselect("Select the district:", options=df_selection1["District"].unique())
df_selection = df_selection1[(df_selection1["District"].isin(district))]

# --- Function to plot pie + table ---
import matplotlib.pyplot as plt

def plot_pie_and_table(df, column, title, header_color, row_color, title_color):
    # --- Pie Chart ---
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))  # smaller overall height
    df_grouped = df.groupby("Crop")[column].sum().reset_index()
    df_grouped = df_grouped.sort_values(by=column, ascending=False)

    # Pie
    ax[0].pie(df_grouped[column], labels=df_grouped["Crop"], autopct="%1.1f%%")
    ax[0].set_title(title, color=title_color, fontsize=12)

    # --- Table ---
    table_data = [[crop, f"{val:.2f}"] for crop, val in zip(df_grouped["Crop"], df_grouped[column])]
    table_data.insert(0, ["Crop", column])  # header row

    ax[1].axis("off")
    table = ax[1].table(cellText=table_data,
                        loc="center",
                        cellLoc="center",
                        bbox=[0, 0, 1, 1])  # fits tightly in axis

    # Colors
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_color)

    # Smaller font & scale
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(0.9, 0.9)  # shrink table a bit

    plt.tight_layout()
    plt.show()

# --- Premium ---
plot_pie_and_table(df_selection, "Premium in Crore", "Premium Paid in Crore per Crop", 
                   header_color="#99CCFF", row_color="#F0F8FF", title_color="lightskyblue")

# --- Sum Insured ---
plot_pie_and_table(df_selection, "Sum Insured in Crore", "Sum Insured in Crore per Crop", 
                   header_color="#FFCC99", row_color="#FFF8DC", title_color="lightcoral")

# --- Claim ---
plot_pie_and_table(df_selection, "Claim in Crore", "Claim in Crore per Crop", 
                   header_color="#90EE90", row_color="#F5FFFA", title_color="lightgreen")









