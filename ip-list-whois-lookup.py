import whois

def lookup_ip(ip_list):
    for ip in ip_list:
        # Look up the IP address using the whois library
        whois_info = whois.whois(ip)

        # Print the whois information
        print(whois_info)

def main():
    # Prompt the user for a list of IP addresses
    ip_list_str = input("Enter a list of IP addresses separated by commas: ")

    # Split the list of IP addresses into a list
    ip_list = ip_list_str.split(',')

    # Look up each IP address
    lookup_ip(ip_list)

if __name__ == "__main__":
    main()
