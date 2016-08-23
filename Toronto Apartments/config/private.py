SLACK_TOKEN = "xoxp-65955659840-65962774757-71237534758-3febd3ef15"

#min rent per month
MIN_PRICE = 800

#max rent per month 
MAX_PRICE = 1800

##location preferences

#site to search on

CRAIGSLIST_SITE = "toronto"

#craigslist subdirectories
AREAS = ["oak", "yrk", "drh", "bra", "mss", "tor"]


BOXES = {
	"liberty_village": [
		[79.2538, 43.3831],
		[79.2438, 43.3804]
	],

	"parkdale": [
		[79.2647, 43.3831],
		[79.2538, 43.3815]
	],

	"roncesvalles": [
		[79.2734, 43.3922],
		[79.2638, 43.3821]
	],

	"little_italy": [
		[79.2524, 43.3934],
		[79.2429, 43.3910]
	],

	"yonge-stclair": [
		[79.2405, 43.4138],
		[79.2317, 43.4105]
	],

	"davisville": [
		[79.2415, 43.4209],
		[79.2316, 43.4143]
	],

	"yonge_eglinton": [
		[79.2435, 43.4259],
		[79.2314, 43.4211]
	],

	"annex_yorkville": [
		[79.2508, 43.4028],
		[79.2325, 43.3949]
	],

	"corso-italia": [
		[79.2705, 43.4109],
		[79.2501, 43.4036]
	],

	"leslieville": [
		[79.2114, 43.4015],
		[79.1919, 43.3925]
	],

	"beaches": [
		[79.1835, 43.4029],
		[79.1649, 43.3951]
	],

	"junction-highpark": [
		[79.2850, 43.4012],
		[79.2701, 43.3902]
	]
}

#if listing does not fall into boxes coordinates will check neighborhoods

NEIGHBORHOODS = ["liberty village", "queen west", "little italy", "roncesvalles", "parkdale", "corso italia",
				"yonge and st.clair", "davisville", "yonge and eglinton", "annex", "yorkville", "beaches",
				"leslieville", "junction", "high park", "king west"]

#transit preference
MAX_TRANSIT_DIST = 2 #km

TRANSIT_STATIONS = {
	"st_andrew": [43.647525, -79.384486],
	"osgoode": [43.650844, -79.386594],
	"st-patrick": [43.654831, -79.388348],
	"queens-park": [43.65988, -79.390477],
	"musuem": [43.667122, -79.393473],
	"union": [43.645221, -79.38057],
	"king": [43.648998, -79.377798],
	"queen": [43.652423, -79.379251],
	"dundas": [43.656249, -79.380898],
	"college": [43.661325, -79.383075],
	"wellesley": [43.665459, -79.383888],
	"bloor-yonge": [43.670935, -79.38591],
	"bay": [43.670147, -79.390695],
	"st-george": [43.668262, -79.399858],
	"rosedale": [43.676895, -79.388708],
	"summerhill": [43.682296, -79.390772],
	"st-clair": [43.687796, -79.392203],
	"davisville": [43.697689, -79.397182],
	"eglinton": [43.706159, -79.398332],
	"lawrence": [43.726581, -79.402609],
	"york-mills": [43.744621, -79.406303],
	"sheppard-yonge": [43.762035, -79.411897],
	"north-york-centre": [43.768509, -79.412729],
	"finch": [43.780467, -79.414636],
	"bayview": [43.766874, -79.386304],
	"bessarion": [43.769076, -79.375909],
	"leslie": [43.770637, -79.367605],
	"don-mills": [43.775207, -79.34576],
	"sherbourne": [43.672167, -79.376432],
	"castle-frank": [43.673819, -79.368546],
	"broadview": [43.676871, -79.358322],
	"chester": [43.678236, -79.352455],
	"pape": [43.679918, -79.344909],
	"donlands": [43.680978, -79.337865],
	"greenwood": [43.682578, -79.330272],
	"coxwell": [43.684143, -79.323041],
	"woodbine": [43.686408, -79.312638],
	"main-street": [43.689022, -79.301686],
	"victoria-park": [43.694262, -79.288575],
	"warden": [43.711442, -79.27906],
	"kennedy": [43.732269, -79.264011],
	"lawrence-east": [43.750526, -79.270305],
	"ellesmere": [43.76688, -79.276306],
	"midland": [43.770404, -79.272253],
	"scarborough-centre": [43.774395, -79.258056],
	"mccowan": [43.774931, -79.251818],
	"spadina": [43.667357, -79.40381],
	"dupont": [43.674855, -79.407081],
	"st-clair-west": [43.684088, -79.415716],
	"eglinton-west": [43.699606, -79.436748],
	"glencairn": [43.708779, -79.440729],
	"lawrence-west": [43.716219, -79.444407],
	"yorkdale": [43.724612, -79.447516],
	"wilson": [43.734467, -79.450109],
	"downsview": [43.749703, -79.461912],
	"bathurst": [43.666445, -79.411217],
	"christie": [43.66412, -79.418319],
	"ossington": [43.662437, -79.426176],
	"dufferin": [43.660186, -79.435455],
	"lansdowne": [43.659149, -79.443177],
	"dundas-west": [43.656972, -79.452893],
	"keele": [43.655517, -79.459802],
	"high-park": [43.653965, -79.46649],
	"runnymede": [43.651697, -79.475979],
	"jane": [43.649946, -79.483832],
	"old-mill": [43.650185, -79.495003],
	"royal-york": [43.648177, -79.511264],
	"islington": [43.645444, -79.523984],
	"kipling": [43.636991, -79.536319]
}


CRAIGSLIST_HOUSING_SECTION = "apa"

##system settings

#how long to sleep between scrapes of craigslist
SLEEP_INTERVAL = 20 * 60 #20 minutes


SLACK_CHANNEL = "#housing"


SLACK_TOKEN = os.getenv("SLACK_TOKEN", "xoxp-65955659840-65962774757-71237534758-3febd3ef15")