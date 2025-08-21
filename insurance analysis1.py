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
def plot_pie_and_table(data, value_col, pie_title, header_color="#FFA07A", row_color="#F5F5F5", title_color="blue"):
    # Pie Chart
    data_sorted = data[["Crop", value_col]].sort_values(by=value_col, ascending=False)
    fig1 = px.pie(
        data_sorted, values=value_col, names="Crop",
        title=f"<b style='color:{title_color};'>{pie_title}</b>"
    )
    fig1.update_traces(textinfo="label+value")
    st.plotly_chart(fig1)

    # Table
    data_sorted.reset_index(drop=True, inplace=True)
    fig, ax = plt.subplots(1, 1, figsize=(3, 2))
    table_data = [data_sorted.columns.tolist()] + data_sorted.values.tolist()

    n_rows, n_cols = len(data_sorted), len(data_sorted.columns)
    row_colors = [[row_color] * n_cols for _ in range(n_rows + 1)]
    row_colors[0] = [header_color] * n_cols  # header row color

    ax.axis("off")
    ax.axis("tight")
    table = ax.table(cellText=table_data, cellColours=row_colors, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(8)

    for col in range(n_cols):
        table.auto_set_column_width([col])
    for key, cell in table.get_celld().items():
        cell.set_fontsize(8)
        row, col = key
        if row == 0:
            cell.set_text_props(weight="bold", color="black")  # header text bold

    st.pyplot(fig)

# --- Premium ---
plot_pie_and_table(df_selection, "Premium in Crore", "Premium Paid in Crore per Crop", 
                   header_color="#99CCFF", row_color="#F0F8FF", title_color="lightskyblue")

# --- Sum Insured ---
plot_pie_and_table(df_selection, "Sum Insured in Crore", "Sum Insured in Crore per Crop", 
                   header_color="#FFCC99", row_color="#FFF8DC", title_color="lightcoral")

# --- Claim ---
plot_pie_and_table(df_selection, "Claim in Crore", "Claim in Crore per Crop", 
                   header_color="#90EE90", row_color="#F5FFFA", title_color="lightgreen")





