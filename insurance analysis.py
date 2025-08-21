import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(page_title="Distrcit and Year Wise Analysis-Kharif",layout="wide")
df=pd.read_excel(r"C:\Users\ADMIN\Downloads\Ashwin_Sharvari.xlsx")
df["Crop"]=df["Crop"] +df["Year"].astype(str)

#st.dataframe(df)

st.title("Distrcit and Year Wise Analysis-Kharif")


st.sidebar.header("Please Select the Year:")
year=st.sidebar.multiselect("Select the Year:",options=df["Year"].unique())

    

df_selection1=df[(df["Year"].isin(year))]
district=st.sidebar.multiselect("Select the district:",options=df_selection1["District"].unique())
df_selection=df_selection1[(df_selection1["District"].isin(district))]




xyz=df_selection[["Crop","Premium in Crore"]]
xyz.sort_values(by="Premium in Crore",ascending=False,inplace=True)
fig1=px.pie(xyz, values='Premium in Crore', names='Crop', title='Premium Paid in Crore Per Crop ')

st.plotly_chart(fig1)
xyz.reset_index(drop=True,inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[xyz.columns.tolist()]+xyz.values.tolist()
            
n_rows=len(xyz)
n_cols=len(xyz.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

xy=df_selection[["Crop","Sum Insured in Crore"]]
xy.sort_values(by="Sum Insured in Crore",ascending=False,inplace=True)
fig1=px.pie(xy, values='Sum Insured in Crore', names='Crop', title='Sum Insured in Crore Per Crop ')

st.plotly_chart(fig1)
xy.reset_index(drop=True,inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(3,2))



table_data=[xy.columns.tolist()]+xy.values.tolist()
            
n_rows=len(xy)
n_cols=len(xy.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x=df_selection[["Crop","Claim in Crore"]]
x.sort_values(by="Claim in Crore",ascending=False,inplace=True)
fig1=px.pie(x, values='Claim in Crore', names='Crop', title='Claim in Crore Per Crop ')

st.plotly_chart(fig1)
x.reset_index(drop=True,inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x.columns.tolist()]+x.values.tolist()
            
n_rows=len(x)
n_cols=len(x.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)



