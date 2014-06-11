Set WshShell = CreateObject("WScript.Shell")
Dim CloseTime,i
CloseTime = 1*60
Set s = CreateObject("sapi.spvoice")
s.Speak "Count down start!"
For i = CloseTime To 1 Step - 1
REM WshShell.popup "current time is" & i
WScript.Sleep 1000
Next
s.Speak "Time's up!"
MsgBox "timeout on IE"
Set WshShell = Nothing