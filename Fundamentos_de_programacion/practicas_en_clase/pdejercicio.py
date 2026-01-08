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
#})

#df.to_excel("reporte.xlsx")
# df=df.sort_values("monthly_salary",ascending=False)
# df=df.head(5)
# df=(df["employee_name"].str[0]== "A") & (df["employee_name"].str.endswith("a"))
print(df["employee_name"].value_counts())
