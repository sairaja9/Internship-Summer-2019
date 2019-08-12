Sub L_PDF()
For Each myChart In ActiveSheet.ChartObjects
    myChart.Activate
    ActiveWindow.SelectedSheets.PrintOut Copies:=1, Collate:=True, _
        IgnorePrintAreas:=False
Next myChart
End Sub