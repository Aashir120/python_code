import rpyc

connection = rpyc.connect('192.168.100.11',19961)
connection.root.run_command('ipconfig')

# import rpyc
# import datetime

# AD_SERVER_IP = '192.168.0.173'
# AD_BOT_PORT = 19961
# domain_controller = 'DC=hqvfx,DC=com'
# users_ou = 'OU=All,OU=Employee,{}'.format(domain_controller)
# groups_ou = 'OU=Employee_Groups,{}'.format(domain_controller)


# def send_command(command):
#     if not command:
#         return
#     try:
#         connection = rpyc.connect(AD_SERVER_IP, AD_BOT_PORT)
#         connection.root.run_command(command)
#     except Exception as Err:
#         print('Error in send command', str(Err))


# def create_user(username, employee_id, display_name,  active=False):
#     """
#     Create New user in AD
#     :param username:
#     :param employee_id:
#     :param display_name:
#     :param active:
#     :return:
#     """
#     if active:
#         disabled = 'no'
#     else:
#         disabled = 'yes'

#     description = "User added by AD BOT on  {}".format(datetime.datetime.now())
#     default_password = 'DefaultP@55w0rD'

#     dn = '"CN={},{}"'.format(username, users_ou)
#     groups = '"cn=All,{}" ' \
#              '"cn=USB_Deny,{}" '.format(groups_ou,
#                                         groups_ou)
#     command = 'dsadd user ' \
#               '{} ' \
#               '-samid "{}" ' \
#               '-upn "{}" ' \
#               '-display "{}" ' \
#               '-empid "{}" ' \
#               '-desc "{}" ' \
#               '-disabled {} ' \
#               '-pwd {} ' \
#               '-pwdneverexpires yes ' \
#               '-mustchpwd yes ' \
#               '-memberof {} ' \
#               '-acctexpires never ' \
#               ''.format(
#                 dn,
#                 username,
#                 username,
#                 display_name,
#                 employee_id,
#                 description,
#                 disabled,
#                 default_password,
#                 groups,
#                 )
#     send_command(command)


# def manage_user(username, mode):
#     """
#     This function can manage active directory users
#     :param username:
#     :param mode:
#     :return:
#     """
#     dn = 'CN={},{}'.format(username, users_ou)
#     cmd = ''
#     if mode == 'disable':
#         cmd = 'dsmod user {} -disabled yes'.format(dn)
#     elif mode == 'enable':
#         cmd = 'dsmod user {} -disabled no'.format(dn)
#     elif mode == 'delete':
#         cmd = 'dsrm -noprompt "cn={},{}"'.format(username, users_ou)
#     send_command(cmd)


# def user_password_change(username, new_password):
#     """
#     This function can change active directory password
#     :param new_password:
#     :param username:
#     :return:
#     """
#     dn = 'CN={},{}'.format(username, users_ou)
#     cmd = 'dsmod user {} -pwd {}'.format(dn, new_password)
#     send_command(cmd)


# def ad_group(group_name, mode):
#     """
#     Add and Remove Group
#     :param group_name:
#     :param mode:
#     :return:
#     """
#     cmd = ''
#     if mode == 'add':
#         group_description = 'Group created by AD Bot'
#         cmd = 'dsadd group "cn={}, {}"' \
#               ' -desc "{}"'.format(group_name, groups_ou, group_description)
#     elif mode == 'remove':
#         cmd = 'dsrm -noprompt "cn={},{}"'.format(group_name, groups_ou)
#     send_command(cmd)


# def group_user(group_name, mode, username):
#     """
#     Add and Remove User from groups
#     :param group_name:
#     :param mode:
#     :param username:
#     :return:
#     """
#     dn = 'CN={},{}'.format(username, users_ou)
#     cmd = ''
#     if mode == 'add':
#         cmd = 'dsmod group "cn={},{}"' \
#               ' -addmbr "{}"'.format(group_name, groups_ou, dn)
#     elif mode == 'remove':
#         cmd = 'dsmod group "cn={},{}"' \
#               ' -rmmbr "{}"'.format(group_name, groups_ou, dn)
#     send_command(cmd)
