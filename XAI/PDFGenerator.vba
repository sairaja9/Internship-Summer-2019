Sub PDF()
i = 1
For Each myChart In ActiveSheet.ChartObjects
    myChart.Activate
    myPDF = "C:\Users\saira\OneDrive\DPgraphs\PDFs\" & i & ".pdf"
    ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF, Filename:=myPDF, Quality:=xlQualityStandard, IncludeDocProperties:=True, IgnorePrintAreas:=False, OpenAfterPublish:=False
    i = i + 1
Next myChart
End Sub