# test_eg_feed.py




# read_rates  
  
import os  
  
def process_row(row):  
    print row  
      
    for k,v in row.items():    
       print '  ',k,v   
  
  
  
def run():  
    print '#################################'  
      
    file_dir = r'C:\MH\dev'  
    file_name = r'CcyRates1Year.csv'  
      
    fileName = os.path.join(file_dir,file_name)  
    print 'fileName', fileName  
      
      
    if not os.path.isfile(fileName):  
        print 'Error File %s does not exist' %fileName  
        return  
      
    try:  
        file = open(fileName)  
        data = file.read()  
        file.close()  
    except IOError:  
        print 'Error reading file %s' %fileName  
      
    data = data.split()  
      
    headers = data[0].split(',')  
      
    for count, row in enumerate(data[1:]):#  
        print row  
        r = dict(zip(headers,row.split(',') ))  
      
        process_row(r)  
      
        break  
        if count > 3 : break  
