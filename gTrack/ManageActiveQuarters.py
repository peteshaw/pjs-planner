'NOT SURE WHAT THIS DOES, IT CALCULATES THE quarter end based on the 
'quarter value (typicall "Qn YYYY" ie "Q1 2022")
'kind of a duplicate of the new quarter generate workflow'

vList = ActiveQuarters

var strQuarter = left(vList.Quarter,2)
var year = right(vList.Quarter, 4)

case select strQuarter
  case 'Q01'
    year += 1
    nextQuarter = 'Q02-' + year.toString()
    nextStartDate = date('01','01',year)
    nextEndDate = date('03','31',year)
  case 'Q02'  
    nextQuarter = 'Q03-'+ year.toString()
    nextStartDate = date('04','01',year)
    nextEndDate = date('06','30',year)
  case 'Q03'
    nextQuarter = 'Q04'+ year.toString()
    nextStartDate = date('07','01',year)
    nextEndDate = date('09','30',year)
  cacase 'Q04'
    nextQuarter = 'Q01'+ year.toString()
    nextStartDate = date('10','01',year)
    nextEndDate = date('12','31',year)
end select

vList.QuarterEnd = nextEndDate
