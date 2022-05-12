# Veracode_XML_Report_To_Excel_File_Converter
This script is used to convert the Veracode XML report to Excel file and also change the severity of finding from number to string (Critical, High, Medium, Low, Informational)

| Severity | String        |
|----------|---------------|           
|    5     | Critical      |
|    4     | High          |
|    3     | Medium        |
| 2 and 1  | Low           |
|    0     | Informational |


## Steps of using it:
1. Copy the exe file/Python file to the Veracode XML file folder.
2. Run the command "Veracode_XML_to_CSV.exe Veracode_XML_File.xml" or "python3 Veracode_XML_to_CSV.py Veracode_XML_File.xml"
3. The output report will generate by the name "Veracodeout.xlsx"

_**For more details check my blog:** https://lazyhacker.medium.com/_

## Output file looks like below screenshot:

![Alt text](https://raw.githubusercontent.com/crazywifi/Veracode_XML_Report_To_Excel_File_Converter/main/poc.PNG)
