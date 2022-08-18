def worksheet_2_frame(worksheet_name: gspread.models.Spreadsheet, tab_name: str) -> pd.DataFrame: 
  """This functions takes the worksheetName and tabname as input and outputs a dataframe."""
  frame = worksheet_name.worksheet(tab_name)
  rows = frame.get_all_values()
  frame = pd.DataFrame.from_records(rows)
  return frame


# Here we define a funtion to replace the colum headers
def replace_column_headers(frame: pd.DataFrame, header_level: int, drop_range: tuple, sql: Binary) -> pd.DataFrame: 
  """This functions takes a dataframe and replaces the columns with the desired row and removes duplicates from range."""
  frame.columns = frame.iloc[header_level]
  frame.drop(index=drop_range, inplace=True)
  frame.columns = frame.columns.str.strip()
  if sql == True:
    frame.columns = frame.columns.str.replace(" ", "_")
  return frame
