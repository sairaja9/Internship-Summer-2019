Sub CreateChart()
'
' CreateChart Macro
'
' Keyboard Shortcut: Ctrl+y
'
    Dim CombatUnits As Range
    Set CombatUnits = Range("J2:K2")
    
    Dim Pylons As Range
    Set Pylons = Range("E2")
    
    Dim Counter As Integer
    Dim Max As Integer
    
    Dim TitleLocation As Range
    Set TitleLocation = Range("A2")
    
    Dim Title As String
    
    Dim i As Integer
    For i = 2 To 7
        
        Set NewChart = Worksheets(1).ChartObjects(1).Duplicate
        
        Counter = 0
        Max = i - 1
        While Counter < Max
            NewChart.IncrementTop 215#
            Counter = Counter + 1
        Wend
        
        NewChart.Select
        
        With ActiveChart
            .HasTitle = True
            .ChartTitle.Text = TitleLocation.Value
        End With
        
        ActiveChart.ChartArea.Select
        ActiveChart.PlotArea.Select
        Application.CutCopyMode = False
        
        ActiveChart.FullSeriesCollection(1).Values = CombatUnits
        Set CombatUnits = CombatUnits.Offset(0, -2)
        ActiveChart.FullSeriesCollection(2).Values = CombatUnits
        Set CombatUnits = CombatUnits.Offset(0, -2)
        ActiveChart.FullSeriesCollection(3).Values = CombatUnits
        ActiveChart.FullSeriesCollection(4).Values = Pylons
        
        Title = TitleLocation.Value
        ActiveChart.Export "C:\Users\saira\OneDrive\DPgraphs\" + Title + ".png"
        
        Set CombatUnits = CombatUnits.Offset(1, 4)
        Set Pylons = Pylons.Offset(1, 0)
        Set TitleLocation = TitleLocation.Offset(1, 0)
        
    Next i
    
End Sub