import download_data

def main():
	dataCode = 'YAHOO/AAPL' # Desired data can be found via www.quandl.com, check for code name
	dataCode = 'UGID/POPCHG_TUR' 
	startDate = "2001-01-01"
	finishDate = "2100-01-01"
	timeRange = "monthly"
	dataType = 'pandas'

	dataSet = download_data.get(dataCode, startDate, finishDate, timeRange, dataType)
	#dataSet = download_data.get() # default
	print dataSet
	print type(dataSet)

if __name__ == "__main__":
	main()