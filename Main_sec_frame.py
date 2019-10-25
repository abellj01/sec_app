'''
Created on 30 Sep 2019

@author: aymar

'''
print("         Welcome to Geo Cyber Sec Assessment - Protect Your Business\n")

industry = input("Select your industry (Defense /Finance /Public Sector /Charity /Online_Services /Other): ")

risk = 0
score = 0

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
        if q1_data == "Y" :
            score += 1
        q2_data = input("    Are backup data restores tested at appropriate intervals (at least monthly)? (Y/N) ")
        if q2_data == "Y" :
            score += 1
        q3_data = input("    Are all backups secured with an appropriate level of protection for the type of data they contain? (Y/N) ")
        if q3_data == "Y" :
            score += 1
    if q_web == "Yes" :
        q4_web = input("    Do you carry out a vulnerability scan on your web app? (Y/N) ")
        if q4_web == "Y" :
            score += 1
        q5_web = input("    Have you ever had a penetration test carried out on your web application? (Y/N) ")
        if q5_web == "Y" :
            score += 1
    if q_location == "Yes" :
        q6_location = input("    Do you have firewalls at the boundaries between your start-up internal networks and the internet? (Y/N) ")
        if q6_location == "Y" :
            score += 1
        q7_location = input("    Does your start-up have up to date information asset register? (Y/N) ")
        if q7_location == "Y" :
            score += 1
    if q_size == "Yes" :
        q8_size = input("    Do you have a person responsible for security and data protection awareness? (Y/N) ")
        if q8_size == "Y" :
            score += 1
        q9_size = input("    Are all information security incidents or suspected weaknesses reported and recorded? (Y/N) ")
        if q9_size == "Y" :
            score += 1
        q10_size = input("    Do you report incidents to external bodies as required, such as law enforcement for criminal activity\n and the ICO for personal data breaches? (Y/N) ")
        if q10_size == "Y" :
            score += 1
    if q_third_party == "Yes" :
        q11_third_party = input("    Do you use cloud providers to store company information? (Y/N) ")
        if q11_third_party == "Y" :
            score += 1
        q12_third_party = input("    Where do your cloud providers store your data? (Y/N) ")
        if q12_third_party == "Y" :
            score += 1
        q13_third_party = input("    Is your data encrypted whilst being stored by your cloud provider(s)? (Y/N) ")
        if q13_third_party == "Y" :
            score += 1
    if q_sec_policy == "Yes" :
        q14_sec_policy = input("    Do your policy refer to security incident management? (Y/N) ")
        if q14_sec_policy == "Y" :
            score += 1
        q15_sec_policy = input("    Do you know any specific regulations relating to information security which apply to your start-up? (Y/N) ")
        if q15_sec_policy == "Y" :
            score += 1

other_score = 0
if industry == "Other" :
    q1_firewall = input("    Are your business tools (laptop/mobile/tablet) protected by a firewall to stop external attacks\n and help prevent data breaches? (Y/N) ")
    if q1_firewall == "Y" :
        other_score += 1
    q2_sec_config = input("    Are your business tools (laptop/mobile/tablet) configured to reduce vulnerabilities\n and provide only the functionality and services required? (Y/N) ")
    if q2_sec_config == "Y" :
        other_score += 1
    q3_access_cntrl = input("    Do your business tools (laptop/mobile/tablet) have separate accounts (administator account and basic user)? (Y/N) ")
    if q3_access_cntrl == "Y" :
        other_score += 1
    q4_malware_protection = input("    Do your business tools (laptop/mobile/tablet) have effective anti-malware defences\n to protect them from malware infection? (Y/N) ")
    if q4_malware_protection == "Y" :
        other_score += 1
    q5_patch_mangmt = input("    Are software and applications within your business tools (laptop/mobile/tablet) updated regurlarly\n and the latest security patches applied? (Y/N) ")
    if q5_patch_mangmt == "Y" :
        other_score += 1

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
    if risk > 4 :
        print("    Your Security risk: High")
    elif risk > 2 :
        print("    Your Security risk: Medium")
    else :
        print("    Your Security risk: Low")

    if score > 10 :
        print("    Your Security score: Green")
    elif score > 5 :
        print("    Your Security score: Orange")
    else :
        print("    Your Security score: Red")
else:
    print("\nSummary")
    print("    Sorry, your industry is not listed")
    f = open("other.txt", "r")
    print(f.read())
    f.close()
    print("    Your basic security score", other_score)
