var vList = volunteer list
var vLookup = VF Lookup frmo DTS
var vOrgLookup = Org POC Lookup

vList.EmployeeEmail = vList.EmployeeName.DisplayName

vList.Title = vList.EmployeeName.DisplayName + "SWB Vounteer Request'

var deploymentStatus = lookup(SELECT vLookup.current_deployment_state WHERE vList.employeeEmail = vLookup.work_emailss)
var levelOne = lookup(SELECT vLookup.level_1_organization WHERE vList.employeeEmail = vLookup.work_emailss)
var levelTwo = lookup(SELECT vLookup.level_2_organization WHERE vList.employeeEmail = vLookup.work_emailss)
var personOrg = levelOne + "-" + levelTwo

var orgReviewer = lookup(SELECT vLookup.POC_Group  WHERE vOrgLookup.Org_Name = personOrg)
vList.Deployed_YN = deploymentStatus

if orgReviewer == "" then
  orgReviewer = "SWB-No_Approver"

If vList.Employee is in vLookup.work_emailss then
  vList.NRC_Roster_or_IM_Title_YN = "yes"
  vList.Org_From_VF = "NOT FOUND"
Else
  
