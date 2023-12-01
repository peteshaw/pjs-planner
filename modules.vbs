Private Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal lngMilliSeconds As Long)
Private Declare PtrSafe Function SetCursorPos Lib "user32" (ByVal x As Long, ByVal y As Long) As Long
Private Declare PtrSafe Sub mouse_event Lib "user32" (ByVal dwFlags, ByVal dx, ByVal dy, ByVal cButtons, ByVal dwExtraInfo As Long)
Public Declare PtrSafe Function GetCursorPos Lib "user32" (lpPoint As POINTAPI) As Long
Public Type POINTAPI
    x As Long: y As Long
End Type


Sub Start()
    MouseMove
End Sub

Sub StopLoop()
    Dim myWS As Worksheet, myWB As Workbook

    Set myWB = ThisWorkbook
    Set myWS = myWB.Sheets("rnd")

    STOPPED = myWS.Range("stopValue").Value
    LogInformation (STOPPED)
    
    myWS.Range("stopValue").Value = STOPPED + 1
    
End Sub




Sub MouseMove()
    Dim lngCurPos As POINTAPI
    Dim StartTime, SecondsElapsed As Double
    Dim MinutesElapsed As String
    Dim xx As Worksheet, yy As Workbook
    Dim x1, y1, counter As Integer

    StartTime = Timer
    StartTime1 = Timer
    GetCursorPos lngCurPos
    x2 = lngCurPos.x
    y2 = lngCurPos.y

    Set yy = ThisWorkbook
    Set xx = yy.Sheets("rnd")
    
    SecondsToActivate = xx.Range("B4").Value
    SecondsToActivate = Hour(SecondsToActivate) * 3600 + Minute(SecondsToActivate) * 60 + Second(SecondsToActivate)
    counter = 0
    
    xx.Range("b6").Value = 0
    LogInformation ("Loop starting")
    
    Do
        DoEvents
        GetCursorPos lngCurPos
        x1 = lngCurPos.x
        y1 = lngCurPos.y
        LogInformation ("cursor is at " + CStr(x1) + " and " + CStr(y1))
        
        If x1 <> x2 Or y1 <> y2 Then
            StartTime = Timer
        End If
            SecondsElapsed = Round(Timer - StartTime, 2)
            MinutesElapsed = Format(((Timer - StartTime) - 0.5) / 86400, "hh:mm:ss")
        With xx
            .Range("B1").Value = Format(((SecondsToActivate - SecondsElapsed) + 0.5) / 86400, "hh:mm:ss")
            .Range("B2").Value = counter
            .Range("B3").Value = Format(((Timer - StartTime1) - 0.5) / 86400, "hh:mm:ss")
        End With
    
        stopFlag = xx.Range("b6").Value
        xx.Range("B7").Value = "running"
    
        If stopFlag > 0 Then
            xx.Range("b7").Value = STOPPED
            LogInformation ("Stopping!")
            Exit Do
        End If
    
        If SecondsElapsed >= SecondsToActivate Then
            For I = 1 To 99
            For j = 1 To 99
                SetCursorPos x1 + j, y1
            Next j
            For j = 99 To 0 Step -1
                SetCursorPos x1 + j, y1
            Next j
            Next I
            LogInformation ("sending f12")
            SendKeys "{F13}", True: Sleep 88: SendKeys "{F13}", True: Sleep 88
            StartTime = Timer
            counter = counter + 1
        End If
        GetCursorPos lngCurPos
        x2 = lngCurPos.x
        y2 = lngCurPos.y
        Sleep (1000)
        LogInformation ("Next Loop")
    Loop

End Sub

Public Sub WaitSeconds(intSeconds As Integer)
  ' Comments: Waits for a specified number of seconds
  ' Params  : intSeconds      Number of seconds to wait
  ' Source  : Total Visual SourceBook
  On Error GoTo PROC_ERR
  Dim datTime As Date
  datTime = DateAdd("s", intSeconds, Now)

  Do
   ' Yield to other programs (better than using DoEvents which eats up all the CPU cycles)
    Sleep 100
    DoEvents
  Loop Until Now >= datTime

PROC_EXIT:
  Exit Sub

PROC_ERR:
  MsgBox "Error: " & Err.Number & ". " & Err.Description, , "modDateTime.WaitSeconds"
  Resume PROC_EXIT
End Sub


Sub LogInformation(LogMessage As String)
    Const LogFileName As String = "c:\tools\log.txt"
    Dim FileNum As Integer
    Dim logMsg As String
    logMsg = Format(Now(), "YYYYMMDDhhmmss") + "-" + LogMessage
    FileNum = FreeFile ' next file number
    Open LogFileName For Append As #FileNum ' creates the file if it doesn't exist
    Print #FileNum, logMsg ' write information at the end of the text file
    Close #FileNum ' close the file
End Sub

