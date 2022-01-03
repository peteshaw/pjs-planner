vList = e-Procurement-System-Accesses
if vList.System = DMARTs then
  if vList.Status = Pending then
    Email DMARTS-Approvers( DMARTS Pending Email )
  else if vList.status = Approved
    Email DMARTS-Approvers( DMARTS Approved Email )

if vList.System = DMARTs then
  if vList.Status = Pending then
    Email DMARTS-Approvers( DMARTS Pending Email )
  else if vList.status = Approved
    Email DMARTS-Approvers( DMARTS Approved Email )

else if 
