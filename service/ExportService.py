import pandas as pd


def export_to_excel(files_info_arr, output_file_name):
    pandas_frame = pd.DataFrame([t.__dict__ for t in files_info_arr])
    pandas_frame.to_excel(output_file_name)


