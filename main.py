import socket


def lgw_template_with_pbx(ccm_ip):
    print("inside lgw_template_with_pbx()")


def lgw_template_without_pbx():
    print("inside lgw_template_without_pbx()")


def get_registration_mode_config():
    line_port = input("Enter the line port: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    otg = input("Enter the OTG: ")
    registrar_domain = input("Enter the registrar domain: ")
    outbound_proxy = input("Enter the outbound proxy: ")
    registration_mode_config = {
        "user_lineport": line_port,
        "username": username,
        "user_password": password,
        "otg": otg,
        "registrar_domain": registrar_domain,
        "outbound_proxy": outbound_proxy,
        "transport": "tls"
    }
    return registration_mode_config


def validate_dialpeer(dial_peer_to_pbx):
    try:
        if int(dial_peer_to_pbx) < 100 or int(dial_peer_to_pbx) > 999:
            print("Invalid dial-peer to pbx. Please enter a value between 100-999")
            exit()
    except ValueError:
        print("Invalid dial-peer to pbx. Please enter a value between 100-999")
        exit()




def get_dial_peer_to_pbx():
    # read user input for dial-peer to pbx
    # in the user input, inform that if they enter 0 then the script will generate a value for dial-peer to pbx
    dial_peer_to_pbx = input("Enter the dial-peer to pbx (0 for auto): ")

    # if user enters a value that is not an integer or within the range of 100-999 then prompt return an error message
    validate_dialpeer(dial_peer_to_pbx)
    if dial_peer_to_pbx == "0":
        dial_peer_to_pbx = "200"
    return dial_peer_to_pbx


def get_dial_peer_to_webex_calling():
    dial_peer_to_webex_calling = input("Enter the dial-peer to pbx (0 for auto): ")
    # if user enters a value that is not an integer or within the range of 100-999 then prompt return an error message
    validate_dialpeer(dial_peer_to_webex_calling)
    if dial_peer_to_webex_calling == "0":
        dial_peer_to_webex_calling = "100"
    return dial_peer_to_webex_calling


def get_fqdn():
    fqdn = input("Enter the fqdn for the local gateway: ")
    return fqdn


def get_local_gateway_type():
    local_gateway_type = input("Enter the local gateway type (reg/cert): ")
    # if user does not enter "reg" or "cert" then prompt return an error message
    if local_gateway_type != "reg" and local_gateway_type != "cert":
        print("Invalid local gateway type. Please enter reg or cert")
        exit()
    return local_gateway_type


def read_user_input():

    #  local gateway type
    local_gateway_type = get_local_gateway_type()
    # method to switch between reg and cert
    if local_gateway_type == "cert":
        fqdn = get_fqdn()
    #  dial-peer to pbx
    dial_peer_to_pbx = get_dial_peer_to_pbx()
    #  dial-peer to webex calling
    dial_peer_to_webex_calling = get_dial_peer_to_webex_calling()
    option = input("Do you want to enter the PBX IP address? (yes/no): ")
    if option == "yes":
        pbx_ip = input("Enter the PBX IP address: ")
        # sanitize the ip address entered and throw an error if the ip address is invalid
        try:
            socket.inet_aton(pbx_ip)
        except socket.error:
            print("Invalid IP address")
            exit()
        lgw_template_with_pbx(pbx_ip)
    else:
        lgw_template_without_pbx()


def main():
    read_user_input()


if __name__ == '__main__':
    main()

