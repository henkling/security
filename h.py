import subprocess
domain = input('Enter the Domain: ')
output = subprocess.check_output(f'nslookup {domain}', shell=True, encoding='UTF-8') 
output2 = subprocess.check_output(f'nslookup {domain}', shell=True, encoding='UTF-8') 
