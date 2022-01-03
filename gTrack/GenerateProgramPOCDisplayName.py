vList = ProgramPOC
On ListChange()
If vList.FirstName == ""  then
  vList.Displayname = vList.LastName
else
  vList.DisplayName = vList.FirstName & " " & vList.LastName
endif