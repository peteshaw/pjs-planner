'CHECK FOR TRIGGER CONDITIONS

vList = ProgramReports
vMaster = Master list
vGrant = GrantAwardPrograms
vConfig = ReportConfig
vReports = Recieved Reports

vMaster.select(vMaster.ID = 1)
vGrant.join(vList.GrantAwardProgramAward = vGrant.ID)
vConfig.join(vList.ReportConfigID= vCOnfig.ID)

if vMaster.TriggerNewQuarter = no and
  vList.forceManualUpdate = no then  
  quit()
else  
  vList.forceManualUpdate = no
  if vGrant.ClosedDate > 0 then
    quit()
  end if
end if

'SET  NEW QUARTER VARIABLES
'STARTING WITH A CURRENT QUARTER, NAME, START AND END, CALCULATE THE NEXT QUARTER

var strQuarter = left(vMaster.Quarter,2)
var nextYear = right(vMaster.Quarter,4)

case select strQuarter
  case 'Q01'
    nextYear += 1
    nextQuarter = 'Q02-' + nextYear.toString()
    nextStartDate = date('01','01',nextYear)
    nextEndDate = date('03','31',nextYear)
  case 'Q02'  
    nextQuarter = 'Q03-'+ nextYear.toString()
    nextStartDate = date('04','01',nextYear)
    nextEndDate = date('06','30',nextYear)
  case 'Q03'
    nextQuarter = 'Q04'+ nextYear.toString()
    nextStartDate = date('07','01',nextYear)
    nextEndDate = date('09','30',nextYear)
  cacase 'Q04'
    nextQuarter = 'Q01'+ nextYear.toString()
    nextStartDate = date('10','01',nextYear)
    nextEndDate = date('12','31',nextYear)
end select


'NOW FIGURE OUT THE NEW DUE DATES BASES ON THE REPORT CONFIG INFORMATION
var dueStart

if vConfig.Reference = 'Quarter Start' then
  dueStart = nextStartDate
else if vConfig.Reference = 'Quarter End' then  
  dueStart = nextEndDate
else if vConfig.Reference = 'POP Start' then
  dueStart = vGrant.POPStart
endif

if vConfig.Timeframe = 'Days' then
  DueStart.addDays(vConfig.ReportTime)
else if vCOnfig.TimeFrame = 'Months' then
  DueStart.addMonths(vCOnfig.ReportTime)
end if

'CREATE THE RECIVED REPORT ITEM IF NEEDED'

if vGrant.POPStart <= nextStartDate and 
    vGrant.POPEnd >= nextEndDate and 
    vGrant.NonRegionalized == 'No' then
  var newReportID = vReports.addRecord({
    Active Flag = Yes,
    GrantAwardProgram = vList.GrantAwardPrograms,
    DueDate = DueStart,
    GrantAward = vGrant.GrantAward,
    Program = vGrant.ProgramID,
    GranteeID = vGrant.GranteeID,
    ReportConfiguration = vList.ReportConfigurationID,
    IsFinal = 'No',
    Quarter = nextQuarter,
    QuarterName = nextQuarter
    QuarterStartDate = nextStartDate, 
    QuarterEndDate = nextEndDate
  })

end If

'CREATE FINAL REPORT IF NEEDED
if vGrant.POPStart < nextStartDate 
    and vGrant.NonRegionalized == 'No' 
    and vList.FinalReprtGenerated is Null then
  vList.FinalReportGenerated =today
  var finalReportID = vReports.addRecord({
        Active Flag = Yes,
    GrantAwardProgram = vList.GrantAwardPrograms,
    DueDate = DueStart,
    GrantAward = vGrant.GrantAward,
    Program = vGrant.ProgramID,
    GranteeID = vGrant.GranteeID,
    ReportConfiguration = vList.ReportConfigurationID,
    IsFinal = 'Yes',
    Quarter = nextQuarter,
    QuarterName = nextQuarter
    QuarterStartDate = nextStartDate, 
    QuarterEndDate = nextEndDate
  })