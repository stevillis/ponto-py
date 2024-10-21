import pandas as pd
import streamlit as st


def format_hour(total_hours):
    """
    Format the total hours into a string representation of hours and minutes.

    Parameters:
    total_hours (float): The total hours to be formatted.

    Returns:
    str: A string representing the total hours in the format 'Xh:Ym'.
    """
    if total_hours is None:
        return "0h:0m"

    abs_hours = abs(int(total_hours))
    abs_minutes = abs(int((total_hours - int(total_hours)) * 60))

    sign = "-" if total_hours < 0 else ""

    return f"{sign}{abs_hours}h:{abs_minutes}m"


def format_df_hours(row):
    """
    Format the total hours from a DataFrame row into a string representation of hours and minutes.

    Parameters:
    row (pd.Series): A pandas Series containing the 'Total_Hours' column.

    Returns:
    str: A string representing the total hours in the format 'Xh:Ym'.
    """
    total_hours = row["Total_Hours"]
    if pd.isna(total_hours):
        total_hours = None

    return format_hour(total_hours)


def required_hours(october_df):
    """
    Calculate the total required hours based on the number of entries in the October dataframe.

    Parameters:
    - october_df: DataFrame containing the entries for the month of October.

    Returns:
    - Total required hours calculated as 8.75 multiplied by the number of entries in the October dataframe.
    """
    return 8.75 * october_df.shape[0]


def hours_balance(october_df):
    """
    Calculate the balance of hours by subtracting the required hours from the total hours in the October dataframe.

    Parameters:
    - october_df: DataFrame containing the entries for the month of October.

    Returns:
    - A string representing the balance of hours in the format 'Xh:Ym'.
    """
    return format_hour(october_df["Total_Hours"].sum() - required_hours(october_df))


@st.cache_data
def get_data():
    """
    Retrieve and preprocess data from an Excel file, calculate total hours worked, and format the hours into 'Xh:Ym' representation.

    Returns:
        pd.DataFrame: Processed DataFrame containing total hours and formatted hours.
    """

    # Read data
    october_df = pd.read_excel("out.xlsx")

    # Convert rows to datetime
    october_df["Data"] = pd.to_datetime(october_df["Data"])

    for col in ["Entrada1", "Saída1", "Entrada2", "Saída2", "Entrada3", "Saída3"]:
        october_df[col] = pd.to_datetime(
            october_df["Data"].astype(str) + " " + october_df[col].astype(str),
            format="%Y-%m-%d %H:%M:%S",
            errors="coerce",
        )

    # Calculate total hours
    october_df["Total_Hours"] = 0.0
    for index, row in october_df.iterrows():
        total_hours = 0

        if pd.notna(row["Entrada1"]) and pd.notna(row["Saída1"]):
            total_hours += (row["Saída1"] - row["Entrada1"]).total_seconds() / 3600

        if pd.notna(row["Entrada2"]) and pd.notna(row["Saída2"]):
            total_hours += (row["Saída2"] - row["Entrada2"]).total_seconds() / 3600

        if pd.notna(row["Entrada3"]) and pd.notna(row["Saída3"]):
            total_hours += (row["Saída3"] - row["Entrada3"]).total_seconds() / 3600

        october_df.loc[index, "Total_Hours"] = total_hours

    october_df["Formatted_Hours"] = october_df.apply(format_df_hours, axis=1)

    return october_df


if __name__ == "__main__":
    st.title("Ponto Py - Controle de ponto")

    october_df = get_data()

    st.metric(
        label="Horas trabalhadas",
        value=format_hour(required_hours(october_df)),
        delta=hours_balance(october_df),
    )
