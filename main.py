def lgw_template_with_pbx(outbound_proxy, ccm_ip):
    print("The outbound proxy is: " + outbound_proxy)
    print("The CUCM IP address is: " + ccm_ip)


def lgw_template_without_pbx(outbound_proxy):
    print("The outbound proxy is: " + outbound_proxy)


# read user input a value for "dial-peer to pbx". This value will be used to create the dial-peer
# user may enter 0 for dial-peer to pbx and the script will create a dial-peer with a generated value
# user may enter a value for dial-peer to pbx and the script will create a dial-peer with the value entered
def get_dial_peer_to_pbx():
    dial_peer_to_pbx = input("Enter the dial-peer to pbx: ")
    if dial_peer_to_pbx == "0":
        dial_peer_to_pbx = "200"
    return dial_peer_to_pbx


# read fqdn for the local gateway if certificate-based local gateway is selected
def get_fqdn():
    fqdn = input("Enter the fqdn for the local gateway: ")
    return fqdn


# read user input a value for "dial-peer to webex calling". This value will be used to create the dial-peer
# user may enter 0 for dial-peer to webex calling and the script will create a dial-peer with a generated value
# user may enter a value for dial-peer to webex calling and the script will create a dial-peer with the value entered
def get_dial_peer_to_webex_calling():
    dial_peer_to_webex_calling = input("Enter the dial-peer to webex calling: ")
    if dial_peer_to_webex_calling == "0":
        dial_peer_to_webex_calling = "100"
    return dial_peer_to_webex_calling


# read user input for registration-based vs certificate-based local gateway
# user may enter "reg" for registration-based local gateway
# user may enter "cert" for certificate-based local gateway
def get_local_gateway_type():
    local_gateway_type = input("Enter the local gateway type (reg/cert): ")
    # if user does not enter "reg" or "cert" then prompt return an error message
    if local_gateway_type != "reg" and local_gateway_type != "cert":
        print("Invalid local gateway type. Please enter reg or cert")
        exit()
    return local_gateway_type


def read_user_input():
    outbound_proxy = input("Enter the outbound proxy: ")
    #  local gateway type
    local_gateway_type = get_local_gateway_type()
    # local gateway type is certificate-based then read fqdn
    if local_gateway_type == "cert":
        fqdn = get_fqdn()
    #  dial-peer to pbx
    dial_peer_to_pbx = get_dial_peer_to_pbx()
    #  dial-peer to webex calling
    dial_peer_to_webex_calling = get_dial_peer_to_webex_calling()
    option = input("Do you want to enter the CUCM IP address? (yes/no): ")
    if option == "yes":
        ccm_ip = input("Enter the CUCM IP address: ")
        lgw_template_with_pbx(outbound_proxy, ccm_ip)
    else:
        lgw_template_without_pbx(outbound_proxy)


def main():
    read_user_input()


if __name__ == '__main__':
    main()

