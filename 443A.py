ip_str = input()

ip_str = ip_str.replace('{','')
ip_str = ip_str.replace('}','')
ip_str = ip_str.replace(',','')
ip_str = ip_str.split()

ip_str_set = set(ip_str)

print(len(ip_str_set))