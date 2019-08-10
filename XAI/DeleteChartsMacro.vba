Sub DeleteCharts()

Set CurrentSheet = ActiveSheet

For Each Worksheet In ActiveWorkbook.Worksheets
    For Each ChartObject In Worksheet.ChartObjects
        ChartObject.Activate
        If ActiveChart.HasTitle = True Then
            ActiveChart.Parent.Delete
        End If
    Next
Next

'Worksheets("Sheet1").Activate

End Sub