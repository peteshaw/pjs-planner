vList = ReceivedReports
vGrants = GrantAwardProgram
vGrants.join(vList, vList.GrantAwardProgramID = vGrant.ID)


OnChange(){
  'fix dates for new recived finals'
  'turned off for batch updates'
  if vList.IsFinal == yes and RecievedDate <> Null {
    var projCloseRevise = vGrant.ProjectedCLoseRevised.add(90, 'days')
    vGrant.ProjectedCLoseRevised = projCloseRevise 

  }

  'fix Q1'
  if left(vList.QuarterName, 3) == 'Q01' then
    var lastyear = lastright(vList.QuarterName,4) - 1
    var vQuarterName = 'Q01' + lastyear.toString()
    var vQuarterStart = date(10,1,lastyear)
    var vQuarterEnd = date(12,31,lastyear)
    vList.QuarterName = vQuarterName
    vList.QuarterStart = vQuarterStart
    vList.QuarterEnd = vQuarterEnd
  end if

'HANDLE THE RECIEVED FLAG'
'turned off for batch updates'
  if vList.isRecieved == 'No' and vList.ReceivedDate <> null then 
    vList.isRecieved = 'Yes'
  else if vList.isRecieved == 'Yes' and vList.ReceivedDate <> null then
    vList.isRecieved = No
  end if

  'update quarters from original quarter values
  'currently turned off

} 