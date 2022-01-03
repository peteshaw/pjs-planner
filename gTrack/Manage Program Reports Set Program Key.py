vList = ProgramReports
'THIS SEEMS TO JUST BE CONCERNED WITH MAKING SURE A FEW FIELDS ARE UPDATED

OnCHANGE() {
  var ProgramKey = vList.GrantAwardProgramId

  if vList.ProgramIdKey <> ProgramKey then
    pause(5, minutes)
    vList.ProgramIdKey = ProgramIdKey
  end if
}