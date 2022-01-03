vList.UI_Status = 'submitted'
vList.ApprovalStatus = 'Approved'
vList.ManagedCLPEnd = 4/30/2021
vList.DaysExtended = 122 

vGrant.ManagedCLPEnd = 8/29/2022
vGrant.ProjectedCloseRevised = 11/26/2022

vList = CLP_Extensions
vGrants = GrantAwardProgram
vGrants.join(vList, vList.GrantAwardProgramID = vGrant.ID)
if UI_status = locked then terminate

if vList.UI_Status == 'submitted' and vList.ApprovalStatus = 'Approved' then 

  var newCLP-ManagedCLPEnd = vList.GrantAwardProgram.ManagedCLPEnd
  var newGrant-ManagedCLPEnd =  vList.GrantAwardProgram.ManagedCLPEnd + vList.DaysExtended
  var newProjectCloseRevised = newGrant-ManagedCLPEnd + 90
    
  vList.ManagedCLPEnd = newCLP-ManagedCLPEnd
  vGrant.ManagedCLPEnd = newGrant-ManagedCLPEnd
  vGrant.ProjectedCLoseRevised = newProjectCloseRevised

  vList.UI_Status = 'Locked'

'not sure the purpose of this 
If vList.Status == 'Submitted' and vList.ApprovalStatus == 'Denied' then  
  vList.UI_Status = 'Locked'
  

'Formula for newGrant-ManagedCLPEnd - unformatted
addDays(body('newCLPManagedCLPEnd'),int(outputs('Get_item')?['body/Days_Extended']))

'formatted'
formatDateTime(addDays(body('newCLPManagedCLPEnd'),int(outputs('Get_item')?['body/Days_Extended'])),"d")


adddays(datevalue)

convertTimeZone(outputs('Get_item')?['body/GrantAwardProgram_x003a_ManagedC/Value'],"utc","eastern standard time","d")

For the newGrant-ManagedCLPEnd, we need to add days (convert to int)


addDays(body('newCLPManagedCLPEnd'),int(outputs('Get_item')?['body/Days_Extended']))

addDays(body('newCLPManagedCLPEnd'),int(outputs('Get_item')?['body/Days_Extended']))

formatDateTime(variables('GrantManagedCLPEnd'),'d')

working - newGrant-managed
addDays(body('newCLPManagedCLPEnd'),int(outputs('Get_item')?['body/Days_Extended'])),'d')



adddays(variables('GrantManagedCLPEnd'))

adddays(triggerOutputs()?['body/GrantAwardProgram_x003a_ManagedC/Value'])

adddays(string(triggerOutputs()?['body/GrantAwardProgram_x003a_ManagedC/Value']),int(triggerOutputs()?['body/Days_Extended']))
addDays(body('newCLPManagedCLPEnd'),int(outputs('Get_item')?['body/Days_Extended']))
adddays(variables('GrantManagedCLPEnd'),variables('intDaysExtended'))
int(triggerOutputs()?['body/GrantAwardProgram_x003a_ManagedC/Value'],variables('daysToExtend'))
addDays(triggerOutputs()?['body/GrantAwardProgram_x003a_ManagedC/Value'],variables('daysToExtend'))