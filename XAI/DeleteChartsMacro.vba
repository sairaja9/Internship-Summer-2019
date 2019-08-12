Sub DeleteCharts()

Worksheets("Sheet1").Activate
Set CurrentSheet = ActiveSheet

For Each Worksheet In ActiveWorkbook.Worksheets
    For Each ChartObject In Worksheet.ChartObjects
        ChartObject.Activate
        If ActiveChart.HasTitle = True Then
            ActiveChart.Parent.Delete
        End If
    Next ChartObject
Next Worksheet

End Sub