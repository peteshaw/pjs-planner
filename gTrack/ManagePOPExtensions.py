vList = POP_Extensions
vGrants = GrantAwardProgram
vGrants.join(vList, vList.GrantAwardProgramID = vGrant.ID)
if UI_status = locked then terminate

if vList.ui == 'Submitted' and vList.ApprovalStatus = 'Approved' then 
  var vDaysExtended = vList.DaysExtended
  vList.OriginalPOPEnd = vGrant.POPEnd
  var vNewCloseOutPeriodEnd = vGrant.ManagedCLPEnd + DaysExtended
  var vNewProjectCloseRevised = vManagedCLPDate.add(90, 'days')

  vGrant.NotifcationClose1 = vGrant.NotifcationClose1 + DaysExtended
  vGrant.NotifcationClose2 = vGrant.NotifcationClose2 + DaysExtended
  vGrant.NotifcationClose3 = vGrant.NotifcationClose3 + DaysExtended
  
 
  'UPDATE GRANT AWARD PROGRAMS '
  with vGrant
    .POPEnd = vList.endDateRequested
    .ManagedCLPEnd = vNewCloseOutPeriodEnd
    .NotificationClose1 = vNewNotificationToClose1
    .NotificationClose2 = vNewNotificationToClose2
    .NotificationClose3 = vNewNotificationToClose3
    .ProjectedCloseRevised = vNewProjectCloseRevised
  end with


'not sure the purpose of this 
If vList.Status == 'Submitted' and vList.ApprovalStatus == 'Denied' then  
  vList.UI_Status = 'Locked'