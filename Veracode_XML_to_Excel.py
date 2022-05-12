import xml.etree.ElementTree as ET
import xlsxwriter
import pyfiglet
from pyfiglet import fonts
import sys
import argparse
from termcolor import colored
from colorama import init

init()
G  = '\033[32m' 
O  = '\033[33m' 
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

def banner():
    print (colored(pyfiglet.figlet_format("Veracode XML Report to Excel Converter", font="standard"), "red"))
    print (G+BOLD+"By Rishabh Sharma [Follow: https://lazyhacker.medium.com]\n"+END)


def parsingxmldata(inxml):
    mytree = ET.parse(inxml)
    myroot = mytree.getroot()
    workbook = xlsxwriter.Workbook('Veracodeout.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'severity')
    worksheet.write('B1', 'Vulnerability Name')
    worksheet.write('C1', 'issueid')
    worksheet.write('D1', 'Description')
    worksheet.write('E1', 'Remidiation')
    worksheet.write('F1', 'Sourcepath_Line')
    worksheet.write('G1', 'Mitigation_Status')
    row = 1
    col = 0
    
    for severity in myroot.findall("{https://www.veracode.com/schema/reports/export/1.0}severity/{https://www.veracode.com/schema/reports/export/1.0}category/{https://www.veracode.com/schema/reports/export/1.0}cwe/{https://www.veracode.com/schema/reports/export/1.0}staticflaws/"):
        dic = (severity.attrib)
        for i in dic:
            if (i == "severity"):
                severity1 = (dic[i])
                if (severity1 == "5"):
                    severity1 = "Critical"
                if (severity1 == "4"):
                    severity1 = "High"
                if (severity1 == "3"):
                    severity1 = "Medium"
                if (severity1 == "2" or severity1 == "1"):
                    severity1 = "Low"
                if (severity1 == "0"):
                    severity1 = "Informational"
            if (i == "categoryname"):
                cate1 = (dic[i])
                cate1 = cate1.replace(",","")
            if (i == "issueid"):
                issueid1 = (dic[i])
            if (i == "description"):
                desc = str(dic[i])
                description =(desc.split('\r\n\r\n', 1)[0])
                description = description.replace(",","")
                recommendation = (desc.split('\r\n\r\n', 1)[1])
                recommendation = recommendation.replace('\r', '').replace('\n', '')
                recommendation = recommendation.replace(",","")
            if (i=="sourcefile"):
                sfile = (dic[i])
            if (i=="line"):
                sline = (dic[i])
            if (i == "mitigation_status"):
                mitistatus = (dic[i])
            if (i=="sourcefilepath"):
                spath = (dic[i])
                sfilesline = str(sfile+":"+sline)
                print (severity1+","+cate1+","+issueid1+","+description+","+recommendation+","+sfilesline+","+mitistatus)
                worksheet.write(row, col, severity1)
                worksheet.write(row, col + 1, cate1)
                worksheet.write(row, col + 2, issueid1)
                worksheet.write(row, col + 3, description)
                worksheet.write(row, col + 4, recommendation)
                worksheet.write(row, col + 5, sfilesline)
                worksheet.write(row, col + 6, mitistatus)
                row += 1
                
    workbook.close()

        
def main():
    banner()
    parser = argparse.ArgumentParser(description='Convert Veracode XML report to CSV')
    parser.add_argument('infile', help='XML report you want to parse')
    args = parser.parse_args()
    inxml = args.infile
    parsingxmldata(inxml)
    
    
    
if __name__ =='__main__':
        main()
