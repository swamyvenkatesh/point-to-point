dict1 = {
'ACP_RailAvailRS':
			{
				'OriginDestinationOptions':
				 			{'OriginDestinationOption':
				 				{'OriginLocation':
				 						{	'@Name' : 'Paris'		 						}


				 						},

				 			  },
				 			  {'Journeys':
				 			  	'journey':{'journey_segment':}
				 			  	'fare_rphs':['1,2,3']

				 			  }

				'Fares':
						{
						'Fare':''
						}
			}
	

}

for i,k in dict1.items():
	# print i, "^^^^^^^" 
	# print k, "#########3"
	for ii, jj in k.items():
		# print jj
		for one, two in jj.items():
			# print two
			for one1, two2 in two.items():
				# print two2
				print two2.get('@Name')
				print two2.get('Suni')
				print two2['@Name']
				print two2['Suni']
	# print i["@Name"]

# print dict1['ACP_RailAvailRS'], "$$$"
# print dict1['ACP_RailAvailRS']['OriginDestinationOptions'], "$$$"
# print dict1['ACP_RailAvailRS']['OriginDestinationOptions']['OriginDestinationOption'], "$$$"
# print dict1['ACP_RailAvailRS']['OriginDestinationOptions']['OriginDestinationOption']['OriginLocation'], "$$$"
print dict1['ACP_RailAvailRS']['OriginDestinationOptions']['OriginDestinationOption']['OriginLocation']['@Name'], "$$$"