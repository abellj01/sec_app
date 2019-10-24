'''
Created on 30 Sep 2019

@author: aymar

'''
print("         Welcome to Geo Cyber Sec Assessment - Protect Your Business\n")

industry = input("Select your industry (Defense /Finance /Public Sector /Charity /Online_Services /Other): ")

risk = 0

if industry == "Online_Services" :
    q_data = input("    Is Data central to your business? (Yes/No): ")
    if q_data == "Yes" :
        risk += 1
    q_web = input("    Is your solution a Web Application? (Yes/No): ")
    if q_web == "Yes" :
        risk += 1
    q_location = input("    Do you and business partner(s) work from home too? (Yes/No): ")
    if q_location == "Yes" :
        risk += 1
    q_size = input("    Is the company size greater than 3? (Yes/No): ")
    if q_size == "Yes" :
        risk += 1
    q_third_party = input("    Do you use Third parties for support and consultancy? (Yes/No)")
    if q_third_party == "Yes" :
        risk += 1
    q_sec_policy = input("    Do you have an information security policy? (Yes/No)")
    if q_sec_policy == "Yes" :
        risk += 1

    print("\nCan you please tell us a bit more about your business")
    if q_data == "Yes" :
        q1_data = input("    Are data stored on your personal computer backed up regularly (at least weekly)? (Y/N) ")
        q2_data = input("    Are backup data restores tested at appropriate intervals (at least monthly)? (Y/N) ")
        q3_data = input("    Are all backups secured with an appropriate level of protection for the type of data they contain? (Y/N) ")
    if q_web == "Yes" :
        q4_web = input("    Do you carry out a vulnerability scan on your web app? (Y/N) ")
        q5_web = input("    Have you ever had a penetration test carried out on your web application? (Y/N) ")
    if q_location == "Yes" :
        q6_location = input("    Do you have firewalls at the boundaries between your start-up internal networks and the internet? (Y/N) ")
        q7_location = input("    Does your start-up have up to date information asset register? (Y/N) ")
    if q_size == "Yes" :
        q8_size = input("    Do you have a person responsible for security and data protection awareness? (Y/N) ")
        q9_location = input("    Are all information security incidents or suspected weaknesses reported and recorded? (Y/N) ")
        q10_location = input("    Do you report incidents to external bodies as required, such as law enforcement for criminal activity\n and the ICO for personal data breaches? (Y/N) ")
    if q_third_party == "Yes" :
        q11_third_party = input("    Do you use cloud providers to store company information? (Y/N) ")
        q12_third_party = input("    Where do your cloud providers store your data? (Y/N) ")
        q13_third_party = input("    Is your data encrypted whilst being stored by your cloud provider(s)? (Y/N) ")
    if q_sec_policy == "Yes" :
        q14_sec_policy = input("    Do your policy refer to security incident management? (Y/N) ")
        q15_sec_policy = input("    Do you know any specific regulations relating to information security which apply to your start-up? (Y/N) ")

if industry == "Defense" or industry == "D" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following DEFENSE text file.\n")
    print("    It is worth knowing that the Ministry of Defence mandated Cyber Essentials")
    print("    for all its new suppliers and also their relevant supply chain")
elif industry == "Finance" or industry == "F" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following FINANCE text file.")
elif industry == "Public Sector" or industry == "P" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following PUBLIC SECTOR text file.\n")
    print("    The UK Government Department of Health, National Data Guardian (NDG) published 'Review of data security, consent \n    and opt-outs' which recommended All health and social care organisations should provide evidence \n    that they are taking action to improve cyber security, for example through the ‘Cyber Essentials’ scheme.")
elif industry == "Charity" or industry == "C" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following CHARITY text file.")
elif industry == "Online_Services" :
    print("\nSummary")
    print("    My security risk is ", risk)
else:
    print("\nSummary")
    print("    Sorry, your industry is not listed")
    print("    What Next:\n    We recommend reading the contents of 'other' text file because:")
    f = open("other.txt", "r")
    print(f.read())
    f.close()
