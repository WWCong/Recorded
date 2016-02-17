do while (true)
    set ws = createobject("wscript.shell")
    ws.run "python code.pyw"
    Randomize
	slp = DateDiff("s", Now, CDate(DateValue(DateAdd("d", 1, Now)) & " 09:00:00"))
    slp = slp + Int((1800 * Rnd) + 1)
    log("Next run time: " & DateAdd("s", slp, Now))
    Wscript.Sleep slp * 1000
loop

Sub log(str)
    set fso = createobject("scripting.filesystemobject")
    set file = fso.opentextfile("vbslog.txt", 8, ture)
    file.writeline "--------------- " & Now & "---------------"
    file.writeline str
    file.writeline ""
    file.close
End Sub