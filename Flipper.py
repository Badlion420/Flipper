import shodan

SHODAN_API_KEY = "jB3765IuOpRRXrXsgOll51IMiiSA2G5C"
api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Search Shodan
    results = api.search("windows 7")
    # Show the results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print(result)
except shodan.APIError as e:
    print("Error: {}".format(e))

