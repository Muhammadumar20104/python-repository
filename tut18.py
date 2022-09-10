from urllib import request, response
link ='https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1631316931&period2=1662852931&interval=1d&events=history&includeAdjustedClose=true'

def fun(pass_link):
    response = request.urlopen(pass_link)
    response2=response.read()
    data_str=str(response2)
    lines=data_str.split("\\n")
    placing_file= r'file'
    fx = open(placing_file,"w")
    for line in lines:
        fx.write(line + '\n')
    fx.close
    
fun(link)
    