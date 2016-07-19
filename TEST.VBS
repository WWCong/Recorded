
Randomize
slp = DateDiff("s", Now, CDate(DateValue(Now) & " 9:00:00")) > 0
slp = DateDiff("s", Now, CDate(DateValue(DateAdd("d", 1, Now)) & " 09:00:00"))
slp = slp + Int((1800 * Rnd) + 1)
msgbox DateAdd("s", slp, Now)