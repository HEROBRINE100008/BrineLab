if gg.isVisible(true) then
	gg.setVisible(false)
end

gg.clearResults()
gg.setRanges(gg.REGION_ANONYMOUS)

gg.alert("Vaya al primer parachoques del auto y comprelo")

while true do

	if gg.isVisible(true) then
		gg.setVisible(false)
		gg.searchNumber("0",gg.TYPE_DWORD)
		break
	end
end

	gg.alert("Ahora compre el segundo")

while true do

	if gg.isVisible(true) then
		gg.setVisible(false)
		gg.searchNumber("1",gg.TYPE_DWORD)
		break
	end
end

	gg.alert("Ahora compre el tercero")

while true do

	if gg.isVisible(true) then
		gg.setVisible(false)
		gg.searchNumber("2",gg.TYPE_DWORD)
		break
	end
end

	gg.alert("Ahora compre el primero nuevamente")

while true do

	if gg.isVisible(true) then
		gg.setVisible(false)
		gg.searchNumber("0",gg.TYPE_DWORD)
		revert = gg.getResults(100)
		gg.editAll("-1", gg.TYPE_DWORD)
		gg.alert("Ahora cambie de auto y vuelva a este y ya no tendrá parachoques")
		break
	end
end
