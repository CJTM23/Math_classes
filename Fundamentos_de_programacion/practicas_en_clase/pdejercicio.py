import pandas as pd

df = pd.read_csv("hr_dataset.csv")
#print(df)
print(df.columns)

#e=(df.loc[: ,"job_level"] == "Senior") & (df.loc[: ,"performance_score"] < 2)
#e=(df["job_level"] == "Senior") & (df["performance_score"] < 2)
#df=df[e]
#print(df)
#df["año_de_nacimiento"] = 2025-df["age"]
#print(df)

#df=df.groupby(["department","job_level"]).agg({
#"monthly_salary":["mean","sum"],
#"employee_name":["count"]
#})d

#df.to_excel("reporte.xlsx")
# df=df.sort_values("monthly_salary",ascending=False)
# df=df.head(5)
# df=(df["employee_name"].str[0]== "A") & (df["employee_name"].str.endswith("a"))
#print(df["employee_name"].value_counts())

##eliminar datos
# sBooleana=df["job_level"].isna()
# df=df[sBooleana]
# print(df)
# df=df[~sBooleana]
# df=df.dropna()

##eliminar dato y reemplazarlo

# df.loc[df["job_level"].isna(),"job_level"] ="sin Titulo"
# print(df[['employee_name', 'department', 'job_level']])

# empleados con 45,23,57,35,44
# sBooleana=df["age"].isin([45,23,57,35,44])
# print(df[sBooleana])

#empleados sin repetir nombres
nombres=df["employee_name"].unique()
print(nombres.size)

#top
print(df["performance_score"].nlargest(3))
print(df.nlargest(5,columns=["performance_score"]))
print(df.nlargest(5,columns=["performance_score","monthly_salary"]))
print(df.nsmallest(10,columns=["performance_score","monthly_salary"]))