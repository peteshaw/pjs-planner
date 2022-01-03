if vList.UI_Status == 'submitted' and vList.ApprovalStatus = 'Approved' then 

  vList.ManagedCLPEnd  = vList.GrantAwardProgram.ManagedCLPEnd
  vGrant.ManagedCLPEnd =  vList.GrantAwardProgram.ManagedCLPEnd + vList.DaysExtended
  vGrant.ProjectedCLoseRevised = newGrant-ManagedCLPEnd + 90
    

  vList.UI_Status = 'Locked'
